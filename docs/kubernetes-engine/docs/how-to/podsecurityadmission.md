---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission/
title: Apply predefined Pod-level security policies using PodSecurity \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:11.713674+00:00
---

# Apply predefined Pod-level security policies using PodSecurity  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Apply predefined Pod-level security policies using PodSecurity Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to apply predefined Pod-level security controls in your Google Kubernetes Engine (GKE) clusters by using the `PodSecurity` admission controller. Applying security controls to your Pods can help you meet security and compliance requirements. On this page, you learn more about `PodSecurity` and how to apply it to your Pods.

This page is for Security specialists who want to apply security controls to their GKE clusters. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following concepts:

  * [Kubernetes documentation for the Pod Security admission controller](https://kubernetes.io/docs/concepts/security/pod-security-admission/)
  * [Kubernetes documentation for _Pod Security Standards_](https://kubernetes.io/docs/concepts/security/pod-security-standards/)



## About `PodSecurity`

_`PodSecurity`_ is a Kubernetes admission controller that lets you apply _Pod Security Standards_ to Pods that run on your GKE clusters. Pod Security Standards are predefined security policies that cover the high-level needs of Pod security in Kubernetes. These policies range from being highly permissive to highly restrictive.

You can apply the following Pod Security Standards to your GKE clusters:

  * **Privileged** : An unrestricted policy that provides the widest level of permissions. Allows for known privilege escalations.
  * **Baseline** : A minimally restrictive policy that allows the default, minimally specified Pod configuration. Prevents known privilege escalations.
  * **Restricted** : A highly restrictive policy that follows Pod hardening best practices.



You can use the `PodSecurity` admission controller to apply Pod Security Standards in the following modes:

  * **Enforce** : Policy violations reject Pod creation. An audit event is added to the audit log.
  * **Audit** : Policy violations trigger adding an audit event to the audit log. Pod creation is allowed.
  * **Warn** : Policy violations trigger a user-facing warning. Pod creation is allowed.



The `PodSecurity` admission controller embeds these policies into the Kubernetes API.

**Note:** You can't create policies that override the [built-in security settings in GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security#built-in-security).

If you want to create and apply custom security policies at the Pod level, consider using the [Gatekeeper](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper) admission controller instead.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have a GKE Autopilot or Standard cluster running version 1.23 or later. 
    * For Autopilot clusters, [enroll in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#enrolling_a_cluster_in_a_release_channel) in which the default version is 1.23 or later.
    * For Standard clusters, enroll in a release channel or [upgrade the cluster to a specific version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).



## Requirements

The `PodSecurity` admission controller is available and enabled by default on clusters running the following GKE versions:

  * Version 1.25 or later: Stable
  * Version 1.23 and version 1.24: Beta



To check whether a GKE version is available and is the default version for your release channel, refer to the [Release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).

## Apply Pod Security Standards using `PodSecurity`

To use the `PodSecurity` admission controller, you must apply specific Pod Security Standards in specific modes to specific namespaces. You can do this by using namespace labels. In this exercise, you do the following:

  * Create two new namespaces
  * Apply security policies to each namespace
  * Test the configured policies



In the following GKE versions, GKE ignores policies that you apply to the `kube-system` namespace:

  * 1.23.6-gke.1900 and later
  * 1.24.0-gke.1200 and later



In earlier GKE versions, avoid enforcing policies in `kube-system`.

### Create new namespaces

Create namespaces in your cluster:
    
    
    kubectl create ns baseline-ns
    kubectl create ns restricted-ns
    

This command creates the following namespaces:

  * `baseline-ns`: For permissive workloads
  * `restricted-ns`: For highly restricted workloads



### Use labels to apply security policies

Apply the following Pod Security Standards:

  * `baseline`: Apply to `baseline-ns` in the `warn` mode
  * `restricted`: Apply to `restricted-ns` in the `enforce` mode


    
    
    kubectl label --overwrite ns baseline-ns pod-security.kubernetes.io/warn=baseline
    kubectl label --overwrite ns restricted-ns pod-security.kubernetes.io/enforce=restricted
    

These commands achieve the following result:

  * Workloads in the `baseline-ns` namespace that violate the `baseline` policy are allowed, and the client displays a warning message.
  * Workloads in the `restricted-ns` namespace that violate the `restricted` policy are rejected, and GKE adds an entry to the audit logs.



Verify that the labels were added:
    
    
    kubectl get ns --show-labels
    

The output is similar to the following:
    
    
    baseline-ns       Active   74s   kubernetes.io/metadata.name=baseline-ns,pod-security.kubernetes.io/warn=baseline
    restricted-ns     Active   18s   kubernetes.io/metadata.name=restricted-ns,pod-security.kubernetes.io/enforce=restricted
    default           Active   57m   kubernetes.io/metadata.name=default
    kube-public       Active   57m   kubernetes.io/metadata.name=kube-public
    kube-system       Active   57m   kubernetes.io/metadata.name=kube-system
    

### Test the configured policies

To verify that the `PodSecurity` admission controller works as intended, deploy a workload that violates the `baseline` and the `restricted` policy to both namespaces. The following example manifest deploys an `nginx` container that allows privilege escalation.

  1. Save the following manifest as `psa-workload.yaml`:
         
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
         

  2. Apply the manifest to the `baseline-ns` namespace:
         
         kubectl apply -f psa-workload.yaml --namespace=baseline-ns
         

The output is similar to the following:
         
         Warning: would violate PodSecurity "baseline:latest": privileged (container "nginx" must not set securityContext.privileged=true)
         

The `baseline` policy allows the Pod to deploy in the namespace.

  3. Verify that the Pod deployed successfully:
         
         kubectl get pods --namespace=baseline-ns -l=app=nginx
         

  4. Apply the manifest to the `restricted-ns` namespace:
         
         kubectl apply -f psa-workload.yaml --namespace=restricted-ns
         

The output is similar to the following:
         
         Error from server (Forbidden): error when creating "workload.yaml": pods "nginx"
         is forbidden: violates PodSecurity "restricted:latest": allowPrivilegeEscalation
         != false (container "nginx" must set securityContext.allowPrivilegeEscalation=false),
         unrestricted capabilities (container "nginx" must set securityContext.capabilities.drop=["ALL"]),
         runAsNonRoot != true (pod or container "nginx" must set securityContext.runAsNonRoot=true),
         seccompProfile (pod or container "nginx" must set securityContext.seccompProfile.type
         to "RuntimeDefault" or "Localhost")
         

The Pod won't deploy in the namespace. An audit entry is added to the log.




### View policy violations in the audit logs

Policy violations in the `audit` and `enforce` modes are recorded in the audit logs for your cluster. You can view these logs using the Logs Explorer in the Google Cloud console.

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, specify the following to retrieve `audit` and `enforce` mode audit logs:
         
         resource.type="k8s_cluster"
         protoPayload.resourceName:"/pods/nginx"
         protoPayload.methodName="io.k8s.core.v1.pods.create"
         (labels."pod-security.kubernetes.io/audit-violations":"PodSecurity" OR protoPayload.response.reason="Forbidden")
         

  3. Click **Run query**.

  4. In the **Query results** section, expand the `Forbidden` log entry for inspecting `enforce` mode rejection logs. The details are similar to the following:
         
         {
           ...
           protoPayload: {
             @type: "type.googleapis.com/google.cloud.audit.AuditLog"
             authenticationInfo: {1}
             authorizationInfo: [1]
             methodName: "io.k8s.core.v1.pods.create"
             request: {6}
             requestMetadata: {2}
             resourceName: "core/v1/namespaces/restricted-ns/pods/nginx"
             response: {
               @type: "core.k8s.io/v1.Status"
               apiVersion: "v1"
               code: 403
               details: {2}
               kind: "Status"
               message: "pods "nginx" is forbidden: violates PodSecurity "restricted:latest": privileged
                       (container "nginx" must not set securityContext.privileged=true),
                       allowPrivilegeEscalation != false (container "nginx" must set
                       securityContext.allowPrivilegeEscalation=false), unrestricted capabilities
                       (container "nginx" must set securityContext.capabilities.drop=["ALL"]),
                       runAsNonRoot != true (pod or container "nginx" must set securityContext.runAsNonRoot=true),
                       seccompProfile (pod or container "nginx" must set securityContext.seccompProfile.type
                       to "RuntimeDefault" or "Localhost")"
               metadata: {0}
               reason: "Forbidden"
               status: "Failure"
               }
               serviceName: "k8s.io"
               status: {2}
             }
           receiveTimestamp: "2022-02-01T19:19:25.353235326Z"
           resource: {2}
           timestamp: "2022-02-01T19:19:21.469360Z"
         }
         

  5. Expand the `audit-violations` log entry for inspecting `audit` mode logs. The details are similar to the following:
         
         {
           ...
           labels: {
             ...
             pod-security.kubernetes.io/audit-violations: "would violate PodSecurity "baseline:latest": privileged
                                                         (container "nginx" must not set securityContext.privileged=true)"
             pod-security.kubernetes.io/enforce-policy: "privileged:latest"
           }
           operation: {4}
           protoPayload: {10}
           receiveTimestamp: "2023-12-26T05:18:04.533631468Z"
           resource: {2}
           timestamp: "2023-12-26T05:17:36.102387Z"
         }
         




## Clean up

To avoid incurring charges to your Google Cloud account, delete the namespaces:
    
    
    kubectl delete ns baseline-ns
    kubectl delete ns restricted-ns
    

## Alternatives to `PodSecurity`

In addition to using the built-in Kubernetes `PodSecurity` admission controller to apply Pod Security Standards, you can also use [Gatekeeper](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies-with-gatekeeper), an admission controller based on the [Open Policy Agent (OPA)](https://www.openpolicyagent.org/), to create and apply custom Pod-level security controls.

## What's next

  * [Learn more about Pod Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/).
  * [Learn more about the `PodSecurity` admission controller](https://kubernetes.io/docs/concepts/security/pod-security-admission/).
  * [Migrate from PodSecurityPolicy to the `PodSecurity` admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-podsecuritypolicy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
