---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes/
title: Create Standard clusters and node pools with Arm nodes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:52.699951+00:00
---

# Create Standard clusters and node pools with Arm nodes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Create Standard clusters and node pools with Arm nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to create a GKE Standard cluster or node pool with Arm nodes so that you can run Arm workloads on Google Kubernetes Engine (GKE). To learn how to deploy Arm workloads on Autopilot clusters, see [Deploy Autopilot workloads on Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads).

You can create clusters with Arm nodes by using the [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series), or [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) machine series. To learn more about the benefits of Arm and choose the best machine series for your workloads, see [Arm VMs on Compute](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute).

With GKE, you can create a cluster that has node pools with one architecture type (for example, Arm) or multiple architecture types (for example, Arm and x86). When you run nodes with multiple architecture types, you can deploy workloads across architectures to the same cluster.

This document is for Operators and Developers who provision and configure cloud resources who deploy workloads. For more information about common roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this document, familiarize yourself with [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Review the [requirements and limitations for C4A, N4A, and T2A nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations).
  * Ensure that you have the necessary permissions to create clusters. At minimum, you should be a [Kubernetes Engine Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container).



## Set up IAM service accounts for GKE

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

**Best practice:** Instead of using the Compute Engine default service account, create a _custom service account_ for your nodes to use and give it only the permissions that GKE needs to run system tasks. For more information, see [Configure a custom node service account](https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts#configure-custom-account). 

To grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account, complete the following steps:

### Console

  1. Go to the **Welcome** page: 

[Go to Welcome](https://console.cloud.google.com/welcome)

  2. In the **Project number** field, click content_copy **Copy to clipboard**.
  3. Go to the **IAM** page: 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  4. Click person_add **Grant access**.
  5. In the **New principals** field, specify the following value: 
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with the project number that you copied. 
  6. In the **Select a role** menu, select the **Kubernetes Engine Default Node Service Account** role.
  7. Click **Save**.



### gcloud

  1. Find your Google Cloud project number: 
         
         gcloud projects describe PROJECT_ID \
             --format="value(projectNumber)"

Replace `PROJECT_ID` with your project ID.

The output is similar to the following:
         
         12345678901
         

  2. Grant the `roles/container.defaultNodeServiceAccount` role to the Compute Engine default service account: 
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
             --role="roles/container.defaultNodeServiceAccount"

Replace `PROJECT_NUMBER` with the project number from the previous step.




## Create a cluster with an Arm node pool

The following instructions explain how to create a new cluster with a node pool running Arm nodes from the [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [N4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series), or [Tau T2A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines) machine series.

You can use the gcloud CLI, the Google Cloud console, or Terraform to create the cluster.

### gcloud

Create a new zonal cluster with the default node pool using Arm nodes:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --node-locations NODE_LOCATIONS \
        --machine-type ARM_MACHINE_TYPE \
        --num-nodes NUM_NODES
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster with an Arm node pool.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters. The selected region or zone must be one of the [available locations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations) for the Arm machine series that you choose.
  * `NODE_LOCATIONS`: the zone(s) for your node pool, such as `us-central1-a`. You must choose from the [available zones](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations) for the Arm machine series or node pool creation might fail.
  * `ARM_MACHINE_TYPE`: one of the available [C4A machine shapes](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [N4A machine shapes](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series), or [T2A machine shapes](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines), such as `c4a-standard-8`, `n4a-standard-4`, or `t2a-standard-16`.
  * `NUM_NODES`: the number of nodes for your Arm node pool.



We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

To specify a custom service account in the gcloud CLI, add the following flag to your command:
    
    
    --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace SERVICE_ACCOUNT_NAME with the name of your minimally-privileged service account.

If you want to set additional settings for your cluster, see the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) reference for a complete list of available settings on cluster creation.

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. Configure your cluster. For more information, see the instructions for [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster), or [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).

  3. Choose a location where Arm nodes are available.

     1. In the **Cluster basics** section, under **Location type** , choose Zonal or Regional:
     2. In the drop-down menu, choose a zone or region [where Arm nodes are available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations).
     3. Check the box to **Specify default node locations**. Select zone(s) [where Arm nodes are available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations).
  4. To select an Arm machine type, in the **Nodes** subsection, under **Configure node settings > Machine configuration > Machine family**, select **GENERAL-PURPOSE**. In the **Series** drop-down menu, select **C4A** , **N4A** , or **T2A**. In the **Machine type** drop-down menu, choose from the available options.

  5. Optionally, specify a custom IAM service account for your nodes: 
     1. In the **Advanced settings** page, expand the **Security** section.
     2. In the **Service account** menu, select your preferred service account.

We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

  6. Click **Create**.




### Terraform

To create a zonal cluster with the default node pool using Arm nodes using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name               = "gke-standard-zonal-arm-cluster"
      location           = "us-central1-a"
      node_locations     = ["us-central1-b", "us-central1-f"]
      initial_node_count = 2
    
      node_config {
        machine_type    = "t2a-standard-1"
        service_account = google_service_account.default.email
      }
    }

For more information about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## Add an Arm node pool to a GKE cluster

You can add a new node pool to a GKE Standard cluster using gcloud CLI, the Google Cloud console, or Terraform.

As a best practice for creating a GKE cluster using any types of nodes, we recommend that you create and use a minimally-privileged Identity and Access Management (IAM) service account for your node pools to use instead of the Compute Engine default service account.

**Note:** If you don't use custom IAM service accounts to create your GKE clusters or node pools, ensure that the default Compute Engine service account in your project has the required permissions for GKE. In organizations that enforce the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account won't automatically get the required permissions for GKE. This constraint is enforced by default for organizations that were created on or after May 3, 2024. For details, see [Default GKE node service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts#default-gke-service-agent). 

For instructions on creating a minimally-privileged service account, refer to [Hardening your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

### gcloud

Add an Arm node pool to an existing cluster:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --node-locations NODE_LOCATIONS \
        --machine-type ARM_MACHINE_TYPE \
        --num-nodes NUM_NODES \
        --service-account SERVICE_ACCOUNT
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the new Arm node pool for your existing cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `CLUSTER_NAME`: the name of the cluster where you want to add an Arm node pool.
  * `NODE_LOCATIONS`: the zone(s) for your node pool, such as `us-central1-a`. You must choose from the [available zones](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations) for the Arm machine series or node pool creation might fail.
  * `ARM_MACHINE_TYPE`: one of the available [C4A machine shapes](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series), [N4A machine shapes](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n4a_series), or [T2A machine shapes](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines), such as `c4a-standard-8`, `n4a-standard-4`, or `t2a-standard-16`.
  * `NUM_NODES`: the number of nodes for your Arm node pool.



We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

To specify a custom service account in the gcloud CLI, add the following flag to your command:
    
    
    --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace SERVICE_ACCOUNT_NAME with the name of your minimally-privileged service account.

If you want to set additional settings for your node pool, see the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) reference for a complete list of available settings on node pool creation.

### Console

To add an Arm node pool to an existing cluster, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. Configure your node pool.

  6. Choose node locations [where Arm nodes are available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations).

     1. In the **Node pool details** section, check the **Specify node locations** box.
     2. Select zone(s) [where Arm nodes are available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke#arm-requirements-limitations).
  7. To select an Arm machine type, in the **Nodes** subsection, under **Configure node settings > Machine configuration > Machine family**, select **GENERAL-PURPOSE**. In the **Series** drop-down menu, select **C4A** , **N4A** , or **T2A**. In the **Machine type** drop-down menu, choose from the available options.

  8. In the navigation menu, click **Security**. 

  9. Optionally, specify a custom IAM service account for your nodes: 
     1. In the **Advanced settings** page, expand the **Security** section.
     2. In the **Service account** menu, select your preferred service account.

We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

  10. Click **Create** to add the node pool.




### Terraform

To add a node pool that uses Arm nodes to an existing cluster using Terraform, refer to the following example:
    
    
    resource "google_container_node_pool" "default" {
      name           = "gke-standard-zonal-arm-node-pool"
      cluster        = google_container_cluster.default.id
      node_locations = ["us-central1-a"]
      node_count     = 1
    
      node_config {
        machine_type = "t2a-standard-1"
    
        service_account = google_service_account.default.email
      }
    }

Replace `google_container_cluster.default.id` with the name of your cluster.

For more information about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## What's next

  * [Build multi-architecture images for Arm workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm)
  * [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment)
  * [Migrate x86 application on GKE to multi-arch with Arm](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
