---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-taints/
title: Configure workload separation in GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:39:36.470638+00:00
---

# Configure workload separation in GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-taints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Configure workload separation in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to tell Google Kubernetes Engine (GKE) to schedule your Pods together, separately, or in specific locations.

_Workload separation_ lets you use [taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to tell GKE to separate Pods onto different nodes, place Pods on nodes that meet specific criteria, or to schedule specific workloads together. What you need to do to configure workload separation depends on your GKE cluster configuration. The following table describes the differences:

Workload separation configuration  
---  
  
  * Autopilot
  * [Standard with node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable)

| Add a toleration for a specific key:value pair to your Pod specification, and select that key:value pair using a nodeSelector. GKE creates nodes, applies the corresponding node taint, and schedules the Pod on the node. For instructions, refer to Separate workloads in Autopilot clusters on this page.  
Standard without node auto-provisioning | 

  1. Create a node pool with a node taint and a node label
  2. Add a toleration for that taint to the Pod specification

For instructions, refer to [Isolate your workloads in dedicated node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes). **Caution:** With this method, if existing tainted nodes don't have enough resources to support a Pod with a toleration, the Pod remains in the Pending state.  
  
This guide uses an example scenario in which you have two workloads, a batch job and a web server, that you want to separate from each other.

## When to use workload separation in GKE

Workload separation is useful when you have workloads that perform different roles and shouldn't run on the same underlying machines. Some example scenarios include the following:

  * You have a batch coordinator workload that creates Jobs that you want to keep separate.
  * You run a game server with a matchmaking workload that you want to separate from session Pods.
  * You want to separate parts of your stack from each other, such as separating a server from a database.
  * You want to separate some workloads for compliance or policy reasons.

**Warning:** Workload separation should **never** be used as a primary security boundary. It is not a method of isolating untrusted workloads, and doesn't mitigate all escalation paths. Workload separation is not intended for use as a defense mechanism. To learn about the risks of using Kubernetes scheduling as an isolation method, see [Avoiding privilege escalation attacks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes#avoiding-privesc).

## Pricing

In Autopilot clusters, you're billed for the resources that your Pods request while running. For details, refer to [Autopilot pricing](https://cloud.google.com/kubernetes-engine/pricing#autopilot_mode). Pods that use workload separation have [higher minimum resource requests](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#workload-separation) enforced than regular Pods.

In Standard clusters, you're billed based on the hardware configuration and size of each node, regardless of whether Pods are running on the nodes. For details, refer to [Standard pricing](https://cloud.google.com/kubernetes-engine/pricing#standard_mode).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have a GKE cluster. To learn how to create a cluster, use one of the following:

    * [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) (recommended)
    * [Create a Standard cluster with node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#enable)
    * [Create a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster#create-regional-multi-zone-nodepool)



## Separate workloads in Autopilot clusters

To separate workloads from each other, add a toleration and a node selector to each workload specification that defines the node on which the workload should run. This method also works on Standard clusters that have node auto-provisioning enabled.

  1. Save the following manifest as `web-server.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: web-server
         spec:
           replicas: 6
           selector:
             matchLabels:
               pod: nginx-pod
           template:
             metadata:
               labels:
                 pod: nginx-pod
             spec:
               **tolerations :
               - key: group
                 operator: Equal
                 value: "servers"
                 effect: NoSchedule
               nodeSelector:
                 group: "servers"**
               containers:
               - name: web-server
                 image: nginx
         

This manifest includes the following fields:

     * `spec.tolerations`: GKE can place the Pods on nodes that have the `group=servers:NoSchedule` taint. GKE can't schedule Pods that don't have this toleration on those nodes.
     * `spec.nodeSelector`: GKE must place the Pods on nodes that have the `group: servers` node label.

GKE adds the corresponding labels and taints to nodes that GKE automatically provisions to run these Pods.

  2. Save the following manifest as `batch-job.yaml`:
         
         apiVersion: batch/v1
         kind: Job
         metadata:
           name: batch-job
         spec:
           completions: 5
           backoffLimit: 3
           ttlSecondsAfterFinished: 120
           template:
             metadata:
               labels:
                 pod: pi-pod
             spec:
               restartPolicy: Never
               **tolerations :
               - key: group
                 operator: Equal
                 value: "jobs"
                 effect: NoSchedule
               nodeSelector:
                 group: "jobs"**
               containers:
               - name: pi
                 image: perl
                 command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
         

This manifest includes the following fields:

     * `spec.tolerations`: GKE can place the Pods on nodes that have the `group=jobs:NoSchedule` taint. GKE can't schedule Pods that don't have this toleration on those nodes.
     * `spec.nodeSelector`: GKE must place the Pods on nodes that have the `group: jobs` node label.

GKE adds the corresponding labels and taints to nodes that GKE automatically provisions to run these Pods.

  3. Deploy the workloads:
         
         kubectl apply -f batch-job.yaml web-server.yaml
         




When you deploy the workloads, GKE does the following for each workload:

  1. GKE looks for existing nodes that have the corresponding node taint and node label specified in the manifest. If nodes exist and have available resources, GKE schedules the workload on the node.
  2. If GKE doesn't find an eligible existing node to schedule the workload, GKE creates a new node and applies the corresponding node taint and node label based on the manifest. GKE places the Pod on the new node.



The presence of the `NoSchedule` effect in the node taint ensures that workloads without a toleration don't get placed on the node.

## Verify the workload separation

List your Pods to find the names of the nodes:
    
    
    kubectl get pods --output=wide
    

The output is similar to the following:
    
    
    NAME                          READY   ...   NODE
    batch-job-28j9h               0/1     ...   gk3-sandbox-autopilot-nap-1hzelof0-ed737889-2m59
    batch-job-78rcn               0/1     ...   gk3-sandbox-autopilot-nap-1hzelof0-ed737889-2m59
    batch-job-gg4x2               0/1     ...   gk3-sandbox-autopilot-nap-1hzelof0-ed737889-2m59
    batch-job-qgsxh               0/1     ...   gk3-sandbox-autopilot-nap-1hzelof0-ed737889-2m59
    batch-job-v4ksf               0/1     ...   gk3-sandbox-autopilot-nap-1hzelof0-ed737889-2m59
    web-server-6bb8cd79b5-dw4ds   1/1     ...   gk3-sandbox-autopilot-nap-1eurxgsq-f2f3c272-n6xm
    web-server-6bb8cd79b5-g5ld6   1/1     ...   gk3-sandbox-autopilot-nap-1eurxgsq-9f447e18-275z
    web-server-6bb8cd79b5-jcdx5   1/1     ...   gk3-sandbox-autopilot-nap-1eurxgsq-9f447e18-275z
    web-server-6bb8cd79b5-pxdzw   1/1     ...   gk3-sandbox-autopilot-nap-1eurxgsq-ccd22fd9-qtfq
    web-server-6bb8cd79b5-s66rw   1/1     ...   gk3-sandbox-autopilot-nap-1eurxgsq-ccd22fd9-qtfq
    web-server-6bb8cd79b5-zq8hh   1/1     ...   gk3-sandbox-autopilot-nap-1eurxgsq-f2f3c272-n6xm
    

This output shows that the `batch-job` Pods and the `web-server` Pods always run on different nodes.

## Limitations of workload separation with taints and tolerations

You can't use the following key prefixes for workload separation:

  * GKE and Kubernetes-specific keys
  * *cloud.google.com/
  * *kubelet.kubernetes.io/
  * *node.kubernetes.io/



You should use your own, unique keys for workload separation.

## Separate workloads in Standard clusters without node auto-provisioning

Separating workloads in Standard clusters without node auto-provisioning requires that you manually create node pools with the appropriate node taints and node labels to accommodate your workloads. For instructions, refer to [Isolate your workloads in dedicated node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes). Only use this approach if you have specific requirements that require you to manually manage your node pools.

## Create a cluster with node taints

When you create a cluster in GKE, you can assign node taints to the cluster. This assigns the taints to _all nodes created with the cluster_.

If you create a node pool, the node pool does not inherit taints from the cluster. If you want taints on the node pool, you must use the `--node-taints` flag when you create the node pool.

If you create a Standard cluster with node taints that have the `NoSchedule` effect or the `NoExecute` effect, GKE can't schedule some GKE managed components, such as `kube-dns` or `metrics-server` on the default node pool that GKE creates when you create the cluster. GKE can't schedule these components because they don't have the corresponding tolerations for your node taints. You must add a new node pool that satisfies one of the following conditions:

  * No taints
  * A taint that has the `PreferNoSchedule` effect
  * The `components.gke.io/gke-managed-components=true:NoSchedule` taint



Any of these conditions allow GKE to schedule GKE managed components in the new node pool.

For instructions, refer to [Isolate workloads on dedicated nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-nodes).

### gcloud

Create a cluster with node taints:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --node-taints KEY=VALUE:EFFECT
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `EFFECT`: one of the following effects: `PreferNoSchedule`, `NoSchedule`, or `NoExecute`.
  * `KEY=VALUE`: a key-value pair associated with the `EFFECT`.



### Console

Create a cluster with node taints:

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Configure your cluster as desired.

  3. From the navigation pane, under **Node Pools** , expand the node pool you want to modify, and then click **Metadata**.

  4. In the **Node taints** section, click _add_ **Add Taint**.

  5. In the **Effect** drop-down list, select the desired effect.

  6. Enter the desired key-value pair in the **Key** and **Value** fields.

  7. Click **Create**.




### API

When you use the API to create a cluster, include the `nodeTaints` field under `nodeConfig:
    
    
    POST https://container.googleapis.com/v1/projects/PROJECT_ID/zones/COMPUTE_ZONE/clusters
    
    {
      'cluster': {
        'name': 'example-cluster',
        'nodeConfig': {
          'nodeTaints': [
            {
              'key': 'special',
              'Value': 'gpu',
              'effect': 'PreferNoSchedule'
            }
          ]
          ...
        }
        ...
      }
    }
    

## Remove all taints from a node pool

To remove all taints from a node pool, run the following command:
    
    
    gcloud beta container node-pools update POOL_NAME \
        --node-taints="" \
        --cluster=CLUSTER_NAME
    

Replace the following:

  * `POOL_NAME`: the name of the node pool to change.
  * `CLUSTER_NAME`: the name of the cluster of the node pool.



## What's next

  * [Enforce pre-defined security policies using the PodSecurity admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission)
  * [Run a full-stack workload at scale](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/full-stack-scale)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
