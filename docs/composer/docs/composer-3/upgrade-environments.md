---
url: https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments/
title: Upgrade environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:44.932452+00:00
---

# Upgrade environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/upgrade-environments/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Upgrade environments Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/upgrade-environments "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to upgrade your environment to a new Airflow version.

## About upgrade operations

In Managed Airflow (Gen 3), you **don't manage the Managed Airflow version** of your environment:

  * Managed Airflow automatically upgrades the infrastructure components of your environment. These components are related to Managed Airflow functionality and do not change how Airflow works or how your Airflow DAGs are executed.
  * Managed Airflow doesn't automatically upgrade Airflow version and build, Airflow components, or components closely related to Airflow workloads. They are not changed when the infrastructure components upgrade automatically.
  * You can manually upgrade to a new Airflow [version or build](https://docs.cloud.google.com/composer/docs/composer-versioning-overview).



For example, you can use the same version and build of Airflow for several months, without performing any upgrades, and your environment still receives latest Managed Airflow updates, fixes, and improvements of the environment's infrastructure components. When later you decide to move to a new version or build of Airflow, you upgrade the Airflow version in your environment.

### About Airflow version upgrade

Your environment **changes the version or build of Airflow** in the following way:

  * You control the Airflow version (and build) of your environment. You can perform the Airflow version upgrade operation when you choose to switch your environment to a different version of Airflow. For example, this might happen if the current version and build of Airflow are [no longer supported](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

  * Managed Airflow re-deploys your environment's Airflow components using the specified Airflow [version and build](https://docs.cloud.google.com/composer/docs/composer-versions).

  * Managed Airflow applies Airflow configuration changes, such as custom PyPI packages or Airflow configuration option overrides, if your environment had them before the upgrade.

  * Managed Airflow updates the Airflow `airflow_db` connection to point to the new Cloud SQL database.




Changing the Airflow version doesn't change how you connect to the resources in your environment, such as the URL of your environment's bucket, or Airflow web server.

### About automatic infrastructure upgrade operations

Managed Airflow periodically runs **automatic infrastructure upgrade operations** :

  * Automatic infrastructure upgrade operations run periodically during [maintenance windows](https://docs.cloud.google.com/composer/docs/composer-2/specify-maintenance-windows) specified for the environment.

  * It is not possible to disable automatic infrastructure upgrades in Managed Airflow (Gen 3). You can control the time periods when automatic upgrades can run by specifying custom maintenance windows for your environment.

  * This operation is visible in Google Cloud console and environment's logs, like any other long-running operation. While the operation is running, you can't start other operations at the environment level (but you can still run Airflow DAGs).

  * In some cases, automatic infrastructure upgrades can restart Airflow components. During such restarts, Airflow workers are gracefully terminated with a grace period of 24 hours. If you have tasks that need more than 24 hours to complete, consider using deferrable operators. An upgrade might result in a short period of unavailability for environment's infrastructure components, such as environment monitoring.




### Limitations of upgrade and rollback operations

Upgrade operations have the following limitations:

  * [Managed Airflow releases](https://docs.cloud.google.com/composer/docs/release-notes) are gradually rolled out to all regions supported by Managed Airflow over several days. The latest version from a release in progress might not be available in your region yet.

  * In Managed Airflow (Gen 3), you can roll back an upgrade to an earlier version or build of Airflow with the following limitations:

    * Rollbacks are supported for upgrades done **from** Airflow 3 versions, or from Airflow 2 versions starting with the airflow-2.7.3-build.0 build.
    * Rollbacks are supported for upgrades done **to** target versions airflow-2.11.1-build.20 or later, airflow-3.2.2-build.7 or later, and airflow-3.3.1-build.3 or later.
    * You can start the rollback operation within 30 days of the upgrade. If the target Airflow build is past its end of support date, it's still possible to roll back to it. You can do skip-version rollbacks. If you've upgraded more than once within 30 days, you can roll back to any previously used version as long as it satisfies eligibility constraints.
    * The environment is in a `RUNNING` state when you start the rollback.

  * You can't upgrade your environment if the Airflow database contains more than 20 GB of data. During an upgrade, a warning is shown if the Airflow database size is more than 20 GB. In this case, [perform the database maintenance](https://docs.cloud.google.com/composer/docs/composer-3/cleanup-airflow-database) to reduce the database size.

  * If you use the XCom mechanism to transfer files, make sure that you [use it according to Airflow's guidelines](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcoms.html#object-storage-xcom-backend). Transferring big files or a large number of files using XCom impacts Airflow database's performance and can lead to failures when loading snapshots or upgrading your environment. Consider using alternatives such as Cloud Storage to transfer large volumes of data.




## Before you begin

**Caution:**

  * Make sure that you **know the differences** between the current version of Airflow and the version that you are upgrading to. The new version can include different versions of preinstalled packages, patches from Managed Airflow, or changes in Airflow functionality, provided by the Airflow open source project. You can [check the versions of provider packages](https://docs.cloud.google.com/composer/docs/composer-versions) that are included in a specific version.

  * Make sure that **your DAGs are compatible** with the new Airflow version and new versions of all provider packages (including the Airflow provider package for Google Cloud and Google services). Incompatible changes can cause your DAGs to no longer work.

  * Unlike automatic infrastructure upgrades, when an environment upgrades to a new Airflow version or build, or rolls back to a previous one, then **all running tasks are terminated**. After an upgrade is completed, Airflow schedules these tasks for a retry, depending on the way you configure retries for your DAGs.




  * We recommend to [create a new snapshot](https://docs.cloud.google.com/composer/docs/composer-3/save-load-snapshots) of the environment to be able to re-create the environment in case this is needed.

  * Your account must have a role that can trigger environment upgrade operations. In addition, the service account of the environment must have a role that has enough permissions to perform upgrade operations. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-3/access-control).




## Check that your environment is up to date

Managed Airflow displays warnings when your environment's Airflow build approaches its end of support date. You can use these warnings to always keep your environment [supported](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support).

![A deprecation message is displayed on the Environment details page](https://docs.cloud.google.com/static/composer/docs/images/environment-deprecation-message-composer-3.png)**Figure 1.** A deprecation message is displayed on the Environment details page 

Managed Airflow keeps track of the Airflow version and build that your environment is based on. When it approaches the [end of support date](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-deprecation-and-support), you can see a warning in the list of environments and on the **Environment details** page.

**Note:** You can always upgrade your environment, even if the environment's Airflow version and build are past their support period. 

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

Managed Airflow provides a list of Airflow builds that you can upgrade your environment to.

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

You can check if PyPI packages installed in your environment have any conflicts with preinstalled packages in the new Airflow version or build.

A successful check means that there are no conflicts in PyPI package dependencies between the current and the specified version. However, an upgrade operation might still not be successful because of other reasons.

###  Console 

To run an upgrade check for your environment:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab, locate the **Image version** entry, and click **Upgrade**.

  4. In the **Environment version upgrade** dialog, in the **New version** drop-down list, select an Airflow version or build that you want to upgrade to.

  5. In the **PyPI packages compatibility** section, click **Check for conflicts**.

  6. Wait until the check is complete. If there are PyPI package dependency conflicts, then the displayed error messages contain details about conflicting packages and package versions.




###  gcloud 

To run an upgrade check for your environment, run the [`environments check-upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/check-upgrade) command with the Airflow version or build. that you want to upgrade to.
    
    
    gcloud composer environments check-upgrade \
      ENVIRONMENT_NAME \
      --location LOCATION \
      --airflow-version VERSION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `VERSION` with the new Airflow [version and build](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to upgrade to, in the `airflow-x.y.z-build.t` format. You can use all [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases).



Example:
    
    
    gcloud composer environments check-upgrade example-environment \
      --location us-central1 \
      --airflow-version airflow-2.11.1-build.21
    

Example output:
    
    
    Waiting for [projects/example-project/locations/us-central1/environments/
    example-environment] to be checked for PyPI package conflicts when upgrading
    to composer-3-airflow-2.11.1-build.21. Operation [projects/example-project/locations/
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
    

Replace `VERSION` with the new version that you want to upgrade to, in the `composer-3-airflow-x.y.z-build.t` format. 

## Check for conflicts with Managed Airflow (Gen 3)

Managed Airflow (Gen 3) is the latest major version of Managed Airflow. You can check if a Managed Airflow (Gen 2) environment can be upgraded to Managed Airflow (Gen 3) with an upgrade check. The following description **applies to Managed Airflow (Gen 2) environments**.

While it isn't possible to migrate your environment from Managed Airflow (Gen 2) to Managed Airflow (Gen 3) in-place, you can check for compatibility problems using an upgrade check. We recommend to do it before [migrating to Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-2/migrate-composer-3-script).

To check for compatibility with Managed Airflow (Gen 3), make a regular upgrade check of your Managed Airflow (Gen 2) environment and specify a Managed Airflow (Gen 3) version as a target.

Each reported conflict can have the following types:

  * `BLOCKING` conflicts report incompatible environment configuration elements that aren't supported in Managed Airflow (Gen 3). We recommend to address these conflicts before starting a migration to Managed Airflow (Gen 3).

  * `NON_BLOCKING` conflicts report environment configuration elements that are different in Managed Airflow (Gen 3) and might cause unexpected behavior. For example, changes of the default values such as default maintenance windows are reported as non-blocking conflicts. We recommend to check if these conflicts can cause problems before starting the migration process.

  * PyPI package conflicts are also reported as part of this check. They are reported separately from the configuration conflicts, in the same way as for a regular PyPI package compatibility check.




###  Console 

To check for compatibility with Managed Airflow (Gen 3), use gcloud CLI or the Cloud Composer API. Google Cloud console supports only checks for PyPI package compatibility.

###  gcloud 

To check for compatibility with Managed Airflow (Gen 3), run the [`environments check-upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/environments/check-upgrade) command and specify a Managed Airflow (Gen 3) version as a target.
    
    
    gcloud composer environments check-upgrade \
      ENVIRONMENT_NAME \
      --location LOCATION \
      --image-version COMPOSER_3_VERSION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `COMPOSER_3_VERSION` with the Airflow [version and build](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to upgrade to, in the `airflow-x.y.z-build.t` format. You can use all [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases).



Example:
    
    
    gcloud composer environments check-upgrade example-environment \
      --location us-central1 \
      --image-version composer-3-airflow-2
    

Example conflict messages:
    
    
    ...
    - message: Error validating property [core]unit_test_mode. Overriding [core]
    unit_test_mode is not permitted.
    type: BLOCKING
    - message: Environment variables [GOOGLE_CLOUD_PROJECT] may not be overridden.
    type: BLOCKING
    - message: You have to specify Worker CPUs to be 0.5, 1.0 or multiples of 2.0.
    type: BLOCKING
    - message: The environment uses a default maintenance window, which is
    different in Composer 2 and Composer 3. Unless set to a custom value, the
    maintenance window will be changed to a new default after the upgrade.
    type: NON_BLOCKING
    ...
    

As an alternative, you can run this check asynchronously. Use the `--async` argument to make an asynchronous call, then check the result with the [`gcloud composer operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/composer/operations/describe) command.

###  API 

Construct an [`environments.checkUpgrade`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/checkUpgrade) API request.

Specify the image version in the `imageVersion` field:
    
    
    {
      "imageVersion": "COMPOSER_3_VERSION"
    }
    

Replace `COMPOSER_3_VERSION` with the Airflow [version and build](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to upgrade to, in the `airflow-x.y.z-build.t` format. You can use all [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases).

## Upgrade your environment

**Caution:** Pause all DAGs and wait for in-progress tasks to finish before upgrading.

To upgrade your environment to a new version or build of Airflow: 

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. Locate the **Image version** item and click **Upgrade**.

  5. From the **Image version** drop-down menu, select an Airflow version or build that you want to upgrade to.

  6. Click **Upgrade**.




###  gcloud 
    
    
    gcloud composer environments update \
      ENVIRONMENT_NAME \
      --location LOCATION \
      --airflow-version VERSION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `VERSION` with the new Airflow [version and build](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to upgrade to, in the `airflow-x.y.z-build.t` format. You can also use all [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases).



For example:
    
    
    gcloud composer environments update \
      example-environment \
      --location us-central1 \
      --airflow-version airflow-2.11.1-build.21
    

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
            "imageVersion": "composer-3-airflow-2.11.1-build.21"
          }
        }
      }
    

###  Terraform 

The `image_version` field in the `config.software_config` block controls the Airflow version and build of your environment. In this field, specify a new Airflow version and build. 
    
    
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
  * `LOCATION` with the region where the environment is located. 
  * `VERSION` with the new Airflow [version and build](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to upgrade to, in the `airflow-x.y.z-build.t` format. You can also use all [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases).



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        software_config {
          image_version = "airflow-2.11.1-build.21"
        }
      }
    }
    

## Roll back an upgrade

You can roll back an environment upgrade if you encounter degraded performance, Airflow bugs, or compatibility issues with your DAGs, plugins, or dependencies.

You can roll back an upgrade within 30 days of the upgrade operation if the environment is in the `RUNNING` state. It's possible to roll back to versions that have reached their end of support date. For more information, see Limitations of upgrade and rollback operations.

In addition to rolling back a single upgrade, you can:

  * Perform multiple successive rollbacks:

Example: A > B > C > B > A (if rolling back to B and A satisfies limitations).

  * Perform skip-version rollbacks:

Example: A > B > C > A (if rolling back to A satisfies limitations).




During a rollback, **only the Airflow build of the environment is reverted** to the specified version. Managed Airflow preserves your environment's data and state during rollbacks:

  * DAG files and execution history: All DAG definitions, DAG run history, task instance states, and XComs remain intact in the metadata database.

**Warning:** When an environment rolls back, all running tasks are terminated immediately. After the rollback completes, Airflow schedules these tasks for retry based on your DAG retry configuration.
  * Environment configuration: Airflow configuration overrides, environment variables, custom PyPI packages, and scaling settings are preserved. If you use non-strict PyPI package version requirements for your custom PyPI packages, your environment might have a different package version after the rollback (this version will still satisfy the specified version requirement).

If you changed environment configuration during the upgrade, such as modifying environment variables or adjusting resource limits for Airflow components, these changes aren't reverted. If required, you can revert the changes manually before or after the rollback.

  * Logs and monitoring: Task execution logs stored in Cloud Logging and metrics history in Cloud Monitoring are preserved.




Airflow database schema updates (Alembic migrations) are automatically rolled back to match the target Airflow version schema. For the list of database migrations that are present in each Airflow version, see [Airflow Database Migrations](https://airflow.apache.org/docs/apache-airflow/stable/migrations-ref.html) in Airflow documentation. During a rollback operation, all listed migrations between the current Airflow version and the target Airflow version are rolled back.

**Caution:** If a database migration dropped a column during the upgrade, the rollback recreates the column in the Airflow database schema, **but does not restore the previous data in that column**. This can result in data loss in the Airflow metadata database.

### Find the previously used version

To find the previously used version:

###  gcloud 

You can find the information about the previously used image version in the operations:
    
    
    gcloud composer operations list \
    --locations LOCATION \
    --filter='metadata.resource ~ "environments/ENVIRONMENT_NAME$" (metadata.operationType=UPDATE OR metadata.operationType=CREATE)'
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



The output contains the log of environment operations. The last operation of the `UPDATE` type will be the upgrade that you want to roll back. Find the `UPDATE` (or `CREATE` if there's only one upgrade) operation that precedes it. Usually, this is the second-to-last item on the list.

In the following example, the `71c3d5c9-5b26-4a98-8b19-7f62e9f4ed51` operation is the upgrade to roll back, the `63da3be2-3acf-4fb4-986a-90552a6df8b3` operation is the upgrade to the previously used version.
    
    
    ┌──────────────────────────────────────┬───────────────┬─────────────┬──────────────────────────────┬───────────┬─────────────────────────────┐
    │                 UUID                 │      TYPE     │   LOCATION  │      TARGET_ENVIRONMENT      │   STATE   │         CREATE_TIME         │
    ├──────────────────────────────────────┼───────────────┼─────────────┼──────────────────────────────┼───────────┼─────────────────────────────┤
    │ 71c3d5c9-5b26-4a98-8b19-7f62e9f4ed51 │ UPDATE        │ us-central1 │ example-environment          │ SUCCEEDED │ 2026-10-15T11:18:32.084039Z │
    │ 63da3be2-3acf-4fb4-986a-90552a6df8b3 │ UPDATE        │ us-central1 │ example-environment          │ SUCCEEDED │ 2026-08-15T10:56:10.628514Z │
    │ 4ebc18a9-25bb-4325-b4c9-0957c67c078b │ UPDATE        │ us-central1 │ example-environment          │ SUCCEEDED │ 2026-06-09T11:30:50.922080Z │
    │ 8618f807-abb4-4fc8-9f5b-9353079f6e79 │ UPDATE        │ us-central1 │ example-environment          │ SUCCEEDED │ 2026-05-31T06:57:27.816925Z │
    │ 22022864-0fa5-4d1b-92c6-c3f382b43a35 │ UPDATE        │ us-central1 │ example-environment          │ SUCCEEDED │ 2025-11-17T11:52:36.923698Z │
    │ ec5bf071-e6c6-4760-b3c9-4a117cb08f7b │ CREATE        │ us-central1 │ example-environment          │ SUCCEEDED │ 2025-11-17T11:17:58.133979Z │
    └──────────────────────────────────────┴───────────────┴─────────────┴──────────────────────────────┴───────────┴─────────────────────────────┘
    

Describe the operation:
    
    
    gcloud composer operations describe OPERATION_UUID \
      --location LOCATION \
      --format="value(response.config.softwareConfig.imageVersion)"
    

Replace:

  * `OPERATION_UUID` with the previous upgrade operation's UUID obtained with the previous command.
  * `LOCATION` with the region where the environment is located.



The output of this command is the previously used version.

### Run the rollback operation

To roll back your environment to a previous build or version of Airflow:

###  Console 

Rolling back an upgrade is not supported in Google Cloud console. Use gcloud CLI, API, or Terraform instead.

###  gcloud 
    
    
    gcloud composer environments update \
      ENVIRONMENT_NAME \
      --location LOCATION \
      --airflow-version VERSION
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `VERSION` with the new Airflow [version and build](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to roll back to, in the `airflow-x.y.z-build.t` format. It's not possible to use [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases) for the rollback operation.



Example:
    
    
    gcloud composer environments update \
      example-environment \
      --location us-central1 \
      --airflow-version airflow-2.11.1-build.21
    

###  API 

  1. Construct an [`environments.patch`](https://docs.cloud.google.com/composer/docs/reference/rest/v1/projects.locations.environments/patch) API request.

  2. In this request:

     1. In the `updateMask` parameter, specify the `config.softwareConfig.imageVersion` mask.

     2. In the request body, in the `imageVersion` field, specify a version that you want to roll back to.




For example:
    
    
    // PATCH https://composer.googleapis.com/v1/projects/example-project/
    // locations/us-central1/environments/example-environment?updateMask=
    // config.softwareConfig.imageVersion
    
      {
        "config": {
          "softwareConfig": {
            "imageVersion": "composer-3-airflow-2.11.1-build.21"
          }
        }
      }
    

###  Terraform 

The `image_version` field in the `config.software_config` block controls the Airflow version and build of your environment. In this field, specify an Airflow version and build that you want to roll back to.
    
    
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
  * `LOCATION` with the region where the environment is located.
  * `VERSION` with the Airflow [version and build](https://docs.cloud.google.com/composer/docs/composer-versions) that you want to roll back to, in the `airflow-x.y.z-build.t` format. It's not possible to use [version aliases](https://docs.cloud.google.com/composer/docs/composer-versioning-overview#version-aliases) for the rollback operation.



Example:
    
    
    resource "google_composer_environment" "example" {
      provider = google-beta
      name = "example-environment"
      region = "us-central1"
    
      config {
        software_config {
          image_version = "airflow-2.11.1-build.21"
        }
      }
    }
    

If a rollback operation fails during execution, Managed Airflow automatically attempts to restore the environment to its pre-operation state, which is the Airflow version and build that were used before the rollback was started. Review the operation error message and logs in Cloud Logging for troubleshooting details.

**Caution:** A rollback operation **isn't atomic**. A failed rollback operation can still produce artifacts or changes. For example, a DAG processor might start processing DAG files, potentially interacting with external systems, and if workers then fail to start, then the environment will be restored to the pre-rollback state.

## What's next

  * [Troubleshooting updates and upgrades](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-updates-upgrades)
  * [List of versions](https://docs.cloud.google.com/composer/docs/composer-versions)
  * [Managed Airflow versioning](https://docs.cloud.google.com/composer/docs/composer-versioning-overview)
  * [Update environments](https://docs.cloud.google.com/composer/docs/composer-3/update-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
