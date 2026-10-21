---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-managed-cni/
title: Troubleshoot managed CNI \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:43.054897+00:00
---

# Troubleshoot managed CNI  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/troubleshooting/troubleshoot-managed-cni/

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot managed CNI

This page explains common managed CNI problems with Cloud Service Mesh and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.27/docs/getting-support).

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

Note that in-cluster resources require at least `memory: 100Mi` on each node. For more information see [Cloud Service Mesh requirements](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/provision-control-plane#requirements). If your cluster already has sufficient memory allocated, see [Pod unschedulable](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#PodUnschedulable) for additional troubleshooting steps.

## Nodes stuck in NotReady status with missing containerID error

You may see this error when your cluster nodes are unable to become ready after upgrading your Google Kubernetes Engine (GKE) version.

**Error message:**

`container runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: missing containerID`

**Cause:**

This issue stems from an incompatibility between the Cloud Service Mesh Container Network Interface (CNI) version 1.20.x and the [Container Network Interface (CNI) plugins in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-architecture#how-pod-networking-works). The CNI plugins require compatibility with the CNI 1.1.0 spec. Clusters running GKE version `1.35.1-gke.1516000` or later automatically enable support for this spec. Because Cloud Service Mesh CNI version 1.20.x doesn't support CNI spec version 1.1.0, node health checks fail and the nodes remain in a `NotReady` status.

**Workaround:**

If your cluster is still running Cloud Service Mesh CNI version 1.20.x, don't upgrade your GKE node pools to `1.35.1-gke.1516000` or later.

If you have already upgraded and are experiencing this issue, the recommended workaround is to downgrade your GKE version to a version older than `1.35.1-gke.1516000` until your cluster's managed CNI is upgraded to version 1.23.x or later.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
