---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading/
title: Manage version upgrades for instances and pipelines \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:33.910187+00:00
---

# Manage version upgrades for instances and pipelines  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/upgrading/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Manage version upgrades for instances and pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This page describes upgrading the version of your instances or batch pipelines.

Upgrade your Cloud Data Fusion instances and batch pipelines to the latest platform and plugin versions for the latest features, bug fixes, and performance improvements.

## Before you begin

**Caution:** Before you upgrade, stop all running pipelines, suspend all pipeline schedules and disable all upstream triggers, such as Managed Service for Apache Airflow triggers. Upgrading an instance that has running pipelines can have unpredictable results and affect instance availability.

  * **Plan a scheduled downtime for the upgrade.** The process takes up to an hour.
  * In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)




## Limitations

  * After you create a Cloud Data Fusion instance, you cannot change its edition, even through an upgrade operation.

  * Don't trigger an upgrade with Terraform, as it deletes and recreates the instance, instead of performing an in-place upgrade. This issue results in the loss of any existing data within the instance.

  * Cloud Data Fusion doesn't restart pipelines that stop as a result of the upgrade operation.

  * When you upgrade an instance from versions prior to 6.11.0, expect greater downtime for the upgrade, especially if the instance handles a lot of data.

  * Upgrading real-time pipelines isn't supported, except in pipelines created in version 6.8.0 with a Kafka real-time source. For a workaround, see Upgrade real-time pipelines.




## Upgrade Cloud Data Fusion instances

To upgrade a Cloud Data Fusion instance to a new Cloud Data Fusion version, go to the **Instance details** page:

  1. In the Google Cloud console, go to the Cloud Data Fusion page.

  2. Click **Instances** , and then click the instance's name to go to the **Instance details** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)




Then perform the upgrade using either the Google Cloud console or gcloud CLI:

### Console

  1. Click **Upgrade** for a list of available versions.

  2. Select a version.

  3. Click **Upgrade**.

  4. Verify that the upgrade was successful:

     1. Refresh the **Instance details** page.

     2. Click **View instance** to access the upgraded instance in the Cloud Data Fusion web interface.

     3. Click **System admin** in the menu bar.

The new version number appears at the top of the page.

  5. To prevent your pipelines from getting stuck when you run them in the new version, grant the required roles in your upgraded instance.




### gcloud

  1. To upgrade to a new Cloud Data Fusion version, run the following gcloud CLI command from a local terminal [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) session:
         
         gcloud beta data-fusion instances update INSTANCE_ID \
             --project=PROJECT_ID \
             --location=LOCATION_NAME \
             --version=AVAILABLE_INSTANCE_VERSION
         

     * Optional: If applicable for your instance, add the [`--enable_stackdriver_logging`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--enable_stackdriver_logging), [`--enable_stackdriver_monitoring`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--enable_stackdriver_monitoring), and [`--labels`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--labels) flags.

     * Optional: You can pass the CDAP properties, such as `enable.unrecoverable.reset`, as [`--options`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/data-fusion/instances/update#--options).

  2. Verify that the upgrade was successful by following these steps:

     1. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page.

     2. Click **View instance** to access the upgraded instance in the Cloud Data Fusion web interface.

     3. Click **System Admin** in the menu bar.

The new version number appears at the top of the page.

  3. To prevent your pipelines from getting stuck when you run them in the new version, grant the required roles in your upgraded instance.




## Upgrade batch pipelines

To upgrade your Cloud Data Fusion batch pipelines to use the latest plugin versions:

  1. [Set environment variables](https://docs.cloud.google.com/data-fusion/docs/reference/cdap-reference#set-up).

  2. **Recommended:** Back up all pipelines. You can back up pipelines in one of two ways:

     * Download the zip file by following these steps:

       1. To trigger a zip file download, back up all pipelines with the following command:
    
    echo $CDAP_ENDPOINT/v3/export/apps
    

       1. Copy the URL output to your browser.
       2. Extract the downloaded file, then confirm that all pipelines were exported. The pipelines are organized by namespace.
     * Back up pipelines using [Source Control Management](https://docs.cloud.google.com/data-fusion/docs/how-to/source-control-management) (SCM), available in version 6.9 and later. SCM provides GitHub integration, which you can use to back up pipelines.

  3. Upgrade pipelines by following these steps:

     1. Create a variable that points to the `pipeline_upgrade.json` file that you will create in the next step to save a list of pipelines.
            
            export PIPELINE_LIST=PATH/pipeline_upgrade.json
            

Replace PATH with the path to the file.

     2. Create a list of all pipelines for an instance and namespace using the following command. The result is stored in the `$PIPELINE_LIST` file in `JSON` format. You can edit the list to remove pipelines that don't need upgrades.
            
            curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/apps -o $PIPELINE_LIST
            

Replace NAMESPACE_ID with the namespace where you want the upgrade to happen.

     3. Upgrade the pipelines listed in `pipeline_upgrade.json`. Insert the NAMESPACE_ID of pipelines to be upgraded. The command displays a list of upgraded pipelines with their upgrade status.
            
            curl -N -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_ID/upgrade --data @$PIPELINE_LIST
            

Replace NAMESPACE_ID with the namespace ID of the pipelines that are getting upgraded.

  4. To prevent your pipelines from getting stuck when you run them in the new version, grant the required roles in your upgraded instance.




## Upgrade real-time pipelines

Upgrading real-time pipelines is not supported, except in pipelines created in version 6.8.0 with a Kafka real-time source.

For everything else, you instead do the following:

  1. Stop and export the pipelines.
  2. Upgrade the instance.
  3. Import the real-time pipelines into your upgraded instance.



## Upgrade to enable Replication

Replication can be enabled in Cloud Data Fusion environments in version 6.3.0 or later. If you have version 6.2.3, upgrade to 6.3.0, then upgrade to the latest version. You can then [enable Replication](https://docs.cloud.google.com/data-fusion/docs/how-to/enable-replication).

## Grant roles for upgraded instances

After the upgrade completes, grant the [Cloud Data Fusion Runner role](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission#runtime-permission) (`roles/datafusion.runner`) and [Cloud Storage Admin role](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission#admin-permission) (`roles/storage.admin`) to the Managed Service for Apache Spark service account in your [project](https://docs.cloud.google.com/data-fusion/docs/concepts/security#projects).

## What's next

  * [Manage patch revisions](https://docs.cloud.google.com/data-fusion/docs/how-to/upgrade-to-patch-revision) for Cloud Data Fusion instances.
  * Learn about [versioning in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/versioning).
  * Refer to the [available version and patch revision upgrades](https://docs.cloud.google.com/data-fusion/docs/concepts/available-upgrades).
  * [Troubleshoot upgrades](https://docs.cloud.google.com/data-fusion/docs/support/troubleshoot-upgrades).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
