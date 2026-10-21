---
url: https://docs.cloud.google.com/composer/docs/composer-1/upgrade-environments/
title: Upgrade environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:02.539184+00:00
---

# Upgrade environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/upgrade-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Upgrade environments Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page describes how to upgrade your environment to a new Managed Airflow or Airflow version.

## About upgrade operations

You can upgrade the Managed Airflow version, the Airflow version, or both at the same time.

When you change the version of Airflow or Managed Airflow used by your environment:

  * Managed Airflow re-deploys your [environment's components](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture) using new versions of [Managed Airflow images](https://docs.cloud.google.com/composer/docs/composer-versions).

  * Managed Airflow applies Airflow configuration changes, such as custom PyPI packages or Airflow configuration option overrides, if your environment had them before the upgrade.

  * Managed Airflow updates the Airflow `airflow_db` connection to point to the new Cloud SQL database.




Upgrading doesn't change how you connect to the resources in your environment, such as the URL of your environment's bucket, or Airflow web server.

### Limitations of upgrade and rollback operations

Upgrade operations have the following limitations:

  * [Managed Airflow releases](https://docs.cloud.google.com/composer/docs/release-notes) are gradually rolled out to all regions supported by Managed Airflow over several days. The latest version from a release in progress might not be available in your region yet.

  * You can't downgrade to an earlier Managed Airflow or Airflow version.

  * In Google Cloud console, you can upgrade only to the latest supported versions of Managed Airflow (Gen 2).

  * In Google Cloud CLI, API, or Terraform, you can upgrade an environment to the latest supported versions, three previous versions of Managed Airflow (Gen 2), the last patch version of the previous minor version, and to versions with an extended upgrade timeline. It's not possible to upgrade to other versions of Managed Airflow (Gen 2), even if they are still supported and can be used to create a new environment.

Example of upgrade choices for Google Cloud CLI, API, and Terraform:

    * Latest versions: `composer-2.11.5-airflow-*`
    * Three previous Managed Airflow (Gen 2) versions: `composer-2.11.4-airflow-*`, `composer-2.11.3-airflow-*`, `composer-2.11.2-airflow-*`.
    * Last patch of the previous Managed Airflow (Gen 2) minor version: `composer-2.10.2-airflow-*`
    * Managed Airflow (Gen 2) versions with an extended upgrade timeline: `composer-2.10.2-airflow-*`, `composer-2.10.1-ariflow-*`, `composer-2.9.7-airflow-*`, and other versions with an extended upgrade timeline.
  * The version that you upgrade to must support your environment's current Python version.

  * The Compute Engine API quota limits can prevent upgrades. In Google Cloud console, navigate to the **IAM and Admin** > **Quotas and System Limits** page and check if the **Compute Engine API** quota for CPU is not exceeded. If the quota threshold is being approached, request Quota extension before proceeding with upgrade operation.

  * It is not possible to upgrade to a different major version of Managed Airflow or Airflow in-place. You can manually transfer DAGs and configuration between environments. For more information, see:

    * [Migrate from Managed Airflow (Legacy Gen 1), Airflow 1 to Managed Airflow (Gen 2), Airflow 2](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-1).
    * [Migrate from Managed Airflow (Legacy Gen 1), Airflow 2 to Managed Airflow (Gen 2), Airflow 2](https://docs.cloud.google.com/composer/docs/composer-1/migrate-composer-2-af-2).
    * [Migrate from Managed Airflow (Legacy Gen 1), Airflow 1 to Managed Airflow (Legacy Gen 1), Airflow 2](https://docs.cloud.google.com/composer/docs/composer-1/migrate-environments-airflow-2).

  * You can't upgrade your environment if the Airflow database contains more than 16 GB of data. During an upgrade, a warning is shown if the Airflow database size is more than 16 GB. In this case, [perform the database maintenance](https://docs.cloud.google.com/composer/docs/composer-1/cleanup-airflow-database) to reduce the database size.

  * If you use the XCom mechanism to transfer files, make sure that you [use it according to Airflow's guidelines](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html#object-storage-xcom-backend). Transferring big files or a large number of files using XCom impacts Airflow database's performance and can lead to failures when loading snapshots or upgrading your environment. Consider using alternatives such as Cloud Storage to transfer large volumes of data.




## Before you begin

**Caution:**

  * Make sure that you **know the differences** between the current versions of Airflow and Managed Airflow and the versions that you are upgrading to. The new version can include different versions of preinstalled packages, patches from Managed Airflow, or changes in Airflow functionality, provided by the Airflow open source project. You can [check the versions of provider packages](https://docs.cloud.google.com/composer/docs/composer-versions) that are included in a specific version.

  * Make sure that **your DAGs are compatible** with the new Airflow version and new versions of all provider packages (including the Airflow provider package for Google Cloud and Google services). Incompatible changes can cause your DAGs to no longer work.

  * During an upgrade operation, **all running tasks are terminated**. After the upgrade is completed, Airflow schedules these tasks for a retry, depending on the way you configure retries for your DAGs.

  * Do not upgrade GKE clusters of your Managed Airflow environments to newer versions. Use the GKE version that was pre-configured during the environment creation and rely on auto-upgrades of the GKE service.




  * We recommend to [create a new snapshot](https://docs.cloud.google.com/composer/docs/composer-1/save-load-snapshots) of the environment to be able to re-create the environment in case this is needed.

  * Your account must have a role that can trigger environment upgrade operations. In addition, the service account of the environment must have a role that has enough permissions to perform upgrade operations. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control).




## Check that your environment is up to date

Managed Airflow displays warnings when your environment's image approaches its end of full support date. You can use these warnings to always keep your environment [supported](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

![A deprecation message is displayed on the Environment details page](https://docs.cloud.google.com/static/composer/docs/images/environment-deprecation-message.png)**Figure 1.** A deprecation message is displayed on the Environment details page 

Managed Airflow keeps track of the Managed Airflow image version that your environment is based on. When it approaches the [end of support date](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support), you can see a warning in the list of environments and on the **Environment details** page.

**Note:** You can always upgrade your environment, even if Managed Airflow image version is past its full support period. 

To check if your environment is up to date:

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In the **Image version** field, one of the following messages is displayed:

     * **Newest available version**. Your environment image is fully supported.

     * **New version available**. Your environment image is fully supported and you can upgrade it to a later version.

     * **Support for this image version ends in...** Your environment image approaches the end of the full support period.

     * **This version is not supported as of...** Your environment is past the full support period.




###  gcloud 

This functionality is not available through Google Cloud CLI. You can View suggested upgrades instead, which shows new versions that are available.

###  API 

This functionality is not available through API. You can View suggested upgrades instead, which shows new versions that are available.

## View suggested upgrades

Managed Airflow provides a list of Managed Airflow versions that you can upgrade your environment to.

**Note:** The list of suggested versions **doesn't list all available versions that you can use**. For example, you can upgrade to several previous versions of Managed Airflow. For more information about Managed Airflow versions that you can choose for upgrading, see Limitations of upgrade operations.

To view Managed Airflow versions suggested for an upgrade:

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab and click **Upgrade Image Version**.

  4. For the list of suggested versions, click the Managed Airflow **Image version** drop-down menu.




###  gcloud 
    
    
    gcloud composer environments list-upgrades \
      ENVIRONMENT_NAME \
      --location LOCATION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud composer environments list-upgrades example-environment \
      --location us-central1
    

###  API 

You can view available versions for a location. To do so, construct an [`imageVersions.list`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.imageVersions/list) API request.

For example:
    
    
    // GET https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/imageVersions
    

## Check for PyPI package conflicts

You can check if PyPI packages installed in your environment have any conflicts with preinstalled packages in the new Managed Airflow image.

A successful check means that there are no conflicts in PyPI package dependencies between the current and the specified version. However, an upgrade operation might still not be successful because of other reasons.

###  Console 

To run an upgrade check for your environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab, locate the **Image version** entry, and click **Upgrade**.

  4. In the **Environment version upgrade** dialog, in the **New version** drop-down list, select a Managed Airflow version that you want to upgrade to.

  5. In the **PyPI packages compatibility** section, click **Check for conflicts**.

  6. Wait until the check is complete. If there are PyPI package dependency conflicts, then the displayed error messages contain details about conflicting packages and package versions.




###  gcloud 

To run an upgrade check for your environment, run the [`environments check-upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/check-upgrade) command with the Managed Airflow image version. that you want to upgrade to.
    
    
    gcloud composer environments check-upgrade \
      ENVIRONMENT_NAME \
      --location LOCATION \
      --image-version VERSION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `VERSION` with the new [Managed Airflow image version](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to upgrade to, in the `composer-a.b.c-airflow-x.y.z` format. You can use all [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases).



Example:
    
    
    gcloud composer environments check-upgrade example-environment \
      --location us-central1 \
      --image-version composer-1.20.12-airflow-1.10.15
    

Example output:
    
    
    Waiting for [projects/example-project/locations/us-central1/environments/
    example-environment] to be checked for PyPI package conflicts when upgrading
    to composer-1.20.12-airflow-1.10.15. Operation [projects/example-project/locations/
    us-central1/operations/04d0e8b2-...]...done.
    ...
    
    Response:
    '@type': type.googleapis.com/
    google.cloud.orchestration.airflow.service.v1.CheckUpgradeResponse
    buildLogUri: ...
    **containsPypiModulesConflict: CONFLICT**
    pypiConflictBuildLogExtract: |-
    The Cloud Build image build failed: Build failed; check build logs for
    details. Full log can be found at ...
    **Error details: tensorboard 2.2.2 has requirement
    setuptools >=41.0.0, but you have setuptools 40.3.0.**
    

As an alternative, you can run an upgrade check asynchronously. Use the `--async` argument to make an asynchronous call, then check the result with the [`gcloud composer operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/operations/describe) command.

###  API 

Construct an [`environments.checkUpgrade`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/checkUpgrade) API request.

Specify the image version in the `imageVersion` field:
    
    
    {
      "imageVersion": "VERSION"
    }
    

Replace `VERSION` with the new version that you want to upgrade to, in the `composer-a.b.c-airflow-x.y.z` format. 

## Upgrade your environment

**Caution:** Pause all DAGs and wait for in-progress tasks to finish before upgrading.

To upgrade your environment to a later version of Managed Airflow or Airflow: 

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. Locate the **Image version** item and click **Upgrade**.

  5. From the **Image version** drop-down menu, select a Managed Airflow version that you want to upgrade to.

  6. Click **Upgrade**.




###  gcloud 
    
    
    gcloud composer environments update \
      ENVIRONMENT_NAME \
      --location LOCATION \
      --image-version VERSION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `VERSION` with the new [Managed Airflow image version](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to upgrade to, in the `composer-a.b.c-airflow-x.y.z` format. You can also use all [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases).



For example:
    
    
    gcloud composer environments update \
      example-environment \
      --location us-central1 \
      --image-version composer-1.20.12-airflow-1.10.15
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.softwareConfig.imageVersion` mask.

     2. In the request body, in the `imageVersion` field, specify a new version that you want to upgrade to.




For example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.softwareConfig.imageVersion
    
      {
        "config": {
          "softwareConfig": {
            "imageVersion": "composer-1.20.12-airflow-1.10.15"
          }
        }
      }
    

###  Terraform 

**Warning:** If you specify a different major version of Airflow or Managed Airflow, Terraform **deletes your environment and creates a new one**. You can upgrade only within minor versions of Airflow or Managed Airflow.

The `image_version` field in the `config.software_config` block controls the Managed Airflow image of your environment. In this field, specify a new Managed Airflow image. 
    
    
      resource "google_composer_environment" "example" {
      provider = google-beta
      name = "ENVIRONMENT_NAME"
      region = "LOCATION"
    
      config {
        software_config {
          image_version = "VERSION"
        }
      }
    }
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located. the new [Managed Airflow image version](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to upgrade to, in the `composer-a.b.c-airflow-x.y.z` format. You can also use all [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases).



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        software_config {
          image_version = "composer-1.20.12-airflow-1.10.15"
        }
      }
    }
    

## What's next

  * [Troubleshooting updates and upgrades](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-updates-upgrades)
  * [List of versions](https://docs.cloud.google.com/composer/docs/composer-versions)
  * [Managed Airflow versioning](https://docs.cloud.google.com/composer/docs/composer-versioning-overview)
  * [Update environments](https://docs.cloud.google.com/composer/docs/composer-1/update-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
