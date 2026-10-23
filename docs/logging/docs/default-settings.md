---
url: https://docs.cloud.google.com/logging/docs/default-settings/
title: Configure default resource settings for Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:41:26.570131+00:00
---

# Configure default resource settings for Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/default-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Configure default resource settings for Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

Configuring default resource settings for Cloud Logging for an organization or folder lets you control where new system-created log buckets are stored, whether they require customer-managed encryption keys (CMEK), and how the `_Default` log sink routes logs. Child resources automatically inherit these settings, which you configure by using the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).

These settings don't apply to observability buckets. To configure defaults for observability buckets, see [Set defaults for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets).

## Overview

The organization resource is at the highest level of the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). The organization resource is the parent of these child resources: Google Cloud projects, folders, billing accounts, and, regarding Logging, [log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries).

For organizations and folders, you can configure default resource settings for Cloud Logging. These settings let you specify the location of log buckets, the encryption model, and the configuration of the default log sink. Child resources inherit their parent's default resource settings.

**Note:** Any default resource settings for Cloud Logging that you change apply only to resources that are created after the configuration is complete; the new settings don't apply to resources that already exist.

You can use default resource settings for Cloud Logging to configure the following:

  * Whether new log buckets in a resource are encrypted with a customer-managed key, and if so, the Cloud KMS key to use for encryption.

**You can't change how the encryption key for a log bucket is managed after the log bucket is created.**

**Note:** If the default resource settings for Cloud Logging have a CMEK setting, then the default resource settings must also set the storage location.


  * The storage location for new [`_Default` and `_Required` log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries) created by child resources, and for queries saved by the **Logs Explorer** or **Observability Analytics** pages. By setting the storage location, you can [control where your logs are stored](https://docs.cloud.google.com/logging/docs/region-support).

**You can't change the location of these log buckets after they are created.**

If a resource has default resource settings for Cloud Logging that specify a storage location but don't have a CMEK setting, then new log buckets in the resource don't require CMEK.



  * Whether the [`_Default` log sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) is enabled or disabled for new projects in the resource.

  * The inclusion filters or exclusion filters that are applied to all new `_Default` sinks in the child resources.




Example configurations:

  * For an organization, the default resource settings for Cloud Logging specify a storage location. For new projects in the organization, the `_Default` and `_Required` log buckets are created in the specified location. Also, queries saved by the **Logs Explorer** or **Observability Analytics** pages are stored in the specified location. These queries include the recent queries that are automatically saved after being run, and queries saved by members of the Google Cloud project.


  * For an organization, the default resource settings for Cloud Logging specify a storage location. Additionally, for a folder in the organization, the default resource settings for Cloud Logging specify a different storage location. For new projects that are in the folder, the `_Default` and `_Required` buckets are created in the location specified by the folder's settings. For projects that aren't in the folder, their `_Default` and `_Required` buckets are created in the location specified by the organization's settings.

  * For an organization, you configure the default resource settings for Cloud Logging to specify a location and CMEK. For the folder named `Non-CMEK`, you configure the default resource settings for Cloud Logging to only specify a location. If you create a project that isn't in the folder named `Non-CMEK`, then the `_Default` and `_Required` buckets are created in the same location as the Cloud Key Management Service key, and these log buckets are encrypted by that key. However, if you create a new project in the folder named `Non-CMEK`, its log buckets are created in the location specified by that folder's settings, and those log buckets aren't encrypted by CMEK.

  * For an organization, you configure the default resource settings for Cloud Logging to apply an exclusion filter that applies to new `_Default` sinks. The filter excludes Data Access audit logs from being routed through the `_Default` sink in all child resources, which prevents the Data Access audit logs from being stored in the `_Default` bucket.




## Before you begin

This document doesn't contain information about how to configure the default resource settings for Cloud Logging to have a CMEK setting. For information about that topic, see [Configure CMEK for Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

Do the following:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Ensure that your Identity and Access Management role on the organization or folder includes the following Cloud Logging permissions:

     * `logging.settings.get`
     * `logging.settings.update`
  3. Identify the location where you want to store your logs and queries. For a list of the supported storage locations, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).




## View default resource settings for Cloud Logging

To view the default resource settings for Cloud Logging, use the [`gcloud logging settings describe`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/describe) command:

###  FOLDER 
    
    
     gcloud logging settings describe --folder=FOLDER_ID
    

Before running the previous command, make the following replacement:

  * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).



###  ORGANIZATION 
    
    
    gcloud logging settings describe --organization=ORGANIZATION_ID
    

Before running the previous command, make the following replacement:

  * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



The previous command returns information about the default resource settings for Cloud Logging. The following is an example response:
    
    
    name: organizations/ORGANIZATION_ID/settings
    kmsKeyName: KMS_KEY_NAME
    kmsServiceAccountId: SERVICE_ACCT_NAME@gcp-sa-logging.iam.gserviceaccount.com
    storageLocation: europe-west1
    disableDefaultSink: false
    

The value of the SERVICE_ACCT_NAME might have the format `cmek-12345` or `service-12345@...`. If you can't use the Google Cloud CLI, then run the Cloud Logging API method [`getSettings`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/getSettings).

## Set the storage location

**Note:** If the default resource settings for Cloud Logging specify a location and have a CMEK setting, then the location you specify must match the location of the Cloud KMS key. For more information, see [Configure CMEK for Logging](https://docs.cloud.google.com/logging/docs/routing/managed-encryption).

[Log buckets](https://docs.cloud.google.com/logging/docs/store-log-entries) are the containers in your Google Cloud projects, billing accounts, folders, and organizations that store and organize your log data. For each Google Cloud project, billing account, folder, and organization, Logging automatically creates two log buckets: `_Required` and `_Default`, which are automatically stored in the `global` location.

For organizations and folders, the default resource settings for Cloud Logging control where new `_Required` and `_Default` log buckets are created, and where queries that you run in the **Logs Explorer** and **Observability Analytics** pages are stored. The locations of existing queries and log buckets aren't changed.

For organizations and folders, the following occurs when you configure the default resource settings for Cloud Logging to specify a location:

  * For new child resources created in the organization or folder, their `_Required` and `_Default` buckets inherit their parent's default resource settings.


  * New and recent queries that you run in the **Logs Explorer** or **Observability Analytics** pages are stored in the specified location.



When the default resource settings for Cloud Logging specify a location, that location doesn't apply to user-defined log buckets or to queries saved by using the Logging API.

### Configure the organization policies

**Note:** You aren't required to configure an organization policy when you want to configure default resource settings for Cloud Logging. For information about organization policies and how to configure them, see [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

Logging supports organization policies that can [restrict where data can be stored](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). If such a policy exists for your organization, then you can only create log buckets in locations that are allowed by the policy.

When an organization policy that specifies a location constraint exists, the policy values for the constraint must include the location specified in the default resource settings for Cloud Logging. Before you update default resource settings for Cloud Logging, review and, if necessary, update organization policies.

To view or update organization policies, do the following:

  1. In the Google Cloud console, go to the **Organization Policies** page: 

[Go to **Organization Policies**](https://console.cloud.google.com/projectselector/iam-admin/orgpolicies?supportedpurview=project,folder,organizationId)

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin**.

  2. Select your organization.

  3. View and, if necessary, update the constraint with the ID `constraints/gcp.resourceLocations`. If this constraint isn't configured, then an update isn't required.

For information about how to view specific constraints and how to edit these constraints, see [Creating and editing policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#creating_and_editing_policies).




### Set the storage location for new system-created log buckets

**Note:** If your default resource settings for Cloud Logging have a CMEK setting, then you must also set a storage location. That location must match the location of the Cloud Key Management Service key.

To configure the default resource settings for Cloud Logging to specify a location setting, run the [`gcloud logging settings update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/update) command and include the `--storage-location` flag:

###  FOLDER 
    
    
    gcloud logging settings update --folder=FOLDER_ID --storage-location=LOCATION
    

Before running the previous command, make the following replacements:

  * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).
  * LOCATION: The location where new `_Default` and `_Required` log buckets are created, and where queries are stored. For a list of supported locations, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).



###  ORGANIZATION 
    
    
    gcloud logging settings update --organization=ORGANIZATION_ID --storage-location=LOCATION
    

Before running the previous command, make the following replacements:

  * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).
  * LOCATION: The location where new `_Default` and `_Required` log buckets are created, and where queries are stored. For a list of supported locations, see [Supported regions](https://docs.cloud.google.com/logging/docs/region-support#bucket-regions).



If you can't use the Google Cloud CLI, then run the Cloud Logging API method [`updateSettings`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/updateSettings).

For information about resolving errors, see [Troubleshoot setting the location for new system-created log buckets](https://docs.cloud.google.com/logging/docs/routing/troubleshoot-cmek-orgs#troubleshoot-default-storage).

## Configure the `_Default` sink

Logging provides a predefined [`_Default` sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks) for each Google Cloud project, billing account, folder, and organization resource. Any log generated in the resource that matches the inclusion filter and isn't excluded is routed to the resource's predefined, correspondingly named [`_Default`](https://docs.cloud.google.com/logging/docs/store-log-entries#default-bucket) bucket.

For organizations and folders, the default resource settings for Cloud Logging let you configure the following behavior of the `_Default` sink:

  * You can disable the creation of a `_Default` sink for new child resources.

  * You can configure an inclusion filter or several exclusion filters that apply to the `_Default` sinks of new projects.




### Disable the `_Default` sink

You can disable the `_Default` sinks for all new resources in an organization or folder; disabling the `_Default` sinks prevents logs from being stored in the resource's `_Default` bucket. If you stop storing logs in a resource's `_Default` bucket, then the logs that would have been routed to that bucket are excluded from storage in Logging, unless those logs are explicitly included in another user-defined sink for that resource.

To disable the `_Default` sinks for a resource and any of its child resources, run the following [`gcloud logging settings update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/update) command:

###  FOLDER 
    
    
    gcloud logging settings update --folder=FOLDER_ID --disable-default-sink
    

Before running the previous command, make the following replacement:

  * FOLDER_ID: The unique numeric identifier of the folder. For information about using folders, see [Creating and managing folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders).



###  ORGANIZATION 
    
    
    gcloud logging settings update --organization=ORGANIZATION_ID --disable-default-sink
    

Before running the previous command, make the following replacement:

  * ORGANIZATION_ID: The unique numeric identifier of the organization. For information about getting this identifier, see [Getting your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



The `disable-default-sink` flag applies only to the `_Default` sink that routes logs into the `_Default` bucket.

You can re-enable the `_Default` sinks by running the following [`gcloud logging settings update`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/settings/update) command:

###  FOLDER 
    
    
    gcloud logging settings update --folder=FOLDER_ID --no-disable-default-sink
    

###  ORGANIZATION 
    
    
    gcloud logging settings update --organization=ORGANIZATION_ID --no-disable-default-sink
    

### Configure the filters of `_Default` sinks

**Note:** The default resource settings for Cloud Logging apply only to newly created resources. You can't use the process documented in this section to configure the filter of an existing `_Default` sink.

The predefined `_Default` sink routes any log entries that match the sink criteria to the corresponding `_Default` bucket. You can send a Cloud Logging API command to override the built-in [inclusion filter](https://docs.cloud.google.com/logging/docs/routing/overview#inclusion-filters) in the `_Default` sink or to append a filter. The built-in exclusion filter for the `_Default` sink is empty. However, the API command also lets you add [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

**Note:** If you add exclusion filters and if you want the `_Default` log sink to be listed on the **Logs Router** page, then you must specify a name for each exclusion filter. If you omit the `name` field, then you must use the Cloud Logging API or the Google Cloud CLI to view the details of the sink. In the following example, the exclusion filter is named `exclude-data-access`.

To specify an inclusion filter or exclusion filter that is applied to all `_Default` sinks of new resources in an organization or folder, run the Cloud Logging API method [`updateSettings`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/TopLevel/updateSettings) and specify the `defaultSinkConfig` object.

You can execute the `updateSettings` method by using the [APIs Explorer](https://docs.cloud.google.com/logging/docs/api) widget on the method's reference page. The following example illustrates sample parameters:

  * **name** (URL): `organizations/ORGANIZATION_ID/settings`
  * **updateMask** : `"default_sink_config"`
  * **Request body** , which contains an instance of `Settings`:
        
        "defaultSinkConfig": {
          {
          "filter": "NOT LOG_ID(\"externalaudit.googleapis.com/activity\") "
          "AND NOT LOG_ID(\"cloudaudit.googleapis.com/system_event\") "
          "AND NOT LOG_ID(\"externalaudit.googleapis.com/system_event\") "
          "AND NOT LOG_ID(\"cloudaudit.googleapis.com/access_transparency\") "
          "AND NOT LOG_ID(\"externalaudit.googleapis.com/access_transparency\") ",
          "exclusions": [
             {
                "name": "exclude-data-access",
                "description": "Prevents Data Access audit logs from being routed",
                "filter": "log_id(\"cloudaudit.googleapis.com/data_access\")",
             }
          ],
          "mode": OVERWRITE
          }
        }
        




The built-in inclusion filter for the `_Default` sink includes the statement `AND NOT LOG_ID("externalaudit.googleapis.com/activity")`, which prevents Admin Activity audit logs from being routed to the `_Default` log bucket. In the previous example, the inclusion filter is changed so that Admin Activity audit logs are routed to the `_Default` log bucket. The example also adds an exclusion filter named `exclude-data-access` that prevents Data Access audit logs from being routed to the `_Default` bucket.

## Troubleshoot configuration errors

For troubleshooting information, see [Troubleshoot CMEK and default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/routing/troubleshoot-cmek-orgs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
