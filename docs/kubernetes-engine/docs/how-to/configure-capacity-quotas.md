---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-quotas/
title: Configure granular resource limits \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:40.568860+00:00
---

# Configure granular resource limits  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure granular resource limits Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To improve how effectively you manage infrastructure costs and quota, you can define maximum resource limits for the Google Kubernetes Engine (GKE) cluster autoscaler. This document shows you how to use the CapacityQuota custom resource to specify autoscaling resource limits for subsets of nodes. Unlike [cluster-wide resource limits](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#resource-limits), you can select specific nodes in a CapacityQuota by using Kubernetes label selectors.

This document is intended for platform administrators who manage cluster scaling and infrastructure. You should be familiar with Kubernetes node labels and the GKE [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

## How CapacityQuota resource limits work

A CapacityQuota is a cluster-scoped Kubernetes custom resource that you configure in a manifest and apply to the cluster. You use the following fields in the CapacityQuota specification to select nodes and specify resource limits:

  * `selector`: filter for specific nodes by using one or more label selectors. For example, you can select all of the nodes for a specific ComputeClass or nodes that have two specific labels.
  * `limits`: specify maximum resource limits for the nodes that match the selectors. For example, you can limit the amount of CPU that can be used by a specific custom ComputeClass, or limit the number of GPUs of a particular type.



When a scale-up operation begins, the cluster autoscaler checks the proposed node against all CapacityQuotas that match the node labels and against any configured cluster-wide resource limits. GKE creates the node only if the node doesn't violate any configured resource limits.

## Limitations

  * GKE rejects CapacityQuotas that specify the `node.kubernetes.io/instance-type` and `beta.kubernetes.io/instance-type` label selectors. To limit nodes that use a specific machine type, create a custom ComputeClass that has `machineType` priority rules and select that ComputeClass in your CapacityQuota.
  * Similarly to cluster-wide limits, CapacityQuotas might prevent ComputeClass [active migration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#active-migration) from happening. Because active migration is a scale-up operation, the cluster autoscaler checks the potential new node against all applicable CapacityQuotas and cluster-wide resource limits. If the new node violates any of these limits, then GKE doesn't create the node and the active migration doesn't occur. This situation happens only if the CapacityQuota is already at, or close to the configured limits.
  * CapacityQuota limits aren't strict limits. In rare scenarios, you might notice that GKE exceeds the configured limits by a small margin.
  * CapacityQuota limits are enforced only by the cluster autoscaler. You can exceed the limits by scaling up the cluster manually, or by changing the limits to lower than the current usage.
  * If nodes in the cluster exceed the configured CapacityQuota limits, then the cluster autoscaler blocks the creation of new nodes that match the exceeded CapacityQuota. The cluster autoscaler doesn't scale down existing nodes that match the CapacityQuota.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster that runs at version 1.36.2-gke.2064000 or later. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



## Configure resource limits in a CapacityQuota

You can select the nodes that a CapacityQuota applies to by using either or both of the following methods:

  * Select nodes by using exact node labels: specify one or more node label key-value pairs in the `matchLabels` field. GKE finds nodes that have all of the labels that you specify. This method is similar to using the `nodeSelector` field in a Pod specification.

  * Select nodes by using expressions: specify one or more label selector expressions by specifying the label key, operators, and values. This method is similar to using the `nodeAffinity` field in a Pod specification.


**Caution:** If you create a CapacityQuota without specifying selectors, the CapacityQuota matches all of the nodes in the cluster. The limits that you specify are cluster-wide limits.

### Select nodes by using node labels

To construct a CapacityQuota based on node label matching by using the `matchLabels` field, follow these steps:

  1. Save one of the following example CapacityQuotas, each of which is intended for a specific use case:

     * Configure resource limits for an entire custom ComputeClass by specifying the `cloud.google.com/compute-class` label:
           
           apiVersion: autoscaling.x-k8s.io/v1beta1
           kind: CapacityQuota
           metadata:
             name: capacity-quota-compute-class
           spec:
             selector:
               matchLabels:
                 cloud.google.com/compute-class: my-class
             limits:
               resources:
                 cpu: 12
           

This CapacityQuota restricts the cluster autoscaler to a maximum of 12 CPUs across all of the nodes that GKE creates for the `my-class` ComputeClass.

     * Configure limits for the number of GPUs of a specific type by using the `cloud.google.com/gke-accelerator` label and the `nvidia.com/gpu` resource name:
           
           apiVersion: autoscaling.x-k8s.io/v1beta1
           kind: CapacityQuota
           metadata:
             name: capacity-quota-gpu
           spec:
             selector:
               matchLabels:
                 cloud.google.com/compute-class: my-gpu-class
                 cloud.google.com/gke-accelerator: nvidia-tesla-t4
             limits:
               resources:
                 nvidia.com/gpu: 16
           

This CapacityQuota restricts the cluster autoscaler to a maximum of 16 NVIDIA Tesla T4 GPUs in the `my-gpu-class` ComputeClass. If you omit the ComputeClass selector, then the limit applies to all NVIDIA Tesla T4 GPU nodes in the cluster.

     * Configure limits for the number of nodes that GKE creates in a specific zone by using the `topology.kubernetes.io/zone` label and the `nodes` resource name:
           
           apiVersion: autoscaling.x-k8s.io/v1beta1
           kind: CapacityQuota
           metadata:
             name: capacity-quota-zone
           spec:
             selector:
               matchLabels:
                 topology.kubernetes.io/zone: us-central1-b
             limits:
               resources:
                 nodes: 64
           

This CapacityQuota restricts the cluster autoscaler to 64 nodes in the `us-central1-b` zone.

  2. Create the CapacityQuota:
         
         kubectl apply -f PATH_TO_MANIFEST_FILE
         

Replace `PATH_TO_MANIFEST_FILE` with the path to the CapacityQuota manifest file that you created.




### Select nodes by using expressions

For more complex targeting, CapacityQuota supports defining the `matchExpressions` field in addition to the `matchLabels` field. The `matchExpressions` enables operators like `In`, `NotIn`, `Exists`, and `DoesNotExist`.

  1. Create a CapacityQuota manifest that uses the `matchExpressions` field. The following example CapacityQuota applies CPU and memory limits to nodes running on specific high-performance machine families by grouping them by using the `In` operator:
         
         apiVersion: autoscaling.x-k8s.io/v1beta1
         kind: CapacityQuota
         metadata:
           name: capacity-quota-high-perf-machines
         spec:
           selector:
             matchExpressions:
               - key: cloud.google.com/machine-family
                 operator: In
                 values:
                   - c2
                   - c3
                   - c3d
           limits:
             resources:
               cpu: 64
               memory: 128Gi
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f PATH_TO_MANIFEST_FILE
         

Replace `PATH_TO_MANIFEST_FILE` with the path to the CapacityQuota manifest file that you created.




## Verify the CapacityQuota configuration

This section shows you how to verify that a CapacityQuota actively enforces limits by deploying an example workload that violates those limits. To perform this verification, follow these steps:

  1. Save the following example ComputeClass as `test-capacityquota-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: test-capacityquota-class
         spec:
           priorities:
           - machineFamily: n2
           nodePoolAutoCreation:
             enabled: true
         

This ComputeClass can auto-create nodes that use the N2 machine series.

  2. Create the ComputeClass:
         
         kubectl apply -f test-capacityquota-class.yaml
         

  3. Save the following example CapacityQuota as `test-capacityquota.yaml`:
         
         apiVersion: autoscaling.x-k8s.io/v1beta1
         kind: CapacityQuota
         metadata:
           name: test-capacityquota
         spec:
           selector:
             matchLabels:
               cloud.google.com/compute-class: test-capacityquota-class
           limits:
             resources:
               cpu: 8
         

This CapacityQuota restricts the autoscaler to a maximum of 8 CPU resources for the `test-capacityquota-class` ComputeClass.

  4. Create the CapacityQuota:
         
         kubectl apply -f test-capacityquota.yaml
         

  5. Save the following Deployment as `test-capacityquota-workload.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: test-capacityquota-workload
         spec:
           replicas: 16
           selector:
             matchLabels:
               app: test-capacityquota-workload
           template:
             metadata:
               labels:
                 app: test-capacityquota-workload
             spec:
               containers:
               - name: test
                 image: gcr.io/google_containers/pause
                 resources:
                   limits:
                     cpu: 500m
               nodeSelector:
                 cloud.google.com/compute-class: test-capacityquota-class
         

This Deployment creates 16 Pods, each of which requests 500 mCPU. Because nodes reserve some CPU for system components, the sum of the CPU resources across all of the nodes that GKE must create to run the 16 Pods is greater than `8`.

  6. Create the Deployment:
         
         kubectl apply -f test-capacityquota-workload.yaml
         

  7. Wait for about two minutes, and then verify the Pod scheduling status:
         
         kubectl get pods -l app=test-capacityquota-workload
         

The cluster autoscaler scales nodes up to the CapacityQuota limit of 8 CPUs. After this limit is reached, the autoscaler doesn't create nodes. As a result, some Pods in the Deployment remain in the `Pending` status.

  8. To verify that the CapacityQuota is what caused the `Pending` status, describe one of the pending Pods:
         
         kubectl describe pod PENDING_POD_NAME
         

Replace `PENDING_POD_NAME` with the name of a Pod that's stuck in the `Pending` state.

The output is similar to the following, which indicates that the CapacityQuota blocked node scale-up:
         
         Pod didn't trigger scale-up: 1 exceeded quota: "CapacityQuota/test-capacityquota", resources: cpu
         

You can also view these events by using the [cluster autoscaler visibility logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility). Check the `noScaleUp` event, like in the following example:
         
         {
           "jsonPayload": {
             "noDecisionStatus": {
               "noScaleUp": {
                 "skippedMigs": [
                   {
                     "reason": {
                       "parameters": [
                         "exceeded quota: \"CapacityQuota/test-capacityquota\", resources: cpu"
                       ],
                       "messageId": "no.scale.up.mig.skipped"
                     },
                     "mig": {
                       "name": "gke-test-grp",
                       "zone": "us-central1-f",
                       "nodepool": "nap-n2-highcpu-2-test"
                     }
                   }
                 ]
               }
             }
           }
         }
         




## Check the usage and validity of CapacityQuotas

The `status` field in the CapacityQuota API resource provides information about resource usage for nodes that match the CapacityQuota and the validity of the CapacityQuota specification.

To check the status of a CapacityQuota, run the following command:
    
    
    kubectl describe capacityquota CAPACITY_QUOTA_NAME
    

Replace `CAPACITY_QUOTA_NAME` with the name of the CapacityQuota that you want to inspect.

In the output, check the following fields:

  * To check the resource usage of matched nodes, use the `status.used` field:
        
        status:
          conditions:
          - lastTransitionTime: "2026-07-27T10:00:00Z"
            message: "CapacityQuota is valid"
            reason: "Valid"
            status: "True"
            type: "cluster-autoscaler.kubernetes.io/valid"
          **used :
            resources:
              cpu: 32
              memory: 128Gi**
        

The `status.used` field is intended for observability and isn't used by the cluster autoscaler to enforce limits. This field displays usage only after a successful scale-up operation. The cluster autoscaler also tracks pending nodes internally and factors those pending nodes into subsequent scale-up evaluations. This internal tracking helps to prevent limits from being exceeded.

  * To check the validity of a CapacityQuota, use the `status.conditions` field:
        
        status:
          **conditions :
          - lastTransitionTime: "2026-07-27T10:00:00Z"
            message: "CapacityQuota is valid"
            reason: "Valid"
            status: "True"
            type: "cluster-autoscaler.kubernetes.io/valid"**
          used:
            resources:
              cpu: 32
              memory: 128Gi
        

The `cluster-autoscaler.kubernetes.io/valid` condition verifies whether the CapacityQuota uses a valid configuration, such as a correctly formatted selector. If the value in the `status` field for this condition is `True`, then the CapacityQuota is valid and your limits are enforced. However, if the value in the `status` field is `False`, or if the condition is not yet present, then the limits aren't enforced. The `message` field provides details about why the CapacityQuota isn't valid.




## What's next

  * Learn more about [how the cluster autoscaler works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
  * See the [CapacityQuota API reference](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/capacityquota)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
