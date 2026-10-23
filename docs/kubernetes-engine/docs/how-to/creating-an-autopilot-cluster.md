---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster/
title: Create an Autopilot cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:46.479869+00:00
---

# Create an Autopilot cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Create an Autopilot cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page explains how to create a Google Kubernetes Engine (GKE) cluster in [Autopilot mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes). Autopilot is a GKE mode of operation that lets you focus on your services and applications, while GKE manages your nodes and infrastructure. When you deploy your workloads, GKE provisions, configures, and manages the resources and hardware, including when you scale. 

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * If you are using a newly created Google Cloud project, you must first explicitly [link a billing account to your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project) before you can enable the Kubernetes Engine API or provision cluster resources.
  * Ensure you have the correct permissions to create clusters. At minimum, you should be a [Kubernetes Engine Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container).
  * If you want to register your new cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), ensure that you have the required [APIs and permissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin).

**Caution:** If you have the organization policy constraint [constraints/compute.vmExternalIpAccess](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) configured to `Deny All` or to restrict external IPs to specific VM instances at the organization, folder, or project level where you are trying to create a public GKE Autopilot cluster, then your cluster creation operations will fail. See the [troubleshooting information](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#external-ip) for details.

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




## Create an Autopilot cluster

The minimum information that you need to specify when creating a new Autopilot cluster is a name, project (usually the current project), and region (usually the default region for command line tools). However, there are many more possible configuration settings, some of which can't be changed after cluster creation. Ensure that you understand which settings can't be changed after cluster creation, and that you choose the right setting when creating a cluster if you don't want to have to create it again.

You can see an overview of cluster configuration options in [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters), and a complete list of possible options in the [`gcloud container clusters create-auto`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) and Terraform [`google_container_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#argument-reference) reference guides.

You can create an Autopilot cluster by using the Google Cloud CLI, the Google Cloud console, or by using Terraform:

### gcloud

Run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new Autopilot cluster.
  * `LOCATION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
  * `PROJECT_ID`: your project ID.



We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

To specify a custom service account in the gcloud CLI, add the following flag to your command:
    
    
    --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace SERVICE_ACCOUNT_NAME with the name of your minimally-privileged service account.

**Caution:** You cannot modify the IAM service account on an existing Autopilot cluster.

For a list of other options that you can specify, see the [`gcloud container clusters create-auto`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) reference documentation.

### Console

Perform the following tasks:

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

  2. In the **Cluster basics** section, complete the following:

  3. Enter the **Name** for your cluster.

  4. Select a [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.

     1. Optional: If you want to register your new cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), go to the **Fleet registration** section, and follow the Google Cloud console instructions for [Create and register a new cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#console) to complete your cluster registration.
  5. For the **Networking** section, refer to [Customize your network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#configure-control-plane-access) for configuration instructions. 

  6. Optionally, specify a custom IAM service account for your nodes: 
     1. In the **Advanced settings** page, expand the **Security** section.
     2. In the **Service account** menu, select your preferred service account.

We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

  7. Optionally, configure other settings such as maintenance windows and advanced security features.

  8. Click **Create**.




### Terraform

To create a minimal Autopilot cluster using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name     = "gke-autopilot-basic"
      location = "us-central1"
    
      enable_autopilot = true
    }

To create an Autopilot cluster that uses a custom IAM service account, follow these steps:

  1. Create an IAM service account and grant it the `roles/container.defaultNodeServiceAccount` role on the project:
         
         resource "google_service_account" "default" {
           account_id   = "gke-node-service-account"
           display_name = "GKE node service account"
         }
         
         data "google_project" "project" {
         }
         
         resource "google_project_iam_member" "default" {
           project = data.google_project.project.project_id
           role    = "roles/container.defaultNodeServiceAccount"
           member  = "serviceAccount:${google_service_account.default.email}"
         }

  2. Create an Autopilot cluster that uses the new service account:
         
         resource "google_container_cluster" "default" {
           name     = "autopilot-custom-account"
           location = "us-central1"
         
           enable_autopilot = true
         
           cluster_autoscaling {
             auto_provisioning_defaults {
               service_account = google_service_account.default.email
             }
           }
         }




The example on this page covers provisioning a basic Autopilot cluster. For an end-to-end example that configures a custom VPC network and deploys a sample workload, see [Create a cluster and deploy a workload using Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster-using-terraform). For more information about using Terraform, see [Provision GKE resources with Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Create an Autopilot cluster with a specific release channel and version

By default, GKE enrolls new Autopilot clusters in the Regular [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels), with the default GKE version in the channel. You can change the release channel when you create an Autopilot cluster using the gcloud CLI, the Google Cloud console, or by using Terraform.

You can also set a specific GKE version when you create a cluster using the gcloud CLI. Setting the cluster version is only useful if you have a specific version requirement. To set the cluster version, specify the `--cluster-version` flag in the [`gcloud container clusters create-auto` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--cluster-version). The version that you specify must be an available GKE version.

The following instructions for setting the release channel and version are optional. Unless you require a specific GKE version, we recommend that you keep the default release channel setting.

###  gcloud 

Run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=LOCATION \
        --release-channel=RELEASE_CHANNEL
    

Replace `RELEASE_CHANNEL` with the name of the [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels) for the cluster. The default is `Regular`.

Optionally, specify `--cluster-version=CLUSTER_VERSION`, replacing `CLUSTER_VERSION` with the GKE version for the cluster, like `1.29.4-gke.1043002`. The version that you specify applies until a newer version becomes the default in your release channel. GKE then [automatically upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#cluster_upgrades) your cluster to the new default version. If you omit this flag, GKE sets the version to the [release channel's default version](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions).

To check the available versions, refer to [What versions are available in a channel?](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_versions_are_available_in_a_channel). You can run any minor version in your selected channel or choose [a subset of patch versions from other channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions).

###  Console 

To set the release channel when you create an Autopilot cluster, do the following:

  1. In the Google Cloud console, go to the **Create an Autopilot cluster** page. 

[Go to Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

  2. In the **Cluster basics** section, complete the following:

     1. Specify a **Name**.
     2. Select a **Region**.
  3. In the **Advanced settings** section, choose a **release channel**.

  4. Optionally, configure other settings for your new cluster.

  5. Click **Create**.




### Terraform

To set the release channel and the cluster version when you create an Autopilot cluster using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name     = "gke-autopilot-release-channel"
      location = "us-central1"
    
      enable_autopilot = true
    
      release_channel {
        channel = "REGULAR"
      }
    }

To learn more about using Terraform, see [Provision GKE resources with Terraform](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

You can also change the release channel and GKE version for existing clusters. For instructions, refer to [Manually upgrading a control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp) and to [Selecting a new release channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#selecting_a_new_release_channel).

## Connect to the cluster

### gcloud
    
    
    gcloud container clusters get-credentials CLUSTER_NAME \
        --location=LOCATION \
        --project=PROJECT_ID
    

This command configures `kubectl` to use the cluster you created.

### Console

  1. In the cluster list, beside the cluster that you want to connect to, click _more_vert_ **Actions** , and then click **Connect**.

  2. Click **Run in Cloud Shell** when prompted. The generated command is copied into your Cloud Shell, for example:
         
         gcloud container clusters get-credentials autopilot-cluster --location=us-central1 --project=autopilot-test
         

  3. Press **Enter** to run the command.




## Verify the cluster mode

You can verify that your cluster is an Autopilot cluster by using the gcloud CLI or the Google Cloud console.

### gcloud

To verify that your cluster is created in Autopilot mode, run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION
    

The output contains the following:
    
    
    autopilot:
      enabled: true
    

### Console

To verify that your cluster is created in Autopilot mode, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Find your cluster in the cluster list. Under **Mode** , it should say **Autopilot**.




## What's next

  * Learn how to [deploy a stateless application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateless-apps).
  * Learn how to [scale an application](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/scaling-apps).
  * Learn more about [GKE Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).
  * Learn how to [harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
