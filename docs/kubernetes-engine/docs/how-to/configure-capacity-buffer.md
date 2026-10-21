---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-buffer/
title: Configure capacity buffers \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:55.574093+00:00
---

# Configure capacity buffers  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-capacity-buffer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure capacity buffers Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) [ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Capacity buffers improve the responsiveness and reliability of critical workloads by proactively managing spare cluster capacity and suspended states of pre-provisioned, pre-configured capacity by using a Kubernetes CapacityBuffer CustomResourceDefinition (CRD). Using capacity buffers lets you explicitly define a specific amount of unused node capacity within your cluster. This reserved capacity helps to reduce Pod scheduling time.

When a high-priority workload needs to scale up quickly, the new workload can use the empty capacity immediately without waiting for node provisioning. This approach minimizes latency and avoids resource contention during sudden spikes in demand.

This page provides methods for configuring capacity buffers: a fixed replicas buffer, a resource limits buffer, and a percentage-based buffer.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Create, or have access to, a GKE cluster on version 1.35.2-gke.1842000 for active buffers, and version 1.36.0-gke.2253000 or later for standby buffers.
  * Enable [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) on your Standard clusters. In Autopilot clusters, node auto-provisioning is already enabled. Node auto-provisioning is optional but recommended for active buffers and required for standby buffers.



## Create prerequisite Kubernetes objects

To configure a CapacityBuffer, you need a namespace that holds all of the required objects (the CapacityBuffer itself, and additional resources like a PodTemplate or workload). The PodTemplate and CapacityBuffer must be in the same namespace. You can create a namespace or use an existing namespace, including the `default` namespace.

Depending on which type of CapacityBuffer you're configuring, you also require one of the following:

  * **PodTemplate** : defines the resource requirements for a single unit of buffer capacity. The configuration specified in the CapacityBuffer object references the Pod template.
  * **Workload** : an existing workload that you reference in the CapacityBuffer object. This guide uses a Deployment object as an example workload, but capacity buffers support any of the following resource types:

    * Deployment
    * ReplicaSet
    * StatefulSet
    * ReplicationController
    * Job
    * CustomResourceDefinitions (CRDs) that implement the `scale` subresource.

**Note:** If you are using a custom CRD and a GKE version earlier than 1.36.0-gke.2459000, you might need to manually grant the cluster autoscaler permissions to read the scale subresource. See Permission errors for custom scalable resources.



This section provides examples of these objects. If you already have a workload that you want to configure with a capacity buffer, proceed to Apply a capacity buffer.

To create an example Kubernetes workload, complete the following steps:

  1. Save the following manifest as `namespace.yaml`:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: capacity-buffer-example
           labels:
             name: capacity-buffer-example
         

This manifest creates a namespace called `capacity-buffer-example`.

  2. Optional: to use capacity buffers with a custom ComputeClass, save the following manifest as `custom-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: ccc-example
           namespace: capacity-buffer-example
         spec:
           # Buffers are also created according to these priorities
           priorities:
           - machineFamily: n4
           - machineFamily: n4d
           - machineFamily: c4
           - machineFamily: c4d
           nodePoolAutoCreation:
             enabled: true
         

This manifest creates a custom `ComputeClass` that defines and controls the compute priorities for the nodes that GKE provisions. To learn more, see [custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

  3. Save the following manifest as `buffer-pod-template.yaml`:
         
         apiVersion: v1
         kind: PodTemplate
         metadata:
           name: buffer-unit-template
           namespace: capacity-buffer-example # the namespace must be the same namespace as the CapacityBuffer
         template:
           spec:
             terminationGracePeriodSeconds: 0
             containers:
             - name: buffer-container
               image: registry.k8s.io/pause:3.9
               resources:
                 requests:
                   cpu: "1"
                   memory: "1Gi"
                 limits:
                   cpu: "1"
                   memory: "1Gi"
             # Optional: Using buffers with a custom ComputeClass /
             # controls the properties of the provisioned nodes.
             nodeSelector:
               cloud.google.com/compute-class: ccc-example
         

This manifest creates a `PodTemplate` that defines the resource requirements for a single unit of buffer capacity (`1` CPU and `1Gi` Memory). This configuration specifies the size of capacity units that GKE provisions for the buffer. For example, with this PodTemplate, GKE won't consider nodes with less than 1 CPU and 1Gi of available resources as part of the buffer, if the cluster scales up.

  4. Save the following manifest as `sample-workload-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: critical-workload-ref
           namespace: capacity-buffer-example # the namespace must be the same namespace as the CapacityBuffer
         spec:
           replicas: 10
           selector:
             matchLabels:
               app: critical-workload
           template:
             metadata:
               labels:
                 app: critical-workload
             spec:
               containers:
               - name: busybox
                 image: busybox
                 command: ["sleep", "3600"]
                 resources:
                   requests:
                     cpu: 100m
               # Optional: Using buffers with a custom ComputeClass /
               # controls the properties of the provisioned nodes.
               nodeSelector:
                 cloud.google.com/compute-class: ccc-example
         

This manifest creates a sample Deployment with 10 replicas, which is the reference object for the percentage-based buffer example in the next section.

  5. Apply the manifests to your cluster:
         
         kubectl apply -f namespace.yaml -f custom-compute-class.yaml -f buffer-pod-template.yaml -f sample-workload-deployment.yaml
         

  6. Verify that GKE created the objects:
         
         kubectl get podtemplate -n capacity-buffer-example
         kubectl get deployment critical-workload-ref -n capacity-buffer-example
         

The output is similar to the following:
         
         NAME                   AGE
         buffer-unit-template   1m
         
         NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
         critical-workload-ref   10/10   10           10          1m
         




## Apply a capacity buffer

This section provides examples of the different types of capacity buffers that you can apply to your workloads.

**Note:** It might take up to 5 minutes for the capacity buffer to react to changes.

### Configure a fixed replicas buffer

Configuring a CapacityBuffer with fixed replicas specifies the exact number of buffer units that you want based on a PodTemplate.

To create a buffer with fixed replicas, complete the following steps:

  1. Save the following manifest as `cb-fixed-replicas.yaml`:
         
         apiVersion: autoscaling.x-k8s.io/v1beta1
         kind: CapacityBuffer
         metadata:
           name: fixed-replica-buffer
           namespace: NAMESPACE
         spec:
           podTemplateRef:
             name: POD_TEMPLATE
           replicas: 3
           provisioningStrategy: "STRATEGY"
         

Replace the following:

     * `NAMESPACE`: the name of your namespace, for example `capacity-buffer-example`.
     * `POD_TEMPLATE`: the PodTemplate that defines your resource requirements, for example `buffer-unit-template`.
     * `STRATEGY`: the provisioning strategy, either `"buffer.x-k8s.io/active-capacity"` (default) or `"buffer.gke.io/standby-capacity"`.

This manifest creates a CapacityBuffer resource that references a PodTemplate to request a specific number of buffer units.

  2. Apply the manifest:
         
         kubectl apply -f cb-fixed-replicas.yaml
         

  3. Confirm that GKE applied the capacity buffer:
         
         kubectl get capacitybuffer fixed-replica-buffer -n NAMESPACE
         

The `replicas` field in the status should show `3`, which reflects the number of replicas that you defined in the manifest. The `STATUS` field should show `ReadyForProvisioning`.




### Configure a resource limits buffer

You can use the `limits` field to define a maximum amount of resources that the buffer should consume, calculated based on your PodTemplate size.

To create a resource limits buffer, complete the following steps:

  1. Save the following manifest as `cb-resource-limits.yaml`:
         
         apiVersion: autoscaling.x-k8s.io/v1beta1
         kind: CapacityBuffer
         metadata:
           name: resource-limit-buffer
           namespace: NAMESPACE
         spec:
           podTemplateRef:
             name: POD_TEMPLATE
           limits:
             cpu: "5"
             memory: "5Gi"
           provisioningStrategy: "STRATEGY"
         

Replace the following:

     * `NAMESPACE`: the name of your namespace, for example `capacity-buffer-example`.
     * `POD_TEMPLATE`: the PodTemplate that defines your resource requirements, for example `buffer-unit-template`.
     * `STRATEGY`: the provisioning strategy, either `"buffer.x-k8s.io/active-capacity"` (default) or `"buffer.gke.io/standby-capacity"`.

This manifest creates a CapacityBuffer resource with a total limit of 5 CPUs and 5 GiB Memory. If you're using the PodTemplate example from the previous step, you define each unit as `1` CPU and `1Gi` Memory, which should result in 5 buffer units.

  2. Apply the manifest:
         
         kubectl apply -f cb-resource-limits.yaml
         

  3. Confirm that GKE applied the capacity buffer:
         
         kubectl get capacitybuffer resource-limit-buffer -n NAMESPACE
         

Check the CapacityBuffer status. The `replicas` field should show a value derived from the limits that you defined. If you're using the PodTemplate example from the previous section, you should see `5` buffer units because this is the maximum number of units that fit within the defined limits.




### Configure a percentage-based buffer

Configuring a percentage-based buffer dynamically sizes the buffer based on a percentage of an existing scalable workload. Percentage-based capacity buffers are supported only for Kubernetes scalable objects that implement the [scale subresource](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#scale-subresource), such as Deployments, StatefulSets, ReplicaSets, or Jobs. You can't define a percentage-based buffer for Pod templates because they don't have a `replicas` field.

We generally recommend starting with fixed replicas or resource limit strategies, rather than percentage-based buffers. Percentage-based buffers are less responsive to sudden scale-ups if the workload scales to low numbers or zero, because the safety margin scales in proportion to active Pods. They are useful mainly for large deployments that never scale to very low replica counts.

To create a percentage-based buffer, complete the following steps:

  1. Save the following manifest as `cb-percentage-based.yaml`:
         
         apiVersion: autoscaling.x-k8s.io/v1beta1
         kind: CapacityBuffer
         metadata:
           name: percentage-buffer
           namespace: NAMESPACE
         spec:
           scalableRef:
             apiGroup: apps
             kind: Deployment
             name: SCALABLE_RESOURCE_NAME
           percentage: 20
           provisioningStrategy: "STRATEGY"
         

Replace the following:

     * `NAMESPACE`: the name of your namespace.
     * `SCALABLE_RESOURCE_NAME`: the name of your scalable resource, for example `critical-workload-ref`.
     * `STRATEGY`: the provisioning strategy, either `"buffer.x-k8s.io/active-capacity"` (default) or `"buffer.gke.io/standby-capacity"`.

This manifest creates a CapacityBuffer resource that requests a buffer size equivalent to 20% of the referenced resource's replicas. If you're using the Deployment example from the previous section, the replica value is set to `10`.

**Note:** You can set the value of the `percentage` field to greater than `100` if you require a buffer larger than the current size of the referenced workload. Non-whole buffer replica counts, resulting from percentage field values lower than 100, are rounded down.
  2. Apply the manifest:
         
         kubectl apply -f cb-percentage-based.yaml
         

  3. Confirm that GKE applied the capacity buffer:
         
         kubectl get capacitybuffer percentage-buffer -n NAMESPACE
         

Check the CapacityBuffer status. The `replicas` field should show a value from the percentage calculation. If you're using the Deployment example from the previous section, you should see `2` buffer units, which is 20% of the 10 replicas defined in the Deployment.

  4. Test the dynamic scaling by manually scaling the Deployment up to 20 replicas:
         
         kubectl scale deployment critical-workload-ref -n NAMESPACE --replicas=20
         

The CapacityBuffer controller reacts and automatically scales the buffer to 4 replicas.




## Customize standby buffer behavior

You can use annotations to customize how standby buffers start and refresh. Add these annotations to the `metadata.annotations` field of your CapacityBuffer resource:

  * `buffer.gke.io/standby-capacity-init-time`: the amount of time a node remains active after creation before it's suspended. The format is a duration string (for example, `5m` or `1h`). The default is `5m`.
  * `buffer.gke.io/standby-capacity-refresh-frequency`: how often suspended nodes are refreshed. The default is `24h`.



The following example shows a manifest with these optional fields to customize the behavior of standby buffers:
    
    
    apiVersion: autoscaling.x-k8s.io/v1beta1
    kind: CapacityBuffer
    metadata:
      name: customized-standby-buffer
      namespace: my-namespace
      annotations:
        buffer.gke.io/standby-capacity-init-time: "15m"
        buffer.gke.io/standby-capacity-refresh-frequency: "12h"
    spec:
      podTemplateRef:
        name: buffer-unit-template
      replicas: 3
      provisioningStrategy: "buffer.gke.io/standby-capacity"
    

## Preload images on standby buffers

To speed up workload startup times when a standby node resumes, you can preload container images by using a DaemonSet. The DaemonSet runs during the start-up period before the node is suspended.

To preload images by using the DaemonSet, complete the following steps:

  1. Save the following manifest as `image-puller-daemonset.yaml`:
         
         apiVersion: apps/v1
         kind: DaemonSet
         metadata:
           name: image-prefetch-daemonset
           namespace: NAMESPACE
         spec:
           selector:
             matchLabels:
               name: image-prefetch
           template:
             metadata:
               labels:
                 name: image-prefetch
             spec:
               tolerations:
               - key: "buffer.gke.io/standby-node-suspended"
                 operator: "Exists"
               initContainers:
               - name: image-puller
                 image: IMAGE_NAME
                 command: ["sh", "-c", "true"]
               containers:
               - name: pause
                 image: registry.k8s.io/pause:3.9
         

Replace the following:

     * `NAMESPACE`: the namespace for the DaemonSet, for example `capacity-buffer-example`.
     * `IMAGE_NAME`: the name of the image to preload, for example `your-app-image:latest`.
  2. Apply the DaemonSet manifest to your cluster:
         
         kubectl apply -f image-puller-daemonset.yaml
         

  3. Verify that the DaemonSet is created:
         
         kubectl get daemonset image-prefetch-daemonset -n NAMESPACE
         

  4. Verify that your capacity buffer is created and ready for provisioning:
         
         kubectl get capacitybuffer CAPACITY_BUFFER_NAME -n NAMESPACE
         

Check the status. The `STATUS` field should show `ReadyForProvisioning`.




## Monitor capacity buffer status and performance

You can monitor the status and health of your capacity buffers by using `kubectl` commands and Cloud Monitoring metrics.

### Verify CapacityBuffer resource status

To check the health of your capacity buffers and verify that they are ready to receive workloads, complete the following steps:

  1. Get the status of all capacity buffers across the cluster:
         
         kubectl get capacitybuffer -A
         

  2. Inspect the detailed status, conditions, and event logs of a specific buffer:
         
         kubectl describe capacitybuffer CAPACITY_BUFFER_NAME -n NAMESPACE
         




### Identify suspended standby buffer nodes

Standby buffer VMs are pre-provisioned, but kept in a suspended state to help reduce costs. You can recognize these suspended nodes because they have a custom condition. To audit suspended node instances, run the following command:
    
    
    kubectl get nodes -o custom-columns='NAME:.metadata.name,SUSPENDED:.status.conditions[?(@.type=="Suspended")].status'
    

A status of `True` indicates a standby VM is suspended. A status of `False` or `<none>` indicates an active, running node.

### Monitor performance with Cloud Monitoring

To help monitor the performance of capacity buffers, monitor the following resources in Cloud Monitoring:

  * **Reaction latency (`cluster_autoscaler/reaction_time_milliseconds`)**: Tracks the duration for the Cluster Autoscaler to make a scaling decision based on your CapacityBuffer pending demand.
  * **Cluster Autoscaler logs** : Search for log entries like `"Capacity pod processor injecting ..."` to observe active buffer Pod replacement events.



## Remove capacity buffers

If you no longer need a capacity buffer for your workloads, delete the CapacityBuffer object. This removes the placeholder Pods and allows the cluster autoscaler to scale down the nodes.
    
    
    kubectl delete capacitybuffer CAPACITY_BUFFER_NAME -n NAMESPACE
    

Replace `CAPACITY_BUFFER_NAME` with the name of the CapacityBuffer that you want to delete.

## Troubleshooting

The following section contains information on resolving common issues with capacity buffers.

### Capacity buffer not ready due to billing model

If you create a CapacityBuffer for a workload that uses the [Pod-based billing model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#pricing) (pay-per-Pod), the capacity buffer won't be ready for provisioning.

To identify this issue, check the CapacityBuffer status:
    
    
    kubectl describe capacitybuffer BUFFER_NAME -n NAMESPACE
    

Look for a condition of the type `ReadyForProvisioning` with a status of `False`.

To resolve this issue, ensure that your CapacityBuffer references a workload or PodTemplate that is compatible with node-based billing.

### Permission errors for custom scalable resources

If you configure a CapacityBuffer to work with custom scalable objects (using the `scalableRef` field), the cluster autoscaler might fail to scale the buffer if it lacks the necessary permissions. This issue only occurs in GKE versions earlier than 1.36.0-gke.2459000.

To resolve this issue, manually grant the required permissions by creating a `ClusterRole` and `ClusterRoleBinding`, such as in the following example:
    
    
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: custom-scale-getter
    rules:
    - apiGroups: ["api.example.com"]
      resources: ["customreplicatedresources/scale"]
      verbs: ["get"]
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: ca-custom-scale-getter
    subjects:
    - kind: User
      name: "system:cluster-autoscaler"
      namespace: kube-system
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: custom-scale-getter
    

For more information about configuring RBAC, see the [Kubernetes RBAC documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole).

### Buffer Pods aren't scheduled on nodes provisioned by custom ComputeClasses

If your CapacityBuffer configuration dependency (for example, a PodTemplate) selects a custom ComputeClass, you might encounter an issue where buffer Pods aren't scheduled on the newly provisioned nodes. This issue causes the cluster autoscaler to repeatedly create redundant node pools and nodes while idle nodes are deleted.

This issue occurs if the custom ComputeClass provisions nodes with taints or specific runtime requirements, and your buffer Pods (or the PodTemplate they rely on) don't have matching tolerations or settings.

To resolve this issue, update your CapacityBuffer configuration to specify the required tolerations, node selectors, or runtime classes. For example, if your dependency selects a custom ComputeClass configured with GKE Sandbox, update the dependency to do one of the following:

  * Specify the `spec.runtimeClassName: gvisor` field.
  * Include an explicit toleration for the `sandbox.gke.io/runtime=gvisor:NoSchedule` taint.



For more information, see the [custom ComputeClass documentation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).

## What's next

  * Learn more about [capacity buffers](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/capacity-buffer).
  * Refer to the [CapacityBuffer CRD documentation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/capacitybuffer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
