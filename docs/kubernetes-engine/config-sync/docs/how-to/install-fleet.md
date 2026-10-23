---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-fleet/
title: Install Config Sync as a fleet default \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:52.003275+00:00
---

# Install Config Sync as a fleet default  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-fleet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Install Config Sync as a fleet default Stay organized with collections  Save and categorize content based on your preferences. 

You can install Config Sync as a fleet default so that all new clusters added to your fleet automatically have Config Sync enabled with the settings that you want. By setting up fleet-level defaults, you help ensure that every new GKE on Google Cloud cluster registered to the fleet inherits a standard Config Sync setup, including the version and connections to your source of truth. This process simplifies cluster provisioning and helps maintain a uniform configuration management baseline.

This page explains the following:

  * How to configure these fleet-level default settings using the Google Cloud CLI, Google Cloud console, or Terraform.
  * How to apply default settings to existing clusters.
  * How to disable the fleet default configuration if needed.



For general information about fleet default configurations, see [Manage fleet-level features](https://docs.cloud.google.com/anthos/fleet-management/docs/manage-features).

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

## Limitations

  * Configuring Helm as a source type is not supported as a fleet default.
  * The Google Cloud console does not support connecting to a source of truth as a default setting. Instead, you must use the **Deploy packages** feature after creating a cluster.



## Configure fleet-level defaults for a Git repository

To configure fleet-level defaults for Config Sync, complete the following steps:

###  gcloud 

  1. Create a manifest named `apply-spec.yaml` with the following contents. If you've already created a manifest, you don't need to create a new one.
         
         applySpecVersion: 1
         spec:
           configSync:
             enabled: true
             sourceType: git
             sourceFormat: unstructured
             syncRepo: REPO
             syncRev: REVISION
             secretType: SECRET_TYPE
             # only required if gcpserviceaccount is the secretType
             # gcpServiceAccountEmail: EMAIL
             metricsGcpServiceAccountEmail: METRICS_EMAIL
         

Replace the following:

     * `REPO`: the URL of your Git repository, for example `https://github.com/GoogleCloudPlatform/anthos-config-management-samples`. Use the HTTPS format for the URL, or the SSH format if `ssh` is the sourceType.
     * `REVISION`: the Git revision (tag or hash) or branch name to sync from. When using a hash, it must be a full hash, and not an abbreviated form.
     * `SECRET_TYPE`: the authentication method used to connect to your Git repository. For public repositories, use `none`. For private repositories, use one of the following:

       * `ssh`: use an SSH key pair.
       * `cookiefile`: use a `cookiefile`.
       * `token`: use a token.
       * `gcpserviceaccount`: use a Google service account if Workload Identity Federation for GKE is enabled. Secure Source Manager or Cloud Source Repositories only.
       * `gcenode`: use a Google service account if Workload Identity Federation for GKE is not enabled. Secure Source Manager or Cloud Source Repositories only.
       * `githubapp`: use a GitHub App to authenticate to a GitHub repository.

For more information about connecting your Git repository to Config Sync, see [Grant Config Sync access to Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git).

     * `EMAIL`: if `gcpserviceaccount` is the `secretType`, uncomment this field and add the Google service account email address, for example `config-sync@PROJECT_ID.iam.gserviceaccount.com`.

     * `METRICS_EMAIL`: the email of the Google Cloud Service Account (GSA) used for exporting Config Sync metrics to Cloud Monitoring. For more information on setting up metrics export, see [Monitor Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring).

For a complete list of fields that you can add to the `apply-spec` manifest, see [gcloud apply spec fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields).

  2. Apply the `apply-spec` file with your default fleet settings by running the following command:
         
         gcloud beta container fleet config-management enable \
             --fleet-default-member-config=apply-spec.yaml
         




###  Console 

  1. In the Google Cloud console, go to the **Feature Manager** page.

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features/overview)

  2. In the **Config Sync** pane, click **Configure**.

  3. Review your fleet-level settings. All new clusters that you create in the fleet inherit these settings.

  4. Optional: To change the default settings, click **Customize fleet settings**. In the dialog that appears, do the following:

     1. Select the Config Sync version that you want to use.
     2. Click **Save changes**.
  5. Click **Configure**.

  6. In the **Configuring fleet settings** confirmation dialog, click **Confirm**. If you haven't previously enabled Config Sync, clicking **Confirm** also enables the `anthosconfigmanagement.googleapis.com` API.




Although you can't configure your source of truth settings as a fleet default from the Google Cloud console, you can select multiple clusters when you use the **Deploy a package** feature.

###  Terraform 

To enable Config Sync as a fleet default, refer to the following example:
    
    
    resource "google_gke_hub_feature" "default" {
      name     = "configmanagement"
      location = "global"
    
      fleet_default_member_config {
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
    }

Replace the following:

  * `REPO`: the URL to the Git repository that contains your configuration files.
  * `BRANCH`: the repository branch, for example `main`.
  * `DIRECTORY`: the path within the Git repository that represents the top level of the repository you want to sync.
  * `SECRET`: the secret auth type.



For more information about using Terraform, see [Provision Config Sync resources with Terraform](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/terraform).

## Configure fleet-level defaults for an OCI image

To configure fleet-level defaults for Config Sync, complete the following steps:

###  gcloud 

  1. Create a manifest named `apply-spec.yaml` with the following contents. If you've already created a manifest, you don't need to create a new one.
         
         applySpecVersion: 1
         spec:
           configSync:
             enabled: true
             sourceType: oci
             sourceFormat: unstructured
             syncRepo: REPO
             secretType: SECRET_TYPE
             # only required if gcpserviceaccount is the secretType
             # gcpServiceAccountEmail: EMAIL
             metricsGcpServiceAccountEmail: METRICS_EMAIL
         

Replace the following:

     * `REPO`: the URL of your OCI image with the format `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`. By default, the image is pulled from the `latest` tag, but you can pull in images by `TAG` or `DIGEST` instead. Specify `TAG` or `DIGEST` in the `PACKAGE_NAME`:

       * To pull by `TAG`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME:TAG`
       * To pull by `DIGEST`: `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME@sha256:DIGEST`
**Caution:** Config Sync requires that the OCI layer is compressed in the **`tar`** or **`tar+gzip`** format. Other formats (for example, `tar+bz2`) aren't recognized by Config Sync. Switching from a valid repository to an OCI image with an unsupported format causes managed resources to be pruned without an error.
     * `SECRET_TYPE`: the authentication method used to connect to your OCI image. For public images, use `none` as the value. For private images, use one of the following:

       * `gcpserviceaccount`: Secure Source Manager or Cloud Source Repositories only. Use a Google service account if Workload Identity Federation for GKE is enabled.
       * `gcenode`: Secure Source Manager or Cloud Source Repositories only. Use a Google service account if Workload Identity Federation for GKE is not enabled.

For more information on connecting your OCI image to Config Sync, see [Grant Config Sync access to OCI or Helm](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-helm-oci).

     * `EMAIL`: if `gcpserviceaccount` is the `secretType`, uncomment this field and add the Google service account email address, for example `config-sync@PROJECT_ID.iam.gserviceaccount.com`.

     * `METRICS_EMAIL`: the email of the Google Cloud Service Account (GSA) used for exporting Config Sync metrics to Cloud Monitoring. For more information on setting up metrics export, see [Monitor Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/monitor-config-sync-cloud-monitoring).

For a complete list of fields that you can add to the `apply-spec` manifest, see [gcloud apply spec fields](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields).

  2. Apply the `apply-spec` file with your default fleet settings by running the following command:
         
         gcloud beta container fleet config-management enable \
             --fleet-default-member-config=apply-spec.yaml
         




###  Console 

  1. In the Google Cloud console, go to the **Feature Manager** page.

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features/overview)

  2. In the **Config Sync** pane, click **Configure**.

  3. Review your fleet-level settings. All new clusters you create in the fleet inherit these settings.

  4. Optional: To change the default settings, click **Customize fleet settings**. In the dialog that appears, do the following:

     1. Select the Config Sync version that you want to use.
     2. Click **Save changes**.
  5. Click **Configure**.

  6. In the **Configuring fleet settings** confirmation dialog, click **Confirm**. If you haven't previously enabled Config Sync, clicking **Confirm** also enables the `anthosconfigmanagement.googleapis.com` API.




Although you can't configure your source of truth settings as a fleet default from the Google Cloud console, you can select multiple clusters when you use the **Deploy a package** feature.

###  Terraform 

To enable Config Sync as a fleet default, refer to the following example:
    
    
    resource "google_gke_hub_feature" "configmanagement_feature_member" {
      name     = "configmanagement"
      location = "global"
    
      fleet_default_member_config {
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
    }

Replace the following:

  * `REPO`: the URL to the OCI image repository that contains your configuration files.
  * `DIRECTORY`: the absolute path of the directory containing the resources you want to sync. To use the root directory, leave this field blank.
  * `SECRET`: the secret auth type.



For more information about using Terraform, see [Provision Config Sync resources with Terraform](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/terraform).

## Update existing clusters to inherit fleet defaults

To update existing clusters to use your default Config Sync settings, you can use the Google Cloud console or gcloud CLI to sync selected fleet clusters to your fleet defaults. Alternatively, you can manually configure each cluster with the same settings by using Terraform and following the instructions for installing Config Sync in the previous section. If you previously used Terraform to specify fleet defaults, use the same `configmanagement` and `config_sync` block that you used to set the defaults to configure your chosen clusters.

To sync Config Sync default settings across your fleet, follow these steps:

###  gcloud 

  1. Sync an existing membership to the fleet default configuration:
         
         gcloud beta container fleet config-management apply \
             --origin=FLEET \
             --membership=MEMBERSHIP_NAME
         

Replace `MEMBERSHIP_NAME` with the fleet membership name of the cluster that you want to sync with the fleet default configuration.

  2. Confirm that your membership configurations are synced with the fleet default:
         
         gcloud beta container fleet config-management status
         

The output of this command should display as `Yes` for the `Synced_to_Fleet_Default` status of the membership that you synced.




###  console 

  1. Go to **Feature Manager** :

[Go to Feature Manager: Config Sync](https://console.cloud.google.com/kubernetes/features/config/details)

  2. In the cluster table, select the clusters that you want to sync to fleet settings.

  3. Click **Sync to fleet settings**.




## Disable fleet defaults

To disable Config Sync default settings across your fleet, follow these steps:

  1. To disable the fleet default configuration, run the following command:
         
         gcloud beta container fleet config-management disable --fleet-default-member-config
         

  2. Confirm that the fleet default configuration is disabled:
         
         gcloud beta container fleet config-management status
         




## What's next

  * Learn how to [upgrade Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/upgrade-config-sync).
  * Discover how to [configure syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories).
  * [Use the `nomos` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command).
  * Review the [Default Config Sync permissions](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/config-sync-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
