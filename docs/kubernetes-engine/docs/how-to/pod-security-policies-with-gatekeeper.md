---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper/
title: Apply custom Pod-level security policies using Gatekeeper \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:14.031077+00:00
---

# Apply custom Pod-level security policies using Gatekeeper  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Apply custom Pod-level security policies using Gatekeeper Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to use the Gatekeeper admission controller to apply Pod-level security controls to your Google Kubernetes Engine (GKE) clusters. On this page, you learn how to use Gatekeeper to apply constraints that let you apply security policies to help you meet security requirements for your organization.

This page is for Security specialists who want to apply security controls to their GKE clusters. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following concepts:

  * [General overview of Gatekeeper](https://github.com/open-policy-agent/gatekeeper).
  * [General overview of Open Policy Agent (OPA), which is used by Gatekeeper](https://www.openpolicyagent.org/).



## Gatekeeper overview

Gatekeeper is an admission controller that validates requests to create and update Pods on Kubernetes clusters, using the Open Policy Agent (OPA).

Using Gatekeeper allows administrators to define policies with a _constraint_ , which is a set of conditions that permit or deny deployment behaviors in Kubernetes. You can then enforce these policies on a cluster using a `ConstraintTemplate`. This document provides examples for restricting the security capabilities of workloads to ensure enforce, test, and audit security policies using Gatekeeper.

Gatekeeper can also:

  * **Roll out policies:** Enforce policy in a gradual, scoped manner to limit the risk of disrupting workloads.
  * **Dry-run policy changes:** Provide mechanisms for testing policy impact and range prior to enforcement.
  * **Audit existing policies:** Ensure the application of security controls to new and existing workloads (audit controls).



## Key Gatekeeper concepts

Gatekeeper introduces two concepts in order to provide administrators with a powerful and flexible means of controlling their cluster: **constraints** , and **constraint templates** , both of which are concepts inherited from the Open Policy Agent [Constraint Framework](https://github.com/open-policy-agent/frameworks/tree/master/constraint).

**Constraints** are the representation of your security policy—they define the requirements and range of enforcement. **Constraint templates** are reusable statements (written in [Rego](https://www.openpolicyagent.org/docs/latest/#rego)) that apply logic to evaluate specific fields in Kubernetes objects, based on requirements defined in constraints.

For example, you might have a constraint that declares allowable seccomp profiles that can be applied to Pods in a specific namespace, and a comparable constraint template that provides the logic for extracting these values and handling enforcement.

The following constraint template, from the [Gatekeeper repository](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/pod-security-policy), checks for the existence of `securityContext.privileged` in a Pod specification:
    
    
    apiVersion: templates.gatekeeper.sh/v1beta1
    kind: ConstraintTemplate
    metadata:
      name: k8spspprivilegedcontainer
    spec:
      crd:
        spec:
          names:
            kind: K8sPSPPrivilegedContainer
      targets:
        - target: admission.k8s.gatekeeper.sh
          rego: |
            package k8spspprivileged
    
            violation[{"msg": msg, "details": {}}] {
                c := input_containers[_]
                c.securityContext.privileged
                msg := sprintf("Privileged container is not allowed: %v, securityContext: %v", [c.name, c.securityContext])
            }
            input_containers[c] {
                c := input.review.object.spec.containers[_]
            }
            input_containers[c] {
                c := input.review.object.spec.initContainers[_]
            }
    

To extend the previous constraint template example, the following constraint defines the scope (`kinds`) for the specific enforcement of this constraint template in a `dryrun` mode:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPPrivilegedContainer
    metadata:
      name: psp-privileged-container
    spec:
      enforcementAction: dryrun
      match:
        kinds:
          - apiGroups: [""]
            kinds: ["Pod"]
    

With Gatekeeper, you can create your own constraints and constraint templates to meet your specific needs. You can also use a [standard set of constraints and constraint templates](https://github.com/open-policy-agent/gatekeeper-library/tree/master/library/pod-security-policy) in the [Gatekeeper repository](https://github.com/open-policy-agent/gatekeeper/tree/master/library) that have been defined to enable quick adoption and security enforcement. Each constraint is also accompanied with example Pod configurations.

Google Cloud provides a managed, officially supported version of open source Gatekeeper named [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller). Google doesn't officially support the open source Gatekeeper project.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable Gatekeeper on a cluster with Policy Controller

[Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) is a policy engine built on the [Gatekeeper](https://github.com/open-policy-agent/gatekeeper) open source project. Google recommends the use of Policy Controller because it includes additional features to help enforce policy at scale, including policy-as-code, multi-cluster support, integration with Cloud Logging, and ability to view policy status in the Google Cloud console. Policy Controller is available with GKE, but you can [install Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/install/) on your cluster instead.

To enable Policy Controller on a cluster, follow the [Policy Controller installation guide](https://docs.cloud.google.com/anthos-config-management/docs/how-to/installing-policy-controller).

## Enable constraints and constraint templates

Gatekeeper and its constraint templates can be installed and enabled without adversely impacting existing or new workloads. For this reason, it's recommended that all applicable Pod security constraint templates be applied to the cluster.

Additionally, Gatekeeper constraints can be implemented to enforce controls for specific objects, such as namespaces and Pods.

Observe the example below that limits the scope to **_Pods_** located in the **_production_** namespace by defining them in the constraint match statement:
    
    
    ...
    spec:
      match:
        kinds:
          - apiGroups: [""]
            kinds: ["Pod"]
        namespaces:
          - "production"
    

For more information about the available options for `Constraint` and `ConstraintTemplate` objects, see [How to use Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/docs/howto).

### Test policies

Introducing new policies to existing clusters can have adverse behavior, for example by restricting existing workloads. One of the benefits of using Gatekeeper for Pod security is the ability to test the effectiveness and impact a policy will have without making actual changes, using a dry-run mode. This allows for policy configuration to be tested against running clusters without enforcement. Policy violations are logged and identified without interference.

The following steps demonstrate how a developer, operator, or administrator can apply constraint templates and constraints to determine their effectiveness or potential impact:

  1. Apply the Gatekeeper config for replicating data for audit and dry-run functionality:
         
         kubectl create -f- <<EOF
         apiVersion: config.gatekeeper.sh/v1alpha1
         kind: Config
         metadata:
           name: config
           namespace: "gatekeeper-system"
         spec:
           sync:
             syncOnly:
               - group: ""
                 version: "v1"
                 kind: "Namespace"
               - group: ""
                 version: "v1"
                 kind: "Pod"
         EOF
         

  2. With no constraints applied, run a workload with elevated privileges:
         
         kubectl create -f- <<EOF
         apiVersion: v1
         kind: Pod
         metadata:
           name: nginx
           labels:
             app: nginx
         spec:
           containers:
           - name: nginx
             image: nginx
             securityContext:
               privileged: true
         EOF
         

  3. Load the previous `k8spspprivilegedcontainer` constraint template:
         
         kubectl create -f- <<EOF
         apiVersion: templates.gatekeeper.sh/v1beta1
         kind: ConstraintTemplate
         metadata:
           name: k8spspprivilegedcontainer
         spec:
           crd:
             spec:
               names:
                 kind: K8sPSPPrivilegedContainer
           targets:
             - target: admission.k8s.gatekeeper.sh
               rego: |
                 package k8spspprivileged
         
                 violation[{"msg": msg, "details": {}}] {
                     c := input_containers[_]
                     c.securityContext.privileged
                     msg := sprintf("Privileged container is not allowed: %v, securityContext: %v", [c.name, c.securityContext])
                 }
                 input_containers[c] {
                     c := input.review.object.spec.containers[_]
                 }
                 input_containers[c] {
                     c := input.review.object.spec.initContainers[_]
                 }
         EOF
         

  4. Create a new constraint to extend this constraint template. This time, set the `enforcementAction` to `dryrun`:
         
         kubectl create -f- <<EOF
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: K8sPSPPrivilegedContainer
         metadata:
           name: psp-privileged-container
         spec:
           enforcementAction: dryrun
           match:
             kinds:
               - apiGroups: [""]
                 kinds: ["Pod"]
         EOF
         

  5. With Gatekeeper synchronizing running object data, and passively checking for violations, confirm if any violations were found by checking the `status` of the constraint:
         
         kubectl get k8spspprivilegedcontainer.constraints.gatekeeper.sh/psp-privileged-container -o yaml
         
         
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: K8sPSPPrivilegedContainer
         metadata:
         ...
          name: psp-privileged-container
         ...
         spec:
          enforcementAction: dryrun
          match:
            kinds:
            - apiGroups:
              - ""
              kinds:
              - Pod
         status:
          auditTimestamp: "2019-12-15T22:19:54Z"
          byPod:
          - enforced: true
            id: gatekeeper-controller-manager-0
          **violations:**
          - enforcementAction: **dryrun**
            kind: Pod
            **message: 'Privileged container is not allowed: nginx, securityContext: {"privileged":
              true}'**
            name: nginx
            namespace: default
         

  6. To confirm that the policy doesn't interfere with deployments, run another privileged Pod:
         
         kubectl create -f- <<EOF
         apiVersion: v1
         kind: Pod
         metadata:
           name: privpod
           labels:
             app: privpod
         spec:
           containers:
           - name: nginx
             image: nginx
             securityContext:
               privileged: true
         EOF
         

This new Pod will be successfully deployed.

  7. To clean up the resources created in this section, run the following commands:
         
         kubectl delete k8spspprivilegedcontainer.constraints.gatekeeper.sh/psp-privileged-container
         kubectl delete constrainttemplate k8spspprivilegedcontainer
         kubectl delete pod/nginx
         kubectl delete pod/privpod
         




### Enforce policies

Now that you can confirm the validity and impact of a policy without impacting existing or new workloads, you can implement a policy with full enforcement.

Building on the examples used to validate the policy above, the following steps demonstrate how a developer, operator, or administrator can apply constraint templates and constraints to enforce a policy:

  1. Load the `k8spspprivilegedcontainer` constraint template mentioned earlier:
         
         kubectl create -f- <<EOF
         apiVersion: templates.gatekeeper.sh/v1beta1
         kind: ConstraintTemplate
         metadata:
           name: k8spspprivilegedcontainer
         spec:
           crd:
             spec:
               names:
                 kind: K8sPSPPrivilegedContainer
           targets:
             - target: admission.k8s.gatekeeper.sh
               rego: |
                 package k8spspprivileged
         
                 violation[{"msg": msg, "details": {}}] {
                     c := input_containers[_]
                     c.securityContext.privileged
                     msg := sprintf("Privileged container is not allowed: %v, securityContext: %v", [c.name, c.securityContext])
                 }
                 input_containers[c] {
                     c := input.review.object.spec.containers[_]
                 }
                 input_containers[c] {
                     c := input.review.object.spec.initContainers[_]
                 }
         EOF
         

  2. Create a new constraint to extend this constraint template. This time, don't set the `enforcementAction` key. By default, the `enforcementAction` key is set to `deny`:
         
         kubectl create -f- <<EOF
         apiVersion: constraints.gatekeeper.sh/v1beta1
         kind: K8sPSPPrivilegedContainer
         metadata:
           name: psp-privileged-container
         spec:
           match:
             kinds:
               - apiGroups: [""]
                 kinds: ["Pod"]
         EOF
         

  3. Attempt to deploy a container that declares privileged permissions:
         
         kubectl create -f- <<EOF
         apiVersion: v1
         kind: Pod
         metadata:
           name: nginx
           labels:
             app: nginx
         spec:
           containers:
           - name: nginx
             image: nginx
             securityContext:
               privileged: true
         EOF
         

The following error message should be received:
         
         Error from server ([denied by psp-privileged-container] Privileged container is not allowed:
         nginx, securityContext: {"privileged": true}): error when creating "STDIN": admission webhook "validation.gatekeeper.sh" denied the request: [denied by psp-privileged-container]
         **Privileged container is not allowed: nginx, securityContext: {"privileged": true}**
         

  4. To clean up, run the following commands:
         
         kubectl delete k8spspprivilegedcontainer.constraints.gatekeeper.sh/psp-privileged-container
         kubectl delete constrainttemplate k8spspprivilegedcontainer
         




## Alternatives to Gatekeeper

Gatekeeper lets you declare and apply custom Pod-level security policies. You can also use Kubernetes' built-in [`PodSecurity` admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission) to apply predefined Pod-level security policies. These predefined policies are aligned with the levels defined by the [Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).

## What's next

Gatekeeper provides an incredibly powerful means to enforce and validate security on GKE clusters using declarative policies. Gatekeeper's use extends beyond security however, and can be used in other aspects of administration and operations.

  * [How to use Gatekeeper](https://github.com/open-policy-agent/gatekeeper#how-to-use-gatekeeper)
  * [Gatekeeper demonstrations](https://github.com/open-policy-agent/gatekeeper/tree/master/demo)
  * [Gatekeeper examples](https://github.com/open-policy-agent/gatekeeper-library)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
