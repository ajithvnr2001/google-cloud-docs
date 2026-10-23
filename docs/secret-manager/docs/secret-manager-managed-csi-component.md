---
url: https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component/
title: Use Secret Manager add-on with Google Kubernetes Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:35.721611+00:00
---

# Use Secret Manager add-on with Google Kubernetes Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Use Secret Manager add-on with Google Kubernetes Engine Stay organized with collections  Save and categorize content based on your preferences. 

The integration between Secret Manager and Google Kubernetes Engine (GKE) lets you store sensitive data such as passwords and certificates used by GKE clusters as secrets in Secret Manager.

This page explains how you can use the _Secret Manager add-on_ to access the secrets stored in Secret Manager as volumes mounted in Kubernetes Pods.

This process involves the following steps:

  1. Enable the Secret Manager add-on on a new or existing GKE cluster, and optionally configure automatic rotation of secrets.
  2. Configure applications to authenticate to the Secret Manager API.
  3. Define which secrets to mount onto Kubernetes Pods using a `SecretProviderClass` YAML file. The Secret Manager add-on supports both [global and regional secrets](https://docs.cloud.google.com/secret-manager/docs/secret-manager-secrets-comparison).
  4. Create a volume where the secrets will be mounted. After the volume is attached, applications in the container can access the data in the container file system.



The Secret Manager add-on is derived from the open source [Kubernetes Secrets Store CSI Driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver) and the [Google Secret Manager provider](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp). If you're using the open source Secrets Store CSI Driver to access secrets, you can migrate to the Secret Manager add-on. For information, see [Migrate from the existing Secrets Store CSI Driver](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component#migrate).

**Important:** This document uses the term _secret_ to refer to sensitive data stored in Secret Manager, and not to the _Secret object_ in the GKE API.

## Benefits

The Secret Manager add-on provides the following benefits:

  * You can use a fully managed and supported solution to access Secret Manager secrets from within GKE without any operational overhead.
  * You don't have to write custom code to access secrets stored in Secret Manager.
  * You can store and manage all your secrets centrally in Secret Manager and selectively access secrets from GKE pods using the Secret Manager add-on. By doing this, you can use features offered by Secret Manager such as CMEK encryption, fine-grained access control, managed rotation, lifecycle management, and audit logs, along with using Kubernetes features such as passing secrets to containers in the form of mounted volumes.
  * The Secret Manager add-on is supported on both [Standard clusters and Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison#feature-comparison).
  * The Secret Manager add-on supports nodes that use Container-Optimized OS or Ubuntu node images.



## Limitations

The Secret Manager add-on has the following limitations:

  * The Secret Manager add-on doesn't support the [Sync as Kubernetes Secret](https://secrets-store-csi-driver.sigs.k8s.io/topics/sync-as-kubernetes-secret) feature, which is available in the open source Secrets Store CSI Driver. If you want to synchronize secrets stored in Secret Manager to Kubernetes Secrets, use the integrated secret synchronization feature of Secret Manager. For information, see [Synchronize secrets to Kubernetes Secrets](https://docs.cloud.google.com/secret-manager/docs/sync-k8-secrets).

  * The Secret Manager add-on doesn't support Windows Server nodes.




## Before you begin

  * Enable the Secret Manager and Google Kubernetes Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=secretmanager.googleapis.com,container.googleapis.com)

  * If you want to use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command.

You can't manually set up the Secret Manager add-on using the Google Cloud SDK or the Google Cloud console.

**Note:** For existing gcloud CLI installations, make sure to set the `compute/region` and `compute/zone` [properties](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). By setting default locations, you can avoid errors in gcloud CLI like the following: `One of [--zone, --region, --location] must be supplied: Please specify location`.
  * Ensure that your cluster runs GKE version 1.27.14-gke.1042001 or later with a Linux node image. To use automatic rotation of secrets, your cluster must run GKE version 1.32.2-gke.1059000 or later.

  * If you use a GKE Standard cluster, ensure that your cluster has Workload Identity Federation for GKE enabled. Workload Identity Federation for GKE is enabled by default on an Autopilot cluster. Kubernetes Pods use Workload Identity Federation for GKE to authenticate to the Secret Manager API.




## Enable the Secret Manager add-on

You can enable the Secret Manager add-on on both Standard clusters and Autopilot clusters.

When you enable the add-on on a new or existing cluster, you can also optionally configure automatic rotation of secrets. With automatic rotation enabled, secret updates in Secret Manager are periodically pushed to mounted Pod volumes without requiring a Pod restart. The default rotation interval is 2 minutes (120 seconds), and the minimum allowed interval is 60 seconds. Automatic rotation of secrets requires GKE version 1.32.2-gke.1059000 or later.

### Enable the Secret Manager add-on on a new GKE cluster

To enable the Secret Manager add-on on cluster creation, do the following:

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click _add_box_**Create**.

  3. In the **Create cluster** dialog, for a Standard cluster, click **Configure**.

  4. In the navigation pane, in the **Cluster** section, click **Advanced settings**.

  5. In the **Secret manager** row, click _edit_ **Edit configuration**.

  6. Select the **Enable Secret Manager** checkbox.

  7. Optional: To enable automatic rotation of secrets, select the **Configure auto-rotation** checkbox, and then specify the **Rotation interval** and the **Rotation interval unit**.

  8. Click **Save**.

  9. In the **Workload identity** row, verify that **Details** shows **Enabled**. If it shows **Disabled** , click _edit_ **Edit configuration** , select the **Enable Workload Identity** checkbox, and then click **Save**.

  10. Continue configuring the cluster, and then click **Create**.




### gcloud

**Recommendation:** Enable automatic rotation of secrets (`--enable-secret-manager-rotation`) so that mounted secrets update automatically when secret versions change in Secret Manager without requiring a Pod restart. 

#### { Standard cluster}

To create a Standard cluster with the Secret Manager add-on, choose one of the following options based on your rotation requirements:

##### Option 1 (Recommended): Default automatic rotation

Enable the Secret Manager add-on with automatic rotation using the default 2-minute (120 seconds) interval:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of your cluster
  * LOCATION: the Compute Engine [region](https://cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`
  * VERSION: the specific GKE version that you want to use. Ensure that your cluster runs GKE version 1.32.2-gke.1059000 or later. If the default [release channel](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--release-channel) doesn't include this version, use the `--release-channel` flag to choose a release channel that does.
  * PROJECT_ID: the ID of your Google Cloud project



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-secret-manager \
        --enable-secret-manager-rotation \
        --location=LOCATION \
        --cluster-version=VERSION \
        --workload-pool=PROJECT_ID.svc.id.goog

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME `
        --enable-secret-manager `
        --enable-secret-manager-rotation `
        --location=LOCATION `
        --cluster-version=VERSION `
        --workload-pool=PROJECT_ID.svc.id.goog

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME ^
        --enable-secret-manager ^
        --enable-secret-manager-rotation ^
        --location=LOCATION ^
        --cluster-version=VERSION ^
        --workload-pool=PROJECT_ID.svc.id.goog

##### Option 2: Custom automatic rotation interval

Enable the Secret Manager add-on with automatic rotation and a custom rotation interval:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of the cluster
  * LOCATION: the Compute Engine [region](https://cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`
  * VERSION: the specific GKE version that you want to use. Ensure that your cluster runs GKE version 1.32.2-gke.1059000 or later. If the default [release channel](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--release-channel) doesn't include this version, use the `--release-channel` flag to choose a release channel that does.
  * PROJECT_ID: the ID of your Google Cloud project
  * ROTATION_INTERVAL: the rotation interval in seconds. The value must be a positive integer followed by the suffix `s`. The minimum allowed value is `60s`. For example, to set the interval to 5 minutes, use `300s`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --cluster-version=VERSION \
        --workload-pool=PROJECT_ID.svc.id.goog \
        --enable-secret-manager \
        --enable-secret-manager-rotation \
        --secret-manager-rotation-interval=ROTATION_INTERVAL
        

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME `
        --location=LOCATION `
        --cluster-version=VERSION `
        --workload-pool=PROJECT_ID.svc.id.goog `
        --enable-secret-manager `
        --enable-secret-manager-rotation `
        --secret-manager-rotation-interval=ROTATION_INTERVAL
        

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME ^
        --location=LOCATION ^
        --cluster-version=VERSION ^
        --workload-pool=PROJECT_ID.svc.id.goog ^
        --enable-secret-manager ^
        --enable-secret-manager-rotation ^
        --secret-manager-rotation-interval=ROTATION_INTERVAL
        

##### Option 3: Without automatic rotation

Enable the Secret Manager add-on without automatic rotation:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of your cluster.
  * LOCATION: the Compute Engine [region](https://cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`.
  * VERSION: the specific GKE version that you want to use. Ensure that your cluster runs GKE version 1.27.14-gke.1042001 or later. If the default [release channel](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--release-channel) doesn't include this version, use the `--release-channel` flag to choose a release channel that does.
  * PROJECT_ID: the ID of your Google Cloud project.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME \
        --enable-secret-manager \
        --location=LOCATION \
        --cluster-version=VERSION \
        --workload-pool=PROJECT_ID.svc.id.goog

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME `
        --enable-secret-manager `
        --location=LOCATION `
        --cluster-version=VERSION `
        --workload-pool=PROJECT_ID.svc.id.goog

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create CLUSTER_NAME ^
        --enable-secret-manager ^
        --location=LOCATION ^
        --cluster-version=VERSION ^
        --workload-pool=PROJECT_ID.svc.id.goog

#### { Autopilot cluster}

To create an Autopilot cluster with the Secret Manager add-on, choose one of the following options based on your rotation requirements:

##### Option 1 (Recommended): Default automatic rotation

Enable the Secret Manager add-on with automatic rotation using the default 2-minute (120 seconds) interval:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of your cluster
  * VERSION: the specific GKE version that you want to use. Ensure that your cluster runs GKE version 1.32.2-gke.1059000 or later. To set a specific version, see [Set the version and release channel of a new Autopilot cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version).
  * LOCATION: the Compute Engine [region](https://cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --enable-secret-manager \
        --enable-secret-manager-rotation \
        --cluster-version=VERSION \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME `
        --enable-secret-manager `
        --enable-secret-manager-rotation `
        --cluster-version=VERSION `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME ^
        --enable-secret-manager ^
        --enable-secret-manager-rotation ^
        --cluster-version=VERSION ^
        --location=LOCATION

##### Option 2: Custom automatic rotation interval

Enable the Secret Manager add-on with automatic rotation and a custom rotation interval:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of the cluster
  * VERSION: the specific GKE version that you want to use. Ensure that your cluster runs GKE version 1.32.2-gke.1059000 or later. To set a specific version, see [Set the version and release channel of a new Autopilot cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version).
  * LOCATION: the Compute Engine [region](https://cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`
  * ROTATION_INTERVAL: the rotation interval in seconds. The value must be a positive integer followed by the suffix `s`. The minimum allowed value is `60s`. For example, to set the interval to 5 minutes, use `300s`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --enable-secret-manager \
        --enable-secret-manager-rotation \
        --secret-manager-rotation-interval=ROTATION_INTERVAL \
        --cluster-version=VERSION \
        --location=LOCATION
        

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME `
        --enable-secret-manager `
        --enable-secret-manager-rotation `
        --secret-manager-rotation-interval=ROTATION_INTERVAL `
        --cluster-version=VERSION `
        --location=LOCATION
        

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME ^
        --enable-secret-manager ^
        --enable-secret-manager-rotation ^
        --secret-manager-rotation-interval=ROTATION_INTERVAL ^
        --cluster-version=VERSION ^
        --location=LOCATION
        

##### Option 3: Without automatic rotation

Enable the Secret Manager add-on without automatic rotation:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of your cluster.
  * VERSION: the specific GKE version that you want to use. Ensure that your cluster runs GKE version 1.27.14-gke.1042001 or later. To set a specific version, see [Set the version and release channel of a new Autopilot cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version%3E).
  * LOCATION: the Compute Engine [region](https://cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --enable-secret-manager \
        --cluster-version=VERSION \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME `
        --enable-secret-manager `
        --cluster-version=VERSION `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters create-auto CLUSTER_NAME ^
        --enable-secret-manager ^
        --cluster-version=VERSION ^
        --location=LOCATION

After you have enabled the Secret Manager add-on, you can use the Secrets Store CSI Driver in Kubernetes volumes using the driver and provisioner name: `secrets-store-gke.csi.k8s.io`.

### Enable the Secret Manager add-on on an existing GKE cluster

To enable the Secret Manager add-on on an existing cluster, do the following:

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. On the cluster details page, in the **Security** section, click edit **Secret Manager**.

  4. In the **Edit Secret Manager** dialog, select the **Enable Secret Manager** checkbox.

  5. Optional: To enable automatic rotation of secrets, select the **Configure auto-rotation** checkbox, and then specify the **Rotation interval** and the **Rotation interval unit**.

  6. Click **Save changes**.




### gcloud

**Recommendation:** Enable automatic rotation of secrets (`--enable-secret-manager-rotation`) so that mounted secrets update automatically when secret versions change in Secret Manager without requiring a Pod restart. 

To enable the Secret Manager add-on on an existing cluster, choose one of the following options based on your rotation requirements:

#### Option 1 (Recommended): Default automatic rotation

Enable the Secret Manager add-on with automatic rotation using the default 2-minute (120 seconds) interval on an existing cluster:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of the cluster
  * LOCATION: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-secret-manager \
        --location=LOCATION \
        --enable-secret-manager-rotation

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME `
        --enable-secret-manager `
        --location=LOCATION `
        --enable-secret-manager-rotation

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME ^
        --enable-secret-manager ^
        --location=LOCATION ^
        --enable-secret-manager-rotation

#### Option 2: Custom automatic rotation interval

Enable the Secret Manager add-on with automatic rotation and a custom rotation interval on an existing cluster:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of the cluster
  * LOCATION: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`
  * ROTATION_INTERVAL: the rotation interval in seconds. The value must be a positive integer followed by the suffix `s`. The minimum allowed value is `60s`. For example, to set the interval to 5 minutes, use `300s`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-secret-manager \
        --location=LOCATION \
        --enable-secret-manager-rotation \
        --secret-manager-rotation-interval=ROTATION_INTERVAL

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME `
        --enable-secret-manager `
        --location=LOCATION `
        --enable-secret-manager-rotation `
        --secret-manager-rotation-interval=ROTATION_INTERVAL

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME ^
        --enable-secret-manager ^
        --location=LOCATION ^
        --enable-secret-manager-rotation ^
        --secret-manager-rotation-interval=ROTATION_INTERVAL

#### Option 3: Without automatic rotation

Enable the Secret Manager add-on on an existing cluster without automatic rotation:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of your cluster
  * LOCATION: the Compute Engine [region](https://cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --enable-secret-manager \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME `
        --enable-secret-manager `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME ^
        --enable-secret-manager ^
        --location=LOCATION

### Verify the Secret Manager add-on installation

To verify that the Secret Manager add-on is installed on the Kubernetes cluster, run the following command:
    
    
      gcloud container clusters describe CLUSTER_NAME --location LOCATION | grep secretManagerConfig -A 4
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster
  * `LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of your cluster, such as `us-central1`



## Manage automatic secret rotation

When you enable automatic rotation of secrets (`--enable-secret-manager-rotation`), the Secret Manager add-on periodically checks Secret Manager for new versions of the secrets specified in the `SecretProviderClass` custom resource. The `--secret-manager-rotation-interval` flag determines how often the add-on checks for updates (default: 120s; minimum: 60s).

When the add-on detects a new secret version in Secret Manager, it updates the mounted secret file in the Pod volume without requiring a Pod restart.

### Disable automatic rotation of secrets on an existing cluster

To disable automatic rotation of secrets on an existing cluster, do the following:

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. On the cluster details page, in the **Security** section, click edit **Secret Manager**.

  4. In the **Edit Secret Manager** dialog, clear the **Configure auto-rotation** checkbox.

  5. Click **Save changes**.




### gcloud

To disable automatic rotation of secrets on an existing cluster, run the following command:

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of your cluster
  * LOCATION: the Compute Engine [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster, such as `us-central1`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --no-enable-secret-manager-rotation

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME `
        --location=LOCATION `
        --no-enable-secret-manager-rotation

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME ^
        --location=LOCATION ^
        --no-enable-secret-manager-rotation

## Configure applications to authenticate to the Secret Manager API

The Google Secret Manager provider uses the [workload identity](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#what_is) of the Pod that a secret is mounted onto when authenticating to the Secret Manager API. To allow your applications to authenticate to the Secret Manager API using Workload Identity Federation for GKE, follow these steps:

  * Create a [Kubernetes ServiceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) or use an existing Kubernetes ServiceAccount in the same namespace as the Pod onto which you want to mount the secret.

  * Create an Identity and Access Management (IAM) allow policy for the secret in Secret Manager.




Pods that use the configured Kubernetes ServiceAccount automatically authenticate as the IAM _principal identifier_ that corresponds to the Kubernetes ServiceAccount when accessing the Secret Manager API.

### Create a Kubernetes ServiceAccount

  1. Save the following manifest as `service-account.yaml`:
         
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: KSA_NAME
           namespace: NAMESPACE
         

Replace the following:

     * `KSA_NAME`: the name of your new Kubernetes ServiceAccount
     * `NAMESPACE`: the name of the Kubernetes namespace for the ServiceAccount
  2. Apply the manifest:
         
         kubectl apply -f service-account.yaml
         

  3. Create an IAM allow policy that references the new Kubernetes ServiceAccount and grant it permission to access the secret:
         
         gcloud secrets add-iam-policy-binding SECRET_NAME \
             --role=roles/secretmanager.secretAccessor \
             --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME
         

Replace the following:

     * `SECRET_NAME`: the name of the secret in Secret Manager
     * `PROJECT_NUMBER`: your numerical Google Cloud project number
     * `PROJECT_ID`: the project ID of the Google Cloud project that contains your GKE cluster
     * `NAMESPACE`: the name of the Kubernetes namespace for the ServiceAccount
     * `KSA_NAME`: the name of your existing Kubernetes ServiceAccount



### Use an existing Kubernetes ServiceAccount

Create an IAM allow policy that references the existing Kubernetes ServiceAccount and grant it permission to access the secret:
    
    
    gcloud secrets add-iam-policy-binding SECRET_NAME \
        --role=roles/secretmanager.secretAccessor \
        --member=principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME
    

Replace the following:

  * `SECRET_NAME`: the name of the secret in Secret Manager
  * `PROJECT_NUMBER`: your numerical Google Cloud project number
  * `PROJECT_ID`: the project ID of the Google Cloud project that contains your GKE cluster
  * `NAMESPACE`: the name of the Kubernetes namespace for the ServiceAccount
  * `KSA_NAME`: the name of your existing Kubernetes ServiceAccount



## Define which secrets to mount

To specify which secrets to mount as files in the Kubernetes Pod, create a `SecretProviderClass` YAML manifest and list the secrets to mount and the filename to mount them as. Follow these steps:

  1. Save the following manifest as `app-secrets.yaml`:
         
         apiVersion: secrets-store.csi.x-k8s.io/v1
         kind: SecretProviderClass
         metadata:
           name: SECRET_PROVIDER_CLASS_NAME
         spec:
           provider: gke
           parameters:
             secrets: |
               - resourceName: "projects/PROJECT_ID/secrets/SECRET_NAME/versions/SECRET_VERSION"
                 path: "FILENAME.txt"
         

Replace the following:

     * `SECRET_PROVIDER_CLASS_NAME`: the name for your `SecretProviderClass` object.
     * `PROJECT_ID`: your project ID.
     * `SECRET_NAME`: the secret name.
     * `SECRET_VERSION`: the secret version. The secret version must be in the same region as the cluster.
     * `FILENAME.txt`: the filename where the secret value will be mounted. You can create multiple files using the `resourceName` and `path` variables.

For a regional secret, `resourceName` is the complete path to the secret resource that includes the location of the regional secret. For example, "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_NAME/versions/SECRET_VERSION"

  2. Apply the manifest:
         
         kubectl apply -f app-secrets.yaml -n NAMESPACE
         

Replace `NAMESPACE` with the name of the Kubernetes namespace for the ServiceAccount.

  3. Verify that the `SecretProviderClass` object is created:
         
         kubectl get SecretProviderClasses -n NAMESPACE
         




## Configure a volume where the secrets will be mounted

  1. Save the following configuration as `my-pod.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: POD_NAME
           namespace: NAMESPACE
         spec:
           serviceAccountName: KSA_NAME
           containers:
           - image: IMAGE_NAME
             imagePullPolicy: IfNotPresent
             name: POD_NAME
             resources:
               requests:
                 cpu: 100m
             stdin: true
             stdinOnce: true
             terminationMessagePath: /dev/termination-log
             terminationMessagePolicy: File
             tty: true
             volumeMounts:
               - mountPath: "/var/secrets"
                 name: mysecret
           volumes:
           - name: mysecret
             csi:
               driver: secrets-store-gke.csi.k8s.io
               readOnly: true
               volumeAttributes:
                 secretProviderClass: SECRET_PROVIDER_CLASS_NAME
         

Replace the following:

     * `POD_NAME`: the name of the Kubernetes Pod where the secret is mounted
     * `NAMESPACE`: the name of the Kubernetes namespace for the ServiceAccount
     * `KSA_NAME`: the Kubernetes ServiceAccount that you set up in the step [Configure applications to authenticate to the Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component#configure-workload-identity)
     * `IMAGE_NAME`: name of the container image
     * `SECRET_PROVIDER_CLASS_NAME`: the name for your `SecretProviderClass` object
  2. **In Standard clusters only** , add the following to the `template.spec` field to place the Pods on node pools that use Workload Identity Federation for GKE.

Skip this step in Autopilot clusters, which reject this nodeSelector because every node uses Workload Identity Federation for GKE.
         
         spec:
           **nodeSelector :
             iam.gke.io/gke-metadata-server-enabled: "true"**
         

  3. Apply the configuration to your cluster.
         
         kubectl apply -f my-pod.yaml
         




This step mounts a volume `mysecret` at `/var/secrets` using the CSI driver (secrets-store-gke.csi.k8s.io). This volume references the `SecretProviderClass` object which acts as the provider.

## Migrate from the existing open source Kubernetes Secrets Store CSI Driver

If you use the open source [Kubernetes Secrets Store CSI Driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver) and the [Google Secret Manager provider](https://github.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp), you can migrate your workloads to the managed Secret Manager add-on.

The managed add-on and the open source driver can run concurrently on the same cluster. This capability lets you migrate individual applications and namespaces incrementally without cluster downtime.

To migrate to the Secret Manager add-on, follow these steps:

  1. Enable the Secret Manager add-on on your cluster
  2. Create `SecretProviderClass` manifests
  3. Update workload manifests
  4. Verify the migration
  5. Clean up old open source resources



### Step 1: Enable the Secret Manager add-on on your cluster

Enable the Secret Manager add-on on your existing GKE cluster:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --enable-secret-manager \
        [--enable-secret-manager-rotation \
         --secret-manager-rotation-interval=ROTATION_INTERVAL]
    

Replace the following:

  * CLUSTER_NAME: the name of your cluster
  * LOCATION: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of your cluster, such as `us-central1`
  * Optional: ROTATION_INTERVAL: the frequency at which mounted secrets are automatically updated, such as `120s` or `3600s`. The minimum allowed value is `60s`, and the default is `120s`.

**Note:**

  * The rotation flags (`--enable-secret-manager-rotation` and `--secret-manager-rotation-interval`) are optional. If you omit `--secret-manager-rotation-interval`, the rotation interval defaults to `120s`.
  * Automatic rotation of secrets requires GKE version 1.32.2-gke.1059000 or later.



### Step 2: Create `SecretProviderClass` manifests

Create a `SecretProviderClass` manifest with `provider: gke` for each application. We recommend appending `-gke` to the resource name so that the old and new `SecretProviderClass` resources can coexist during rolling updates.

  1. Save the following manifest as `secret-provider-class-gke.yaml`:
         
         apiVersion: secrets-store.csi.x-k8s.io/v1
         kind: SecretProviderClass
         metadata:
           name: SECRET_PROVIDER_CLASS_NAME**-gke** # Append -gke to coexist with existing SPC
           namespace: NAMESPACE
         spec:
           provider: **gke** # Changed from 'gcp'
           parameters:
             secrets: |
               - resourceName: "projects/PROJECT_ID/secrets/SECRET_NAME/versions/SECRET_VERSION"
                 path: "FILENAME.txt"
         

Replace the following:

     * SECRET_PROVIDER_CLASS_NAME-gke: the name for your new `SecretProviderClass` resource
     * NAMESPACE: the Kubernetes namespace where your workload runs
     * PROJECT_ID: your Google Cloud project ID
     * SECRET_NAME: the name of the secret in Secret Manager
     * SECRET_VERSION: the secret version, such as `latest` or `1`
     * FILENAME.txt: the filename where the secret value is mounted

For regional secrets, specify the full resource path including the location: `"projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_NAME/versions/SECRET_VERSION"`

  2. Apply the new `SecretProviderClass` manifest:
         
         kubectl apply -f secret-provider-class-gke.yaml
         




### Step 3: Update workload manifests

Update your Pod or Deployment manifests to use the managed driver (`secrets-store-gke.csi.k8s.io`) and reference the new `SecretProviderClass` name.

  1. Update the `volumes` section of your workload manifest (such as `deployment.yaml`):
         
         spec:
           containers:
           - name: CONTAINER_NAME
             image: IMAGE_NAME
             volumeMounts:
             - name: secrets-volume
               mountPath: "/var/secrets"
               readOnly: true
           volumes:
           - name: secrets-volume
             csi:
               driver: **secrets-store-gke.csi.k8s.io** # Changed from 'secrets-store.csi.k8s.io'
               readOnly: true
               volumeAttributes:
                 secretProviderClass: SECRET_PROVIDER_CLASS_NAME**-gke** # Reference new SPC name
         

Replace the following:

     * CONTAINER_NAME: the name of the container in your workload
     * IMAGE_NAME: the name of your container image
     * SECRET_PROVIDER_CLASS_NAME-gke: the name for your new `SecretProviderClass` resource
  2. Apply the updated workload manifest to trigger a rolling deployment:
         
         kubectl apply -f deployment.yaml
         




### Step 4: Verify the migration

Verify that your workloads are successfully using the managed add-on:

  1. Check that your pods have rolled out and reached the `Running` state:
         
         kubectl get pods -n NAMESPACE
         

Replace NAMESPACE with the Kubernetes namespace where your workload runs.

  2. Verify that secrets are properly mounted and accessible within the container:
         
         kubectl exec -it POD_NAME -n NAMESPACE -- cat /var/secrets/FILENAME.txt
         

Replace the following:

     * POD_NAME: the name of your Kubernetes Pod
     * NAMESPACE: the Kubernetes namespace where your workload runs
     * FILENAME.txt: the mounted secret filename configured in your `SecretProviderClass`
  3. (Optional) If you enabled automatic rotation, verify secret updates:

     1. Add a new version of the secret in Secret Manager.
     2. Wait for the configured rotation interval, such as 120 seconds.
     3. Inspect the mounted secret file again inside the pod to verify that the content updated without restarting the pod:
            
            kubectl exec -it POD_NAME -n NAMESPACE -- cat /var/secrets/FILENAME.txt
            




### Step 5: Clean up old open source resources

**Caution:** Complete this step only after all workloads in your cluster have been migrated to the managed add-on and verified.

  1. Delete the old `SecretProviderClass` resources:
         
         kubectl delete secretproviderclass OLD_SECRET_PROVIDER_CLASS_NAME -n NAMESPACE
         

Replace the following:

     * OLD_SECRET_PROVIDER_CLASS_NAME: the name of your legacy `SecretProviderClass` resource, such as `my-app-secrets`
     * NAMESPACE: the Kubernetes namespace where your workload runs
  2. If you deployed the open source Google Secret Manager provider plugin using a manifest, delete the DaemonSet:
         
         kubectl delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/secrets-store-csi-driver-provider-gcp/main/deploy/provider-gcp-plugin.yaml
         

  3. If you installed the open source Secrets Store CSI Driver using Helm, uninstall the Helm release:
         
         helm uninstall csi-secrets-store -n kube-system
         




## Disable the Secret Manager add-on

To disable the Secret Manager add-on on an existing Standard cluster or on an Autopilot cluster, run the following command:

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify. 

  3. On the cluster details page, in the **Security** section, click edit **Secret Manager**. 

  4. In the **Edit Secret Manager** dialog, clear the **Enable Secret Manager** checkbox. 

  5. Click **Save changes**. 




### gcloud

Before using any of the command data below, make the following replacements: 

  * CLUSTER_NAME: the name of your cluster
  * LOCATION: the Compute Engine [location](https://cloud.google.com/compute/docs/regions-zones#available) for the cluster, such as `us-central1`



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME \
        --no-enable-secret-manager \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME `
        --no-enable-secret-manager `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud container clusters update CLUSTER_NAME ^
        --no-enable-secret-manager ^
        --location=LOCATION

## What's next

  * Read the [Secret Manager GKE integration release notes](https://docs.cloud.google.com/secret-manager/docs/gke-release-notes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
