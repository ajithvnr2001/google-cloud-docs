---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/auto-join-windows-nodepools/
title: Configure Windows Server nodes to automatically join an Active Directory domain \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:20.266500+00:00
---

# Configure Windows Server nodes to automatically join an Active Directory domain  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/auto-join-windows-nodepools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure Windows Server nodes to automatically join an Active Directory domain Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides instructions to configure your [Windows Server nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows) in your Google Kubernetes Engine (GKE) cluster to automatically join an Active Directory (AD) domain.

If you want to join your Windows Server nodes to a [Managed Microsoft AD](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview) domain and don't require a security group that contains the computer objects of your cluster, you can use the automated domain join feature. For more information, see [Join GKE Windows Server nodes automatically to a Managed Microsoft AD domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/automated-domain-join-gke).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure you have the correct IAM permission to create clusters. At minimum, you should be a [Kubernetes Engine Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/container).



## Configure auto join for Windows Server node pools

  1. Configure AD and your Google Cloud project for automatic joining by completing the instructions in the [Configuring Active Directory for VMs to automatically join a domain](https://docs.cloud.google.com/solutions/configuring-active-directory-for-vms-to-automatically-join-the-domain) tutorial.

  2. Create a GKE cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --enable-ip-alias \
             --num-nodes=NUMBER_OF_NODES \
             --no-enable-shielded-nodes \
             --cluster-version=VERSION
         

Replace the following:

     * `CLUSTER_NAME`: the name of your new cluster.
     * `NUMBER_OF_NODES`: the number of Linux nodes to create. You should provide sufficient compute resources to run cluster add-ons. This is an optional field and, if omitted, uses the default value of 3.
     * `VERSION`: the GKE cluster version, which must be 1.17.14-gke.1200 or later or 1.18.9-gke.100 or later. You can also use the [`--release-channel`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--release-channel) flag to enroll the cluster in a release channel.
     * `--enable-ip-alias` turns on [alias IP](https://docs.cloud.google.com/vpc/docs/alias-ip). Alias IP is required for Windows Server nodes.
     * `--no-enable-shielded-nodes` disables Shielded GKE Nodes.
  3. Set the following variables:
         
         export DOMAIN_PROJECT_ID=PROJECT_ID
         export SERVERLESS_REGION=REGION
         export REGISTER_URL=https://$SERVERLESS_REGION-$DOMAIN_PROJECT_ID.cloudfunctions.net/register-computer
         

Replace the following:

     * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of your domain project.
     * `REGION`: the region to [deploy your Cloud Run function](https://docs.cloud.google.com/solutions/configuring-active-directory-for-vms-to-automatically-join-the-domain) in. Choose a region that supports both [Cloud Run functions](https://docs.cloud.google.com/functions/docs/locations) and [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#supported_regions). The region does not have to be the same region as the one you plan to deploy VM instances in.
  4. Create and start a Windows Server node pool by passing the specialized scriptlet that joins the node to the AD domain:
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --image-type=IMAGE_NAME \
             --no-enable-autoupgrade \
             --machine-type=MACHINE_TYPE_NAME \
             "--metadata=sysprep-specialize-script-ps1=iex((New-Object System.Net.WebClient).DownloadString('$REGISTER_URL'))"
         

Replace the following:

     * `NODE_POOL_NAME`: the name of your Windows Server node pool.
     * `CLUSTER_NAME`: the name of the cluster you created.
     * `IMAGE_NAME`: the node image to use, such as `WINDOWS_LTSC_CONTAINERD`. For more information, see [Choose your Windows Server node image](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#choose_your_windows_server_node_image).
     * `MACHINE_TYPE_NAME`: the machine type. `n1-standard-2` is the minimum recommended machine type as Windows Server nodes require additional resources. Machine types `f1-micro` and `g1-small` are not supported. Each machine type is billed differently. For more information, refer to the [machine type price sheet](https://cloud.google.com/products/compute/pricing#standard_machine_types).



Your Windows Server node is now joined to your Active Directory domain.

## What's next

  * To use a Group Managed Service Account (gMSA) with your Windows Server node pools, see [Using gMSA](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows#using_gmsa).
  * Learn about the [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
