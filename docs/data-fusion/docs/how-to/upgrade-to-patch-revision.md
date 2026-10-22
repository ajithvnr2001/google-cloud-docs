---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-to-patch-revision/
title: Manage patch revisions for instances \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:42.339652+00:00
---

# Manage patch revisions for instances  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-to-patch-revision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage patch revisions for instances Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information and guidelines for managing patch revisions for a Cloud Data Fusion instance.

For more information about how patch revisions differ from other upgrades, see Instance upgrades versus patch revisions.

Patch revisions include critical security updates and bug fixes on your instances. A patch revision only applies fixes on the platform without changing the pipelines or plugins. The upgrade process involves instance and pipeline downtime.

For more information on versioning Cloud Data Fusion, see [Versioning in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/versioning) and [available patch revision upgrades](https://docs.cloud.google.com/data-fusion/docs/concepts/available-upgrades).

## Before you start

  * Before you upgrade to a patch revision, review the release notes for information about the specific fixes it includes. It's important to understand how they might affect your instances.
  * Prepare your environment: 
    * Schedule downtime for the patch revision.
    * **Recommended** : Before you upgrade, stop any running pipelines and disable any upstream triggers, such as Managed Service for Apache Airflow triggers. When the upgrade begins, all running pipelines stop.



## Instance upgrade versus patch revision

Instance upgrade
    These versions include the latest features, feature enhancements, and performance improvements for the platform. Instance upgrades are associated with plugin changes and require pipeline upgrades. For more information, see [Version upgrades: Instances and pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading).
Patch revisions
    These versions only include critical security and bug fixes for the platform and don't change or update the pipeline and plugin features.

## Upgrade to a patch revision for a Cloud Data Fusion instance

To upgrade to a patch revision for your Cloud Data Fusion instance, follow these steps in the Google Cloud console, Google Cloud CLI, or the REST API.

### Console

  1. In the Google Cloud console, go to the Cloud Data Fusion page.

  2. Click **Instances** and select the checkbox by the instance's name.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  3. Click **Upgrade**.

  4. Select the latest patch revision and click **Upgrade**.

  5. To access the upgraded instance in the Cloud Data Fusion web interface, click **View instance**.

  6. To verify that the upgrade was successful, in the Google Cloud console, reload the **Instance details** page. Check the **Version** field for the update.

**Note:** The version number that appears at the top of the **System Admin** page in the Cloud Data Fusion web interface doesn't show the patch revision number.



### gcloud

  1. To update to an available patch revision, run the following gcloud CLI command from a local terminal [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) session:
         
         gcloud beta data-fusion instances update INSTANCE_ID \
           --project=PROJECT_ID \
           --location=LOCATION_NAME \
           --version=CURRENT_INSTANCE_VERSION \
           --patch_revision=AVAILABLE_PATCH_REVISION
         

Replace the following:

     * `INSTANCE_ID`: the name of the instance.
     * `PROJECT_ID`: the ID of the project that contains the Cloud Data Fusion instance.
     * `LOCATION_NAME`: the location of the instance.
     * `CURRENT_INSTANCE_VERSION`: the current version.
     * `AVAILABLE_PATCH_REVISION`: the patch revision to upgrade to.

     * Optional: if applicable for your instance, add the [\--enable_stackdriver_logging](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--enable_stackdriver_logging), [\--enable_stackdriver_monitoring](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--enable_stackdriver_monitoring), and [\--labels](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--labels) flags.

     * Optional: you can pass the CDAP properties, such as `enable.unrecoverable.reset`, as [\--options](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--options).

**Note:** Passing the `patch_revision` argument is optional. If unspecified, the latest available patch revision is used.

For more information, see the [gcloud CLI reference](https://cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update).

  2. Verify that the upgrade was successful by following these steps:

     1. Get the instance details by running the following gcloud CLI command from a local terminal Cloud Shell session:
            
            gcloud beta data-fusion instances describe \
              --project=PROJECT_ID \
              --location=LOCATION_NAME \
              INSTANCE_ID
            

     2. Check that the `PATCH_REVISION` field in the instance details is updated to the specified version.




### REST API

To perform patch revision of Cloud Data Fusion instance, call its [patch()](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/patch) method. Set the `patchRevision` optional field in the request. If you don't specify a patch revision, the latest available one is used.

### Examples

The following examples show how to upgrade an instance to a patch revision with the REST API.

#### Upgrade an instance to a specific patch revision version

Call the `patch()` method:
    
    
    PATCH https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_NAME/instances/INSTANCE_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the Cloud Data Fusion instance.
  * `LOCATION_NAME`: the location of the instance.
  * `INSTANCE_ID`: the name of the instance.



Use the following JSON request body:
    
    
    {
      "version": VERSION_NUMBER,
      "patchRevision": PATCH_REVISION_NUMBER
    }
    

Replace the following:

  * `VERSION_NUMBER`: the version of the instance, such as `6.7.3`.
  * `PATCH_REVISION_NUMBER`: the patch revision version to upgrade to, such as `6.7.3.1`. See the [available patch revisions](https://docs.cloud.google.com/data-fusion/docs/concepts/available-upgrades#available_patch_revisions).



For example, to upgrade a 6.7.3 version instance to the 6.7.3.1 patch revision, use the following JSON request body:
    
    
    {
      "version": 6.7.3,
      "patchRevision": 6.7.3.1
    }
    

#### Upgrade an instance to the default patch revision version

Call the `patch()` method:
    
    
    PATCH https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_NAME/instances/INSTANCE_ID
    

Use the following JSON request body:
    
    
    {
      "version": VERSION_NUMBER
    }
    

Replace `VERSION_NUMBER` with the version of the instance, such as `6.7.3`:
    
    
    {
      "version": 6.7.3
    }
    

## Roll back a patch revision

If you experience unforeseen issues after incorporating a patch revision, revert the patch revision to an earlier, stable state by following these steps.

### gcloud

  1. To roll back to a previous patch revision, run the following gcloud CLI command from a local terminal [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) session:
         
         gcloud beta data-fusion instances update INSTANCE_ID \
           --project=PROJECT_ID \
           --location=LOCATION_NAME \
           --version=CURRENT_INSTANCE_VERSION \
           --patch_revision=STABLE_PATCH_REVISION
         

Replace the following:

     * `INSTANCE_ID`: the name of the instance.
     * `PROJECT_ID`: the ID of the project that contains the Cloud Data Fusion instance.
     * `LOCATION_NAME`: the location of the instance.
     * `CURRENT_INSTANCE_VERSION`: the current version.
     * `STABLE_PATCH_REVISION`: the patch revision to roll back to.

     * Optional: if applicable for your instance, add the [\--enable_stackdriver_logging](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--enable_stackdriver_logging), [\--enable_stackdriver_monitoring](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--enable_stackdriver_monitoring), and [\--labels](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--labels) flags.

     * Optional: you can pass the CDAP properties, such as `enable.unrecoverable.reset`, as [\--options](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--options).

For more information, see the [gcloud CLI reference](https://cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update).

  2. Verify that the rollback was successful by following these steps:

     1. Get the instance details by running the following gcloud CLI command from a local terminal Cloud Shell session:
            
            gcloud beta data-fusion instances describe \
              --project=PROJECT_ID \
              --location=LOCATION_NAME \
              INSTANCE_ID
            

     2. Check that the `PATCH_REVISION` field in the instance details is reverted to the specified version.




### REST API

To roll back a patch revision in a Cloud Data Fusion instance, call its [patch()](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/patch) method. Set the `patchRevision` field in the request to any earlier, stable patch revision.

### Example

This example shows how to roll back an instance from the `6.7.3.1` patch revision to 6.7.3 patch revision using the REST API.

Call the `patch()` method:
    
    
    PATCH https://datafusion.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_NAME/instances/INSTANCE_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the Cloud Data Fusion instance.
  * `LOCATION_NAME`: the location of the instance.
  * `INSTANCE_ID`: the name of the instance.



Use the following JSON request body:
    
    
    {
      "version": VERSION_NUMBER,
      "patchRevision": STABLE_PATCH_REVISION
    }
    

Replace the following:

  * `VERSION_NUMBER`: the version of the instance, such as `6.7.3`.
  * `STABLE_PATCH_REVISION`: the patch revision to roll back to. See the [available patch revisions](https://docs.cloud.google.com/data-fusion/docs/concepts/available-upgrades#available_patch_revisions).



For example, to roll back the instance from the `6.7.3.1` patch revision to the `6.7.3` patch revision, use the following JSON request body:
    
    
    {
      "version": 6.7.3,
      "patchRevision": 6.7.3
    }
    

## What's next

  * [Manage version upgrades](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading) for pipelines and instances.
  * Learn about [versioning in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/versioning).
  * Refer to the [available version and patch revision upgrades](https://docs.cloud.google.com/data-fusion/docs/concepts/available-upgrades).
  * [Troubleshoot upgrades](https://docs.cloud.google.com/data-fusion/docs/support/troubleshoot-upgrades).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
