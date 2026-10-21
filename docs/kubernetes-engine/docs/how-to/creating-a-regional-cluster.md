---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster/
title: Creating a regional cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:51.115478+00:00
---

# Creating a regional cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Creating a regional cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document shows how to create a Standard [regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) to increase availability of the cluster's control plane and workloads during cluster upgrades, automated maintenance, or a zonal disruption.

GKE [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster) clusters are always regional.

## Overview

When you create a regional cluster instead of a [zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#zonal_clusters), the cluster's control plane is replicated across multiple zones in a given region. For node pools in a regional cluster, you can manually specify the zone(s) in which to run the node pools or you can use the default configuration, which replicates each node pool across three zones of the control plane's region. All zones must be within the same region as the cluster's control plane.

Regional clusters replicate resources across multiple zones and consume additional [quotas](https://docs.cloud.google.com/kubernetes-engine/quotas).

To learn about the different cluster availability types, see [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#availability).

The instructions in the following sections show you how to:

  * Create a regional cluster with a single-zone node pool.
  * Create a regional cluster with a multi-zone node pool.



After you create a regional cluster, you cannot convert it to a zonal cluster.

The minimum information that you need to specify when creating a new regional cluster is a name, project (usually the current project), and region (usually the default location for command line tools), using the default settings for all other values. However, there are more possible configuration settings, only some of which are described in this guide and some of which can't be changed after cluster creation. Ensure that you understand which settings can't be changed after cluster creation, and that you choose the right setting when creating a cluster if you don't want to have to create it again.

You can see an overview of cluster configuration options in [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters), and a complete list of possible options in the [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) and Terraform [`google_container_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#argument-reference) reference guides.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure you have the correct permissions to create clusters. At minimum, you should be a [Kubernetes Engine Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container).
  * If you want to register your new cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), ensure that you have the required [APIs and permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin).

**Caution:** If you have the organization policy constraint [constraints/compute.vmExternalIpAccess](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) configured to `Deny All` or to restrict external IPs to specific VM instances at the organization, folder, or project level where you are trying to create a public GKE cluster, then your cluster creation operations will fail. See the [troubleshooting information](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#external-ip) for details.

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




## Create a regional cluster with a single-zone node pool

The following instructions show you how to create a regional cluster with a node pool operating in a single zone within the region. The cluster's control plane is replicated across multiple zones in the specified region, but the nodes are located in the single zone, and are not replicated to other zones.

You can use the gcloud CLI, the Google Cloud console, or Terraform to create the cluster.

If you're developing GKE applications with Cloud Code for VS Code, try [creating clusters with Cloud Code](https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster#create_a_cluster_and_add_it_to_your_kubeconfig).

### gcloud

Before executing the gcloud CLI commands to create the cluster, set the correct project by running the following:
    
    
    gcloud config set project PROJECT_ID
    # gcloud config set billing/quota_project PROJECT_ID
    

To create a regional cluster with the gcloud CLI, use one of the following commands and replace the following variables:

  * `CLUSTER_NAME`: the name of your new regional cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region such as `us-central1`.
  * `COMPUTE_ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your node pool, such as `us-central1-a`. The zone must be in the same region as the cluster control plane.
  * `CHANNEL`: the type of [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), which can be one of `rapid`, `regular`, `stable`, or `None` ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)). By default, the cluster is enrolled in the `regular` release channel.
  * `VERSION`: the [version](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) you want to specify for your cluster.



We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

To specify a custom service account in the gcloud CLI, add the following flag to your command:
    
    
    --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace SERVICE_ACCOUNT_NAME with the name of your minimally-privileged service account.

**Caution:** You can't modify the service account on an existing node pool after creation.

**Using a specific release channel:**

To create a new cluster using a specific release channel, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --node-locations COMPUTE_ZONE \
        **--release-channel CHANNEL**
    

**Using a specific version:**

To create a new cluster using a specific cluster version, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        --node-locations COMPUTE_ZONE \
        **--cluster-version VERSION**
    

**Note:** If you specify a cluster version, the cluster uses that specific version and is enrolled in the most mature release channel where that version is available.

**Example**

The following command creates a regional cluster enrolled in the `regular` release channel (default), with three nodes (default) in the `us-west1-c` zone:
    
    
    gcloud container clusters create my-regional-cluster \
        --location us-west1 \
        --node-locations us-west1-c
    

**Example**

The following command creates a regional cluster enrolled in the `regular` release channel (default), with two nodes located in the `us-west1-c` zone:
    
    
    gcloud container clusters create my-regional-cluster \
        --location us-west1 \
        --node-locations us-west1-c \
        --num-nodes 2
    

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. In the **Cluster basics** section, complete the following:

     1. Enter the **Name** for your cluster. 
     2. For the **Location type** , select **Regional** , and then select the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
     3. If you want to override the default node locations (for example, to run in a single zone), select the **Specify default node locations** checkbox, and then choose the zone(s) in which you want the node pools to run. 
     4. Choose a [**release channel**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). You can, optionally, select **No channel** , but this configuration option is deprecated and will be removed. For more information, see [Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel).

     5. Optional: Specify a control plane version from the **Version** drop-down list. 

  3. Optional: Configure other settings for your new cluster.

  4. Optional: If you want to register your new cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), go to the **Advanced settings** section, and follow the Google Cloud console instructions for [Create and register a new cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#console) to complete your cluster registration.

  5. From the navigation pane, under **Node Pools** , click **default-pool**.

  6. In the **Node pool details** section, complete the following:

     1. Enter a **Name** for the default [Node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
     2. Optional: Choose the **Node version**.
     3. Enter the **Number of nodes** to create in the cluster. You must have available [resource quota](https://docs.cloud.google.com/compute/quotas) for the nodes and their resources (such as firewall routes).
     4. Optional: You can choose to disable node auto-upgrades, however we recommend that you review the [considerations before disabling node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#considerations) before choosing this option. 
  7. From the navigation pane, under **Node Pools** , click **Nodes**.

  8. From the **Image type** drop-down list, select the [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

  9. Choose the default [**Machine configuration**](https://docs.cloud.google.com/compute/docs/machine-types) to use for the instances. Each machine type is billed differently. The default machine type is `e2-medium`. For machine type pricing information, refer to the [machine type price sheet](https://cloud.google.com/compute/pricing#standard_machine_types).

  10. From the **Boot disk type** drop-down list, select the [disk type](https://docs.cloud.google.com/compute/docs/disks).

  11. Enter the **Boot disk size**.

  12. Optional: From the navigation pane, under **Node Pools** , click **Security**. 

  13. Optionally, specify a custom IAM service account for your nodes: 
     1. In the **Advanced settings** page, expand the **Security** section.
     2. In the **Service account** menu, select your preferred service account.

We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

**Caution:** You can't modify the service account on an existing node pool after creation.
  14. Click **Create**.




### Terraform

To create a regional cluster with a single-zone node pool using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name               = "gke-standard-regional-single-zone"
      location           = "us-west1"
      node_locations     = ["us-west1-c"]
      initial_node_count = 2
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Interact with a cluster using kubectl

After you create a cluster, you need to [configure `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#store_info) before you can interact with the cluster from the command line.

## Create a regional cluster with a multi-zone node pool

The following instructions show you how to create a regional cluster with a multi-zone node pool, which is the default set up. The cluster's control plane and nodes are replicated across multiple zones in the specified region.

You can use the gcloud CLI, Google Cloud console, or Terraform to create the cluster.

If you're developing GKE applications with Visual Studio Code, try [creating clusters with Cloud Code](https://docs.cloud.google.com/code/docs/vscode/create-configure-gke-cluster).

### gcloud

Before executing the gcloud CLI commands to create the cluster, set the correct project by running the following:
    
    
    gcloud config set project PROJECT_ID
    # The project set above is used for quota and billing by default.
    # To use a different project for quota and billing, run the following command:
    # gcloud config set billing/quota_project PROJECT_ID
    

To create a regional cluster with the gcloud CLI, use one of the following commands and replace the following variables:

  * `CLUSTER_NAME`: the name of your new regional cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region such as `us-central1`.
  * `CHANNEL`: the type of [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), which can be one of `rapid`, `regular`, `stable`, or `None` ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)). By default, the cluster is enrolled in the `regular` release channel.
  * `VERSION`: the [version](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) you want to specify for your cluster.
  * For regions with more than three [zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) or in cases where fewer zones is preferred, you can use the optional [`--node-locations`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-locations) flag to override the default zones in which the nodes are replicated.



We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

To specify a custom service account in the gcloud CLI, add the following flag to your command:
    
    
    --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace SERVICE_ACCOUNT_NAME with the name of your minimally-privileged service account.

**Using a specific release channel:**

To create a new cluster using a specific release channel, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        **--release-channel CHANNEL**
    

**Using a specific version:**

To create a new cluster using a specific cluster version, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location CONTROL_PLANE_LOCATION \
        **--cluster-version VERSION**
    

**Note:** If you specify a cluster version, the cluster uses that specific version and is _not_ enrolled in a release channel.

**Example**

The following command creates a regional cluster enrolled in the `regular` release channel, with nine nodes in `us-west1` (three zones with three nodes each, which is default):
    
    
    gcloud container clusters create my-regional-cluster --location us-west1
    

**Example**

The following command creates a regional cluster enrolled in the `regular` release channel, with six nodes (three zones with two nodes each, specified by `--num-nodes`):
    
    
    gcloud container clusters create my-regional-cluster \
        --location us-west1 \
        --num-nodes 2
    

**Example**

The following command creates a regional cluster enrolled in the `regular` release channel, with six nodes in two zones (two zones, specified by `--node-locations`, with three nodes each):
    
    
    gcloud container clusters create my-regional-cluster \
        --location us-central1 \
        --node-locations us-central1-b,us-central1-c
    

### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. In the **Cluster basics** section, complete the following:

     1. Enter the **Name** for your cluster. 
     2. For the **Location type** , select **Regional** , and then select the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
     3. If you want to override the default node locations (for example, to run in a single zone), select the **Specify default node locations** checkbox, and then choose the zone(s) in which you want the node pools to run. 
     4. Choose a [**release channel**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). You can, optionally, select **No channel** , but this configuration option is deprecated and will be removed. For more information, see [Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel).

     5. Optional: Specify a control plane version from the **Version** drop-down list. 

  3. Optional: Configure other settings for your new cluster.

  4. Optional: If you want to register your new cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), go to the **Advanced settings** section, and follow the Google Cloud console instructions for [Create and register a new cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#console) to complete your cluster registration.

  5. From the navigation pane, under **Node Pools** , click **default-pool**.

  6. In the **Node pool details** section, complete the following:

     1. Enter a **Name** for the default [Node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
     2. Optional: Choose the **Node version**.
     3. Enter the **Number of nodes** to create in the cluster. You must have available [resource quota](https://docs.cloud.google.com/compute/quotas) for the nodes and their resources (such as firewall routes).
     4. Optional: You can choose to disable node auto-upgrades, however we recommend that you review the [considerations before disabling node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#considerations) before choosing this option. 
  7. From the navigation pane, under **Node Pools** , click **Nodes**.

  8. From the **Image type** drop-down list, select the [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

  9. Choose the default [**Machine configuration**](https://docs.cloud.google.com/compute/docs/machine-types) to use for the instances. Each machine type is billed differently. The default machine type is `e2-medium`. For machine type pricing information, refer to the [machine type price sheet](https://cloud.google.com/compute/pricing#standard_machine_types).

  10. From the **Boot disk type** drop-down list, select the [disk type](https://docs.cloud.google.com/compute/docs/disks).

  11. Enter the **Boot disk size**.

  12. Optional: From the navigation pane, under **Node Pools** , click **Security**. 

  13. Optionally, specify a custom IAM service account for your nodes: 
     1. In the **Advanced settings** page, expand the **Security** section.
     2. In the **Service account** menu, select your preferred service account.

We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

**Caution:** You can't modify the service account on an existing node pool after creation.
  14. Click **Create**.




### Terraform

To create a regional cluster with a multi-zone node pool using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name               = "gke-standard-regional-multi-zone"
      location           = "us-central1"
      node_locations     = ["us-central1-b", "us-central1-c"]
      initial_node_count = 2
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Interact with a cluster using kubectl

After you create a cluster, you need to [configure `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#store_info) before you can interact with the cluster from the command line.

## What's next

  * Learn more about the [types of clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters) you can create.
  * [Create a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
