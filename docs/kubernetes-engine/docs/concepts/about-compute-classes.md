---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes/
title: About GKE ComputeClasses \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:36.912996+00:00
---

# About GKE ComputeClasses  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About GKE ComputeClasses Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can define sets of node attributes and autoscaling settings that Google Kubernetes Engine (GKE) uses to create nodes to run Pods by using _ComputeClasses_. This page describes how ComputeClasses work, use cases and benefits, and the available types of ComputeClasses.

This information is intended for the following people:

  * Cloud architects and platform engineers who want to reduce the overhead associated with cluster infrastructure management.
  * App operators and SRE who want to focus on operating workloads without thinking about the underlying infrastructure.



## About ComputeClasses and cluster autoscaling

A _ComputeClass_ is a set of node attributes and autoscaling settings that exists as a Kubernetes API object in a GKE cluster. You can select a ComputeClass in any Kubernetes workload that you deploy. GKE cluster autoscaling uses the attributes in a ComputeClass to create nodes for workloads.

Platform engineers can use ComputeClasses to configure infrastructure for various types of workloads, so that every new node is optimized for the specific requirements of your applications. ComputeClasses improve the speed and flexibility of GKE autoscaling and provide you with a declarative method of configuring infrastructure options across your clusters. For more information, see the Benefits of using ComputeClasses section.

Specific GKE capabilities and features are available only with ComputeClasses, such as the following:

  * [**Fallback compute priorities**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#choose-priorities): define multiple sets of infrastructure configurations in a ComputeClass, prioritized based on your preferences. During scaling, if the most preferred configuration is unavailable, GKE falls back to the next configuration.
  * [**Active migration to higher priority nodes**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#active-migration): when configured, GKE automatically replaces nodes that are lower on your list of fallback priorities with nodes that are higher on that list over time. As a result, your Pods eventually run on your most preferred nodes in a ComputeClass, even if that hardware wasn't available when you created the workload.
  * [**Autopilot in GKE Standard**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters): run workloads in GKE Autopilot mode to use Autopilot features like the container-optimized compute platform and Pod-based billing, even in Standard clusters. GKE manages these nodes and workloads, providing you with the benefits of Autopilot mode in any cluster.



### Benefits of ComputeClasses

ComputeClasses provide platform admins and operators with benefits like the following:

  * **Improved flexibility, efficiency, and availability of compute capacity** : ComputeClasses expand the capabilities of GKE cluster autoscaling. ComputeClass features like fallback priorities and [node consolidation parameters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#set-autoscaling) can reduce the risk of Pods stuck in a Pending status and increase the range of options that you can use to scale your nodes.
  * **Declarative platform-level configuration** : ComputeClasses let Platform engineers declaratively describe node configurations for various workload types. GKE autoscaling manages node and node pool creation and configuration. You can integrate your ComputeClasses into your CI/CD pipelines to have consistency in provisioned infrastructure across your platform.
  * **Reduced management overhead** : ComputeClasses reduce the complexity of managing infrastructure and workloads at scale. Platform engineers declare classes of infrastructure, and app operators select a relevant class in a workload. GKE manages scaling, node hardware configuration, and applies taints, tolerations, and labels.



## About the ComputeClass custom resource

ComputeClasses are Kubernetes [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). You can define the specification of a ComputeClass in a manifest file and create it in your clusters, similarly to how you define and create your Kubernetes workload resources like Deployments and Services.

The following example manifest defines a ComputeClass named `n4`:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: n4
    spec:
      nodePoolAutoCreation:
        enabled: true
      priorities:
      - machineFamily: n4
      - machineFamily: n2
      whenUnsatisfiable: DoNotScaleUp
    

When a Pod selects this ComputeClass, GKE does the following when it creates new nodes:

  1. GKE creates nodes that use the N4 machine series.
  2. If the N4 machine series isn't available, GKE creates nodes that use the N2 machine series instead.
  3. If the N2 machine series isn't available, GKE waits until resources become available to schedule the Pod.



You can control various settings for your nodes by using ComputeClasses, including accelerators, node system settings, node locations, and the fallback behavior of GKE when hardware resources aren't available. For more information about all of the available configurations for ComputeClasses, see the [ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass).

## ComputeClass selection in workloads

To use a ComputeClass for a GKE workload, you select the ComputeClass in the workload manifest by using a [node selector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) for the `cloud.google.com/compute-class` label.

The following example Deployment manifest selects a ComputeClass:
    
    
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
      template:
        metadata:
          labels:
            app: hello
        spec:
    ** nodeSelector:**
    ** # Replace with the name of a compute class**
    ** cloud.google.com/compute-class: COMPUTE_CLASS **
          containers:
          - name: hello-app
            image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
            ports:
            - containerPort: 8080
            resources:
              requests:
                cpu: "250m"
                memory: "1Gi"

Replace `COMPUTE_CLASS` with the name of a ComputeClass that exists in the cluster. For example, you can specify the `n4` ComputeClass from the About the ComputeClass custom resource section or the `autopilot` [built-in ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-built-in-compute-classes).

### Node configuration in workload specifications

GKE Autopilot clusters and node auto-provisioning in GKE Standard let you use node selectors in your Pods to create nodes that have specific properties like machine families, Spot VMs, or GPUs and TPUs. ComputeClasses let you centrally define these requirements instead of adding individual selectors to every workload.

**Caution:** If the Pods that you deploy in a cluster use node selectors for node attributes in addition to selecting ComputeClasses, you might notice unexpected scaling and scheduling behavior. We recommend that you use either compute classes or individual node selectors, but not both at the same time. For more information about which node labels you can select alongside a ComputeClass, see [Node selectors for system node labels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#system-label-selectors).

## About applying ComputeClasses by default

You can configure GKE to apply a ComputeClass by default to Pods that don't select a specific ComputeClass. You can define a default ComputeClass for specific namespaces or for an entire cluster. For more information about how to configure your clusters or namespaces with a default class, see [Apply ComputeClasses to Pods by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).

The following table describes the effects of setting a ComputeClass as the default for a namespace or for a cluster:

Effects of default ComputeClasses  
---  
Namespace-level default | 

  * GKE applies the ComputeClass only to Pods in a specific namespace.
  * GKE modifies the Pods to add a node selector for the namespace-level default class.
  * GKE scales up only nodes that have node labels and node taints for that ComputeClass, similar to any other compute class.
  * GKE adds node labels and node taints to the nodes that GKE creates for the namespace-level default class.

  
Cluster-level default | 

  * GKE applies the ComputeClass to Pods in any namespace.
  * GKE applies the ComputeClass only to Pods that don't have an existing selector for a ComputeClass.
  * GKE doesn't modify the Pod specifications to add a node selector for the cluster-level default class.
  * GKE scales up nodes that meet any of the following conditions: 
    * The nodes have no labels and taints for a different compute class.
    * The nodes have the `cloud.google.com/compute-class: default` node label.
  * GKE adds the `cloud.google.com/compute-class: default` node label to the nodes that GKE creates for the cluster-level default class. GKE doesn't add any node taints to those nodes.
  * If you update an Autopilot cluster to use a custom compute class as the cluster-level default, GKE won't run Pods on the Autopilot container-optimized compute platform by default. In GKE version 1.34.1-gke.1829001 and later, you can use the Autopilot compute platform for specific Pods by adding the `cloud.google.com/compute-class: autopilot` node selector to those Pods.

  
  
If GKE applies a namespace-level default ComputeClass to a Pod, that Pod won't activate the cluster-level default ComputeClass, because GKE adds a node selector for the namespace-level default class to the Pod.

### Active migration in default ComputeClasses

If the ComputeClass that you use as the namespace-level or cluster-level default has the `activeMigration.optimizeRulePriority` field set to `true`, you might see the following effects:

  * **Cluster-level default compute class** : active migration might be triggered if nodes with lower priority exist and GKE can create nodes with higher priority. Depending on the number of lower-priority nodes, migration might increase workload disruption.
  * **Namespace-level default compute class** : active migration isn't triggered because GKE injects the compute class node selector only into newly created Pods. Existing Pods aren't automatically re-created with the selector.



### Cluster-level default ComputeClasses

When you enable cluster-level default ComputeClasses, a `ComputeClass` object named `default` defines the node autoscaling rules for the cluster. If your cluster already has a ComputeClass named `default`, GKE uses that ComputeClass configuration for the cluster. If the cluster doesn't have a custom ComputeClass named `default`, GKE behaves as if the following `ComputeClass` rules apply:
    
    
    spec:
      whenUnsatisfiable: ScaleUpAnyway
      nodePoolAutoCreation:
        enabled: true
    

By default, GKE doesn't apply any fallback behavior and doesn't change the configuration of autoscaled nodes. To apply specific properties to autoscaled nodes by default, you must deploy a custom ComputeClass named `default`.

Consider the following when you configure your default cluster-level compute class:

  * To prevent Pods from being stuck in a `Pending` state, set the `spec.whenUnsatisfiable` field to `ScaleUpAnyway`. This value lets GKE create nodes even if Pods request Compute Engine machine families that aren't in the priority rules for the cluster-level default class. If you want to force these Pods to use the machine families that are in the default ComputeClass, set this field to `DoNotScaleUp`.
  * To restrict changes to the `default` ComputeClass, use an [RBAC ClusterRole](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#role-and-clusterrole) to restrict **update** , **patch** , **delete** , and **create** operations on the `ComputeClass` resource named `default`.
  * To change the default node consolidation parameters of the cluster autoscaler, use the `spec.autoscalingPolicy` field in your ComputeClass specification. The parameters that you specify for this field in the cluster-level default ComputeClass apply to all of the nodes in your cluster. For more information, see [Set autoscaling parameters for node consolidation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#set-autoscaling).



## What's next

  * [Learn about best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses)
  * [Learn about built-in ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-built-in-compute-classes)
  * [Learn about custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes)
  * [Read the ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass)
  * [Deploy a ComputeClass and select it in a workload](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-attributes-compute-classes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
