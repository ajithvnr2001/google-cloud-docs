---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-dra-workloads/
title: Allocate existing devices to workloads with DRA \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:46.563121+00:00
---

# Allocate existing devices to workloads with DRA  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-dra-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Allocate existing devices to workloads with DRA Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can flexibly request devices for your Google Kubernetes Engine (GKE) workloads by using [dynamic resource allocation (DRA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation). This document shows you how to create a ResourceClaimTemplate to request existing devices in node pools in your cluster, and then create a workload to observe how Kubernetes flexibly allocates the devices to your Pods.

This document is intended for [Application operators](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#operators-app-sre) and [Data engineers](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks#data-ai-engineer) who run workloads like AI/ML or high performance computing (HPC).

## About requesting devices with DRA

When you set up your GKE infrastructure for DRA, the DRA drivers on your nodes create _DeviceClass_ objects in the cluster. A DeviceClass defines a category of devices, such as GPUs, that are available to request for workloads. A platform administrator can optionally deploy additional DeviceClasses that limit which devices you can request in specific workloads.

To request devices within a DeviceClass, you create one of the following objects:

  * **ResourceClaim** : A ResourceClaim lets a Pod or a user request hardware resources by filtering for certain parameters within a DeviceClass. 
  * **ResourceClaimTemplate** : A ResourceClaimTemplate defines a template that Pods can use to automatically create new per-Pod ResourceClaims. 



For more information about ResourceClaims and ResourceClaimTemplates, see [When to use ResourceClaims and ResourceClaimTemplates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation#resourceclaim-vs-resourceclaimtemplate).

The examples in this document use a basic ResourceClaimTemplate to request the specified device configuration. For more information about all of the fields that you can specify, see the [ResourceClaimTemplate API reference](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/resource-claim-template-v1/).

## Limitations

The following limitations apply:

  * [Limitations of DRA in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dynamic-resource-allocation#limitations)
  * Device-specific limitations, which apply regardless of whether you use DRA: [GPU workloads on Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus#before_you_begin)



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that your [GKE clusters are configured for DRA workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/set-up-dra).



## Claim devices and deploy workloads

To request per-Pod device allocation, you create a ResourceClaimTemplate that has your requested device configuration, such as GPUs of a specific type. When you deploy a workload that references the ResourceClaimTemplate, Kubernetes creates ResourceClaims for each Pod in the workload based on the ResourceClaimTemplate. Kubernetes allocates the requested resources and schedules the Pods on corresponding nodes.

To request GPUs in a workload with DRA, follow these steps:

  1. Save the following manifest as `gpu-claim-template.yaml`:
         
         apiVersion: resource.k8s.io/v1
         kind: ResourceClaimTemplate
         metadata:
           name: gpu-claim-template
         spec:
           spec:
             devices:
               requests:
               - name: single-gpu
                 exactly:
                   deviceClassName: gpu.nvidia.com
                   allocationMode: ExactCount
                   count: 1
         

  2. Create the ResourceClaimTemplate:
         
         kubectl create -f gpu-claim-template.yaml
         

  3. To create a workload that references the ResourceClaimTemplate, save the following manifest as `dra-gpu-example.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: dra-gpu-example
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: dra-gpu-example
           template:
             metadata:
               labels:
                 app: dra-gpu-example
             spec:
               containers:
               - name: ctr
                 image: ubuntu:22.04
                 command: ["bash", "-c"]
                 args: ["echo $(nvidia-smi -L || echo Waiting...); sleep infinity"]
                 resources:
                   claims:
                   - name: single-gpu
               resourceClaims:
               - name: single-gpu
                 resourceClaimTemplateName: gpu-claim-template
               tolerations:
               - key: "nvidia.com/gpu"
                 operator: "Exists"
                 effect: "NoSchedule"
         

  4. Deploy the workload:
         
         kubectl create -f dra-gpu-example.yaml
         




## Verify the hardware allocation

You can verify that your workloads have been allocated hardware by checking the ResourceClaim or by looking at the logs for your Pod. To verify the allocation, follow these steps:

  1. Get the ResourceClaim associated with the workload that you deployed:
         
         kubectl get resourceclaims
         

The output is similar to the following:
         
         NAME                                               STATE                AGE
         dra-gpu-example-64b75dc6b-x8bd6-single-gpu-jwwdh   allocated,reserved   9s
         

  2. Get more details about the hardware assigned to the Pod:
         
         kubectl describe resourceclaims RESOURCECLAIM
         

Replace `RESOURCECLAIM` with the full name of the ResourceClaim that you got from the output of the previous step.

The output is similar to the following:
         
         Name:         dra-gpu-example-68f595d7dc-prv27-single-gpu-qgjq5
         Namespace:    default
         Labels:       <none>
         Annotations:  resource.kubernetes.io/pod-claim-name: single-gpu
         API Version:  resource.k8s.io/v1
         Kind:         ResourceClaim
         Metadata:
         # Multiple lines are omitted here.
         Spec:
           Devices:
             Requests:
               Exactly:
                 Allocation Mode:    ExactCount
                 Count:              1
                 Device Class Name:  gpu.nvidia.com
               Name:                 single-gpu
         Status:
           Allocation:
             Devices:
               Results:
                 Device:   gpu-0
                 Driver:   gpu.nvidia.com
                 Pool:     gke-cluster-1-dra-gpu-pool-b56c4961-7vnm
                 Request:  single-gpu
             Node Selector:
               Node Selector Terms:
                 Match Fields:
                   Key:       metadata.name
                   Operator:  In
                   Values:
                     gke-cluster-1-dra-gpu-pool-b56c4961-7vnm
           Reserved For:
             Name:      dra-gpu-example-68f595d7dc-prv27
             Resource:  pods
             UID:       e16c2813-08ef-411b-8d92-a72f27ebf5ef
         Events:        <none>
         

  3. Get logs for the workload that you deployed:
         
         kubectl logs deployment/dra-gpu-example --all-pods=true
         

The output is similar to the following:
         
         [pod/dra-gpu-example-64b75dc6b-x8bd6/ctr] GPU 0: Tesla T4 (UUID: GPU-2087ac7a-f781-8cd7-eb6b-b00943cc13ef)
         

This output indicates that GKE allocated one GPU to the container.




## What's next

  * [Explore more resources for AI/ML orchestration on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
