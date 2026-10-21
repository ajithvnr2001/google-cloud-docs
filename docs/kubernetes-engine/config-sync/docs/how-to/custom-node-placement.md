---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/custom-node-placement/
title: Customize node placement of Config Sync system Pods \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:25.740639+00:00
---

# Customize node placement of Config Sync system Pods  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/custom-node-placement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Customize node placement of Config Sync system Pods Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure the node placement for Config Sync system Pods that are running on your cluster. Configuring node placement can be useful in situations such as isolating Config Sync system Pods to specific nodes for security purposes, or scheduling Config Sync on cheaper nodes for cost saving purposes.

## About MutatingAdmissionPolicy

[MutatingAdmissionPolicy](https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/) is a Kubernetes feature available in Kubernetes version 1.36 and later, which lets you customize the behavior whenever someone writes a change to the Kubernetes API.

In the context of Config Sync, you can use `MutatingAdmissionPolicy` to add node placement parameters into Pods that run in Config Sync system namespaces. These parameters includes Pod spec fields such as [nodeSelector and affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/). This document provides an example of how you can use a `MutatingAdmissionPolicy` with Config Sync, and you can find more examples in the Config Sync [open source repository](https://github.com/GoogleContainerTools/config-sync/tree/main/examples/mutating-admission-policies).

## Set nodeSelectors

The following example shows how you can use a `MutatingAdmissionPolicy` to automatically add a `nodeSelector` to every Pod running in each of the Config Sync system namespaces with the label `configmanagement.gke.io/system: "true"`. Config Sync system namespaces include `config-management-system`, `config-management-monitoring`, and `resource-group-system`.

**Note:** a `MutatingAdmissionPolicy` can't update existing Pods. Pods created before the policy was applied must be updated or recreated.
    
    
    apiVersion: admissionregistration.k8s.io/v1beta1
    kind: MutatingAdmissionPolicy
    metadata:
      name: "my-pod-node-selector"
    spec:
      matchConstraints:
        resourceRules:
        - apiGroups:   [""]
          apiVersions: ["v1"]
          operations:  ["CREATE", "UPDATE"]
          resources:   ["pods"]
      failurePolicy: Fail
      reinvocationPolicy: IfNeeded
      mutations:
      # Basic example of adding nodeSelector: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
      # Similar mutations can be applied for affinities, tolerations, and so on
      - patchType: "JSONPatch"
        jsonPatch:
          expression: >
            [
              JSONPatch{
                op: "add", path: "/spec/nodeSelector",
                value: {
                  "LABEL_KEY": "LABEL_VALUE",
                }
              }
            ]
    ---
    apiVersion: admissionregistration.k8s.io/v1beta1
    kind: MutatingAdmissionPolicyBinding
    metadata:
      name: "configsync-node-selector"
    spec:
      policyName: "my-pod-node-selector"
      matchResources:
        namespaceSelector:
          matchLabels:
            # This namespace selector only selects Config Sync system namespaces
            configmanagement.gke.io/system: "true"
    

Replace the following:

  * `LABEL_KEY`: the label key to be used by the node selector.
  * `LABEL_VALUE`: the label value to be used by the node selector.



After applying this configuration to your cluster, all Config Sync system Pods are scheduled onto nodes with the label LABEL_KEY=LABEL_VALUE.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
