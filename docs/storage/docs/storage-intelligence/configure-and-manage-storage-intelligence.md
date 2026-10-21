---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence/
title: Configure and manage Storage Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:10.129422+00:00
---

# Configure and manage Storage Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/configure-and-manage-storage-intelligence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Configure and manage Storage Intelligence Stay organized with collections  Save and categorize content based on your preferences. 

[Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview) provides insights into your storage usage patterns and helps you manage your data and infrastructure. These insights help you identify areas for cost optimization, performance improvements, and security or compliance enhancements. The service also provides support to relocate and process data. This guide explains how to configure, view, update, and disable Storage Intelligence for your [resource](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#resource).

## Required roles

To get the permissions that you need to configure and manage Storage Intelligence, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to configure and manage Storage Intelligence. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure and manage Storage Intelligence:

  * Configure Storage Intelligence: `storage.intelligenceConfigs.update`
  * View a Storage Intelligence configuration: `storage.intelligenceConfigs.get`
  * Update a Storage Intelligence configuration: `storage.intelligenceConfigs.update`
  * Disable Storage Intelligence: `storage.intelligenceConfigs.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure Storage Intelligence

**Note:** To avoid additional storage charges, delete or remove your past Storage Insights datasets when you configure Storage Intelligence.

### Console

  1. In the Google Cloud console, go to the Storage Intelligence **Configuration** page.

[Go to Configuration](https://console.cloud.google.com/storage/storage-intelligence/configuration)

  2. Click **Enable Storage Intelligence**.

  3. In the **Configure Storage Intelligence** dialog, select the [**resource**](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#resource) that you want to configure Storage Intelligence for.

  4. Click **Continue**.

  5. Optional: To include or exclude specific buckets in your Storage Intelligence configuration, do the following:

     1. To select buckets from specific [locations](https://docs.cloud.google.com/storage/docs/locations#location-r), use the **filter type** menu. To include or exclude buckets, select the location from the **location** menu. For more information, see [Filter by location](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-location).

     2. To select Cloud Storage buckets by name, use the **filter type** menu. To include or exclude buckets, specify the bucket name's regular expression and click **Add regular expression**. For more information, see [Filter by bucket name](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-name).

  6. Click **Enable this configuration**.




### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To configure Storage Intelligence, use the [`gcloud storage intelligence-configs enable`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/intelligence-configs/enable) command with one of the following flags:

     * `--project`: Configure Storage Intelligence for a project. The value is a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). For example, `my-project`.

     * `--sub-folder`: Configure Storage Intelligence for a folder. The value is a [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders). For example, `1234567890`.

     * `--organization`: Configure Storage Intelligence for an organization. The value is an [organization ID](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#benefits_of_the_organization_resource). For example, `9876546738`.

For example, the following command configures Storage Intelligence for a project called `my-project`:
           
           gcloud storage intelligence-configs enable --project=PROJECT_ID

Where PROJECT_ID is a project ID.

To [include or exclude specific buckets](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-name) in your Storage Intelligence configuration, use _any_ one of the following flags:

     * `--exclude-bucket-regexes`: List of bucket ID regexes to be excluded from the Storage Intelligence configuration.
     * `--include-bucket-regexes`: List of bucket ID regexes to be included in the Storage Intelligence configuration.

For example, to exclude all buckets that contain _colddata_ in their names, use the following command:
    
    gcloud storage intelligence-configs enable --organization=54343 --exclude-bucket-regexes=colddata.*

For example, to exclude buckets named _colddata_ , use the following command:
    
    gcloud storage intelligence-configs enable --organization=54343 --exclude-bucket-regexes=colddata

For example, to exclude buckets named _colour_ or _color_ , use the following command:
    
    gcloud storage intelligence-configs enable --organization=my-org --exclude-bucket-regexes=colou?r

To [include or exclude buckets based on their location](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-location) in your Storage Intelligence configuration, use _any_ one of the following flags:

     * `--exclude-locations`: List of locations to be excluded from the Storage Intelligence configuration.
     * `--include-locations`: List of locations to be included in the Storage Intelligence configuration.

For example:
    
    gcloud storage intelligence-configs enable --sub-folder=123456 --include-locations=us-east1,us-west1




### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file with the following details:

     1. `name`: The name of the Storage Intelligence configuration. Use any one of the following formats: 
        * Project: `projects/PROJECT_ID/locations/global/intelligenceConfig`
        * Folder: `folders/FOLDER_ID/locations/global/intelligenceConfig`
        * Organization: `organizations/ORGANIZATION_ID/locations/global/intelligenceConfig`

Where:

        * `PROJECT_ID` is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`
        * `FOLDER_ID` is the Google Cloud folder ID. Folder IDs are numeric, for example, `123456789012`
        * `ORGANIZATION_ID` is the Google Cloud organization ID. Organization IDs are numeric, for example, `123456789012`
     2. Configure the `editionConfig` field. For more information, see [Edition configuration](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#edition-configuration).
     3. Optional: Configure the `filter` object. You can include or exclude buckets based on [Cloud Storage locations](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-location) and [bucket ID regular expressions](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-name).
    
    {
          "name":"projects/PROJECT_ID/locations/global/intelligenceConfig",
          "editionConfig":"EDITION_CONFIGURATION",
          "filter":{
            "includedCloudStorageBuckets":{
                "bucketIdRegexes":[
                  "INCLUDED_BUCKET_ID_REGEX",
                    ...]
            },
            "excludedCloudStorageBuckets":{
                "bucketIdRegexes":[
                  "EXCLUDED_BUCKET_ID_REGEX",
                    ...]
            },
            "includedCloudStorageLocations":{
                "locations":[
                  "INCLUDED_BUCKET_LOCATION",
                    ...]
            },
            "excludedCloudStorageLocations":{
                "locations":[
                  "EXCLUDED_BUCKET_LOCATION",
                    ...]
            }
          }
        }
      

Where:

     * `PROJECT_ID` is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`.
     * `EDITION_CONFIGURATION` is the Storage Intelligence [edition configuration](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#edition-configuration).
     * Optional:`INCLUDED_BUCKET_ID_REGEX` is a regular expression that specifies which bucket IDs to include. You can specify one or multiple regular expressions as a list.
     * Optional: `EXCLUDED_BUCKET_ID_REGEX` is a regular expression that specifies which bucket IDs to exclude. You can specify one or multiple regular expressions as a list.
     * Optional: `INCLUDED_BUCKET_LOCATION` is the [location](https://docs.cloud.google.com/storage/docs/locations) where you want to include buckets in the Storage Intelligence configuration. You can specify one or multiple locations as a list.
     * Optional: `EXCLUDED_BUCKET_LOCATION` is the location where you want to exclude buckets from the Storage Intelligence configuration. You can specify one or multiple locations as a list.
  3. The following sections describe how to use the REST API to configure [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview) for a project, a folder, or an organization. You can also use the REST API to configure the [Storage Intelligence 30-day introductory trial](https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/configure-and-manage-trial). Configure Storage Intelligence or the Storage Intelligence 30-day introductory trial using _any_ one of the following methods.

#### Configure Storage Intelligence for a project

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [configure Storage Intelligence for a project](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/projects.locations/updateIntelligenceConfig).
         
         curl -X POST \
             --data-binary @JSON_FILE_NAME \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/intelligenceConfig?updateMask=UPDATE_MASK"
         

Where:

     * `PROJECT_ID` is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`
     * `UPDATE_MASK` is the comma-separated list of field names that this request updates. The fields use the [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format and are part of the [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig) resource.

#### Configure Storage Intelligence for a folder

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [configure Storage Intelligence for a folder](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/folders.locations/updateIntelligenceConfig).
    
    curl -X POST \
        --data-binary @JSON_FILE_NAME \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://storage.googleapis.com/v2/folders/FOLDER_ID/locations/global/intelligenceConfig?updateMask=UPDATE_MASK"
    

Where:

     * `FOLDER_ID` is the Google Cloud folder ID. Folder IDs are numeric, for example, `123456789012`
     * `UPDATE_MASK` is the comma-separated list of field names that this request updates. The fields use the [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format and are part of the [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig) resource.

#### Configure Storage Intelligence for an organization

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [configure Storage Intelligence for an organization](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/organizations.locations/updateIntelligenceConfig).
    
    curl -X POST \
      --data-binary @JSON_FILE_NAME \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://storage.googleapis.com/v2/organizations/ORGANIZATION_ID/locations/global/intelligenceConfig?updateMask=UPDATE_MASK"
    

Where:

     * `ORGANIZATION_ID` is the Google Cloud organization ID. Organization IDs are numeric, for example, `79293024087`
     * `UPDATE_MASK` is the comma-separated list of field names that this request updates. The fields use the [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format and are part of the [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig) resource.



## View a Storage Intelligence configuration

### Console

  1. In the Google Cloud console, go to the Storage Intelligence **Configuration** page.

[Go to Configuration](https://console.cloud.google.com/storage/storage-intelligence/configuration)

  2. Select the project picker at the top of the page.

  3. In the **Select a resource** dialog, select the [**resource**](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#resource) for which you want to view the Storage Intelligence configuration.




If a resource has Storage Intelligence configured, the **Status** field displays `Enabled`. For resources without Storage Intelligence configured, the **Configure Storage Intelligence** button appears.

### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To view the Storage Intelligence configuration for a resource, use the [`gcloud storage intelligence-configs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/intelligence-configs/describe) command with one of the following flags:

     * `--project`: View the Storage Intelligence configuration for a project. The value is a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). For example, `my-project`.

     * `--sub-folder`: View the Storage Intelligence configuration for a folder. The value is a [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders). For example, `1234567890`.

     * `--organization`: View the Storage Intelligence configuration for an organization. The value is an [organization ID](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#creating-managing-organization). For example, `9876546738`.

For example, the following command views the Storage Intelligence configuration for a project called `my-project`:
           
           gcloud storage intelligence-configs describe --project=PROJECT_ID

Where PROJECT_ID is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`.




### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. The methods for viewing the Storage Intelligence configuration for a resource are detailed in the following sections.

#### View the Storage Intelligence configuration for a project

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [view the Storage Intelligence configuration for a project](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/projects.locations/getIntelligenceConfig).
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/intelligenceConfig"
         

Where:

`PROJECT_ID` is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`.

#### View the Storage Intelligence configuration for a folder

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [view the Storage Intelligence configuration for a folder](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/folders.locations/getIntelligenceConfig).
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             "https://storage.googleapis.com/v2/folders/FOLDER_ID/locations/global/intelligenceConfig"
         

Where:

`FOLDER_ID` is the Google Cloud folder ID. Folder IDs are numeric, for example, `123456789012`.

#### View the Storage Intelligence configuration for an organization

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [view the Storage Intelligence configuration for an organization](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/organizations.locations/getIntelligenceConfig).
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             "https://storage.googleapis.com/v2/organizations/ORGANIZATION_ID/locations/global/intelligenceConfig"
         

Where:

`ORGANIZATION_ID` is the Google Cloud organization ID. Organization IDs are numeric, for example, `79293024087`.




## Update a Storage Intelligence configuration

### Console

  1. In the Google Cloud console, go to the Storage Intelligence **Configuration** page.

[Go to Configuration](https://console.cloud.google.com/storage/storage-intelligence/configuration)

  2. Select the project picker at the top of the page.

  3. In the **Select a resource** dialog, select the [**resource**](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#resource) for which you want to update the Storage Intelligence configuration.

  4. In the **Overview** section, modify any of the editable configuration options to meet your needs. For example, you can disable Storage Intelligence for a resource or change the [edition configuration](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#edition-configuration) to `Inherit from parent` or change the [bucket filters](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#bucket-filters).




### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To update the Storage Intelligence configuration for a resource, use the [`gcloud storage intelligence-configs update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/intelligence-configs/update) command with one of the following flags:

     * `--project`: Update the Storage Intelligence configuration for a project. The value is a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). For example, `my-project`.

     * `--sub-folder`: Update the Storage Intelligence configuration for a folder. The value is a [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders). For example, `1234567890`.

     * `--organization`: Update the Storage Intelligence configuration for an organization. The value is an [organization ID](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#creating-managing-organization). For example, `9876546738`.

For example, the following command updates the Storage Intelligence configuration for a project called `my-project`:
           
           gcloud storage intelligence-configs update --project=PROJECT_ID

Where PROJECT_ID is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`.




### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file with the following details:

     1. `name`: The name of the Storage Intelligence configuration. Use any one of the following formats: 
        * Project: `projects/PROJECT_ID/locations/global/intelligenceConfig`
        * Folder: `folders/FOLDER_ID/locations/global/intelligenceConfig`
        * Organization: `organizations/ORGANIZATION_ID/locations/global/intelligenceConfig`

Where:

        * `PROJECT_ID` is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`
        * `FOLDER_ID` is the Google Cloud folder ID. Folder IDs are numeric, for example, `123456789012`
        * `ORGANIZATION_ID` is the Google Cloud organization ID. Organization IDs are numeric, for example, `123456789012`
     2. Configure the `editionConfig` field. For more information, see [Edition configuration](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#edition-configuration).
     3. Optional: Configure the `filter` object. You can include or exclude buckets based on [Cloud Storage locations](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-location) and [bucket ID regular expressions](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#filter-by-name).
    
    {
          "name":"projects/PROJECT_ID/locations/global/intelligenceConfig",
          "editionConfig":"EDITION_CONFIGURATION",
          "filter":{
            "includedCloudStorageBuckets":{
                "bucketIdRegexes":[
                  "INCLUDED_BUCKET_ID_REGEX",
                    ...]
            },
            "excludedCloudStorageBuckets":{
                "bucketIdRegexes":[
                  "EXCLUDED_BUCKET_ID_REGEX",
                    ...]
            },
            "includedCloudStorageLocations":{
                "locations":[
                  "INCLUDED_BUCKET_LOCATION",
                    ...]
            },
            "excludedCloudStorageLocations":{
                "locations":[
                  "EXCLUDED_BUCKET_LOCATION",
                    ...]
            }
          }
        }
      

Where:

     * `PROJECT_ID` is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`.
     * `EDITION_CONFIGURATION` is the Storage Intelligence [edition configuration](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#edition-configuration).
     * Optional:`INCLUDED_BUCKET_ID_REGEX` is a regular expression that specifies which bucket IDs to include. You can specify one or multiple regular expressions as a list.
     * Optional: `EXCLUDED_BUCKET_ID_REGEX` is a regular expression that specifies which bucket IDs to exclude. You can specify one or multiple regular expressions as a list.
     * Optional: `INCLUDED_BUCKET_LOCATION` is the [location](https://docs.cloud.google.com/storage/docs/locations) where you want to include buckets in the Storage Intelligence configuration. You can specify one or multiple locations as a list.
     * Optional: `EXCLUDED_BUCKET_LOCATION` is the location where you want to exclude buckets from the Storage Intelligence configuration. You can specify one or multiple locations as a list.
  3. The following sections describe how to update the Storage Intelligence configuration for a project, folder, or an organization. Update the Storage Intelligence configuration using one of these methods.

#### Update the Storage Intelligence configuration for a project

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [update the Storage Intelligence configuration for a project](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/projects.locations/updateIntelligenceConfig).
         
         curl -X PATCH \
            --data-binary @JSON_FILE_NAME \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json" \
            "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/intelligenceConfig?updateMask=UPDATE_MASK"
         

Where:

     * `PROJECT_ID` is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`
     * `UPDATE_MASK` is the comma-separated list of field names that this request updates. The fields use the [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format and are part of the [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig) resource.

#### Update the Storage Intelligence configuration for a folder

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [update the Storage Intelligence configuration for a folder](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/folders.locations/updateIntelligenceConfig).
    
    curl -X PATCH \
       --data-binary @JSON_FILE_NAME \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -H "Content-Type: application/json" \
       "https://storage.googleapis.com/v2/folders/FOLDER_ID/locations/global/intelligenceConfig?updateMask=UPDATE_MASK"
    

Where:

     * `FOLDER_ID` is the Google Cloud folder ID. Folder IDs are numeric, for example, `123456789012`
     * `UPDATE_MASK` is the comma-separated list of field names that this request updates. The fields use the [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format and are part of the [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig) resource.

#### Update the Storage Intelligence configuration for an organization

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [update the Storage Intelligence configuration for an organization](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/organizations.locations/updateIntelligenceConfig).
    
    curl -X PATCH \
       --data-binary @JSON_FILE_NAME \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -H "Content-Type: application/json" \
       "https://storage.googleapis.com/v2/organizations/ORGANIZATION_ID/locations/global/intelligenceConfig?updateMask=UPDATE_MASK"
    

Where:

     * `ORGANIZATION_ID` is the Google Cloud organization ID. Organization IDs are numeric, for example, `79293024087`
     * `UPDATE_MASK` is the comma-separated list of field names that this request updates. The fields use the [FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format and are part of the [`IntelligenceConfig`](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig) resource.



## Disable Storage Intelligence

### Console

  1. In the Google Cloud console, go to the Storage Intelligence **Configuration** page.

[Go to Configuration](https://console.cloud.google.com/storage/storage-intelligence/configuration)

  2. Select the project picker at the top of the page.

  3. In the **Select a resource** dialog, select the [**resource**](https://docs.cloud.google.com/storage/docs/storage-intelligence/overview#resource) for which you want to disable Storage Intelligence.

  4. In the **Overview** section, click **Disable** next to the **Status** field.

  5. In the dialog that appears, enter **Disable** and then click **Disable**.




### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To disable the Storage Intelligence configuration for a resource, use the [`gcloud storage intelligence-configs disable`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/intelligence-configs/disable) command with one of the following flags:

     * `--project`: Disable the Storage Intelligence configuration for a project. The value is a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). For example, `my-project`.

     * `--sub-folder`: Disable the Storage Intelligence configuration for a folder. The value is a [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders). For example, `1234567890`.

     * `--organization`: Disable the Storage Intelligence configuration for an organization. The value is an [organization ID](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#creating-managing-organization). For example, `9876546738`.

For example, the following command disables the Storage Intelligence configuration for a project called `my-project`:
           
           gcloud storage intelligence-configs disable --project=PROJECT_ID

Where PROJECT_ID is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`.




### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. The methods to disable Storage Intelligence for a resource are detailed in the following sections.

#### Disable Storage Intelligence for a project

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [disable Storage Intelligence for a project](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/projects.locations/updateIntelligenceConfig).
         
         curl -X PATCH \
          -H "Content-Type: application/json" \
          -d '{
               "edition_config": "DISABLED"
              }' \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/v2/projects/PROJECT_ID/locations/global/intelligenceConfig?updateMask=edition_config"

Where:  
`PROJECT_ID` is the Google Cloud project ID. Project IDs are alphanumeric, for example, `my-project`.

#### Disable Storage Intelligence for a folder

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [disable Storage Intelligence for a folder](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/folders.locations/updateIntelligenceConfig).
         
         curl -X PATCH \
           -H "Content-Type: application/json" \
           -d '{
             "edition_config": "DISABLED"
           }' \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/v2/folders/FOLDER_ID/locations/global/intelligenceConfig?updateMask=edition_config"
         

Where:  
`FOLDER_ID` is the Google Cloud folder ID. Folder IDs are numeric, for example, `123456789012`.

#### Disable Storage Intelligence for an organization

Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) to [disable Storage Intelligence for an organization](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/organizations.locations/updateIntelligenceConfig).
         
         curl -X PATCH \
           -H "Content-Type: application/json" \
           -d '{
             "edition_config": "DISABLED"
           }' \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/v2/organizations/ORGANIZATION_ID/locations/global/intelligenceConfig?updateMask=edition_config"

Where:  
`ORGANIZATION_ID` is the Google Cloud organization ID. Organization IDs are numeric, for example, `79293024087`.




## What's next

  * Learn about [Storage Insights datasets](https://docs.cloud.google.com/storage/docs/insights/datasets).
  * Learn how to [get data insights with Gemini assistance](https://docs.cloud.google.com/storage/docs/analyze-data-gemini).
  * Learn about [inventory reports](https://docs.cloud.google.com/storage/docs/insights/inventory-reports).
  * Learn about [bucket relocation](https://docs.cloud.google.com/storage/docs/bucket-relocation/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
