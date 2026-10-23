---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/troubleshooting/troubleshoot-managed-cni/
title: Troubleshoot managed CNI \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:17.660660+00:00
---

# Troubleshoot managed CNI  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/troubleshooting/troubleshoot-managed-cni/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot managed CNI

This page explains common managed CNI problems with Cloud Service Mesh and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.24/docs/getting-support).

## Unsupported managed CNI enabled configuration

Managed Cloud Service Mesh with the `TRAFFIC_DIRECTOR` control plane implementation requires managed CNI and does not support disabling it. You may see the `CNI_CONFIG_UNSUPPORTED` code in the feature state message if the `mesh.cloud.google.com/managed-cni-enabled` label exists but does not have the value `true` in the control plane revision (CPR) custom resource (CR) or if the CNI entry in the asm-options configmap exists but does not have the value `on`.

To resolve this error message, you must remove any attempts to disable managed CNI.

  * Case 1: Remove the managed CNI Enabled label in the CPR CR in the cluster.
        
        apiVersion: v1
        items:
        - apiVersion: mesh.cloud.google.com/v1beta1
          kind: ControlPlaneRevision
          metadata:
            annotations:
              mesh.cloud.google.com/proxy: '{"managed":"false"}'
            creationTimestamp: "2024-02-18T08:13:30Z"
            generation: 1
            labels:
              app.kubernetes.io/created-by: mesh.googleapis.com
              mesh.cloud.google.com/managed-cni-enabled: false # Remove the "mesh.cloud.google.com/managed-cni-enabled" label
            name: asm-managed
            namespace: istio-system
            resourceVersion: "13422558"
            uid: 3ad755ec-78ab-4d57-8fb9-c5e1a07740d5
        

  * Case 2: Remove the CNI entry asm-options configmap `ASM_OPTS` data string.
        
        apiVersion: v1
        data:
          ASM_OPTS: CNI=off # Remove CNI entry in the ASM_OPTS data.
          multicluster_mode: connected
        kind: ConfigMap
        metadata:
          creationTimestamp: "2024-02-18T08:13:30Z"
          name: asm-options
          namespace: istio-system
          resourceVersion: "1640225"
          uid: 576602da-e60b-4df7-9427-5be06e5bf014
        




## CNI Pod unschedulable

You may see this error if the managed CNI Daemonset cannot schedule Pods in any one of the nodes in the cluster.

Note that in-cluster resources require at least `memory: 100Mi` on each node. For more information see [Cloud Service Mesh requirements](https://docs.cloud.google.com/service-mesh/v1.24/docs/onboarding/provision-control-plane#requirements). If your cluster already has sufficient memory allocated, see [Pod unschedulable](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#PodUnschedulable) for additional troubleshooting steps.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
