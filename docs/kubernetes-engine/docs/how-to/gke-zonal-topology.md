---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-zonal-topology/
title: Place GKE Pods in specific zones \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:13.079442+00:00
---

# Place GKE Pods in specific zones  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gke-zonal-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Place GKE Pods in specific zones Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to tell Google Kubernetes Engine (GKE) to run your Pods on nodes in specific Google Cloud zones using _zonal topology_. This type of placement is useful in situations such as the following:

  * Pods must access data that's stored in a zonal Compute Engine persistent disk.
  * Pods must run alongside other zonal resources such as Cloud SQL instances.



You can also use zonal placement with topology-aware traffic routing to reduce latency between clients and workloads. For details about topology-aware traffic routing, see [Topology aware routing](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/).

Using zonal topology to control Pod placement is an advanced Kubernetes mechanism that you should only use if your situation requires that Pods run in specific zones. In most production environments, we recommend that you use regional resources, which is the GKE default, when possible.

## Zonal placement methods

Zonal topology is built into Kubernetes with the `topology.kubernetes.io/zone: ZONE` node label. To tell GKE to place a Pod in a specific zone, use one of the following methods:

  * **nodeAffinity**: Specify a nodeAffinity rule in your Pod specification for one or more Google Cloud zones. This method is more flexible than a nodeSelector because it lets you place Pods in multiple zones.
  * **nodeSelector**: Specify a nodeSelector in your Pod specification for a single Google Cloud zone.

  * **Compute classes**: Configure your Pod to use a GKE compute class. This approach lets you define a prioritized list of sets of Google Cloud zones. It enables the workload to be moved dynamically to the most preferred set of zones when nodes are available in these zones. For more information, see [About custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes).




### Considerations

Zonal Pod placement using zonal topology has the following considerations:

  * The cluster must be in the same Google Cloud region as the requested zones.
  * In Standard clusters, you must use node auto-provisioning or create node pools with nodes in the requested zones. Autopilot clusters automatically manage this process for you.
  * Standard clusters must be regional clusters.



## Pricing

Zonal topology is a Kubernetes scheduling capability and is offered at no extra cost in GKE.

For pricing details, see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing GKE cluster in the same Google Cloud region as the zones in which you want to place your Pods. To create a new cluster, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



## Place Pods in multiple zones using nodeAffinity

Kubernetes nodeAffinity provides a flexible scheduling control mechanism that supports multiple label selectors and logical operators. Use nodeAffinity if you want to let Pods run in one of a set of zones (for example, in either `us-central1-a` or `us-central1-f`).

  1. Save the following manifest as `multi-zone-affinity.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nginx-deployment
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: nginx-multi-zone
           template:
             metadata:
               labels:
                 app: nginx-multi-zone
             spec:
               containers:
               - name: nginx
                 image: nginx:latest
                 ports:
                 - containerPort: 80
               **affinity :
                 nodeAffinity:
                   requiredDuringSchedulingIgnoredDuringExecution:
                     nodeSelectorTerms:
                     - matchExpressions:
                       - key: topology.kubernetes.io/zone
                         operator: In
                         values:
                         - us-central1-a
                         - us-central1-f**
         

This manifest creates a Deployment with three replicas and places the Pods in `us-central1-a` or `us-central1-f` based on node availability.

Ensure that your cluster is in the `us-central1` region. If your cluster is in a different region, change the zones in the values field of the manifest to valid zones in your cluster region. 

Optional: If you are provisioning TPU VMs, use an [AI zone](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones), like `us-central1-ai1a`. AI zones are specialized locations that are optimized for AI/ML workloads within Google Cloud regions.

  2. Create the Deployment:
         
         kubectl create -f multi-zone-affinity.yaml
         

GKE creates the Pods in nodes in one of the specified zones. Multiple Pods might run on the same node. You can optionally use [Pod anti-affinity](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity) to tell GKE to place each Pod on a separate node.




## Place Pods in a single zone using a nodeSelector

To place Pods in a single zone, use a nodeSelector in the Pod specification. A nodeSelector is equivalent to a `requiredDuringSchedulingIgnoredDuringExecution` nodeAffinity rule that has a single zone specified.

**Caution:** Pods that you place in a single zone by using zonal topology might not be covered by the [Autopilot service level agreement (SLA)](https://cloud.google.com/kubernetes-engine/sla), which covers Autopilot Pods in _multiple zones_. The [Compute Engine SLA](https://cloud.google.com/compute/sla) continues to apply.

  1. Save the following manifest as `single-zone-selector.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nginx-singlezone
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: nginx-singlezone
           template:
             metadata:
               labels:
                 app: nginx-singlezone
             spec:
               **nodeSelector :
                 topology.kubernetes.io/zone: "us-central1-a"**
               containers:
               - name: nginx
                 image: nginx:latest
                 ports:
                 - containerPort: 80
         

This manifest tells GKE to place all replicas in the Deployment in the `us-central1-a` zone.

  2. Create the Deployment:
         
         kubectl create -f single-zone-selector.yaml
         




## Prioritize Pod placement in selected zones using a compute class

GKE compute classes provide a control mechanism that lets you define a list of node configuration priorities. Zonal preferences let you define the zones that you want GKE to place Pods in.

**Caution:** We don't recommend combining zonal preferences in compute classes with previous zonal topology methods in Kubernetes.

### Using location zones priority

Defining zonal preferences in compute classes using location zones priority requires GKE version 1.33.1-gke.1545000 or later.

The following example creates a compute class that specifies a list of preferred zones for Pods.

These steps assume that your cluster is in the `us-central1` region. If your cluster is in a different region, change the values of the zones in the manifest to valid zones in your cluster region.

  1. Save the following manifest as `zones-custom-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: zones-custom-compute-class
         spec:
           priorities:
           - location:
             zones: [us-central1-a, us-central1-b]
           - location:
             zones: [us-central1-c]
           activeMigration:
             optimizeRulePriority: true
           nodePoolAutoCreation:
             enabled: true
           whenUnsatisfiable: ScaleUpAnyway
         

This compute class manifest changes scaling behavior as follows:

     1. GKE tries to place Pods in either `us-central1-a` or in `us-central1-b`.
     2. If `us-central1-a` and `us-central1-b` don't have available capacity, GKE tries to place Pods in `us-central1-c`.
     3. If `us-central1-c` doesn't have available capacity, the `whenUnsatisfiable: ScaleUpAnyway` field makes GKE place the Pods in any available zone in the region.
     4. If a zone that has higher priority in the compute class becomes available later, the `activeMigration.optimizeRulePriority: true` field makes GKE move the Pods to that zone from any lower priority zones. This migration uses the Pod Disruption Budget to help ensure service availability.
  2. Create the Custom Compute Class:
         
         kubectl create -f zones-custom-compute-class.yaml
         

GKE creates a custom compute class that your workloads can reference.

  3. Save the following manifest as `custom-compute-class-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nginx-zonal-preferences
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: nginx-zonal-preferences
           template:
             metadata:
               labels:
                 app: nginx-zonal-preferences
             spec:
               **nodeSelector :
                 cloud.google.com/compute-class: "zones-custom-compute-class"**
               containers:
               - name: nginx
                 image: nginx:latest
                 ports:
                 - containerPort: 80
         

  4. Create the Deployment:
         
         kubectl create -f custom-compute-class-deployment.yaml
         




### Using location zoneTypes priority

Defining zonal preferences in compute classes using location zone types priority requires GKE version 1.35.2-gke.1842000 or later. Selecting a zone type for your pods will, depending on your settings, use or create a new node pool spanning all zones of a given type.

You can specify the following zone types in your compute class:

  * `STANDARD`: General-purpose, Google Cloud zones in a region. Recommended for non-ML workloads.
  * `AI`: Specialized zones optimized for AI/accelerator capacity. Recommended for AI/ML workloads.
  * `CLUSTER_DEFAULT`: Zones specified in the cluster's [`autoprovisioning-locations`](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-locations) (or the cluster's locations if empty).



For more on standard and AI zones see, [About AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones)

#### Restrictions for combining fields

You can't combine the `zoneTypes` field with the `location.zones` field or the `reservations.specific` field in the same priority entry. You can use the `zoneTypes` field and the `location.zones` field in the same compute class as long as you put them in separate priority entries.

Additionally, the `priorityDefaults` field applies to every priority in the compute class. A consequence of this rule is that setting the `zoneTypes` field in the `priorityDefaults` field prevents you from using the `location.zones` field or the `reservations.specific` field in any priority.

#### Valid example: Separate priorities

The following example is valid because `zones` and `zoneTypes` are specified in separate priority entries:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: valid-zonal-preferences
    spec:
      priorities:
      - location:
          zones: [us-central1-a]
      - location:
          zoneTypes: [AI]
    

#### Invalid example: Same priority

The following example is invalid because `zones` and `zoneTypes` are specified in the same priority entry:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: invalid-same-priority
    spec:
      priorities:
      - location:
          zones: [us-central1-a]
          zoneTypes: [AI] # Error: mutually exclusive
    

#### Invalid example: Conflict with defaults

The following example is invalid because setting the `zoneTypes` field in `priorityDefaults` section conflicts with the `zones` field in the priority entry:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: invalid-defaults-conflict
    spec:
      priorityDefaults:
        location:
          zoneTypes: [AI]
      priorities:
      - location:
          zones: [us-central1-a] # Error: merges with defaults
    

#### Usage example

The following example creates a compute class that specifies a list of preferred zone types for Pods.

  1. Save the following manifest as `zone-types-custom-compute-class.yaml`:
         
         apiVersion: cloud.google.com/v1
         kind: ComputeClass
         metadata:
           name: zone-types-custom-compute-class
         spec:
           priorities:
           - location:
             zones: [us-central1-c]
           - location:
             zoneTypes:
             - AI
           - location:
             zoneTypes:
             - CLUSTER_DEFAULT
           activeMigration:
             optimizeRulePriority: true
           nodePoolAutoCreation:
             enabled: true
           whenUnsatisfiable: ScaleUpAnyway
         

This compute class manifest changes scaling behavior as follows:

     1. GKE tries to place Pods in either `us-central1-c` zone.
     2. If `us-central1-c` doesn't have available capacity, GKE tries to place Pods in any `AI` zone in the region.
     3. If none of the `AI` zones have available capacity, GKE tries to place Pods in any of the `CLUSTER_DEFAULT` zones.
     4. If none of the `CLUSTER_DEFAULT` zones have available capacity, the `whenUnsatisfiable: ScaleUpAnyway` field makes GKE place the Pods in any available zone in the region.
     5. If a zone that has higher priority in the compute class becomes available later, the `activeMigration.optimizeRulePriority: true` field makes GKE move the Pods to that zone from any lower priority zones. This migration uses the Pod Disruption Budget to help ensure service availability.
  2. Create the Custom Compute Class:
         
         kubectl create -f zone-types-custom-compute-class.yaml
         

GKE creates a custom compute class that your workloads can reference.

  3. Save the following manifest as `custom-compute-class-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: nginx-zonal-preferences
         spec:
           replicas: 3
           selector:
             matchLabels:
               app: nginx-zonal-preferences
           template:
             metadata:
               labels:
                 app: nginx-zonal-preferences
             spec:
               **nodeSelector: cloud.google.com/compute-class : "zone-types-custom-compute-class"**
               containers:
               - name: nginx
                 image: nginx:latest
                 ports:
                 - containerPort: 80
         

  4. Create the Deployment:
         
         kubectl create -f custom-compute-class-deployment.yaml
         


**Note:** When using the `zoneTypes` field, particularly with a `reservation.affinity` field set to the value `AnyBestEffort`, we recommend setting the `locationPolicy` field to `ANY`. Specifying `locationPolicy: ANY` allows the scale-up orchestrator to use real-time capacity signals for optimal placement.

#### How NAP evaluates `zoneTypes`

When determining whether to reuse an existing node pool or create a new one, node auto-provisioning (NAP) typically requires an exact match between the node pool's existing zones and your requested `zoneTypes`. If you update a priority to include wider zone types (e.g., moving from `[AI]` to `[AI, STANDARD]`), NAP will provision a new node pool to match the new exact shape.

**Note:** Because compact placement and TPU multi-host configurations are strictly single-zone, they follow a different rule. NAP will reuse an existing single-zone node pool as long as its zone is a subset of your selected zoneTypes. It won't attempt to create a new node pool just because the priority defines a wider range of acceptable zones.

#### Machine-type aware trimming

If a machine type (like `h3-standard-88`) is only available in a subset of the zones defined by a type (for example, only in `us-central1-a`), GKE automatically trims the list of node pool locations to only include zones where that hardware is physically present.

## Target AI zones

AI zones are specialized zones used for AI/ML training and inference workloads. These zones provide significant ML accelerator capacity. For more information, see the [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) documentation.

In this document and the GKE documentation, "standard zones" or "zones" refer to non-AI zones within a Google Cloud region.

**Important:** Access to AI zones is restricted unless you've enabled them for your Google Cloud project. To use them, [enable AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#enable_ai_zones) ([Preview](https://cloud.google.com/products#product-launch-stages)).

Before you use an AI zone in GKE, consider the following characteristics:

  * AI zones are physically separate from standard zones to provide additional storage space and power. This separation might result in higher latency, which is generally tolerable for AI/ML workloads.
  * AI zones have a suffix with the `ai` notation. For example, an AI zone in the `us-central1` region is named `us-central1-**ai** 1a`.
  * Currently, only TPU VMs are supported.
  * The cluster's control plane runs in one or more standard zones within the same region as the AI zone.
  * You can run VMs without attached TPUs in an AI zone only if you meet the following requirements:

    * You are already running other workloads that use TPU VMs in the same zone.
    * The non-TPU VMs are either Spot VMs, tied to a reservation, or part of a node pool with a specific accelerator-to-general-purpose VM ratio.
**Note:** Even if GKE lets you create the node pool, Compute Engine provisions the VMs only if these conditions are met. For more information, see [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).
  * AI zones share components, such as networking connections and software rollouts, with standard zones that have the same suffix within the same region. For high-availability workloads, we recommend that you use different zones. For example, avoid using both `us-central1-ai1a` and `us-central1-a` for high availability.




By default, GKE doesn't deploy your workloads in AI zones. To use an AI zone, you must configure one of the following options:

  * **(Recommended) ComputeClasses** : set your highest priority to request on-demand TPUs in an AI zone. ComputeClasses help you define a prioritized list of hardware configurations for your workloads. For an example, see [About ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#ai-zones).
  * **Node auto-provisioning** : use a `nodeSelector` or `nodeAffinity` in your Pod specification to instruct node auto-provisioning to create a node pool in the AI zone. If your workload doesn't explicitly target an AI zone, node auto-provisioning considers only standard zones or zones from [`--autoprovisioning-locations`](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-locations) when creating new node pools. This configuration helps ensure that workloads that don't run AI/ML models remain in standard zones unless you explicitly configure otherwise. For an example of a manifest that uses a `nodeSelector`, see [Set the default zones for auto-created nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#auto-provisioning_locations).
  * **GKE Standard** : if you directly manage your node pools, use an AI zone in the `--node-locations` flag when you create a node pool. For an example, see [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#single-host).



## Verify Pod placement

To verify Pod placement, list the Pods and check the node labels. Multiple Pods might run in a single node, so you might not see Pods spread across multiple zones if you used nodeAffinity.

  1. List your Pods:
         
         kubectl get pods -o wide
         

The output is a list of running Pods and the corresponding GKE node.

  2. Describe the nodes:
         
         kubectl describe node NODE_NAME | grep "topology.kubernetes.io/zone"
         

Replace `NODE_NAME` with the name of the node.

The output is similar to the following:
         
         topology.kubernetes.io/zone: us-central1-a
         




If you want GKE to spread your Pods evenly across multiple zones for improved failover across multiple failure domains, use [topologySpreadConstraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/).

## What's next

  * [Separate GKE workloads from each other](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation)
  * [Keep network traffic in the same topology as the node](https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/)
  * [Spread Pods across multiple failure domains](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
