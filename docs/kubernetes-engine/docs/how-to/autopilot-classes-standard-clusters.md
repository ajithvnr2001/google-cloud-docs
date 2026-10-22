---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters/
title: Run workloads in Autopilot mode in Standard clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:48.085438+00:00
---

# Run workloads in Autopilot mode in Standard clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-classes-standard-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Run workloads in Autopilot mode in Standard clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Cluster administrators and application operators can get the benefits of Google Kubernetes Engine (GKE) Autopilot, like pricing and pre-configured settings, in Standard mode clusters. This document shows you how to use _ComputeClasses_ to deploy an Autopilot workload in a Standard cluster. You should already be familiar with the following concepts:

  * [GKE Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
  * [GKE ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-compute-classes)
  * [Kubernetes node selectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)



## About Autopilot ComputeClasses

GKE provides Kubernetes custom resources named [ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) that can be deployed in your cluster like any other Kubernetes resources. A ComputeClass defines a list of node configurations, like machine types or Spot VMs. You can select ComputeClasses in your workloads, which indicates to GKE that any new nodes should use one of the configurations in that list.

If a workload selects a ComputeClass that has the `autopilot` field enabled, GKE runs the Pods in Autopilot mode. The nodes that GKE creates are managed by Google and include many of the default Autopilot feature and security settings. For more information about the implications of running an Autopilot workload in your Standard clusters, including differences that you might notice when you deploy those workloads, see [About Autopilot mode workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).

### Types of Autopilot ComputeClasses

GKE provides built-in Autopilot ComputeClasses that you can use for most general-purpose workloads. You can also configure a new or existing custom ComputeClass to use Autopilot mode. The type of Autopilot ComputeClass that you use depends on whether your workloads need specific hardware, as follows:

  * **General-purpose workloads** : use one of the built-in Autopilot ComputeClasses, which place Pods on the [_container-optimized compute platform_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#autopilot-compute-platform).
  * **Workloads that require specific hardware** : enable Autopilot mode for any custom ComputeClass, deploy that ComputeClass to the cluster, and select that ComputeClass in your workloads.



For more information about these options, when to use them, and the pricing for each option, see [Hardware selection in Autopilot ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#built-in-custom-autopilot-classes).

## Pricing

GKE Autopilot pricing applies to the workloads and nodes that use an Autopilot ComputeClass. The pricing model that applies depends on the ComputeClass priority rule that GKE uses to create nodes for your workloads. For more information, see [Pricing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#pricing) in "About Autopilot mode workloads in GKE Standard".

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Use a GKE Standard cluster that meets all of the requirements. To create a new cluster, see [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).
  * To avoid workload rejections, learn about the requirements and security constraints of Autopilot. For more information, see [predefined settings for Autopilot nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#predefined-settings-autopilot).



### Requirements

  * Your cluster must run one of the following GKE versions:

    * To use Autopilot in ComputeClasses, the cluster must run 1.34.1-gke.1829001 or later.
    * To use `podFamily` priority rules in custom Autopilot ComputeClasses, the cluster must run 1.35.2-gke.1485000 or later.
  * At least one node pool in the cluster must have no [node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

This node pool is required to run GKE Standard system Pods that can't run on Autopilot nodes in Standard clusters because of the taints that GKE adds to those nodes.

  * [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) is required, and is enabled by default.

  * You must use a VPC-native cluster.

  * If you use Kubernetes NetworkPolicies, your cluster must use [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2). By default, all new clusters use GKE Dataplane V2.

If your cluster doesn't use GKE Dataplane V2, you must [disable network policy enforcement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy#disable-network-policy-enforcement).




### Limitations

  * The `general-purpose-arm` pod family, `autopilot-arm` and `autopilot-arm-spot` ComputeClasses are supported in both Autopilot clusters and Standard clusters with Autopilot ComputeClass, but version requirements differ. For details on version requirements, see [Deploy Autopilot workloads on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads).
  * To update existing ComputeClasses in the cluster to use Autopilot mode, you must recreate those ComputeClasses with an updated specification. For more information, see Enable Autopilot for an existing custom ComputeClass.
  * The built-in Autopilot ComputeClasses don't support enabling Confidential GKE Nodes for your entire cluster. If you enable Confidential GKE Nodes for the cluster, any new Pods that select the built-in Autopilot ComputeClasses remain in the `Pending` state indefinitely.
  * Calico network policy enforcement isn't supported. You must use GKE Dataplane V2 or disable network policy enforcement.
  * The name of your ComputeClass can't begin with `gke` or `autopilot`, which are reserved prefixes.



### Required roles and permissions

To get the permissions that you need to deploy ComputeClasses, ask your administrator to grant you the [Kubernetes Engine Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.developer) (`roles/container.developer`) IAM role on your cluster or project . For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Modify clusters to meet Autopilot requirements

You can use the Google Cloud console to check whether your Standard cluster meets all of the requirements to run workloads in Autopilot mode. You can also use the Google Cloud console to modify the cluster to meet these requirements.

### Modify an existing cluster

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. In the row for the cluster that you want to modify, click more_vert **More actions** > edit **Edit**. The **Cluster details** page opens.

  3. In the **Cluster basics** section, find the **Autopilot compute class compatibility** section.

If this section displays **Enabled** , the cluster is already compatible with Autopilot. Skip to the Select an Autopilot ComputeClass in a workload section.

  4. If the **Autopilot compute class compatibility** section displays **Disabled** , click edit **Edit Autopilot compute class compatibility**.

If this section is unavailable to edit, your cluster uses a permanent setting that's incompatible with Autopilot mode. For example, you can't modify clusters to be VPC-native after cluster creation. If you can't interact with the **Autopilot compute class compatibility** section, you must create a new cluster.

  5. In the **Autopilot compute class compatibility** pane that opens, review the cluster settings that need to change to meet the requirements of Autopilot mode.

  6. Click **Enable Autopilot compute class**. GKE modifies the cluster as needed.




### Modify a new cluster

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page.

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. On the **Cluster basics** page, find the **Maximize deployment options with Autopilot compute class** section. This section shows you the cluster settings that need to change to meet the requirements of Autopilot mode.

  3. Click **Enable Autopilot compute class**. GKE modifies the cluster as needed.

  4. Configure other cluster settings based on your requirements. If you modify a setting that makes the cluster incompatible with Autopilot, a caution message appears.

**Note:** Certain cluster settings, like VPC-native traffic routing, are permanent. If you modify a permanent setting when you create your cluster, you can't update that cluster for Autopilot compatibility later.



## Select an Autopilot ComputeClass in a workload

You can run a workload in Autopilot mode in your Standard cluster by selecting a ComputeClass that uses Autopilot mode. To run a workload in Autopilot mode, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the GKE **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. Click **Deploy** or **Create Job**. The workload creation page for a Deployment or a Job appears.

  3. In the **Nodes** section, select **Autopilot compute class**.

  4. In the **Select compute class** section, in the **Compute class** drop-down list, select a ComputeClass that uses Autopilot mode. This ComputeClass can be any of the following:

     * One of the following [built-in Autopilot ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#built-in-ap-classes), which place general-purpose workloads on the Autopilot container-optimized compute platform:

       * `autopilot`
       * `autopilot-spot`
     * A ComputeClass that you create, such as the `n4-class` ComputeClass that's described in the Configure a custom Autopilot ComputeClass section.

  5. Configure and create the workload.




###  kubectl CLI 

To select an Autopilot ComputeClass in a workload, use a [node selector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector) for the `cloud.google.com/compute-class` label. This is the same label that you use to select any other ComputeClass in GKE. The following steps show you how to create an example Deployment that selects a ComputeClass and verify that the Pods run in Autopilot mode:

  1. Save the following example Deployment as `autopilot-cc-deployment.yaml`:
         
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
               nodeSelector:
                 # Replace with the name of a compute class
                 cloud.google.com/compute-class: COMPUTE_CLASS 
               containers:
               - name: hello-app
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
                 ports:
                 - containerPort: 8080
                 resources:
                   requests:
                     cpu: "250m"
                     memory: "1Gi"

Replace `COMPUTE_CLASS` with the name of the compute class to use. This value can be any of the following:

     * One of the following [built-in Autopilot ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#built-in-ap-classes), which place general-purpose workloads on the Autopilot container-optimized compute platform:

       * `autopilot`
       * `autopilot-spot`
     * A ComputeClass that you create, such as the `n4-class` ComputeClass that's described in the Configure a custom Autopilot ComputeClass section.

  2. Deploy the workload:
         
         kubectl apply -f autopilot-cc-deployment.yaml
         




## Configure a custom Autopilot ComputeClass

You can configure custom ComputeClasses to use Autopilot. Use a custom Autopilot ComputeClass in situations like the following:

  * Your workloads require specific hardware to run optimally, like GPUs or a certain Compute Engine machine series.
  * You want to adjust node settings like zones or taints while using the Autopilot container-optimized compute platform.



If your workloads don't have these requirements, we recommend that you use one of the built-in Autopilot ComputeClasses instead. To select a built-in Autopilot ComputeClass, see the preceding Select an Autopilot ComputeClass in a workload section.

### Create a new custom Autopilot ComputeClass

  1. Save one of the following example ComputeClass manifests:

     * **Select specific machines** :
           
           apiVersion: cloud.google.com/v1
           kind: ComputeClass
           metadata:
             name: n4-class
           spec:
             autopilot:
               enabled: true
             priorities:
             - machineFamily: n4
               spot: true
               minCores: 16
             - machineFamily: n4
               spot: true
             - machineFamily: n4
               spot: false
             activeMigration:
               optimizeRulePriority: true
           

This manifest includes the following fields:

       * `autopilot`: enables Autopilot mode for the ComputeClass. If you specify this field in a ComputeClass that you deploy to an Autopilot cluster, GKE ignores the field.
       * `priorities`: defines an array of three different N4 machine family configurations.
       * `activeMigration`: lets GKE migrate Pods to configurations that are higher in the list of priorities when resources become available.
     * **Use the container-optimized compute platform with modifications** :
           
           apiVersion: cloud.google.com/v1
           kind: ComputeClass
           metadata:
             name: general-purpose-class
           spec:
             autopilot:
               enabled: true
             priorities:
             - podFamily: general-purpose
             priorityDefaults:
               location:
                 zones: ['us-central1-a','us-central1-b','us-central1-f']
           

This manifest includes the following fields:

       * `autopilot`: enables Autopilot mode for the ComputeClass. If you specify this field in a ComputeClass that you deploy to an Autopilot cluster, GKE ignores the field.
       * `priorities.podFamily`: uses the [`podFamily` priority rule](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters#hardware-selection-ap-classes) to run Pods on the Autopilot container-optimized compute platform.
       * `priorityDefaults.location`: defines the zones in which GKE should create nodes for Pods that use the ComputeClass.
  2. Deploy the ComputeClass:
         
         kubectl apply -f PATH_TO_COMPUTECLASS_MANIFEST
         

Replace `PATH_TO_COMPUTECLASS_MANIFEST` with the path to the ComputeClass manifest from the preceding step.

  3. Verify that the ComputeClass exists:
         
         kubectl get computeclasses
         

The output is similar to the following:
         
         NAME                  AGE
         n4-class              3s
         




### Enable Autopilot for an existing custom ComputeClass

**Best Practice** : 

To migrate your workloads to Autopilot mode in stages, or to immediately start node creation, create a new Autopilot ComputeClass and recreate specific workloads to select the new ComputeClass.

You can enable Autopilot in existing custom ComputeClasses that are in a Standard cluster. Enabling Autopilot in a ComputeClass that's in an Autopilot cluster has no effect, because the entire cluster uses Autopilot mode.

After you enable Autopilot for an existing ComputeClass, GKE uses Autopilot to run new Pods that select the ComputeClass. If you have existing Pods on Standard nodes that select the Autopilot ComputeClass, those Pods use Autopilot only when they're recreated.

To update an existing custom ComputeClass to use Autopilot mode, follow these steps:

  1. In a text editor, update the manifest file for your existing ComputeClass to add the `spec.autopilot` field:
         
         spec:
           **autopilot :
             enabled: true**
         

  2. Replace the existing `ComputeClass` resource in the Kubernetes API with the updated specification:
         
         kubectl replace --force -f PATH_TO_UPDATED_MANIFEST
         

Replace `PATH_TO_UPDATED_MANIFEST` with the path to your updated manifest file.

  3. To trigger new node creation, recreate any workloads that use the compute class.




After you apply the updated manifest, any _new_ nodes that GKE creates for this ComputeClass use Autopilot. GKE doesn't modify any existing nodes that were created prior to the update.

## Verify that your workload uses Autopilot

Select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the GKE **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. For your workload, check the value in the **Node type** column. If the workload uses Autopilot mode, this value is **Autopilot-managed**.




###  kubectl CLI 

Check the names of the nodes that run your Pods:
    
    
    kubectl get pods -l=app=hello -o wide
    

The output is similar to the following:
    
    
    NAME                       READY   STATUS    RESTARTS   AGE     IP             NODE                                         NOMINATED NODE   READINESS GATES
    helloweb-79b9f6f75-5wwc9   1/1     Running   0          152m    10.102.1.135   gk3-cluster-1-nap-10abc8ya1-f66c6cef-wg5g   <none>           <none>
    helloweb-79b9f6f75-9skb9   1/1     Running   0          4d3h    10.102.0.140   gk3-cluster-1-nap-10abc8ya1-632bac02-hjl6   <none>           <none>
    helloweb-79b9f6f75-h7bdv   1/1     Running   0          152m    10.102.1.137   gk3-cluster-1-nap-10abc8ya1-f66c6cef-wg5g   <none>           <none>
    

In this output, the `gk3-` prefix in the **Node** column indicates that the node is managed by Autopilot.

## Apply an Autopilot ComputeClass by default

You can set a built-in or custom ComputeClass as the default ComputeClass for a namespace or for an entire cluster. The default ComputeClass applies to any Pod that doesn't explicitly select a different ComputeClass. If you set an Autopilot ComputeClass as the default, you can ensure that all Pods run in Autopilot mode unless a workload selects a different option.

If the ComputeClass that you set as the default uses `podFamily` priority rules, Pods that don't select a different ComputeClass can run as general-purpose Autopilot Pods. This method lets you use the Pod-based billing model by default in your cluster or namespace, and is useful when many of your workloads have no special hardware requirements.

**Note:** To avoid situations where Pods get stuck with a `Pending` status because a node selector is incompatible with your default ComputeClass, set the `whenUnsatisfiable` field to `ScaleUpAnyway` for any ComputeClass that you set as the default.

For more information, see [Apply ComputeClasses to Pods by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-pods-default-compute-classes).

## What's next

  * [Learn about best practices for ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/computeclasses).
  * For the parameters that you can specify in ComputeClasses, see the [ComputeClass CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
