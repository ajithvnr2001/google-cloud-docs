---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/auditing-constraints/
title: Auditing using constraints \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:51.640063+00:00
---

# Auditing using constraints  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/auditing-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Auditing using constraints Stay organized with collections  Save and categorize content based on your preferences. 

Policy Controller [constraint objects](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints) enable you to enforce policies for your Kubernetes clusters. To help test your policies, you can add an enforcement action to your constraints. You can then view violations in constraint objects and logs.

This page is for IT administrators and Operators who want to ensure that all resources running within the cloud platform meet organizational compliance requirements by providing and maintaining automation to audit or enforce, and who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Types of enforcement actions

There are three enforcement actions: `deny`, `dryrun`, and `warn`.

`deny` is the default enforcement action. It's automatically enabled, even if you don't add an enforcement action in your constraint. Use `deny` to prevent a given cluster operation from occurring when there's a violation.

`dryrun` lets you monitor violations of your rules without actively blocking transactions. You can use it to test if your constraints are working as intended, prior to enabling active enforcement using the `deny` action. Testing constraints this way can prevent disruptions caused by an incorrectly configured constraint.

`warn` is similar to `dryrun`, but also provides an immediate message about the violations that occur at admission time.

It's recommended when testing new constraints or performing migration actions, like upgrading platforms, to switch enforcement actions from `deny` to `warn` or `dryrun` so that you can test that your policies work as expected.

## Adding enforcement actions

You can add `enforcementAction: deny` or `enforcementAction: dryrun` to a constraint.

The following example constraint, named `audit.yaml`, adds the `dryrun` action.
    
    
    #audit.yaml
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAllowedUsers
    metadata:
      name: user-must-be-3333
    spec:
      **enforcementAction : dryrun**
      match:
        kinds:
          - apiGroups: [""]
            kinds: ["Pod"]
      parameters:
        runAsUser:
          rule: MustRunAs
          ranges:
            - min: 3333
              max: 3333
    

Create the constraint. For example, apply it using `kubectl apply -f`:
    
    
    kubectl apply -f audit.yaml
    

## Viewing audit results

Audited violations are appended to the Constraint objects and are also written to the logs. Violations that the admission controller rejects do not appear in the logs.

### Viewing audit results in constraint objects

To see violations of a given constraint, run the following command and view the `spec.status` fields.
    
    
    kubectl get constraint-kind constraint-name -o yaml
    

**Note:** You can see a maximum of 20 violations in the output. When there are more than 20 results, you can view the complete list using logs.

#### Example

To see the output of the constraint from `audit.yaml`, run the following command:
    
    
    kubectl get K8sPSPAllowedUsers user-must-be-3333 -o yaml
    

The output you see is similar to the following:
    
    
    apiVersion: constraints.gatekeeper.sh/v1beta1
    kind: K8sPSPAllowedUsers
    metadata:
      creationTimestamp: "2020-05-22T01:34:22Z"
      generation: 1
      name: user-must-be-3333
      resourceVersion: "13351707"
      selfLink: /apis/constraints.gatekeeper.sh/v1beta1/k8spspallowedusers/user-must-be-3333
      uid: 5d0b39a8-9bcc-11ea-bb38-42010a80000c
    spec:
      enforcementAction: dryrun
      match:
        kinds:
        - apiGroups:
          - ""
          kinds:
          - Pod
      parameters:
        runAsUser:
          ranges:
          - max: 3333
            min: 3333
          rule: MustRunAs
     **status :
      auditTimestamp: "2020-05-22T01:39:05Z"
      byPod:
      - enforced: true
        id: gatekeeper-controller-manager-6b665d4c4d-lwnz5
        observedGeneration: 1
     totalViolations: 5
      violations:
      - enforcementAction: dryrun
        kind: Pod
        message: Container git-sync is attempting to run as disallowed user 65533
        name: git-importer-86564db8cb-5r4gs
        namespace: config-management-system
      - enforcementAction: dryrun
        kind: Pod
        message: Container manager is attempting to run as disallowed user 1000
        name: gatekeeper-controller-manager-6b665d4c4d-lwnz5
        namespace: gatekeeper-system
      - enforcementAction: dryrun
        kind: Pod
        message: Container kube-proxy is attempting to run without a required securityContext/runAsUser
        name: kube-proxy-gke-fishy131-default-pool-7369b17c-cckf
        namespace: kube-system
      - enforcementAction: dryrun
        kind: Pod
        message: Container kube-proxy is attempting to run without a required securityContext/runAsUser
        name: kube-proxy-gke-fishy131-default-pool-7369b17c-jnhb
        namespace: kube-system
      - enforcementAction: dryrun
        kind: Pod
        message: Container kube-proxy is attempting to run without a required securityContext/runAsUser
        name: kube-proxy-gke-fishy131-default-pool-7369b17c-xrd8
        namespace: kube-system**
    

### Viewing audit results in logs

You can use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to retrieve, view, and analyze log data for Policy Controller.

To get all Policy Controller logs, run the following command:
    
    
    kubectl logs -n gatekeeper-system -l gatekeeper.sh/system=yes
    

The audit results have `"process":"audit"` in the log lines, so you can pipe the output to another command and filter by these lines. For example, you could use `jq`, which parses JSON files and lets you set a filter for a specific log type.

Example audit result from logging:
    
    
    {
    "level":"info",
    "ts":1590111401.9769812,
    "logger":"controller",
    "msg":"Container kube-proxy is attempting to run without a required securityContext/runAsUser",
    "process":"audit",
    "audit_id":"2020-05-22T01:36:24Z",
    "event_type":"violation_audited",
    "constraint_kind":"K8sPSPAllowedUsers",
    "constraint_name":"user-must-be-3333",
    "constraint_namespace":"",
    "constraint_action":"dryrun",
    "resource_kind":"Pod",
    "resource_namespace":"kube-system",
    "resource_name":"kube-proxy-gke-fishy131-default-pool-7369b17c-xrd8"
    }
    

## What's next

  * Read more about [Creating constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/creating-policy-controller-constraints)
  * Use the [constraint template library](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/latest/reference/constraint-template-library)
  * Learn how to [use constraints instead of PodSecurityPolicies](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/using-constraints-to-enforce-pod-security)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
