---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform/
title: Choose a minimum CPU platform \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:23.780184+00:00
---

# Choose a minimum CPU platform  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Choose a minimum CPU platform Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to specify a minimum CPU platform for nodes in Google Kubernetes Engine (GKE) clusters.

## Why choose a minimum CPU platform?

Specifying a minimum CPU platform is useful if you require specific CPU capabilities and specifications, such as a high base frequency or optimized power management functionality.

Some advanced compute-intensive workloads in graphics, gaming, and analytics industries can make use of the specific features available through different CPU platform feature sets, such as AVX-2 and AVX-512. Choosing a specific CPU platform can yield substantial boosts in execution time and performance. By specifying a minimum CPU platform, your workloads can realize these gains in a more predictable manner, and you can ensure that your nodes never use a CPU platform inappropriate for their workloads.

## How to choose a platform

The following table shows you how to choose a minimum CPU platform based on how you use GKE:

Scope | Description | Supported cluster configuration  
---|---|---  
Workload-level (recommended) | Choose a minimum platform in your Pod specification. GKE schedules those Pods as follows:

  * **Autopilot** : GKE schedules Pods on nodes with the specified platform or later.
  * **Standard** : GKE only schedules Pods on nodes with the specified platform. For example, if an Intel Ice Lake node pool exists and new Pods request a minimum of Intel Cascade Lake, GKE creates a new node pool with Intel Cascade Lake, even though Intel Ice Lake is a more advanced platform.

| 

  * Autopilot running GKE version 1.25 and later.
  * Standard with [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable) running GKE version 1.23 and later.

  
Node and cluster level | Choose a minimum CPU platform when you create a new Standard mode cluster or node pool. This setting doesn't support node auto-provisioning. For instructions, skip to Choose a minimum CPU platform at the node pool level. | New Standard cluster or node pool   
  
## Pricing

You can choose a minimum CPU platform at no additional cost.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Check CPU platform availability

The available CPU platforms varies based on the [compute zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) in which your nodes run. You should check which CPU platforms are available in a zone even if you use Autopilot clusters or regional Standard clusters.

To check the available platforms in a specific zone, run the following command:
    
    
    gcloud compute zones describe COMPUTE_ZONE
    

Replace `COMPUTE_ZONE` with the name of a zone, such as `us-central1-a`. If you use a regional cluster type, specify the name of a zone in that region.

The output is similar to the following:
    
    
    availableCpuPlatforms:
    - Intel Ice Lake
    - Intel Cascade Lake
    - Intel Skylake
    - Intel Broadwell
    - Intel Haswell
    - Intel Ivy Bridge
    - Intel Sandy Bridge
    - AMD Milan
    - AMD Rome
    - Ampere Altra
    - Intel Sapphire Rapids
    

When you use these values to request a minimum CPU platform, replace spaces with underscores in the platform name. For example, `AMD_Milan`.

## Choose a minimum CPU platform at the workload level

If you use GKE Autopilot clusters or GKE Standard clusters with node auto-provisioning, you can choose a minimum CPU platform in your Pod specification. When you deploy the workload, GKE schedules those Pods only on nodes that have the specified platform or newer. We recommend this method.

###  Autopilot 

In Autopilot, request a minimum CPU platform and a compute class. **The compute class must support the CPU platform.** Autopilot supports selecting a minimum CPU platform for the `Balanced` compute class. For a list of available CPU platforms in each compute class, see [When to use specific compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes#when-to-use).

Save the following manifest as `min-cpu.yaml`:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: min-cpu-platform
      labels:
        app: min-cpu
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: min-cpu
      template:
        metadata:
          labels:
            app: min-cpu
        spec:
          **nodeSelector :
            cloud.google.com/compute-class: "COMPUTE_CLASS"
            supported-cpu-platform.cloud.google.com/PLATFORM: "true"**
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
            ports:
            - containerPort: 8080
            resources:
              requests:
                cpu: 250m
    

Replace the following:

  * `PLATFORM`: the name of the CPU platform, such as `AMD_Milan`. The platform name is case-sensitive and must be **underscore-delimited**.
  * `COMPUTE_CLASS`: the name of the compute class, which must be `Balanced`.



###  Standard 

In Standard clusters with node auto-provisioning enabled, request a CPU platform alongside a Compute Engine machine family. The machine family must support the CPU platform. For a list of supported platforms for each machine family, refer to [Compute Engine CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).

Save the following manifest as `min-cpu.yaml`:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: min-cpu-platform
      labels:
        app: min-cpu
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: min-cpu
      template:
        metadata:
          labels:
            app: min-cpu
        spec:
          **nodeSelector :
            cloud.google.com/machine-family: MACHINE_FAMILY
            cloud.google.com/requested-min-cpu-platform: PLATFORM**
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
            ports:
            - containerPort: 8080
            resources:
              requests:
                cpu: 250m
    

Replace the following:

  * `PLATFORM`: the name of the CPU platform, such as `AMD_Milan`. The platform name is case-sensitive and must be **underscore-delimited**.
  * `MACHINE_FAMILY`: the name of the machine family, such as `n2d`.

**Note:** GKE Standard can only schedule Pods on nodes with the specific CPU platform in the `PLATFORM` field. For example, if there's an existing node pool with Intel Ice Lake processors and the Pod requests Intel Cascade Lake, GKE creates a new node pool with Intel Cascade Lake to place the Pods.

Deploy the workload:
    
    
    kubectl apply -f min-cpu.yaml
    

Nodes retain the same platform through their lifecycle, unless the specified CPU platform is retired, in which case your nodes runs on a newer platform.

**Note:** Pods that use the nodeSelector can only schedule on node pools that are created by node auto-provisioning. If you have a manually-created node pool with a CPU platform set, Pods with the workload-level setting won't schedule on those nodes.

## Choose a minimum CPU platform at the node pool level

For GKE Standard clusters without node auto-provisioning, you can specify a minimum CPU platform when you create a new cluster or a node pool. You should only use this approach if you can't use the workload-level setting. This setting doesn't affect node auto-provisioning.

### gcloud

To create a new node pool with a minimum CPU platform using the gcloud CLI, set the `--min-cpu-platform` flag and specify the name of the CPU platform:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --min-cpu-platform PLATFORM
    

Replace the following:

  * `POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `PLATFORM`: the CPU platform that you want to run in the node pool, such as `"Intel Broadwell"`.



### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. Configure the node pool as needed.

  6. From the navigation pane, click **Nodes**.

  7. Under **Machine Configuration** ,

  8. In the **Series** drop-down list, select a [machine type](https://docs.cloud.google.com/compute/docs/machine-types#machine_types).

  9. In the **Machine type** drop-down list, select **Custom**.

  10. Select **Cores** and **Memory** as needed.

  11. Click _expand_more_ **CPU Platform and GPU**.

  12. In the **CPU Platform** drop-down list, select the minimum platform.

  13. Click **Create**.




### API

Include the `minCpuPlatform` property as part of the `nodeConfig` field in the request body. The value for `minCpuPlatform` must be the name of the platform, such as `Intel Haswell`, `Intel Broadwell`, and `Intel Sandy Bridge`.

For example, the following request creates a new node pool running the Intel Broadwell platform:
    
    
    POST https://container.googleapis.com/v1/projects/PROJECT_ID/regions/COMPUTE_REGION/clusters/CLUSTER_NAME/nodePools
    
    {
      'nodePool': {
        'name': 'POOL_NAME',
        'nodeConfig': {
          'minCpuPlatform': 'Intel Broadwell'
          ...
        }
        ...
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `COMPUTE_REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the cluster.
  * `CLUSTER_NAME`: the name of your cluster.
  * `POOL_NAME`: the name of your new node pool.



If you specify the platform when you [create a cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--min-cpu-platform), the minimum CPU platform setting applies to the default node pool in the new cluster.

## Alternatives

GKE also lets you select minimum CPU platforms using the following methods:

Alternatives  
---  
Cluster level flag `--autoprovisioning-min-cpu-platform` flag | This Standard mode cluster-level auto-provisioning setting is deprecated.  
  
## Limitations

The following limitations apply to all methods of selecting a minimum CPU platform:

  * All the [limitations of Compute Engine minimum CPU platforms](https://docs.cloud.google.com/compute/docs/instances/specify-min-cpu-platform#limitations) apply.
  * Availability of specific CPU platforms varies by zone.
  * The E2 machine type don't support minimum CPU platforms. You must select a different machine type.
  * Autopilot clusters only support platform selection for the `Balanced` compute class, not the default or `Scale-Out` compute classes.
  * If your Autopilot workload requests more than 80 vCPUs, the minimum CPU platform must be Intel Ice Lake or later. If you specify a less advanced platform, your Pod might remain in the `Pending` state indefinitely.



The following limitation applies to the cluster or node pool minimum CPU platform setting:

If you select a minimum CPU platform that is less advanced than the default CPU platform in the zone, or if the selected platform is no longer available, GKE checks whether there's a newer platform at the same cost. If a newer platform exists at the same cost, GKE creates the nodes using the newer platform. If a newer platform doesn't exist at the same cost, cluster or node pool creation fails.

## What's next

  * See a list of available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * Learn more about [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones).
  * Learn more about [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
