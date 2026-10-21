---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync/
title: Customize your Config Sync installation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:30:16.438196+00:00
---

# Customize your Config Sync installation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Customize your Config Sync installation Stay organized with collections  Save and categorize content based on your preferences. 

With Config Sync, you can manage your Kubernetes resources by syncing configurations from a central source of truth, such as a Git repository, an OCI image, or a Helm chart. If the [default installation instructions](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default) don't suit your needs, you might need to customize your Config Sync installation.

This page shows you how to perform an advanced installation and configuration of Config Sync. The installation process includes the following:

  * Installing Config Sync on individual clusters using the Google Cloud console, the Google Cloud CLI, or Terraform.
  * Configuring your root repository, including source type, format, and authentication.
  * Verifying the successful installation and configuration of Config Sync.



## Limitations

Config Sync doesn't support configuring `helm` as the source type using the Google Cloud console or the Google Cloud CLI. You can configure your `RootSync` or `RepoSync` object to sync from a Helm repository using the [Kubernetes API](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#kubernetes-api), or [declare it in another source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#managed-control). See [Configuration for the Helm repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository) for more information.

## Before you begin

Before you install Config Sync, prepare your source of truth and a suitable cluster.

### Grant Config Sync access to your source of truth

To synchronize configuration from a source of truth to your clusters, Config Sync requires read-only access to your repository. To authorize Config Sync to read your configurations, complete the following steps:

  * Create, or have access to, a source of truth that contains the configuration files that you want Config Sync to sync to your clusters. For more information, see the following resources:

    * [Add configs to a source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs): conceptual information about configurations.
    * [GitOps best practices](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices): tips and general best practices for organizing and managing your repository.
    * [Use an unstructured repo](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo): recommendations for using and organizing an unstructured repository.
  * If your source of truth is public, no further action is needed. Config Sync doesn't require extra permissions.

  * If your source of truth is private, complete the instructions in one of the following pages:

    * [Grant Config Sync access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git).
    * [Grant Config Sync access to OCI or Helm](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-helm-oci).



### Review cluster requirements

Before you create a cluster, review [cluster requirements](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/cluster-requirements).

## Install Config Sync

When you install Config Sync using the Google Cloud console or the Google Cloud CLI, Config Sync automatically creates a RootSync object named `root-sync`. You can use `kubectl` commands to modify `root-sync` and add additional Config Sync configurations. For more information, see [Configure Config Sync with `kubectl` commands](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl).

### Console

### Install Config Sync

To install Config Sync, all clusters must be registered to a fleet. When you install Config Sync in the Google Cloud console, selecting individual clusters automatically registers those clusters to your fleet.

  1. In the Google Cloud console, go to the **Config** page under the **Features** section. 

[Go to Config](https://console.cloud.google.com/kubernetes/config_management)

  2. Click _add_ **Install Config Sync**.
  3. Select the Config Sync version that you want to use.
  4. Under **Installation options** , select one of the following options: 
     * **Install Config Sync on entire fleet (recommended)** : Config Sync is installed on all clusters in the fleet.
     * **Install Config Sync on individual clusters** : Config Sync is installed on the clusters that you select. Any selected clusters are automatically registered to your fleet.
  5. If you're installing Config Sync on individual clusters, in the **Available clusters** table, select the clusters on which you want to install Config Sync.
  6. Click **Install Config Sync**. In the **Settings** tab, after a few minutes, you should see **Enabled** in the **Status** column for the clusters in your fleet.



### Deploy a package

After you have registered your clusters to a fleet and installed Config Sync, you can configure Config Sync to deploy a package to a cluster from a source of truth. You can deploy the same package to multiple clusters or deploy different packages to different clusters. You can edit a package after deploying it, except for some settings like package name and sync type. For more information, see [Manage packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/manage-packages).

**Note:** If you want Config Sync to render and apply a Helm chart, you must [configure Config Sync with the Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#configuring-config-sync) instead.

To deploy a package, complete the following steps:

  1. In the Google Cloud console, go to the **Config Sync dashboard**.

[Go to Config Sync dashboard](https://console.cloud.google.com/kubernetes/config_management)

  2. Click **Deploy Package**.

  3. In the **Select clusters for package deployment** table, select the cluster that you want to deploy a package to and then click **Continue**.

  4. Select either **Package hosted on Git** or **Package hosted on OCI** as your source type and then click **Continue**.

  5. In the **Package details** section, enter a **Package name** , which identifies the RootSync or RepoSync object.

  6. In the **Sync type** field, choose either **Cluster scoped sync** or **Namespace scoped sync** as the sync type.

Cluster scoped sync creates a RootSync object and Namespace scoped sync creates a RepoSync object. For more information about these objects, see [Config Sync architecture](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/architecture#rootsync-reposync).

  7. In the **Source** section, complete the following:

     * For sources hosted in a Git repository, enter the following fields:

       1. Enter the URL of the Git repository that you're using as a source of truth as the **Repository URL**.
       2. Optional: Update the **Revision** field to check out if you're not using the default `HEAD`.
       3. Optional: Update the **Path** field if you don't want to sync from the root repository.
       4. Optional: Update the **Branch** field if you're not using the default `main` branch.
     * For sources hosted in an OCI image, enter the following fields:

       1. Enter the URL of the OCI image that you're using as a source of truth as the **Image**.
       2. Enter the path of the directory to sync from, relative to the root directory, as the **Directory**.
  8. (Optional): Expand the **Advanced settings** section to complete the following:

     1. Select an **Authentication type**. Config Sync needs read-only access to your source of truth to read the configuration files in the source and apply them to your clusters. Unless your source requires no authentication, such as a public repository, ensure that you grant Config Sync read-only access to your [Git repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret), [OCI image](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#oci-access), or [Helm chart](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#helm-access) (gcloud CLI only). Choose the same authentication type that you configured when you installed Config Sync:

**Note:** for OCI, you can only select **Workload Identity** for authentication.
        * **None** : Use no authentication.
        * **SSH** : Authenticate by using an SSH key pair.
        * **Cookiefile** : Authenticate by using a `cookiefile`.
        * **Token** : Authenticate by using an access token or password.
        * **Google Cloud Repository** : Use a Google service account to access a Cloud Source Repositories repository. Only select this option if Workload Identity Federation for GKE is _not_ enabled in your cluster.
        * **Workload Identity** : Use a Google service account to access a Cloud Source Repositories repository.
     2. Enter a number in seconds to set the **Sync wait time** , which determines how long Config Sync waits between attempts to pull from the source of truth.

     3. Enter a **Git proxy** URL for the HTTPS proxy to be used when communicating with the source of truth.

  9. Click **Deploy Package**.

You are redirected to the Config Sync **Packages** page. After a few minutes, you should see **Synced** in the **Sync status** column for the cluster that you configured. 




###  gcloud 

Before you continue, make sure you've [registered your clusters](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster#register_cluster) to a [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets).

  1. Enable the `ConfigManagement` fleet feature:
         
         gcloud beta container fleet config-management enable
         

  2. Prepare the configuration by creating a file named `apply-spec.yaml` and copying the following YAML file into it.

You can set all of the optional `spec.configSync` fields that you need when you create your manifest, and later use [`kubectl` commands for configuration](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/configure-config-sync-kubectl). You can also only set the `spec.configSync.enabled` field as `true` and omit the optional fields. You can then later use `kubectl` commands to [create additional RootSync objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories) or RepoSyncs that you can fully manage using `kubectl` commands later.
         
         # apply-spec.yaml
         
              applySpecVersion: 1
              spec:
                configSync:
                  enabled: true
                  # If you don't have a source of truth yet, omit the
                  # following fields. You can configure them later.
                  sourceType: SOURCE_TYPE
                  sourceFormat: FORMAT
                  syncRepo: REPO
                  syncRev: REVISION
                  secretType: SECRET_TYPE
                  gcpServiceAccountEmail: EMAIL
                  metricsGcpServiceAccountEmail: METRICS_EMAIL
                  policyDir: DIRECTORY
                  preventDrift: false
         

Replace the following:

     * `SOURCE_TYPE`: add `git` to sync from a Git repository, `oci` to sync from an OCI image, or `helm` to sync from a Helm chart. If no value is specified, the default is `git`.
     * `FORMAT`: add `unstructured` to use an [unstructured repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo) or add `hierarchy` to use a [hierarchical repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo). These values are case-sensitive. This field is optional and the default value is `hierarchy`. We recommend that you add `unstructured`, because this format lets you organize your configs in the way that is most convenient to you.
     * `REPO`: add the URL of the source of truth. Git and Helm repository URLs use either the HTTPS or SSH protocol. For example, `https://github.com/GoogleCloudPlatform/anthos-config-management-samples`. If you plan to use SSH as your `secretType`, enter your URL with the SSH protocol. This field is required and if you don't enter a protocol, the URL is treated as an HTTPS URL.

OCI URLs use the following format: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`. By default, the image is pulled from the `latest` tag, but you can pull in images by `TAG` or `DIGEST` instead. Specify `TAG` or `DIGEST` in the `PACKAGE_NAME`:

       * To pull by `TAG`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME:TAG`
       * To pull by `DIGEST`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME@sha256:DIGEST`
**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`** format. Other formats (for example, `tar+bz2`) won't be recognized by Config Sync. Switching from a valid REPO to an OCI image with an unsupported format will cause managed resources to be pruned without an error.
     * `REVISION`: the Git revision (tag or hash) or branch name to sync from. When using a hash, it must be a full hash, and not an abbreviated form.

     * `SECRET_TYPE`: one of the following `secretTypes`:

### git

       * `none`: Use no authentication.
       * `ssh`: Use an SSH key pair.
       * `cookiefile`: Use a `cookiefile`.
       * `token`: Use a token.
       * `gcpserviceaccount`: Use a Google service account to access a Cloud Source Repositories or Secure Source Manager repository. If you select this authentication type, you need to create an IAM policy binding after you finish configuring Config Sync. For details, see the Google service account tab of the [Grant Config Sync access to Git with a Google service account](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git#google-service-account) section.
       * `gcenode`: Use a Google service account to access a Cloud Source Repositories. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `githubapp`: Use a GitHub App to authenticate to a GitHub repository.

For more information on these authentication types, see [Grant Config Sync access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git).

### oci

       * `none`: Use no authentication
       * `token`: Use a token.
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

### helm

       * `token`: Use a token.
       * `gcenode`: Use the Compute Engine default service account to access an image in Artifact Registry. Only select this option if Workload Identity Federation for GKE is not enabled in your cluster.
       * `gcpserviceaccount`: Use a Google service account to access an image.

       * `EMAIL`: If you added `gcpserviceaccount` as your `secretType`, add your Google service account email address. For example, `acm@PROJECT_ID.iam.gserviceaccount.com`.

       * `METRICS_EMAIL`: the email of the Google Cloud Service Account (GSA) used for exporting Config Sync metrics to Cloud Monitoring. The GSA should have the Monitoring Metric Writer (`roles/monitoring.metricWriter`) IAM role. The Kubernetes ServiceAccount `default` in the namespace `config-management-monitoring` should be [bound to the GSA](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring).

       * `DIRECTORY`: the path of the directory to sync from, relative to the root of the Git repository. All sub-directories of the directory that you specify are included and synced to the cluster. The default value is the root directory of the repository.

For a complete list of fields that you can add to the `spec` field, see [gcloud fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields).

**Note:** If you don't have a source of truth prepared yet, you can enable Config Sync without configuring any settings by setting `spec.configSync.enabled` to `true` and omitting all other `spec.configSync` fields. When you have prepared your repository, edit your `apply-spec.yaml` to add the configuration settings.
  3. Apply the `apply-spec.yaml` file. If you are using an existing manifest, you should apply the file to the cluster that you want to configure with the settings that you fetched in the previous command:
         
         gcloud beta container fleet config-management apply \
             --membership=MEMBERSHIP_NAME \
             --config=CONFIG_YAML_PATH \
             --project=PROJECT_ID
         

Replace the following:

     * `MEMBERSHIP_NAME`: the fleet membership name that you chose when you registered your cluster. You can find the name with `gcloud container fleet memberships list`.
     * `CONFIG_YAML_PATH`: the path to your `apply-spec.yaml` file.
     * `PROJECT_ID`: your project ID.



###  Terraform 

For each cluster that you want to configure Config Sync, apply a `google_gkehub_feature_membership` resource block that contains a `configmanagement` and `config_sync` block, such as in the following example:

### git
    
    
    data "google_project" "default" {}
    
    resource "google_container_cluster" "default" {
      name     = "gke-autopilot-basic"
      location = "us-central1"
    
      fleet {
        project = data.google_project.default.project_id
      }
    
      enable_autopilot = true
    }
    
    resource "google_gke_hub_feature" "configmanagement_feature" {
      name     = "configmanagement"
      location = "global"
    }
    
    resource "google_gke_hub_feature_membership" "configmanagement_feature_member" {
      location = "global"
    
      feature             = google_gke_hub_feature.configmanagement_feature.name
      membership          = google_container_cluster.default.fleet[0].membership_id
      membership_location = google_container_cluster.default.fleet[0].membership_location
    
      configmanagement {
        config_sync {
          # The field `enabled` was introduced in Terraform version 5.41.0, and
          # needs to be set to `true` explicitly to install Config Sync.
          enabled = true
          git {
            sync_repo   = "REPO"
            sync_branch = "BRANCH"
            policy_dir  = "DIRECTORY"
            secret_type = "SECRET"
          }
        }
      }
    }

Replace the following:

  * `REPO`: the URL to the Git repository that contains your configuration files.
  * `BRANCH`: the repository branch, for example `main`.
  * `DIRECTORY`: the path within the Git repository that represents the top level of the repository you want to sync.
  * `SECRET`: the secret auth type.



### oci
    
    
    data "google_project" "default" {}
    
    resource "google_container_cluster" "default" {
      name     = "gke-autopilot-basic"
      location = "us-central1"
    
      fleet {
        project = data.google_project.default.project_id
      }
    
      enable_autopilot = true
    }
    
    resource "google_gke_hub_feature" "configmanagement_feature" {
      name     = "configmanagement"
      location = "global"
    }
    
    resource "google_gke_hub_feature_membership" "configmanagement_feature_member" {
      location = "global"
    
      feature             = google_gke_hub_feature.configmanagement_feature.name
      membership          = google_container_cluster.default.fleet[0].membership_id
      membership_location = google_container_cluster.default.fleet[0].membership_location
    
      configmanagement {
        config_sync {
          # The field `enabled` was introduced in Terraform version 5.41.0, and
          # needs to be set to `true` explicitly to install Config Sync.
          enabled = true
          oci {
            sync_repo   = "REPO"
            policy_dir  = "DIRECTORY"
            secret_type = "SECRET"
          }
        }
      }
    }

Replace the following:

  * `REPO`: the URL to the OCI image repository that contains your configuration files.
  * `DIRECTORY`: the absolute path of the directory containing the resources you want to sync. To use the root directory, leave this field blank.
  * `SECRET`: the secret auth type.



Repeat this process for each cluster that you want to sync.

For more information about using Terraform, see [Terraform support for Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/terraform).

After you configure your root repository, you can optionally [configure syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories), including other root repositories and namespace repositories. The namespace repositories are helpful if you want a repository that contains namespace-scoped configs synced to a particular namespace across clusters.

## Verify the installation

After you install and configure Config Sync, you can verify that the installation completed successfully.

###  gcloud 

Run the following command:
    
    
    nomos status
    

A successful installation shows a status of `SYNCED` or `PENDING`.

For more details about the information supplied by `nomos status`, including reported errors, see [Check Config Sync status](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install) in the `nomos` command-line tool documentation.

###  console 

Complete the following steps:

  1. In the Google Cloud console, go to the **Config** page under the **Features** section. 

[Go to Config](https://console.cloud.google.com/kubernetes/config_management)

  2. On the **Packages** tab, check the **Sync status** column in the cluster table. A successful installation of Config Sync has a status of **Installed**. A successfully configured source of truth has a status of **Synced**.



## Override resource requests and limits

In most cases, the [default resource requests and limits](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/concepts/architecture#resource-requests) for Config Sync components are sufficient. However, you can override the requests and limits for the default CPU and memory to ensure that components have enough resources to operate reliably. For example, if you are syncing a large number of resources to your cluster, you might need to provide more resources to the `reconciler-manager`.

You can override the resource requests and limits for some Config Sync components by using the `deploymentOverrides` field in your `apply-spec.yaml` file when you install Config Sync with the gcloud CLI. You can't use the `deploymentOverrides` field to override other fields in a Deployment, such as the number of replicas.

The `deploymentOverrides` field can only override the resource requests and limits for deployments that are _not_ a root or namespace reconciler, such as the `reconciler-manager`. If you need to override the resources for a root or namespace reconciler, you can use the `spec.override.resources` field in the RootSync or RepoSync object.

The following example shows how to use the `deploymentOverrides` field to set a new CPU request and limit and a new memory request and limit for the `reconciler-manager` container:
    
    
    applySpecVersion: 1
    spec:
      configSync:
        enabled: true
        # ... other fields...
        deploymentOverrides:
        - name: reconciler-manager
          namespace: config-management-system
          containers:
          - name: reconciler-manager
            cpuRequest: 50m
            cpuLimit: 100m
            memoryRequest: 256Mi
            memoryLimit: 512Mi
    

After you have create your `apply-spec.yaml` file, apply it by running the following command:
    
    
    gcloud beta container fleet config-management apply \
        --membership=MEMBERSHIP_NAME \
        --config=apply-spec.yaml \
        --project=PROJECT_ID
    

For a complete list of the fields that you can override, see the [gcloud apply spec fields reference documentation](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/reference/gcloud-apply-fields).

## What's next

  * Learn how to [upgrade Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/upgrade-config-sync).
  * Learn more about the [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/config-management) for configuring Config Sync.
  * Discover how to [configure syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories).
  * [Use the `nomos` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command).
  * Read the [Introduction to troubleshooting Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/troubleshooting-config-sync).
  * Learn how to [uninstall Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/uninstalling-config-sync).
  * Review the [Default Config Sync permissions](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/config-sync-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
