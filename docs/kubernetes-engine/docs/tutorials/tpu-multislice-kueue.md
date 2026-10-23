---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/tpu-multislice-kueue/
title: Orchestrate Multislice workloads using JobSet and Kueue \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:43.139767+00:00
---

# Orchestrate Multislice workloads using JobSet and Kueue  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/tpu-multislice-kueue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Orchestrate Multislice workloads using JobSet and Kueue Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This tutorial demonstrates how to orchestrate multiple multislice workloads on Google Kubernetes Engine (GKE) for improved resource utilization. You deploy a [Jax](https://github.com/google/jax) workload as an example, run it on TPU Multislice, and implement Job queueing with JobSet and [Kueue](https://kueue.sigs.k8s.io). Kueue determines when Jobs should run based on available resources, quotas, and a hierarchy for fair sharing among teams.

This tutorial is intended for Machine learning (ML) engineers and Platform admins and operators who are interested in the container orchestration capabilities of Kubernetes to train LLMs. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/anthos/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following:

  * Current TPU version availability with the [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions)
  * [TPU Multislice in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice)



## Objectives

  1. Prepare your environment with a GKE cluster with three v5e TPU slices. Each TPU slice has a `2x4` topology with 8 chips. Therefore, 24 TPU v5e TPU chips in total.
  2. Create the Kueue resources to ensure that quotas are shared fairly between the workloads.
  3. Run your Multislice workload.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Install JobSet](https://jobset.sigs.k8s.io/docs/installation/) v0.2.3 or later.

  * [Install Kueue](https://kueue.sigs.k8s.io/docs/installation/) v0.4.1 or later.




## Prepare the environment

  1. In the Google Cloud console, start a Cloud Shell instance:   
[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Set the default environment variables by using the by using the [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command:
         
         gcloud config set project PROJECT_ID
         

Replace PROJECT_ID with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




Autopilot clusters that run version 1.29.2-gke.1521000 or later enable TPUs by default. TPUs on Autopilot clusters are configured in the workload specification. For more information, see the Define your Multislice workloads with JobSets section.

### Create a GKE cluster

In Cloud Shell, create a GKE cluster:

###  Autopilot 
    
    
    gcloud container clusters create-auto multislice-cluster \
        --location=CONTROL_PLANE_LOCATION \
        --cluster-version 1.29.2-gke.1521000 \
        --release-channel rapid
    

In this command:

  * The `--location` flag specifies the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones) of the control plane of the cluster.
  * The `--cluster-version` flag specifies Kubernetes version for your cluster.
  * The `--release-channel` flag specifies the [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) for your cluster. In this case, the rapid channel supports the latest versions available in GKE.



###  Standard 
    
    
    gcloud container clusters create multislice-cluster \
        --location=CONTROL_PLANE_LOCATION
    

Replace CONTROL_PLANE_LOCATION with the location in which you want to create your cluster. Ensure it has capacity for the `ct5lp-hightpu-4t` machine type. Cluster creation might take several minutes.

If you use GKE Autopilot mode, skip to the Create the Kueue resources section. Autopilot clusters that run version 1.29.2-gke.1521000 or later enable TPUs by default.

### Create three Standard mode TPU slice node pools

In this section, you create TPU node pools by using the [`gcloud beta container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/node-pools/create) command.

  1. Create the first node pool named `nodepool1`:
         
         gcloud beta container node-pools create nodepool1 \
             --location=CONTROL_PLANE_LOCATION \
             --cluster=multislice-cluster \
             --node-locations=NODE_LOCATION \
             --machine-type=ct5lp-hightpu-4t \
             --tpu-topology=2x4 \
             --project=PROJECT_ID
         

Replace NODE_LOCATION with one or more zones in the cluster region in which you want to create the nodes.

  2. Create the second node pool named `nodepool2`:
         
         gcloud beta container node-pools create nodepool2 \
             --location=CONTROL_PLANE_LOCATION \
             --cluster=multislice-cluster \
             --node-locations=NODE_LOCATION \
             --machine-type=ct5lp-hightpu-4t \
             --tpu-topology=2x4 \
             --project=PROJECT_ID
         

  3. Create the third node pool named `nodepool3`:
         
         gcloud beta container node-pools create nodepool3 \
             --location=CONTROL_PLANE_LOCATION \
             --cluster=multislice-cluster \
             --node-locations=NODE_LOCATION \
             --machine-type=ct5lp-hightpu-4t \
             --tpu-topology=2x4 \
             --project=PROJECT_ID
         




GKE creates three node pools. Each node pool is a separate TPU slice.

In the preceding steps, you used the [`gcloud beta container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/node-pools/create) command to create the node pools. These commands use the following flags:

  * `--node-locations`: the comma-separated list of one or more zones where GKE creates the node pools.
  * `--machine-type`: the type of machine to use for nodes. In this case, you used `ct5lp-hightpu-4t`. For more information about TPU compatible machine types, use the table in [Choose the TPU version](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#choose-tpu-version).
  * `--tpu-topology`: the TPU topology to use for the node pool. In this case, you used `2x4`. For more information about TPU topologies, see [Choose the TPU topology](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#topology).



## Create the Kueue resources

  1. Create the following `kueue.yaml` manifest:
         
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: ResourceFlavor
         metadata:
           name: "vlp-24"
         spec:
           nodeLabels:
             cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
             cloud.google.com/gke-tpu-topology: 2x4
         ---
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: ClusterQueue
         metadata:
           name: "cluster-queue"
         spec:
           namespaceSelector: {}
           queueingStrategy: BestEffortFIFO
           resourceGroups:
           - coveredResources: ["google.com/tpu"]
             flavors:
             - name: "vlp-24"
               resources:
               - name: "google.com/tpu"
                 nominalQuota: 24
         
         ---
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: LocalQueue
         metadata:
           namespace: default
           name: multislice-queue
         spec:
           clusterQueue: cluster-queue
         

  2. Apply the `kueue.yaml` manifest:
         
         kubectl apply -f kueue.yaml
         




GKE creates the following Kueue resources:

  * [ResourceFlavor](https://kueue.sigs.k8s.io/docs/concepts/resource_flavor/): an abstraction of the resources in a cluster. In this example, GKE creates three TPU slices with `2x4` topology. Each TPU slice has a `2x4` topology with 8 chips (24 TPU chips in total).
  * [ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/): a global queue managing workloads and cluster resources.
  * [LocalQueue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/): groups closely related workloads that are typically run by a single tenant (user). Each LocalQueue points to a ClusterQueue from which resources are allocated to run its workloads. A [Kueue Workload](https://kueue.sigs.k8s.io/docs/concepts/workload/) is an abstraction representing a batch workload, in this case, each workload is a JobSet.



## Define your Multislice workloads with JobSets

In this section, you create three JobSets. A Jobset is a workload API that lets you manage a group of Kubernetes Jobs as a unit. The most common use case for a JobSet is distributed training, but you can also use it to run batch workloads.

The following JobSets run a Jax workload which outputs the global number of TPU chips in the slice, then sleeps for 60 seconds to simulate some model training time, then exits.

  1. Install the JobSet API in your cluster:
         
         VERSION=v0.8.1
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/$VERSION/manifests.yaml
         

  2. Create the following `jobsets-multislice.yaml` manifest:

###  Autopilot 
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: multislice-1slice
           labels:
             kueue.x-k8s.io/queue-name: multislice-queue
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 1
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 2x4
                       containers:
                       - name: jax-tpu
                         image: python:3.8
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         command:
                         - bash
                         - -c
                         - |
                           pip install "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                           python -c 'import jax; print("Global device count:", jax.device_count())'
                         resources:
                           limits:
                             google.com/tpu: 4
         
         ---
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: multislice-2slice
           labels:
             kueue.x-k8s.io/queue-name: multislice-queue
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 2
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 2x4
                       containers:
                       - name: jax-tpu
                         image: python:3.8
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         command:
                         - bash
                         - -c
                         - |
                           pip install "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                           python -c 'import jax; print("Global device count:", jax.device_count())'
                           sleep 60
                         resources:
                           limits:
                             google.com/tpu: 4
         ---
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: multislice-3slice
           labels:
             kueue.x-k8s.io/queue-name: multislice-queue
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 3
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 2x4
                       containers:
                       - name: jax-tpu
                         image: python:3.8
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         command:
                         - bash
                         - -c
                         - |
                           sleep 60
                         resources:
                           limits:
                             google.com/tpu: 4
         

###  Standard 
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: multislice-1slice
           labels:
             kueue.x-k8s.io/queue-name: multislice-queue
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 1
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       hostNetwork: true
                       dnsPolicy: ClusterFirstWithHostNet
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 2x4
                       containers:
                       - name: jax-tpu
                         image: python:3.8
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         securityContext:
                           privileged: true
                         command:
                         - bash
                         - -c
                         - |
                           pip install "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                           python -c 'import jax; print("Global device count:", jax.device_count())'
                         resources:
                           limits:
                             google.com/tpu: 4
         
         ---
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: multislice-2slice
           labels:
             kueue.x-k8s.io/queue-name: multislice-queue
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 2
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       hostNetwork: true
                       dnsPolicy: ClusterFirstWithHostNet
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 2x4
                       containers:
                       - name: jax-tpu
                         image: python:3.8
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         securityContext:
                           privileged: true
                         command:
                         - bash
                         - -c
                         - |
                           pip install "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
                           python -c 'import jax; print("Global device count:", jax.device_count())'
                           sleep 60
                         resources:
                           limits:
                             google.com/tpu: 4
         ---
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: multislice-3slice
           labels:
             kueue.x-k8s.io/queue-name: multislice-queue
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 3
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       hostNetwork: true
                       dnsPolicy: ClusterFirstWithHostNet
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 2x4
                       containers:
                       - name: jax-tpu
                         image: python:3.8
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         securityContext:
                           privileged: true
                         command:
                         - bash
                         - -c
                         - |
                           sleep 60
                         resources:
                           limits:
                             google.com/tpu: 4
         

  3. Apply the `jobsets-multislice.yaml` manifest:
         
         kubectl apply -f jobsets-multislice.yaml
         




GKE creates the Jobs with the following resource requests:

  * The `multislice-1slice` JobSet creates one Job that requires one TPU slice in total.
  * The `multislice-2slice` JobSet creates two Jobs that require two TPU slices in total.
  * The `multislice-3slice` JobSet creates three Jobs that require three TPU slice in total.



Because the cluster only has three TPU slices, not all JobSets can run at once. When Kueue enqueues all three of `multislice-3slice` JobSets, its Jobs run alone to completion. The `multislice-1slice` and `multislice-2slice` wait and run together afterwards.

**Note:** To mitigate any issues, ensure that your cluster has all the prerequisites listed in the [Before You Begin](https://jobset.sigs.k8s.io/docs/installation/#before-you-begin) section of the Jobset Installation documentation. If you encounter issues after ensuring your cluster meets the requirements, visit [Jobset Troubleshooting](https://jobset.sigs.k8s.io/docs/troubleshooting/).

### Verify Kueue admitted the workloads

  1. Check the enqueued workloads in Kueue:
         
         kubectl get workloads
         

The output is similar to the following:
         
         NAME                             QUEUE              ADMITTED BY     AGE
         jobset-multislice-1slice-2530a   multislice-queue                   3s
         jobset-multislice-2slice-ffb02   multislice-queue                   4s
         jobset-multislice-3slice-8c695   multislice-queue   cluster-queue   10s
         




Kueue enqueues one or more workloads, depending on the TPU resources they require.

## Monitor the workloads

JobSet and node pool observability metrics and dashboards in the Google Cloud console are generally available.

Training goodput and Cloud ML goodput observability metrics and dashboards in the Google Cloud console are in [Preview](https://cloud.google.com/products#product-launch-stages). To learn more about goodput, see [Introducing ML Productivity Goodput: a metric to measure AI system efficiency](https://cloud.google.com/blog/products/ai-machine-learning/goodput-metric-as-measure-of-ml-productivity).

### Dashboards

To view the status of your TPU multi-host node pools on GKE, go to the **GKE TPU Node Pool Status** dashboard provided by Cloud Monitoring:

[Go to GKE TPU Node Pool Status](https://console.cloud.google.com/monitoring/dashboards/integration/gke.gke-tpu-node-pool-status)

For more information, see [Monitor health metrics for TPU nodes and node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#tpu-node-pool-health-metrics).

To view comprehensive information about the health and performance of JobSets, go to the **JobSet monitoring** dashboard in the Google Cloud console:

[Go to JobSet monitoring dashboard](https://console.cloud.google.com/kubernetes/aiml/jobs)

The JobSet monitoring dashboard includes three tabs:

  * **Overview** : this tab shows the underlying JobSet infrastructure, such as JobSet status, replica readiness, and replica state. The tab also includes goodput metrics and some infrastructure metrics including CPU, GPU, TPU, memory, and storage metrics. For more information, see Monitor JobSet health with metrics.
  * **Training Goodput** ([Preview](https://cloud.google.com/products#product-launch-stages)): this tab provides a comprehensive view of the JobSet's end-to-end operational efficiency, such as the health of underlying node pools and actual workload execution. It provides goodput scores for you to monitor JobSet performance, including scheduling goodput and proxy runtime goodput . For more information, see Monitor JobSet goodput.
  * **Cloud ML Goodput** ([Preview](https://cloud.google.com/products#product-launch-stages)): this tab provides a detailed insight of the JobSet goodput, including badput breakdowns in the application layer.

To use this dashboard, you need to integrate with the [Goodput Measurement API](https://github.com/AI-Hypercomputer/ml-goodput-measurement/tree/main), and instrument the application to send goodput metrics. For more details, see the instructions in the [ML Goodput Measurement library](https://github.com/AI-Hypercomputer/ml-goodput-measurement/blob/main/README.md#usage).




### Monitor which Pods are running
    
    
    kubectl get pods
    

The output is similar to the following:
    
    
    NAME                                READY   STATUS      RESTARTS   AGE
    multislice-1slice-slice-0-0-pf2ll   1/1     Running     0          1s
    multislice-1slice-slice-0-1-55g62   1/1     Running     0          1s
    multislice-2slice-slice-0-0-f4hf7   1/1     Running     0          3s
    multislice-2slice-slice-0-1-c8kv7   1/1     Running     0          3s
    multislice-2slice-slice-1-0-7h46t   1/1     Running     0          3s
    multislice-2slice-slice-1-1-lj9hb   1/1     Running     0          3s
    multislice-3slice-slice-0-0-wzq9t   0/1     Completed   0          2m31s
    multislice-3slice-slice-0-1-zf4dp   0/1     Completed   0          2m30s
    multislice-3slice-slice-1-0-hbfn5   0/1     Completed   0          2m31s
    multislice-3slice-slice-1-1-45fgl   0/1     Completed   0          2m30s
    multislice-3slice-slice-2-0-wjbp4   0/1     Completed   0          2m30s
    multislice-3slice-slice-2-1-lwnvs   0/1     Completed   0          2m30s
    

See that GKE scheduled, created, and ran the Pods for `multislice-3slice` first. Then, GKE ran the Pods from `multislice-1slice` and `multislice-2slice` JobSets.

### Monitor JobSet health with metrics

To understand whether a JobSet is running as expected, or to infer whether it was interrupted, you can use Prometheus metrics from the [JobSet metrics package](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics#ksm-jobset-metrics), such as `kube_jobset_succeeded_replicas`.

Note that Jobset health metrics are supported only in GKE version 1.32.1-gke.135700 or later. JobSet health metrics are enabled by default in newly created clusters with supported versions. For existing clusters that are upgraded to supported versions, customers need to manually enable the JobSet metrics package. For more information, refer to the [documentation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/kube-state-metrics#requirements).

For this tutorial, check the JobSet completion with this PromQL query:
    
    
    kube_jobset_succeeded_replicas{
      cluster="multislice-cluster",
      jobset_name=~"mulitslice-.*"}
    

### Monitor JobSet scheduling

To monitor the scheduling of a JobSet, use the following metrics:

  * `kubernetes.io/jobset/assigned_node_pools`: GKE node pools where a Kubernetes JobSet has scheduled Pods.
  * `kubernetes.io/node_pool/assigned_jobsets`: Kubernetes JobSets that have scheduled Pods on a GKE node pool.
  * `kubernetes.io/jobset/assigned_nodes`: GKE nodes where a Kubernetes JobSet has scheduled Pods.
  * `kubernetes.io/node/assigned_jobsets`: Kubernetes JobSets that have scheduled Pods on a GKE node.



To view the node pools where each JobSet in a specific cluster has scheduled Pods, run the following PromQL query:
    
    
    avg_over_time(
      kubernetes_io:jobset_assigned_node_pools{
        monitored_resource="k8s_entity",
        cluster_name="multislice-cluster"}[${__interval}])
    

To identify the node pools where a specific Jobset has been scheduled, run the following PromQL query:
    
    
    avg_over_time(
      kubernetes_io:jobset_assigned_node_pools{
        monitored_resource="k8s_entity",
        cluster_name="multislice-cluster",
        entity_name=~"multislice-.*"}[${__interval}])
    

To identify the Jobsets that have been scheduled on a specific node pool, run the following PromQL query:
    
    
    avg_over_time(
      kubernetes_io:node_pool_assigned_jobsets{
        monitored_resource="k8s_node_pool",
        cluster_name="multislice-cluster",
        node_pool_name="multislice-np"}[${__interval}])
    

### Monitor JobSet uptime, times to recover (TTR), and times between interruptions (TBI)

The following metrics are useful for monitoring the availability of a JobSet:

  * `kubernetes.io/jobset/uptime`: total time the JobSet has been available.
  * `kubernetes.io/jobset/times_to_recover`: distribution of recovery period for a JobSet. Each sample indicates a single recovery event from a downtime period for the JobSet.
  * `kubernetes.io/jobset/times_between_interruptions`: distribution of the interval between the end of the previous interruption and the beginning of the current interruption for a JobSet. Each sample indicates a single duration between the previous and the current interruption.



These metrics apply to JobSets that have exactly one GPU or TPU replicated job. The calculation of the metrics is based only on the availability of that single replicated job. The metrics are supported in all GKE versions.

To view uptime for the JobSets that you used in this tutorial, run the following PromQL query:
    
    
    avg_over_time(
      kubernetes_io:jobset_uptime{
        monitored_resource="k8s_entity", entity_type="jobset",
        entity_name=~"multislice-.*",cluster_name="multislice-cluster"}[${__interval}])
    

To view the TBI distributions for the JobSets from this tutorial, run the following PromQL query:
    
    
    histogram_quantile(0.50,
      sum_over_time(
        kubernetes_io:jobset_times_between_interruptions_bucket{
          monitored_resource="k8s_entity",entity_type="jobset",
          entity_name=~"multislice-.*",cluster_name="multislice-cluster"}[${__interval}]))
    

You can extend the interval of the query to a longer time horizon, such as 7 days, and compute the mean time between interruptions (MTBI) over this period:
    
    
    sum(sum_over_time(
      kubernetes_io:jobset_times_between_interruptions_sum{
        monitored_resource="k8s_entity",entity_type="jobset",
        entity_name=~"multislice-.*",cluster_name="multislice-cluster"}[${__interval}]))
    /
    sum(sum_over_time(
      kubernetes_io:jobset_times_between_interruptions_count{
        monitored_resource="k8s_entity",entity_type="jobset",
        entity_name=~"multislice-.*",cluster_name="multislice-cluster"}[${__interval}]))
    

To view the TTR distributions, you can run the following PromQL queries:
    
    
    histogram_quantile(0.50,
      sum_over_time(
        kubernetes_io:jobset_times_to_recover_bucket{
          monitored_resource="k8s_entity",entity_type="jobset",
          entity_name=~"multislice-.*",cluster_name="multislice-cluster"}[${__interval}]))
    

After you increase the query interval to a longer time horizon, such as 7 days, you can compute the mean time to recover (MTTR) over this period:
    
    
    sum(sum_over_time(
      kubernetes_io:jobset_times_to_recover_sum{
        monitored_resource="k8s_entity",entity_type="jobset",
        entity_name=~"multislice-.*",cluster_name="multislice-cluster"}[${__interval}]))
    /
    sum(sum_over_time(
      kubernetes_io:jobset_times_to_recover_count{
        monitored_resource="k8s_entity",entity_type="jobset",
        entity_name=~"multislice-.*",cluster_name="multislice-cluster"}[${__interval}]))
    

**Success:** You've successfully run a three Multislice Jax workloads.

### Monitor JobSet goodput

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following metrics are useful for monitoring the performance of a JobSet:

  * `kubernetes.io/jobset/scheduling_goodput`: the fraction of time that all the resources required to run the training JobSet are available.
  * `kubernetes.io/jobset/proxy_runtime_goodput`: the fraction of time that all required accelerators are productive. This metric provides an estimate of the real runtime goodput.

If you need a more accurate measure of runtime goodput, you can instrument your application and integrate with the [Goodput Measurement API](https://github.com/AI-Hypercomputer/ml-goodput-measurement/tree/main). For more details, see the instructions in the [ML Goodput Measurement library](https://github.com/AI-Hypercomputer/ml-goodput-measurement/blob/main/README.md#usage).




To view the scheduling goodput for the JobSet that you used in this tutorial, run the following PromQL query:
    
    
    avg_over_time(
      kubernetes_io:jobset_scheduling_goodput{
        monitored_resource="k8s_entity", entity_type="jobset",
        entity_name=~"multislice-.*",
        cluster_name="multislice-cluster"}[${__interval}])
    

To view the proxy runtime goodput for the JobSets from this tutorial, run the following PromQL query:
    
    
    avg_over_time(
      kubernetes_io:jobset_proxy_runtime_goodput{
        monitored_resource="k8s_entity", entity_type="jobset",
        entity_name=~"multislice-.*",
        cluster_name="multislice-cluster"}[${__interval}])
    

## Enable Kueue workload priorities and preemption

Optionally, you can assign Kueue workloads priorities which determine the order in which enqueued workloads are admitted by Kueue.

**Note:** Depending on the configuration of the ClusterQueue's preemption policy, some preemption scenarios might occur. For example, GKE can preempt a running workload to run a higher priority workload if there are not sufficient resources to run both workloads concurrently. GKE stops and re-enqueues a preempted workload to be continue processing when possible.

  1. Update your `ClusterQueue` to have a preemption policy:
         
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: ResourceFlavor
         metadata:
           name: "vlp-24"
         spec:
           nodeLabels:
             cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
             cloud.google.com/gke-tpu-topology: 2x4
         ---
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: ClusterQueue
         metadata:
           name: "cluster-queue"
         spec:
           namespaceSelector: {}
           resourceGroups:
           - coveredResources: ["google.com/tpu"]
             flavors:
             - name: "vlp-24"
               resources:
               - name: "google.com/tpu"
                 nominalQuota: 24
           **preemption :
             reclaimWithinCohort: Any
             withinClusterQueue: LowerPriority**
         ---
         apiVersion: kueue.x-k8s.io/v1beta1
         kind: LocalQueue
         metadata:
           namespace: default
           name: multislice-queue
         spec:
           clusterQueue: cluster-queue
         

  2. Create a `PriorityClass` for each distinct priority level you want to assign to workloads:
         
         apiVersion: scheduling.k8s.io/v1
         kind: PriorityClass
         metadata:
           name: low-priority
         value: 100
         globalDefault: false
         description: "This low priority class should be used for some Pods only."
         

  3. Assign the `priorityClassName` to your JobSet:

###  Autopilot 
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: low-priority
           labels:
             kueue.x-k8s.io/queue-name: multislice-queue
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 1
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 2x4
                       priorityClassName: low-priority
                       containers:
                       - name: jax-tpu
                         image: python:3.8
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         command:
                         - bash
                         - -c
                         - |
                           sleep 60
                         resources:
                           limits:
                             google.com/tpu: 4 # Number of TPU chips per worker
         

###  Standard 
         
         apiVersion: jobset.x-k8s.io/v1alpha2
         kind: JobSet
         metadata:
           name: low-priority
           labels:
             kueue.x-k8s.io/queue-name: multislice-queue
           annotations:
             alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
         spec:
           failurePolicy:
             maxRestarts: 4
           replicatedJobs:
             - name: slice
               replicas: 1
               template:
                 spec:
                   parallelism: 2
                   completions: 2
                   backoffLimit: 0
                   template:
                     spec:
                       hostNetwork: true
                       dnsPolicy: ClusterFirstWithHostNet
                       nodeSelector:
                         cloud.google.com/gke-tpu-accelerator: tpu-v5-lite-podslice
                         cloud.google.com/gke-tpu-topology: 2x4
                       priorityClassName: low-priority
                       containers:
                       - name: jax-tpu
                         image: python:3.8
                         ports:
                         - containerPort: 8471
                         - containerPort: 8080
                         securityContext:
                           privileged: true
                         command:
                         - bash
                         - -c
                         - |
                           sleep 60
                         resources:
                           limits:
                             google.com/tpu: 4 # Number of TPU chips per worker
         




GKE includes a preemption policy, which defines how Kueue assigns the available resources. The policy specifies that a workload can be preempted if a higher priority workload needs the resources. Workloads with a lower priority value are more likely to be preempted by higher priority workloads.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the individual resource

  1. Delete the Kueue resources:
         
         kubectl delete -f jobsets-multislice.yaml
         kubectl delete -f kueue.yaml
         

  2. Delete the cluster:
         
         gcloud container clusters delete multislice-cluster --location=CONTROL_PLANE_LOCATION
         




## What's next

  * Learn more about [Kueue](https://kueue.sigs.k8s.io/docs/overview/).
  * Learn how to [Implement a Job queuing system with quota sharing between namespaces on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-cohort).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
