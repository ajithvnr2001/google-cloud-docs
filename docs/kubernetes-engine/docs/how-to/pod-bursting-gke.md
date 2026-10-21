---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke/
title: Configure Pod bursting in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:11.487768+00:00
---

# Configure Pod bursting in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure Pod bursting in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to configure Pods to burst into available unused capacity on Google Kubernetes Engine (GKE) nodes.

## What is bursting?

_Bursting_ describes the action of Pods temporarily using more compute capacity on the node than they originally requested.

Kubernetes lets you request specific capacities of resources like CPU or memory for your Pods. You set these requests in your Pod manifest. The Kubernetes scheduler places your Pods on nodes that have enough capacity to accommodate those resource requests.

Some workloads don't use 100% of the requested resources for their entire run time. For example, a workload that consumes extra CPU during its boot period might not require the same amount of resources for normal operations. In these situations, you can set the resource limits for your workload to a higher value than the resource requests or leave the limits unset. GKE allows the workload to temporarily use more resources than you specified in the requests, if that capacity is available.

For more information about how this process works in GKE, see Burstable capacity in GKE in this page.

### Benefits of Pod bursting

Bursting is useful when your Pods only need additional resources for short periods of time to accommodate spikes in resource usage. Example scenarios include the following:

  * You have groups of workloads that are often idle and send a small number of requests per second, but occasionally experience spikes in traffic and would benefit from additional resources to process those requests.
  * Your workloads need more resources during startup than during normal operations.
  * You want to maximize the usage of the compute capacity that you provision.



Bursting lets you request only the resources that your Pod needs for the majority of its runtime and helps ensure that your Pod can consume more resources if needed. The benefits of bursting include the following:

  * **Lower running costs** : You don't need to request the expected peak resource consumption of the workload. Your requests can be for the lower steady-state values. In Autopilot, you pay for the sum of your Pod resource requests, so your running costs are lower.
  * **More efficient resource usage** : You avoid idle compute capacity because your Pods burst into unused capacity. Your workloads are more likely to use all of your paid-for resources.
  * **Improved performance** : Pods can use extra resources as needed to reduce the time to process incoming requests, or to boot up faster during scale-up events.



### When not to use bursting

Kubernetes assigns the `Burstable` _Quality of Service (QoS)_ class to Pods that specify higher resource limits than their requests. `Burstable` QoS Pods are more likely to be evicted when Kubernetes needs to reclaim resources on the node. For more information, see [Burstable QoS class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#burstable) in the Kubernetes documentation.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have a GKE Autopilot cluster running version 1.30.2-gke.1394000 or later, or any version of a GKE Standard cluster. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



### Bursting availability in GKE

Workloads can burst in the following situations:

Bursting availability  
---  
GKE Autopilot mode | The following types of Pods can burst in any GKE version that supports the hardware that the Pods request:

  * [Pods that request GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus)
  * [Pods that request a specific machine series](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/performance-pods)

For all other types of Pods, bursting becomes available when you restart the control plane after ensuring that the cluster meets all of the following conditions:

  * The cluster is running `cgroupv2`. Clusters created with GKE version 1.26 or later, or have migrated to `cgroupv2` will meet this condition. See [check the cgroup mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2#check-cgroup-mode) to determine the current cgroup version, and migrate if needed. 
  * The cluster is running GKE version 1.30.2-gke.1394000 or later.

For details, see [Limitations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#limitations).  
GKE Standard mode | Pods can burst in any GKE version.  
  
### Limitations

  * Autopilot workloads can only use bursting for CPU and memory requests.
  * When you upgrade an Autopilot cluster to a supported version, GKE upgrades the worker nodes to match the control plane version over time. A control plane restart is required to enable bursting, and must happen after all the nodes run a supported version and a supported cgroup mode. The control plane restarts automatically about once a week during operations like scaling, upgrades, or maintenance.

To trigger a control plane restart manually, do the following:

    1. Check whether all of your nodes run version 1.30.2-gke.1394000 or later:
           
           kubectl get nodes
           

The output is similar to the following:
           
           NAME                                          STATUS   ROLES    AGE     VERSION
           gk3-ap-cluster-1-default-pool-18092e49-mllk   Ready    <none>   4m26s   v1.30.2-gke.1349000
           

All of the nodes in the output must show the required version or later.

    2. Confirm that your cluster runs cgroupv2. For instructions, see [Check the cgroup mode](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2#check-cgroup-mode).

    3. Manually start a control plane upgrade to the same version that the cluster already uses.
           
           gcloud container clusters upgrade CLUSTER_NAME --master \
               --cluster-version CURRENT_CLUSTER_VERSION
           

Replace the following:

       * `CLUSTER_NAME`: the name of your existing cluster.
       * `CURRENT_CLUSTER_VERSION`: the version that your cluster is running.



## Connect to the cluster

Run the following command:
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
        --location=LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your existing cluster.
  * `LOCATION`: the location of your cluster.



## Verify that your cluster supports bursting

Bursting is always enabled in Standard mode clusters and for Autopilot mode workloads that request accelerators or specific machine series. Skip to the Deploy a burstable workload section.

The following types of Autopilot workloads can burst only if a GKE-managed DaemonSet named `efficiency-daemon` is running in the cluster:

  * Autopilot Pods that request the `Scale-Out` or `Balanced` [predefined compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use).
  * Autopilot Pods that don't request a compute class.



GKE deploys the `efficiency-daemon` DaemonSet when your Autopilot cluster meets the requirements for bursting, as described in the Bursting availability in GKE section.

To check whether the `efficiency-daemon` DaemonSet exists in your cluster, run the following command:
    
    
    kubectl get daemonset --namespace=kube-system efficiency-daemon
    

The output is similar to the following:
    
    
    NAME                DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE
    efficiency-daemon   1         1         1       1            1           <none>          105d
    

If the output is empty, ensure that the cluster meets all of the requirements and limitations in the Before you begin section.

## Deploy a burstable workload

  1. Save the following manifest as `burstable-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: helloweb
           labels:
             app: hello
         spec:
           selector:
             matchLabels:
               app: hello
               tier: web
           template:
             metadata:
               labels:
                 app: hello
                 tier: web
             spec:
               containers:
               - name: hello-app
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                 ports:
                 - containerPort: 8080
                 resources:
                   **requests :
                     cpu: 250m
                   limits:
                     cpu: 350m**
         

This manifest has the following fields to enable bursting:

     * `resources.requests`: The resources that the container requires to function. Set this value to the capacity that your container will need in the steady-state.
     * `resources.limits`: The maximum resource capacity that the container can use. Setting the limits higher than the requests lets Pods burst up to the specified limit if that capacity is available on the node. If you omit this field, the Pods can burst up to the available burstable capacity on the node. This capacity is calculated as follows: 
       * Autopilot mode: Unused capacity in the sum of the resource requests of Pods on the node.
       * Standard mode: Unused capacity in the node resources.
     * `spec.nodeSelector` and `spec.tolerations`: Optional. Add these fields with custom labels like `pod-type: "non-critical"` to tell GKE to create new nodes to run the burstable Pods. GKE applies taints to these new nodes to prevent other Pods, like critical workloads, from running on the same nodes. Autopilot enforces higher minimum resource requests for Pods that use workload separation. For details, see [Configure workload separation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) and [Resource requests in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#workload-separation).
  2. Deploy the workload:
         
         kubectl apply -f burstable-deployment.yaml
         

The workload might take a few minutes to start.

  3. Check the QoS class of a Pod:
         
         kubectl describe pod helloweb | grep -m 1 "QoS"
         

The output is the following:
         
         QoS Class: Burstable
         


**Success:** You created a burstable group of Pods and placed them in separate nodes in your cluster.

## Burstable capacity in GKE

To facilitate Pod bursting, GKE calculates the _burstable capacity_ for each node in a cluster. This calculation for a specific node is as follows:

  * Autopilot clusters:

    * Pods that request accelerators or request specific machine series: The node allocatable resource capacity, which is the capacity that's available for workload usage. For details , see [Node allocatable resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#node_allocatable_resources).
    * All other Pods: The sum of resource requests of all Pods on that node, regardless of the actual resource capacity of the node. If a Pod is terminated, the burstable capacity reduces by that Pod's requests. The portion of the burstable capacity that isn't in use by running Pods is available to allocate if one of the Pods needs to burst.

Autopilot also adds a predefined buffer to the burstable capacity so that any system Pods on the node that burst beyond their requests don't affect your own burstable Pods.

  * Standard clusters: The node allocatable resource capacity, which is the capacity that's available for workload usage. For details , see [Node allocatable resources](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#node_allocatable_resources).




## Best practices for bursting

Use the following practices with Pod bursting:

  * Set your resource requests equal to your limits for any Pods that provide critical functionality in your environment. This approach helps ensure that those Pods get the `Guaranteed` Kubernetes Quality of Service (QoS) class.
  * Ensure that you only configure memory bursting on Pods that can handle being evicted when Kubernetes needs to reclaim memory on the node.
  * Always request enough memory for your Pod to boot up. Don't rely on memory bursting to meet your boot requirements.
  * To prevent burstable Pods that consistently burst into multiples of their CPU requests from potentially disrupting critical workloads, use [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) to avoid placing those Pods alongside your critical Pods.



### Optimize burstable capacity in Autopilot nodes

Autopilot calculates the burstable capacity as the sum of resource requests of all the Pods on a specific node, including system Pods and DaemonSets. You can optimize the burstable capacity on a node in the following ways. However, bursting is opportunistic and isn't guaranteed.

  * To increase the burstable capacity on nodes for specific workloads, use [Pod affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) to place specific Pods together on the same node.
  * To ensure that a specific burstable capacity is always available on every node, create [DaemonSets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview#daemons) to run on all nodes in the cluster.



## Example of how bursting works

This section uses an example Deployment that has the following burstable Pods to demonstrate how Pod bursting works in GKE Autopilot clusters:

  * Pod 1 requests 250m CPU and has no CPU limit. Pod 1 uses 100m CPU to run.
  * Pod 2 requests 200m CPU and has a 250m CPU limit. Pod 2 uses 100m CPU to run.



Both Pods run on the same node. The _total burstable capacity_ on the node is 450m CPU (the sum of resource requests). Each Pod only uses 100m CPU to run, which means that the node has a remaining _available burstable capacity_ of 250m.

Consider the following scenarios in which a traffic spike occurs:

  * Pod 1 needs an additional 300m CPU: it can burst and use 250m CPU, which is the available burstable capacity. The node no longer has any available burstable capacity.
  * Pod 2 needs an additional 150m CPU: it can burst and use an extra 150m CPU. The node then has 100m CPU remaining of available burstable capacity.
  * Pod 2 needs an additional 200m CPU: it can burst and use 150m CPU, which brings the total usage to 250m CPU for Pod 2. Pod 2 has a 250m CPU limit and can't burst beyond that limit.



### How GKE handles Pods that exceed burstable capacity

If your burstable Pods try to use more resources than the burstable capacity on the node, GKE takes the following actions:

  * **CPU** : If the CPU usage exceeds the burstable capacity, GKE throttles the CPU usage of some containers so that all containers on the node get the CPU that they request.
  * **Memory** : If the memory usage exceeds the burstable capacity, GKE terminates containers to reclaim memory on the node. GKE starts by terminating resource-intensive containers in Pods with a lower QoS.



We recommend that you always request enough memory for normal Pod operation. If a container has a dependency on memory bursting to function normally, it might crash repeatedly if that memory isn't available.

### Use Pod bursting with spare capacity provisioning

GKE lets you deploy idle Pods to reserve extra compute capacity for faster Pod scaling during future high-traffic events like online store flash sales. Other Pods on the same node can burst into this unused reserved capacity so that the capacity isn't idle in the time leading up to your high-traffic event. You can reserve this capacity by using various Kubernetes mechanisms. For example, you can deploy Pods that have a low PriorityClass. For details, see [Provision extra compute capacity for rapid Pod scaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning).

## Pod bursting in GKE Standard clusters

GKE Standard clusters also support Pod bursting by setting the limits higher than the requests or by omitting limits. However, in Standard clusters, you must create and configure node pools with appropriate resource capacity to support bursting. Getting the potential cost reduction of burstable Pods in Standard clusters requires more careful node planning and Pod _bin-packing_ , because you pay for the underlying Compute Engine VMs.

Consider the following in Standard clusters:

  * The maximum resource consumption limit that triggers Kubernetes eviction or CPU throttling is the allocatable resource capacity on the node. To determine this value, see [Plan GKE Standard node sizes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#node_allocatable_resources).

  * Node resource usage in Standard clusters is more likely to reach a Kubernetes eviction threshold because GKE doesn't automatically limit resource consumption if you don't specify limits. Pods that burst into memory are therefore more likely to be terminated by Kubernetes [node-pressure eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/).




## What's next

  * Learn how to [provision extra compute capacity for rapid Pod scaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning).
  * Learn how to [right-size your GKE Standard workloads at scale](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/right-size-workloads-at-scale).
  * Learn how to [troubleshoot Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
