---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas/
title: Schedule GKE workloads with TAS \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:06.635591+00:00
---

# Schedule GKE workloads with TAS  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Schedule GKE workloads with TAS Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus) [ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

AI and ML workloads require significant Pod-to-Pod communication. Because of this requirement, network bandwidth between Pods directly impacts workload execution time and cost. This bandwidth depends on the placement of the virtual machine (VM) instances in the cluster.

This document explains how to optimize the scheduling of your large-scale AI or ML workloads on a Google Kubernetes Engine (GKE) cluster for both performance and reliability. Specifically, you configure your cluster to use Topology Aware Scheduling (TAS) for low-latency communication. This approach minimizes communication overhead and helps maximize performance for your workloads.

## What is Topology Aware Scheduling (TAS)?

[TAS](https://kueue.sigs.k8s.io/docs/concepts/topology_aware_scheduling/) can significantly improve the efficiency of large language model (LLM) training. TAS strategically places workers on the network topology to minimize communication overhead during gradient aggregation, which requires workers to communicate in a specific rank order. By minimizing network hops between sequentially communicating workers, TAS reduces network contention and optimizes bandwidth utilization, leading to faster convergence and shorter training times. With increasingly large LLM models, TAS is essential for maximizing the performance and scalability of distributed training.

TAS works best with densely placed capacity, which can be obtained through reservation-bound capacity. With Spot VMs and other [consumption options](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models), your capacity is less likely to be allocated close together, so TAS might not work well in this scenario.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * To connect to your cluster, run the following command:
        
        gcloud container clusters get-credentials CLUSTER_NAME
        

Replace `CLUSTER_NAME` with the name of your cluster.




## Prepare your GKE cluster

To prepare your GKE cluster to run workloads with TAS, complete the following steps:

  1. Install Kueue with TAS enabled
  2. View the topology of your GKE cluster

  3. Configure Kueue




### Install Kueue with TAS enabled

We recommend that you use TAS with [Kueue](https://kueue.sigs.k8s.io/docs/overview/), a Kubernetes-native system that manages quotas and how jobs should consume them. TAS requires Kueue version `0.10.0` or later, and you must explicitly enable it.

To install Kueue and enable TAS, select one of the following options:

###  Kueue manifest 

  1. Install Kueue:
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/kueue/releases/download/v0.10.0/manifests.yaml
         

  2. Enable TAS in Kueue:
         
         kubectl -n kueue-system patch deployment kueue-controller-manager \
             --type json -p='[{"op": "add", "path": "/spec/template/spec/containers/0/args/-", "value": "--feature-gates=TopologyAwareScheduling=true"}]'
         




###  Helm chart 

Install Kueue with TAS enabled by using a Helm chart:
    
    
    helm install kueue oci://us-central1-docker.pkg.dev/k8s-staging-images/charts/kueue \
        --version="v0.10.0" \
        --create-namespace \
        --namespace=kueue-system \
        --set="controllerManager.featureGates[0].name=TopologyAwareScheduling,controllerManager.featureGates[0].enabled=true"
    

After you install Kueue, you must configure it to understand the infrastructure that it's managing, as explained in the next section.

### View the topology of your GKE cluster

Before you view the topology of A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) nodes provisioned as Spot VMs, you must define [compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement) on the GKE nodes to expose their physical topology for TAS. Otherwise, you encounter errors.

To view the topology of your GKE cluster nodes in a specific node pool, run the following command:
    
    
    kubectl get nodes -l cloud.google.com/gke-nodepool=NODE_POOL_NAME \
        -ocustom-columns='NAME:.metadata.name,BLOCK:.metadata.labels.cloud\.google\.com/gce-topology-block,SUBBLOCK:.metadata.labels.cloud\.google\.com/gce-topology-subblock,HOST:.metadata.labels.cloud\.google\.com/gce-topology-host' | sort -k2,4
    

Replace `NODE_POOL_NAME` with the name of the node pool.

To understand the physical topology of GKE nodes on your VMs in the output, refer to the following node labels:

  * **`cloud.google.com/gce-topology-block`** : the organization-specific ID of the reserved block in which the VM is located.

  * **`cloud.google.com/gce-topology-subblock`** : the organization-specific ID of the sub-block in which the VM is located.

  * **`cloud.google.com/gce-topology-host`** : the ID of the host on which the VM is located.

  * **`kubernetes.io/hostname`** : the hostname of the Kubernetes node. This hostname is typically also the GKE node name.




The more label values two VMs share, the closer the VMs are physically located next to each other. For more information about these terms, see [Terminology](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology).

### Configure Kueue

After you install Kueue, you must configure Kueue to specify the infrastructure that it's managing. Typically, Kueue requires a [ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/) resource quota definition of either static infrastructure, or dynamic infrastructure with cluster autoscaling enabled. The ClusterQueue admits a [Workload](https://kueue.sigs.k8s.io/docs/concepts/workload/) only if the resources that the workload requests are less than or equal to the pool of resources defined in the ClusterQueue. After you configure Kueue as described in this section, Kueue admits workloads using the TAS as follows:

  * **TAS workloads** : Kueue checks both the topology of the physical infrastructure and its current usage.

  * **Non-TAS workloads** : Kueue doesn't check the topology of the physical infrastructure. Kueue manages the entire quota defined in the config and leaves node assignment to kube-scheduler.




To understand how to provide a ClusterQueue resource quota definition to Kueue, review the following examples:

  * **Very high quota** : Kueue practically never stops admission of a workload based on the requested resources. Based on the TAS definitions, Kueue may or may not admit workloads based on the infrastructure topology. For more information, see Very high resource quota.

  * **Realistic quota** : Kueue admits the Workload only if the resources that Workload requests are within these resource quota limits. Based on the TAS definitions, Kueue then checks the infrastructure topology before admitting the Workload. For more information, see Realistic resource quota.




All references to resource quota in the following sections refer to ClusterQueue resource quota.

#### Very high resource quota

The following example uses a very high resource quota, such that Kueue never stops a workload based on the available resource quota. Rather, Kueue uses the topology information of available nodes to try and match the topology with the requirements of the workload.

To use the following resource quota definition, complete the following steps:

  1. Open a file editor of your choice. Then, include the following quota definition in a YAML file named `kueue-tas-config-very-high-quota.yaml`:
         
         apiVersion: kueue.x-k8s.io/v1alpha1
           kind: Topology
           metadata:
             name: "gke-default"
           spec:
             levels:
             - nodeLabel: "cloud.google.com/gce-topology-block"
             - nodeLabel: "cloud.google.com/gce-topology-subblock"
             - nodeLabel: "cloud.google.com/gce-topology-host"
             - nodeLabel: "kubernetes.io/hostname"
         ---
           kind: ResourceFlavor
           apiVersion: kueue.x-k8s.io/v1beta1
           metadata:
             name: "tas-flavor"
           spec:
             nodeLabels:
               cloud.google.com/gke-nodepool: "NODE_POOL_NAME"
             topologyName: "gke-default"
             tolerations:
             - key: "nvidia.com/gpu"
               operator: "Exists"
               effect: NoSchedule
         ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: ClusterQueue
           metadata:
             name: "tas-cluster-queue"
           spec:
             namespaceSelector: {}
             resourceGroups:
             - coveredResources: ["nvidia.com/gpu"]
               flavors:
               - name: "tas-flavor"
                 resources:
                 - name: "nvidia.com/gpu"
                   nominalQuota: 10000000
         ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: LocalQueue
           metadata:
             namespace: "default"
             name: "tas-user-queue"
           spec:
             clusterQueue: "tas-cluster-queue"
         

Replace `NODE_POOL_NAME` with the name of the node pool.

  2. Create and apply the resource quota configuration for the Kueue job queueing system:
         
         kubectl create -f kueue-tas-config-very-high-quota.yaml
         




#### Realistic resource quota

The previous example only configured GPU resources. However, Kueue can manage all Kubernetes-compatible resources.

The following example defines a more-realistic resource quota, including CPU, memory, and GPU. This is for 100 `a3-ultragpu-8g` machines. A single machine has 224 vCPUs, 2944 GB of memory, and 8 GPUs. The same principle applies to [General GPU](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) (A2, A3 Edge, G2, G4, and N1) machine types, using their respective CPU and memory specifications.

To use the following resource quota definition, complete the following steps:

  1. Open a file editor of your choice. Then, include the following quota definition in a YAML file named `kueue-tas-config-real-quota.yaml`:
         
         apiVersion: kueue.x-k8s.io/v1alpha1
           kind: Topology
           metadata:
             name: "gke-default"
           spec:
             levels:
             - nodeLabel: "cloud.google.com/gce-topology-block"
             - nodeLabel: "cloud.google.com/gce-topology-subblock"
             - nodeLabel: "cloud.google.com/gce-topology-host"
             - nodeLabel: "kubernetes.io/hostname"
         ---
           kind: ResourceFlavor
           apiVersion: kueue.x-k8s.io/v1beta1
           metadata:
             name: "tas-flavor"
           spec:
             nodeLabels:
               cloud.google.com/gke-nodepool: "NODE_POOL_NAME"
             topologyName: "gke-default"
             tolerations:
             - key: "nvidia.com/gpu"
               operator: "Exists"
               effect: NoSchedule
         ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: ClusterQueue
           metadata:
             name: "tas-cluster-queue"
           spec:
             namespaceSelector: {} # match all
             resourceGroups:
             - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
               flavors:
               - name: "tas-flavor"
                 resources:
                 # numbers below represent quota of 100 a3-ultragpu-8g machines
                 - name: "cpu"
                   nominalQuota: 22400
                 - name: "memory"
                   nominalQuota: 294400Gi
                 - name: "nvidia.com/gpu"
                   nominalQuota: 800
         ---
           apiVersion: kueue.x-k8s.io/v1beta1
           kind: LocalQueue
           metadata:
             namespace: "default"
             name: "tas-user-queue"
           spec:
             clusterQueue: "tas-cluster-queue"
         

Replace `NODE_POOL_NAME` with the name of the node pool.

  2. Create and apply a resource quota configuration for the Kueue job queueing system:
         
         kubectl create -f kueue-tas-config-real-quota.yaml
         

The output is similar to the following:
         
         topology.kueue.x-k8s.io/gke-default created
         resourceflavor.kueue.x-k8s.io/tas-flavor created
         clusterqueue.kueue.x-k8s.io/tas-cluster-queue created
         localqueue.kueue.x-k8s.io/tas-user-queue created
         




## Schedule workloads with TAS using Kueue

The following scenarios show how you can instruct Kueue and TAS to manage common workload and infrastructure combinations using topology request types and topology request levels:

  * The following are the available topology request _types_ (preferred or required):

    * **`kueue.x-k8s.io/podset-preferred-topology`** : Kueue prioritizes scheduling the entire workload within a given topology level, but still admits a workload that doesn't fit within this topology level. For a workload that might have fit in a single topology level, Kueue might schedule that workload across multiple instances of that topology level.

    * **`kueue.x-k8s.io/podset-required-topology`** : Kueue continues trying to admit this workload until the entire workload can fit within the chosen topology level.

  * The following are the available topology request _levels_ , letting you be more or less specific about the physical infrastructure where you prefer or require your Job to run:

    * `cloud.google.com/gce-topology-block`

    * `cloud.google.com/gce-topology-subblock`

    * `cloud.google.com/gce-topology-host`

    * `kubernetes.io/hostname`




To schedule workloads using these values, use the following Job YAML file:
    
    
    apiVersion: batch/v1
    kind: Job
    metadata:
      generateName: JOB_NAME
      labels:
        kueue.x-k8s.io/queue-name: tas-user-queue
    spec:
      parallelism: NUMBER_OF_REPLICAS
      completions: NUMBER_OF_REPLICAS
      completionMode: Indexed
      template:
        metadata:
          annotations:
            ANNOTATIONS_STRING
        spec:
          containers:
          - name: dummy-job
            image: gcr.io/k8s-staging-perf-tests/sleep:v0.1.0
            args: ["60s"]
            resources:
              requests:
                nvidia.com/gpu: "1"
              limits:
                nvidia.com/gpu: "1"
          restartPolicy: Never
    

Replace the following variables:

  * `JOB_NAME`: a name for the Job.

  * `NUMBER_OF_REPLICAS`: the number of Pods that are running in parallel.

  * `ANNOTATIONS_STRING`: see the following table:

Requested topology type and level | Description | `ANNOTATIONS_STRING`  
---|---|---  
**Preferred** to run within a **hostname** (recommended) | This configuration will admit your workload as long as there are enough resources available to satisfy your workload's resource requirements, even if the capacity is fragmented. Kueue will schedule your Pods as compactly as possible. | `kueue.x-k8s.io/podset-preferred-topology: "kubernetes.io/hostname"`  
**Required** to run within a **host** |  This configuration will admit your workload if and only if there is a host available with enough resources to satisfy your workload's resource requirements.  This is useful when there are multiple VMs per host (for example, smaller machine types) or multiple Pods can run on a single node. In such cases, if the workload is admitted, it will run on a single host. | `kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-host"`  
**Preferred** to run within a **host** | This configuration will admit your workload as long as there are enough resources available to satisfy your workload's resource requirements, even if the capacity is fragmented. Kueue will try to schedule your Pods within a host and will use additional hosts if needed. | `kueue.x-k8s.io/podset-preferred-topology: "cloud.google.com/gce-topology-host"`  
**Required** to run within a **sub-block** | This configuration will admit your workload if and only if there is a sub-block available with enough resources to satisfy your workload's resource requirements. | `kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-subblock"`  
**Preferred** to run within a **sub-block** | This configuration will admit your workload as long as there are enough resources available to satisfy your workload's resource requirements, even if the capacity is fragmented. Kueue will try to schedule your Pods within a sub-block and will use additional sub-blocks if needed. In this case, Kueue will rank higher a sub-block with more available capacity even if it is fragmented compared to a sub-block with just enough capacity to satisfy the requirements. | `kueue.x-k8s.io/podset-preferred-topology: "cloud.google.com/gce-topology-subblock"`  
**Required** to run within a **block** | This configuration will admit your workload if and only if the resources available within a block satisfy your workload's resource requirements. If admitted, Kueue will minimize the number of sub-blocks and hosts to schedule the workload. This might result in fragmentation of your available capacity. | `kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-block"`  
**Preferred** to run within a **block** | This configuration will admit your workload as long as there are enough resources available to satisfy your workload's resource requirements, even if the capacity is fragmented. Kueue will try to schedule your Pods within a block and will use additional blocks if needed. | `kueue.x-k8s.io/podset-preferred-topology: "cloud.google.com/gce-topology-block"`  



### Schedule workloads using PodGroup with TAS using Kueue

When using PodGroups, you must specify three additional fields for every Pod in a PodGroup:

  * **Labels** :

    * **[kueue.x-k8s.io/pod-group-name](http://kueue.x-k8s.io/pod-group-name)** : the name of a PodGroup used for aggregation.

    * **[kueue.x-k8s.io/pod-group-pod-index](http://kueue.x-k8s.io/pod-group-pod-index)** : the index of each individual Pod within the PodGroup.

  * **Annotations** :

    * **[kueue.x-k8s.io/pod-group-total-count](http://kueue.x-k8s.io/pod-group-total-count)** : the total count of Pods within a PodGroup.



Depending on the ML framework that you use, a leader of a PodGroup can either require a GPU or not. Because of a limitation of Kueue, these cases need to be handled differently. The following examples demonstrate how to create a PodGroup of three Pods with one leader and two workers.

#### Case 1: Leader is also a worker and requires a GPU

If the leader is one of the workers and also requires a GPU, then the leader can have any number within the PodGroup. For simplicity, in the following example the index of the leader is `0`:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      generateName: tas-podgroup-leader-
      labels:
        kueue.x-k8s.io/queue-name: tas-user-queue
        kueue.x-k8s.io/pod-group-name: "tas-podgroup-example-group"
        kueue.x-k8s.io/pod-group-pod-index: "0"
      annotations:
        kueue.x-k8s.io/pod-group-total-count: "3"
        kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-block"
    spec:
      containers:
      - name: leader
        image: gcr.io/k8s-staging-perf-tests/sleep:v0.1.0
        args: ["600s"]
        resources:
          requests:
            nvidia.com/gpu: "1"
          limits:
            nvidia.com/gpu: "1"
      restartPolicy: Never
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      generateName: tas-podgroup-worker-1-
      labels:
        kueue.x-k8s.io/queue-name: tas-user-queue
        kueue.x-k8s.io/pod-group-name: "tas-podgroup-example-group"
        kueue.x-k8s.io/pod-group-pod-index: "1"
      annotations:
        kueue.x-k8s.io/pod-group-total-count: "3"
        kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-block"
    spec:
      restartPolicy: Never
      containers:
      - name: worker
        image: gcr.io/k8s-staging-perf-tests/sleep:v0.1.0
        args: ["600s"]
        resources:
          requests:
            nvidia.com/gpu: "1"
          limits:
            nvidia.com/gpu: "1"
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      generateName: tas-podgroup-worker-2-
      labels:
        kueue.x-k8s.io/queue-name: tas-user-queue
        kueue.x-k8s.io/pod-group-name: "tas-podgroup-example-group"
        kueue.x-k8s.io/pod-group-pod-index: "2"
      annotations:
        kueue.x-k8s.io/pod-group-total-count: "3"
        kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-block"
    spec:
      restartPolicy: Never
      containers:
      - name: worker
        image: gcr.io/k8s-staging-perf-tests/sleep:v0.1.0
        args: ["600s"]
        resources:
          requests:
            nvidia.com/gpu: "1"
          limits:
            nvidia.com/gpu: "1"
    

#### Case 2: Leader is not a worker and doesn't require a GPU

If the leader isn't one of the workers because of the Kueue limitation, the leader must have the last index in the PodGroup, because of how Kueue creates PodSets. If the leader doesn't have the last index and the first worker doesn't use the first index, Kueue won't apply rank assignments.

See the following example:
    
    
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      generateName: tas-podgroup-leader-
      labels:
        kueue.x-k8s.io/queue-name: tas-user-queue
        kueue.x-k8s.io/pod-group-name: "tas-podgroup-example-group2"
        kueue.x-k8s.io/pod-group-pod-index: "2"
      annotations:
        kueue.x-k8s.io/pod-group-total-count: "3"
        kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-block"
    spec:
      containers:
      - name: leader
        image: gcr.io/k8s-staging-perf-tests/sleep:v0.1.0
        args: ["600s"]
        resources:
          requests:
            cpu: "1"
          limits:
            cpu: "1"
      restartPolicy: Never
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      generateName: tas-podgroup-worker-0-
      labels:
        kueue.x-k8s.io/queue-name: tas-user-queue
        kueue.x-k8s.io/pod-group-name: "tas-podgroup-example-group2"
        kueue.x-k8s.io/pod-group-pod-index: "0"
      annotations:
        kueue.x-k8s.io/pod-group-total-count: "3"
        kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-block"
    spec:
      restartPolicy: Never
      containers:
      - name: worker
        image: gcr.io/k8s-staging-perf-tests/sleep:v0.1.0
        args: ["600s"]
        resources:
          requests:
            nvidia.com/gpu: "1"
          limits:
            nvidia.com/gpu: "1"
    ---
    apiVersion: v1
    kind: Pod
    metadata:
      generateName: tas-podgroup-worker-1-
      labels:
        kueue.x-k8s.io/queue-name: tas-user-queue
        kueue.x-k8s.io/pod-group-name: "tas-podgroup-example-group2"
        kueue.x-k8s.io/pod-group-pod-index: "1"
      annotations:
        kueue.x-k8s.io/pod-group-total-count: "3"
        kueue.x-k8s.io/podset-required-topology: "cloud.google.com/gce-topology-block"
    spec:
      restartPolicy: Never
      containers:
      - name: worker
        image: gcr.io/k8s-staging-perf-tests/sleep:v0.1.0
        args: ["600s"]
        resources:
          requests:
            nvidia.com/gpu: "1"
          limits:
            nvidia.com/gpu: "1"
    

## What's next

  * To learn more about enabling health node prediction in your GKE cluster, see [Enable node health prediction](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction).

  * To learn about managing common events relevant to GKE clusters and AI workloads, see [Manage AI-optimized GKE clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/manage-gke-clusters).

  * To learn more about scheduling jobs on GKE with Kueue, see [Deploy a batch system using Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro).

  * To deploy GKE clusters with preconfigured Kueue and TAS blueprints, see [GKE deployments overview in Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-deployments-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
