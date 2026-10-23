---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/writable-cgroups/
title: Configure writable cgroups for containers \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:27.302106+00:00
---

# Configure writable cgroups for containers  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/writable-cgroups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure writable cgroups for containers Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can let Google Kubernetes Engine (GKE) workloads manage resources, like CPU and memory, for child processes by using the Linux [cgroups](https://man7.org/linux/man-pages/man7/cgroups.7.html) API. This document shows you how to provide containers with read-write access to the cgroups API without running those containers in privileged mode.

## When to use writable cgroups

By default, Kubernetes provides all Linux containers with read-only access to the cgroups API by mounting the `/sys/fs/cgroup` file system in each container. You can optionally let GKE mount this file system in read-write mode in specific Pods to let root processes manage and constrain resources for child processes.

These writable cgroups help to improve reliability in applications like [Ray](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview) that run system processes and user code in the same container. By writing to the `/sys/fs/cgroup` file system, Ray can reserve portions of a container's resources for critical processes. You can use writable cgroups to improve reliability in these applications without the security risk of using privileged mode for the containers.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an Autopilot or Standard cluster running version 1.34.1-gke.2541000 or later. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).
  * Ensure that your cluster uses cgroup v2. For more information, see [Migrate nodes to Linux cgroup v2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2#check-cgroup-mode).



## Enable writable cgroups for your nodes

Enable writable cgroups on your nodes by customizing the containerd configuration.

In your containerd configuration file, add a `writableCgroups` section and set the `enabled` field to `true`. For more information, see [Customize containerd configuration in GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration).
    
    
    writableCgroups:
      enabled: true
    

You can enable writable cgroups through any of the following supported paths:

  * **Create a new cluster:** specify the configuration file using the `--containerd-config-from-file` flag when creating a new cluster (use the `gcloud container clusters create` or `gcloud container clusters create-auto` command).
  * **Update an existing cluster:** specify the configuration file using the `--containerd-config-from-file` flag when updating cluster-level node defaults (use the `gcloud container clusters update` command). Updating cluster-level node defaults doesn't affect existing nodes. In Standard clusters, you must upgrade existing node pools (use the `gcloud container clusters upgrade` command with the `--node-pool` flag) or re-create them to pick up the configuration.
  * **Create a new node pool:** in Standard clusters, specify the configuration file using the `--containerd-config-from-file` flag when creating a new node pool (use the `gcloud container node-pools create` command).



**Note:** Modifying the `writableCgroups` configuration on an existing node pool by using the `gcloud container node-pools update` command is not supported. Writable cgroups are supported only on Linux node pools; Windows node pools don't support cgroups.

## Use writable cgroups in workloads

After you enable writable cgroups for your cluster or node pools, configure your workloads to meet all of the following requirements:

  * Select a node that has writable cgroups enabled.
  * Enable writable cgroups for one or more containers in the Pod.
  * Use the [Guaranteed Quality of Service (QoS) class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/) by meeting one of the following conditions:

    * For workloads that [specify resources at the Pod level](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#pod-level-resource-specification), set equal values for `resources.requests` and `resources.limits` in the Pod specification.
    * For workloads that specify resources for each container, set equal values for `resources.requests` and `resources.limits` in the specification of every container in the Pod, including init containers.



To configure these requirements, follow these steps:

  1. To select nodes that have writable cgroups enabled, add the `node.gke.io/enable-writable-cgroups: "true"` label to the `spec.nodeSelector` field in your Pod specification:
         
         node.gke.io/enable-writable-cgroups: "true"
         

  2. To enable writable cgroups for your workload, add one of the following annotations to the `metadata.annotations` field in your Pod specification:

     * **Enable for the entire Pod** :
           
           node.gke.io/enable-writable-cgroups: "true"
           

     * **Enable for a specific container in the Pod** :
           
           node.gke.io/enable-writable-cgroups.CONTAINER_NAME: "true"
           

Replace `CONTAINER_NAME` with the name of the container.

  3. To configure the Guaranteed QoS class for your Pod, specify equal CPU and memory requests and limits for every container in the Pod or for the entire Pod, like in the following example:
         
         resources:
           requests:
             cpu: "100m"
             memory: "100Mi"
           limits:
             cpu: "100m"
             memory: "100Mi"
         

You must specify equal requests and limits for every container, even if you enable writable cgroups only for one of the containers in the Pod.




Your final Pod specification should be similar to the following examples.

  * This example enables writable cgroups for all containers in the Pod:
        
        apiVersion: v1
        kind: Pod
        metadata:
          name: writable-cgroups-pod
          **annotations :
            node.gke.io/enable-writable-cgroups: "true"**
        spec:
          **nodeSelector :
            node.gke.io/enable-writable-cgroups: "true"**
          containers:
          - name: container
            image: busybox:stable
            command: ["/bin/sh", "-c"]
            args:
            -   |
              trap 'echo "Caught SIGTERM, exiting..."; exit 0' TERM
              echo "Waiting for termination signal..."
              while true; do sleep 1; done
            **resources :
              requests:
                cpu: "100m"
                memory: "100Mi"
              limits:
                cpu: "100m"
                memory: "100Mi"**
        

  * This example enables writable cgroups for a specific container in a multi-container Pod:
        
        apiVersion: v1
        kind: Pod
        metadata:
          name: writable-cgroups-per-container
          **annotations :
            node.gke.io/enable-writable-cgroups.busybox-container: "true"**
        spec:
          **nodeSelector :
            node.gke.io/enable-writable-cgroups: "true"**
          containers:
          - name: busybox-container
            image: busybox:stable
            command: ["/bin/sh", "-c"]
            args:
            -   |
              trap 'echo "Caught SIGTERM, exiting..."; exit 0' TERM
              echo "Waiting for termination signal..."
              while true; do sleep 1; done
            **resources :
              requests:
                cpu: "100m"
                memory: "100Mi"
              limits:
                cpu: "100m"
                memory: "100Mi"**
          - name: container-disabled
            image: busybox:stable
            command: ["/bin/sh", "-c"]
            args:
            -   |
              trap 'echo "Caught SIGTERM, exiting..."; exit 0' TERM
              echo "Waiting for termination signal..."
              while true; do sleep 1; done
            **resources :
              requests:
                cpu: "100m"
                memory: "100Mi"
              limits:
                cpu: "100m"
                memory: "100Mi"**
        




## Verify that the cgroup file system is writable

To verify the permissions on the `/sys/fs/cgroup` file system for a Pod or a container, follow these steps:

  1. Identify a Pod that you want to check. You can use one of the sample Pods from the Use writable cgroups in workloads section.
  2. Create a shell session in the Pod:
         
         kubectl exec -it POD_NAME -- /bin/sh
         

Replace `POD_NAME` with the name of the Pod.

  3. Describe the mounted cgroup file system:
         
         mount | grep cgroup
         

The output is similar to the following:
         
         cgroup on /sys/fs/cgroup type cgroup2 (**rw** ,nosuid,nodev,noexec,relatime)
         

In this output, `rw` indicates that the file system is writable. If you see `ro` in the output, the file system is read-only.




## What's next

  * [Customize containerd configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
