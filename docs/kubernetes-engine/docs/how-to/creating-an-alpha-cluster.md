---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-alpha-cluster/
title: Creating an alpha cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:51.484781+00:00
---

# Creating an alpha cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-alpha-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Creating an alpha cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

[Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters) are short-lived Google Kubernetes Engine (GKE) clusters that enable Kubernetes alpha APIs and features and can run alpha versions of upcoming minor versions. This document shows you how to create an alpha cluster, enable or disable specific feature gates, and run alpha patch versions in the Rapid release channel. Alpha clusters are intended for early adopters and platform administrators who want to experiment with upcoming Kubernetes features and versions.

For more information about how GKE clusters work and how to choose which type of GKE cluster to create, see [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) and [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Review the [limitations of alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters#limitations).



### Required roles

To get the permissions that you need to create and interact with alpha clusters, ask your administrator to grant you the [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

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




## Create an alpha cluster

You can create an alpha cluster by using the Google Cloud console or the gcloud CLI. We recommend that you use the gcloud CLI for the following reasons:

  * You can enroll your cluster in the Rapid release channel, which is [recommended for alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#rapid-vs-alpha-cluster).
  * You can specify the alpha or beta feature gates to enable or disable differently from the default values.




### Console

  1. In the Google Cloud console, go to the **Create a Kubernetes cluster** page. 

[Go to Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

  2. In the **Cluster basics** section, complete the following:

     1. Enter the **Name** for your cluster. 
     2. For the **Location type** , select **Zonal** , and then select the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.
     3. If you are creating a multi-zonal cluster, select the **Specify default node locations** checkbox, and then choose additional zones in which you'd like the node pools to run. 
     4. From the **Release channel** drop-down list, select **No channel** ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)).

**Note:** To enroll an alpha cluster in the Rapid channel, which is recommended, use the gcloud CLI instructions instead. Or, after you create the cluster, [enroll the existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster) in the Rapid channel.
     5. Optional: Specify a control plane version from the **Version** drop-down list. 

  3. Optional: Configure other settings for your new cluster.

  4. Optional: If you want to register your new cluster to a [fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs), go to the **Advanced settings** section, and follow the Google Cloud console instructions for [Create and register a new cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#console) to complete your cluster registration.

  5. From the navigation pane, under **Node Pools** , click **default-pool**.

  6. In the **Node pool details** section, complete the following:

     1. Enter a **Name** for the default [Node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
     2. Optional: Choose the **Node version**.
     3. Enter the **Number of nodes** to create in the cluster. You must have available [resource quota](https://docs.cloud.google.com/compute/quotas) for the nodes and their resources (such as firewall routes).
     4. Optional: You can choose to disable node auto-upgrades, however we recommend that you review the [considerations before disabling node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#considerations) before choosing this option. 
     5. Clear **Enable auto-upgrade** and **Enable auto-repair**. 
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
  14. In the navigation pane, click **Advanced settings**.

  15. In the **Kubernetes alpha features** row, click _edit_ **Edit configuration**.

  16. Select **Enable Kubernetes alpha features in this cluster**.

  17. Read and acknowledge the warning by selecting **I understand the consequences**.

  18. Click **Save**.

  19. Click **Create**.




### gcloud

Run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --release-channel=CHANNEL \
        --enable-kubernetes-alpha \
        --no-enable-autorepair \
        --no-enable-autoupgrade \
        --location CONTROL_PLANE_LOCATION [\
        --alpha-cluster-feature-gates FEATURE_GATES_LIST]
    

Replace the following:

  * `CLUSTER_NAME`: the name you choose for the cluster.
  * `CHANNEL`: the type of release channel. This value must be one of the following:

    * `rapid`: enroll in the Rapid release channel, which is the recommended channel for alpha clusters.
    * `regular`: enroll in the Regular release channel.
    * `stable`: enroll in the Stable release channel.
    * `none`: don't enroll in a release channel. This option is [deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel) and will be removed.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.

  * `--cluster-version VERSION`: (optional) specifies the GKE [version](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades) to run in the cluster. If omitted, the cluster runs the _default patch version for cluster creation_ for the selected release channel, as shown in the [Current versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) table.

  * `FEATURE_GATES_LIST`: the list of feature gates to enable or disable differently from the default values. Each string represents the enablement or disablement of a feature gate. For example, `featureX=true, featureY=false`. When you omit this flag, GKE creates the cluster using the default values for GKE, meaning all alpha feature gates available with the Kubernetes version are enabled. The beta feature gates enabled by default by Kubernetes are also enabled. For more information about which feature gates are available with specific versions, and which beta features are enabled by default, see [Feature gates for Alpha or Beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features) in the Kubernetes documentation. When you include this flag, you modify which feature gates are enabled from how the feature gates are set by default by GKE. For more information, see [Feature gates and alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters#feature-gates).

**Warning:** If you attempt to create a cluster using the `--alpha-cluster-feature-gates` flag, but list an invalid feature gate, including a feature gate that is unsupported for the specific Kubernetes version, the cluster might be created in an error state. For more information, see Troubleshoot creating an alpha cluster with feature gates.



We strongly recommend that you specify a minimally-privileged IAM service account that your nodes can use instead of the Compute Engine default service account. To learn how to create a minimally-privileged service account, see [Use a least privilege service account](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#use_least_privilege_sa).

To specify a custom service account in the gcloud CLI, add the following flag to your command:
    
    
    --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com

Replace SERVICE_ACCOUNT_NAME with the name of your minimally-privileged service account.

You are prompted to acknowledge a warning that the alpha cluster is not upgraded and is deleted after 30 days:
    
    
    This will create a cluster with Kubernetes alpha features enabled.
    - This cluster will not be covered by the GKE SLA and should
      not be used for production workloads.
    - You will not be able to upgrade the master or nodes.
    - The cluster will be deleted after 30 days.
    

### Interact with a cluster using kubectl

After you create a cluster, you need to [configure `kubectl`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#store_info) before you can interact with the cluster from the command line.

## Check feature gate state for an alpha cluster

With alpha clusters, you can selectively enable or disable feature gates. For more information, see [Feature gates and alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters#feature-gates).

To check the feature gate state for your cluster, see [Check feature gate state](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/feature-gates#check-feature-gate-state).

## Run alpha patch versions in alpha clusters

Alpha clusters that you enroll in the Rapid release channel can run [alpha patch versions](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) of upcoming Kubernetes minor versions. These alpha versions provide early access to test features and changes in the next minor version before GKE makes that minor version available to all clusters in the Rapid channel.

To identify and run alpha patch versions in alpha clusters, follow these steps:

  1. Identify the available alpha versions in the Rapid channel:
         
         gcloud container get-server-config \
             --flatten="channels" --filter="channels.channel=RAPID" \
             --location=LOCATION \
             --format="yaml(channels.channel,channels.previewVersions)"
         

Replace `LOCATION` with the region in which you plan to create the alpha cluster, such as `us-central1`.

The output is similar to the following:
         
         channels:
           channel: RAPID
           previewVersions:
           - 1.37.0-gke.1173000+preview
         

If the output is empty, then alpha versions aren't available in that region. Try a different region or check the [Rapid channel release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid) for version information.

  2. Create the alpha cluster:
         
         gcloud container clusters create CLUSTER_NAME \
             --release-channel=rapid \
             --enable-kubernetes-alpha \
             --no-enable-autorepair \
             --no-enable-autoupgrade \
             --location=CONTROL_PLANE_LOCATION \
             --cluster-version=ALPHA_VERSION
         

Replace the following:

     * `CLUSTER_NAME`: a name for the alpha cluster.
     * `CONTROL_PLANE_LOCATION`: the region or zone for the cluster's control plane. Use the same region that you checked for alpha version availability in the previous step or a zone in that region.
     * `ALPHA_VERSION`: the specific alpha patch version to run in the cluster, from the output of the previous step.



## Check when an alpha cluster expires

To check when alpha clusters expire, run the following command:
    
    
    gcloud container clusters list
    

## Troubleshoot creating an alpha cluster with feature gates

If you attempt to create a cluster with an invalid feature gate, or a feature gate that's unsupported for the Kubernetes version of your cluster, the cluster can be created in an error state.

You can find a message similar to the following in Cloud Logging:
    
    
    failed to set feature gates from initial flags-based config:
    unrecognized feature gate: UNRECOGNIZED_FEATURE_GATE_NAME
    

If you encounter this error, delete the failed cluster. Check the spelling and compatibility of the feature gates with the given Kubernetes version. Then, try to create the cluster again.

## What's next

  * Learn more about the [types of clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters) you can create.
  * [Learn about managing your clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters).
  * [Learn how to delete clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
