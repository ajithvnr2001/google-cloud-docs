---
url: https://docs.cloud.google.com/telecom-network-automation/docs/manage-gke/
title: Manage GKE infrastructure \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:37.402051+00:00
---

# Manage GKE infrastructure  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/manage-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Manage GKE infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

A GKE blueprint contains custom resources you can combine to specify the intent to deploy a GKE cluster. The following list defines the role of each custom resource:

  * `ContainerCluster`: creates a private GKE cluster with a provisioned service mesh.
  * `ClusterInit`: initializes the cluster's lifecycle that Telecom Network Automation (Telecom Network Automation) manages. This lifecycle includes installing Telecom Network Automation components on the GKE cluster.
  * `SourceRepoRepository` and `Repository`: sets up the GitOps pipeline for the created GKE cluster using Cloud Source Repository and Porch along with ConfigSync, installed from the previous resource.
  * `ContainerNodePool`: creates a node pool with Ubuntu OS, SSD disk type and `e2-standard-2 machine` type as default. You can edit these details.



When creating a deployment, you can customize the blueprint using following parameters in the `setters.yaml` file:

Parameter | Description  
---|---  
`project-id` | The project id of the current project.  
`project-num` | The project number of the current project.  
`cluster-name` | The name of the GKE cluster.  
`location` | The compute location of the cluster  
`master-ip-range` | The IP CIDR block that GKE main nodes use  
`cluster-ipv4-cidr-blocks` | The IP CIDR block that pods use.  
`services-ipv4-cidr-blocks` | The IP CIDR block that services use.  
`compute-network-name` | The name of the compute network. Change this name if you don't intend to use a VPC where an Orchestration cluster is created for the GKE cluster.  
`clients-ipv4-cidr-blocks` | The IP CIDR block for clients that access the cluster  
`node-count` | The number of nodes in the node pool per zone. If a regional cluster is created, the number of nodes in the node pool increases to three times the original amount.  
`nodepool-name` | The name of the node pool.  
`node-machine-type` | The type of the node machine.  
  
## GKE blueprints

### Create a GKE blueprint

  1. From the navigation menu, click **Blueprints.**
  2. From the drop-down menu, select your preferred Orchestration cluster.
  3. Click **Import from Library.**
  4. Select **GKE Cluster blueprint**.
  5. Click **Add Blueprint**.
  6. On the next page, specify a name for the blueprint. 
     1. Optionally, add any labels you need.
  7. Click **Create**. Your blueprint appears in the **Draft Blueprints** list.



### Edit a blueprint

  1. From the navigation menu, click **Blueprints > Drafts Blueprint**.
  2. Select your preferred blueprint. A blueprint editor appears.
  3. Edit the `cluster.yaml` and `nodepool.yaml` files.
  4. Afterwards, click **Save File**.

**Note:** You must save each file individually.



### Propose a blueprint

  1. From the navigation menu, click **Blueprints > Drafts Blueprint**.
  2. Select your preferred blueprint. A blueprint editor appears.
  3. Click **Propose**. The status of the blueprint updates to **Proposed**.



### Approve a blueprint

  1. From the navigation menu, click **Blueprints**.
  2. Click the **Action** icon on your preferred blueprint.
  3. Select **Approve**. The blueprint appears in **Approved Blueprints**.



## GKE deployment

### Create a GKE Deployment

  1. From the navigation menu, click **Blueprints > Approved Blueprints**.
  2. Click the GKE blueprint you want to deploy.
  3. Click **Create Deployment**.
  4. Provide a name for the deployment.
  5. Click **Create Deployment**. The deployment appears in **Draft Deployment**.



### Edit a GKE deployment

  1. From the navigation menu, click **Blueprints**.
  2. Select the GKE deployment you want to edit. A deployment editor appears.
  3. Edit the `setters.yaml` file.
  4. Afterwards, click **Save File**.



### Apply a GKE deployment

  1. From the navigation menu, click **Blueprints**.
  2. Select the name of the GKE deployment you want to apply. A deployment editor appears.
  3. Click **Deploy**. A confirmation dialog appears.
  4. Confirm the deployment by clicking **Deploy**. The deployment appears in **Applied Deployment**.

**Note:** The GKE cluster name must be less than 15 characters, and have a unique cluster name for each blueprint deployment. Deleting a GKE blueprint deployment does not* *make the cluster name reusable.

### Delete a GKE cluster

  1. From the navigation menu, click **Deployments > Applied Deployments**.
  2. Select the GKE deployment you want to delete.
  3. Click **Delete**.
  4. Confirm the deletion of the deployment.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
