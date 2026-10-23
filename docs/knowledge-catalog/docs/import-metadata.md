---
url: https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata/
title: Import metadata using a custom pipeline \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:33.479696+00:00
---

# Import metadata using a custom pipeline  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import metadata using a custom pipeline Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to import metadata from a third-party system into Knowledge Catalog (formerly Dataplex Universal Catalog) by using the metadata import API methods and your own pipeline. Knowledge Catalog metadata consists of entries and their aspects.

If you instead want to use a Google Cloud-managed orchestration pipeline to extract and import metadata, we suggest using a [managed connectivity pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview). With a managed connectivity pipeline, you bring your own connector that extracts metadata and generates output in a format that can be used as input by the metadata import API methods (the metadata import file). Then, you use Workflows to orchestrate the pipeline tasks.

You can run the following kinds of metadata import jobs:

  * **Full sync of entries with incremental import of their aspects**. Supported for custom entries.
  * **Incremental import of aspects only**. Supported for aspects that belong to custom entries and system entries. For custom entries, you can modify both optional aspects and required aspects. For system entries, you can modify optional aspects.



## High-level steps

To import metadata using the metadata import API, follow these high-level steps:

  1. Determine the job scope.

Also, understand how Knowledge Catalog applies the comparison logic and the sync mode for entries and aspects.

  2. Create one or more metadata import files that define the data to import.

  3. Save the metadata import files in a Cloud Storage bucket.

  4. Run a metadata import job.




The steps on this page assume that you're familiar with Knowledge Catalog metadata concepts, including entry groups, entry types, and aspect types. For more information, see [About metadata in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).

## Before you begin

Before you import metadata, complete the tasks in this section.

### Required roles

To ensure that the [Knowledge Catalog service account](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control#service-accounts) has the necessary permissions to access the Cloud Storage bucket, ask your administrator to grant the Knowledge Catalog service account the **Storage Object Viewer** (`roles/storage.objectViewer`) IAM role and the `storage.buckets.get` permission on the bucket.

To get the permissions that you need to manage metadata import jobs, ask your administrator to grant you the following IAM roles: 

  * Modify entries and their aspects in a full entry sync metadata job: 
    * [**Dataplex Entry Type User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`) on the entry type or the project where the entry type is defined
    * [**Dataplex Aspect Type User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`) on the aspect type or the project where the aspect type is defined
  * Modify required aspects in an aspect-only metadata job: 
    * [**Dataplex Entry Type User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryTypeUser) (`roles/dataplex.entryTypeUser`) on the entry type or the project where the entry type is defined
    * [**Dataplex Aspect Type User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`) on the aspect type or the project where the aspect type is defined
  * Modify optional aspects in an aspect-only metadata job: [**Dataplex Aspect Type User** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser) (`roles/dataplex.aspectTypeUser`) on the aspect type or the project where the aspect type is defined. Note that when modifying optional aspects in an aspect-only metadata job, you don't need permissions for the associated entry type. 
  * Create metadata import jobs: 
    * [**Dataplex Entry Group Importer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupImporter) (`roles/dataplex.entryGroupImporter`) on the project or the resource
    * [**Dataplex Entry and EntryLink Owner** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`) on the project or the resource
  * View metadata jobs: [**Dataplex Metadata Job Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobViewer) (`roles/dataplex.metadataJobViewer`) on the project 
  * Create, view, and cancel metadata jobs: [**Dataplex Metadata Job Owner** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Create Google Cloud resources

Prepare the following Google Cloud resources:

  1. [Create entry groups](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-entry-group) for the entries that you want to import.
  2. [Create aspect types](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#create-aspect-type) for the aspects that you want to import.
  3. [Create entry types](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-entry-type) for the entries that you want to import.
  4. If you're running an aspect-only metadata job, [create entries](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-custom-entry) for the aspects that you want to import.
  5. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store your metadata import files.



## Components of a metadata import job

When you import metadata, consider the following components of a metadata job:

  * **Job scope** : the entry groups, entry types, and aspect types to include in the job.
  * **Sync mode** : how the entries and aspects in the job are updated.
  * **Metadata import file** : a file that defines the values to set for the entries and aspects in the job. You can provide multiple metadata import files in the same metadata job. You save the files in Cloud Storage.
  * **Comparison logic** : how Knowledge Catalog determines which entries and aspects to modify.



### Job scope

The job scope defines the entry groups, the entry types, and the aspect types that you want to include in a metadata import job. When you import metadata, you modify the entries and aspects that belong to resources within the job's scope.

To define the job scope, follow these guidelines:

  * **Entry groups** : specify one or more entry groups to include in the job. The job modifies only the entries and aspects that belong to these entry groups. The entry groups and the job must be in the same region.

  * **Entry types** : specify one or more entry types to include in the job. The job modifies only the entries and aspects that belong to these entry types. The location of an entry type must either match the location of the job, or the entry type must be global.

  * **Aspect types** : specify one or more aspect types to include in the job. The job modifies only the aspects that belong to these aspect types. The location of an aspect type must either match the location of the job, or the aspect type must be global.

**Note:** Importing aspects of type [`data-rules`](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules#data-rules-fields) and [`data-quality-rule-template`](https://docs.cloud.google.com/knowledge-catalog/docs/reuse-data-quality-rules#rule-template-fields) isn't supported from the metadata job.



The job scope must include all of the entry types and aspect types that you specify in the metadata import file.

You specify the job scope when you create a metadata job.

### Sync mode

The sync mode specifies how the entries and aspects in a metadata import job are updated. You provide a sync mode for both entries and aspects. Depending on what resources you want to import, the following combinations of sync modes are supported.

Goal | Entry sync mode | Aspect sync mode | Results  
---|---|---|---  
Import entries and their aspects | `FULL` | `INCREMENTAL` |  All entries in the job's scope are modified. If an entry exists in Knowledge Catalog but isn't included in the metadata import file, the entry is deleted when you run the metadata job. An aspect is modified only if the metadata import file includes a reference to the aspect in the `updateMask` field and the `aspectKeys` field. See Structure of an import item.  
Import aspects only | `NONE` | `INCREMENTAL` |  Aspects are modified if they are part of the job's scope, and if the metadata import file includes a reference to the aspects in the `aspectKeys` field. See Structure of an import item. Other metadata that belongs to entries in the job's scope isn't modified.  
  
You specify the sync mode when you create a metadata job.

### Metadata import file

The metadata import file is a collection of the entries and aspects that you want to modify. It defines the values to set for all of the fields that belong to these entries and aspects. You prepare the file before you run a metadata import job.

These general guidelines apply:

  * You can provide multiple metadata import files in the same metadata job.
  * When you run a full entry sync metadata job, the entries that you provide in the file completely replace all of the existing entries for any resources that are within the job's scope. This means that you must include values for all of the entries in a job, not just the values that you want to add or update. To get a list of the current entries in your project to use as a starting point, use the [`entries.list` API method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/list).

**Caution:** If an entry exists in Knowledge Catalog but isn't included in the metadata import file, the entry is deleted when you run the metadata job. If the metadata import file contains no data, all entries and aspects that belong to the job's scope are deleted.
  * You must provide a metadata import file as part of a metadata job. If you want to delete all existing data for the entries that are within the job's scope, provide an empty metadata import file.

  * All of the entries and aspects that you include in the file must belong to the entry groups, entry types, and aspect types that you define in the job's scope.




Use the detailed guidelines in the following sections to create a metadata import file.

#### Structure of the file

Each line in the metadata import file contains a JSON object that corresponds to one import item. An _import item_ is an object that describes the values to modify for an entry and its attached aspects.

You can provide multiple import items in a single metadata import file. However, don't provide the same import item more than once in a metadata job. Use a newline character (`0x0a`) to separate each import item.

A metadata import file with a newline character between each import item looks like the following example:
    
    
    { "entry": { "name": "entry 1", #Information about entry 1 }
    { "entry": { "name": "entry 2", #Information about entry 2 }
    

#### Structure of an import item

Each import item in the metadata import file can include the following fields (see [`ImportItem`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.ImportItem)). The following example is formatted with line breaks for readability, but when you save the file, include a newline character only after each import item. Don't include line breaks between the fields of a single import item.
    
    
    {
      "entry": {
        "name": "ENTRY_NAME",
        "entryType": "ENTRY_TYPE",
        "entrySource": {
          "resource": "RESOURCE",
          "system": "SYSTEM",
          "platform": "PLATFORM",
          "displayName": "DISPLAY_NAME",
          "description": "DESCRIPTION",
          "createTime": "ENTRY_CREATE_TIMESTAMP",
          "updateTime": "ENTRY_UPDATE_TIMESTAMP"
        },
        "aspects": {
          "ASPECT": {
            "data": {
              "KEY": "VALUE"
            },
            "aspectSource": {
              "createTime": "ASPECT_CREATE_TIMESTAMP",
              "updateTime": "ASPECT_UPDATE_TIMESTAMP"
            }
          },
          # Additional aspect maps
        },
        "parentEntry": "PARENT_ENTRY",
        "fullyQualifiedName": "FULLY_QUALIFIED_NAME"
      },
      "updateMask": "UPDATE_MASK_FIELDS",
      "aspectKeys": [
        "ASPECT_KEY",
        # Additional aspect keys
      ],
    }
    

Replace the following:

  * `entry`: information about an entry and its attached aspects. In an aspect-only metadata import job, Knowledge Catalog ignores all optional fields for an entry except for the aspect maps.

    * ENTRY_NAME: the relative resource name of the entry, in the format `projects/PROJECT_ID_OR_NUMBER/locations/LOCATION_ID/entryGroups/ENTRY_GROUP_ID/entries/ENTRY_ID`.
    * ENTRY_TYPE: the relative resource name of the entry type that was used to create this entry, in the format `projects/PROJECT_ID_OR_NUMBER/locations/LOCATION_ID/entryTypes/ENTRY_TYPE_ID`.
    * `entrySource`: information from the source system about the data resource that is represented by the entry: 
      * RESOURCE: the name of the resource in the source system.
      * SYSTEM: the name of the source system.
      * PLATFORM: the platform containing the source system.
      * DISPLAY_NAME: a user-friendly display name.
      * DESCRIPTION: a description of the entry.
      * ENTRY_CREATE_TIMESTAMP: the time the entry was created in the source system.
      * ENTRY_UPDATE_TIMESTAMP: the time the entry was updated in the source system.
    * `aspects`: the aspects that are attached to the entry. The `aspect` object and its data are called an aspect map.

      * ASPECT: an aspect that is attached to the entry. Depending on how the aspect is attached to the entry, use one of the following formats:

        * If the aspect is attached directly to the entry, provide the relative resource name of its aspect type, in the format `PROJECT_ID_OR_NUMBER.LOCATION_ID.ASPECT_TYPE_ID`.
        * If the aspect is attached to the entry's path, provide the aspect type's path, in the format `PROJECT_ID_OR_NUMBER.LOCATION_ID.ASPECT_TYPE_ID@PATH`.
      * KEY and VALUE: the content of the aspect, according to its aspect type metadata template. The content must be encoded as UTF-8. The maximum size of the field is 120 KB. The `data` dictionary is required, even if it is empty.

      * ASPECT_CREATE_TIMESTAMP: the time the aspect was created in the source system.

      * ASPECT_UPDATE_TIMESTAMP: the time the aspect was updated in the source system.

    * PARENT_ENTRY: the resource name of the parent entry.

    * FULLY_QUALIFIED_NAME: a name for the entry that can be referenced by an external system. See [Fully qualified names](https://docs.cloud.google.com/knowledge-catalog/docs/fully-qualified-names).

  * UPDATE_MASK_FIELDS: the fields to update, in paths that are relative to the `Entry` resource. Separate each field with a comma.

In a full entry sync job, Knowledge Catalog includes the paths of all of the fields for an entry that can be modified, including aspects. The `updateMask` field is ignored when an entry is created or re-created.

In an aspect-only metadata job, set this value to `aspects`.

  * ASPECT_KEY: the aspects to modify. Supports the following syntaxes:

    * `ASPECT_TYPE_REFERENCE`: matches the aspect type for aspects that are attached directly to the entry.
    * `ASPECT_TYPE_REFERENCE@PATH`: matches the aspect type and the specified path.
    * `ASPECT_TYPE_REFERENCE@*`: matches the aspect type for all paths.
    * `*@PATH`: matches all aspects types on the specified path.

Replace `ASPECT_TYPE_REFERENCE` with a reference to the aspect type, in the format `PROJECT_ID_OR_NUMBER.LOCATION_ID.ASPECT_TYPE_ID`.

In a full entry sync job, if you leave this field empty, it is treated as specifying exactly those aspects that are present within the specified entry. Knowledge Catalog implicitly adds the keys for all of the required aspects of an entry.




#### File requirements

The metadata import file has the following requirements:

  * The file must be formatted as a [JSON Lines](https://jsonlines.org/) file, which is a newline-delimited JSON file. Use a newline character (`0x0a`) to separate each import item.
  * The file must use UTF-8 character encoding.
  * Supported file extensions are `.jsonl` and `.json`.
  * The file size of each metadata import file must be less than 1 GiB. The maximum total size for all data in the metadata job is 3 GB. This includes all files and metadata associated with the job.
  * The entry types and aspect types that you specify in the file must be part of the metadata job's scope.
  * The file must be uploaded to a Cloud Storage bucket. Don't save the file in a folder named `CLOUD_STORAGE_URI/deletions/`.



### Comparison logic

Knowledge Catalog determines which entries and aspects to modify by comparing the values and timestamps that you provide in the metadata import file with the values and timestamps that exist in your project.

At a high level, Knowledge Catalog updates the values in your project when at least one proposed change in the metadata import file will change the state of your project when the job runs, without introducing out-of-date data. The proposed change must be referenced in the update mask field or the aspect keys field in the metadata import file.

The comparison logic varies depending on what kind of metadata import job you run.

#### Full entry sync job

In a full entry sync metadata job, for each entry that is part of the job's scope, Knowledge Catalog does one of the following things:

  * **Creates an entry and attached aspects**. If the metadata import file includes an entry that doesn't exist in your project, Knowledge Catalog creates the entry and attached aspects. 
  * **Deletes an entry and attached aspects**. If an entry exists in your project, but the metadata import file doesn't include the entry, Knowledge Catalog deletes the entry and its attached aspects from your project.
  * **Updates an entry and attached aspects**. If an entry exists in both the metadata import file and in your project, Knowledge Catalog evaluates the entry source timestamps and the aspect source timestamps that are associated with the entry to determine which values to modify. Then, Knowledge Catalog does one or more of the following things:

    * **Re-creates the entry**. If the entry source create timestamp in the metadata import file is more recent than the corresponding timestamp in your project, Knowledge Catalog re-creates the entry in your project.
    * **Updates the entry**. If the entry source update timestamp in the metadata import file is more recent than the corresponding timestamp in your project, Knowledge Catalog updates the entry in your project.
    * **Creates an aspect**. If an aspect doesn't exist in your project, and is included in an aspect map, the update mask field, and the aspect keys field in the metadata import file, Knowledge Catalog creates the aspect.
    * **Deletes an aspect**. If an aspect exists in your project, and is included in the update mask field and the aspect keys field in the metadata import file, but isn't included in an aspect map, Knowledge Catalog deletes the aspect.
    * **Updates an aspect**. If an aspect exists in your project and is included in an aspect map, the update mask field, and the aspect keys field in the metadata import file, and the aspect source update timestamp in the metadata import file is more recent than the corresponding timestamp in your project, Knowledge Catalog updates the aspect.

If an aspect source update timestamp isn't provided in the metadata import file, but the corresponding entry is marked for an update, Knowledge Catalog also updates the aspect.

However, if at least one aspect in the metadata import file has an older timestamp than the corresponding timestamp in your project, then Knowledge Catalog doesn't make any updates for the attached entry.




#### Aspect-only job

In an aspect-only metadata job, for each aspect that is part of the job's scope, Knowledge Catalog does one of the following things:

  * **Creates an aspect**. If an aspect doesn't exist in your project, and is included in an aspect map, the update mask field, and the aspect keys field in the metadata import file, Knowledge Catalog creates the aspect.
  * **Deletes an aspect**. For optional aspects, if the aspect exists in your project, and is included in the update mask field and the aspect keys field in the metadata import file, but isn't included in an aspect map, Knowledge Catalog deletes the aspect.

Required aspects can't be deleted.

  * **Updates an aspect**. If an aspect exists in your project and is included in an aspect map, the update mask field, and the aspect keys field in the metadata import file, and the aspect source update timestamp in the metadata import file is more recent than the corresponding timestamp in your project, Knowledge Catalog updates the aspect.

If an aspect source update timestamp isn't provided in the metadata import file, Knowledge Catalog also updates the aspect.

Knowledge Catalog updates aspects based on the aspect source update timestamp, regardless of the corresponding entry's entry source update timestamp.




## Create a metadata import file

Before you import metadata, create a metadata import file for your job. Follow these steps:

  1. Prepare a metadata import file by following the guidelines that are described previously in this document.
  2. [Upload the file to a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects).



You can provide multiple metadata import files in the same metadata job. To provide multiple files, save the files in the same Cloud Storage bucket. When run the job, you specify a bucket, not a specific file. Knowledge Catalog imports metadata from all of the files that are saved in the bucket, including files that are in subfolders.

## Run a metadata import job

After you create a metadata import file, run the metadata import job.

### REST

To import metadata, use the [`metadataJobs.create` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create).

Before using any of the request data, make the following replacements: 

  * PROJECT_NUMBER: your Google Cloud project number or project ID.
  * LOCATION_ID: the Google Cloud location, such as `us-central1`.
  * METADATA_JOB_ID: optional. The metadata job ID.
  * CLOUD_STORAGE_URI: the URI of the Cloud Storage bucket or folder that contains the metadata import files. For more information about the file requirements, see [Metadata import file](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#metadata-import-file).

  * ENTRY_GROUP: the relative resource name of the entry groups that are in scope for the job, in the format `projects/PROJECT_ID_OR_NUMBER/locations/LOCATION_ID/entryGroups/ENTRY_GROUP_ID`. For more information, see [Job scope](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#job-scope). 
  * ENTRY_TYPE: the relative resource name of an entry type that is in scope for the job, in the format `projects/PROJECT_ID_OR_NUMBER/locations/LOCATION_ID/entryTypes/ENTRY_TYPE_ID`. For more information, see [Job scope](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#job-scope). 

  * ASPECT_TYPE: the relative resource name of an aspect type that is in scope for the job, in the format `projects/PROJECT_ID_OR_NUMBER/locations/LOCATION_ID/aspectTypes/ASPECT_TYPE_ID`. Optional when creating a full entry sync job, required when creating an aspect-only job. For more information, see [Job scope](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#job-scope). 
  * ENTRY_SYNC_MODE: the entry sync mode, such as `FULL` or `NONE`. For more information, see [Sync mode](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#sync-mode). 
  * LOG_LEVEL: the level of logs to capture, such as `INFO` or `DEBUG`. For more information, see [View job logs and troubleshoot](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#troubleshoot-logs). 



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/TARGET_PROJECT_NUMBER/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID

Request JSON body: 
    
    
    {
      "type": "IMPORT",
      "import_spec": {
        "source_storage_uri": "gs://CLOUD_STORAGE_URI/",
        "scope": {
          "entryGroups": [
            "ENTRY_GROUP"
          ],
          "entry_types": [
            "ENTRY_TYPE"
          ],
          "aspect_types": [
            "ASPECT_TYPE"
          ]
        },
        "entry_sync_mode": "ENTRY_SYNC_MODE",
        "aspect_sync_mode": "INCREMENTAL",
        "log_level": "LOG_LEVEL"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/TARGET_PROJECT_NUMBER/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/TARGET_PROJECT_NUMBER/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID" | Select-Object -Expand Content

The response identifies a long-running operation.

## Get details about a metadata job

To get information about a metadata job, such as the status of the job and the number of entries that were modified, use the following steps. For more information about how to troubleshoot a failed job, see the View job logs and troubleshoot section of this document.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for GetMetadataJob</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void GetMetadataJobRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [GetMetadataJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetMetadataJobRequest.html) request = new [GetMetadataJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.GetMetadataJobRequest.html)
            {
                MetadataJobName = [MetadataJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataJobName.html).[FromProjectLocationMetadataJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataJobName.html#Google_Cloud_Dataplex_V1_MetadataJobName_FromProjectLocationMetadataJob_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[METADATAJOB]"),
            };
            // Make the request
            [MetadataJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataJob.html) response = catalogServiceClient.[GetMetadataJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_GetMetadataJob_Google_Cloud_Dataplex_V1_GetMetadataJobRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.GetMetadataJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#GetMetadataJobRequest.
    	}
    	resp, err := c.GetMetadataJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[GetMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataJobRequest.html);
    import com.google.cloud.dataplex.v1.[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob.html);
    import com.google.cloud.dataplex.v1.[MetadataJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJobName.html);
    
    public class SyncGetMetadataJob {
    
      public static void main(String[] args) throws Exception {
        syncGetMetadataJob();
      }
    
      public static void syncGetMetadataJob() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [GetMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataJobRequest.html) request =
              [GetMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetMetadataJobRequest.html).newBuilder()
                  .setName([MetadataJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJobName.html).of("[PROJECT]", "[LOCATION]", "[METADATAJOB]").toString())
                  .build();
          [MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob.html) response = catalogServiceClient.getMetadataJob(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the metadata job, in the format
     *  `projects/{project_id_or_number}/locations/{location_id}/metadataJobs/{metadata_job_id}`.
     */
    // const name = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callGetMetadataJob() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const response = await dataplexClient.getMetadataJob(request);
      console.log(response);
    }
    
    callGetMetadataJob();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_get_metadata_job():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[GetMetadataJobRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.GetMetadataJobRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_metadata_job](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_get_metadata_job)(request=request)
    
        # Handle the response
        print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the get_metadata_job call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#get_metadata_job.
    #
    def get_metadata_job
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::GetMetadataJobRequest.new
    
      # Call the get_metadata_job method.
      result = client.get_metadata_job request
    
      # The returned object is of type Google::Cloud::Dataplex::V1::MetadataJob.
      p result
    end

### REST

To get information about a metadata job, use the [`metadataJobs.get` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/get).

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: your Google Cloud project number or project ID.
  * `LOCATION_ID`: the Google Cloud location, such as `us-central1`.
  * `METADATA_JOB_ID`: the metadata job ID.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/TARGET_PROJECT_NUMBER/locations/LOCATION_ID/metadataJobs/METADATA_JOB_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/TARGET_PROJECT_NUMBER/locations/LOCATION_ID/metadataJobs/METADATA_JOB_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/TARGET_PROJECT_NUMBER/locations/LOCATION_ID/metadataJobs/METADATA_JOB_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/123456789012/locations/us-central1/metadataJobs/my-metadata-job",
      "uid": "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d",
      "createTime": "2026-07-17T16:30:15Z",
      "updateTime": "2026-07-17T16:35:15Z",
      "type": "IMPORT",
      "importSpec": {
        "sourceStorageUri": "gs://my-bucket/",
        "scope": {
          "entryGroups": [
            "projects/123456789012/locations/us-central1/entryGroups/my-entry-group"
          ],
          "entryTypes": [
            "projects/123456789012/locations/us-central1/entryTypes/my-entry-type"
          ],
          "aspectTypes": [
            "projects/123456789012/locations/us-central1/aspectTypes/my-aspect-type"
          ]
        },
        "entrySyncMode": "FULL",
        "aspectSyncMode": "INCREMENTAL",
        "logLevel": "INFO"
      },
      "status": {
        "state": "SUCCEEDED"
      },
      "importResult": {
        "deletedEntries": "2",
        "updatedEntries": "5",
        "createdEntries": "10",
        "unchangedEntries": "20",
        "updateTime": "2026-07-17T16:35:15Z"
      }
    }
    

## Get a list of metadata jobs

You can get a list of the most recent metadata jobs. Older jobs that have reached a terminal state are periodically deleted from the system.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using System;
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for ListMetadataJobs</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void ListMetadataJobsRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [ListMetadataJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListMetadataJobsRequest.html) request = new [ListMetadataJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListMetadataJobsRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                Filter = "",
                OrderBy = "",
            };
            // Make the request
            PagedEnumerable<ListMetadataJobsResponse, MetadataJob> response = catalogServiceClient.[ListMetadataJobs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_ListMetadataJobs_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Iterate over all response items, lazily performing RPCs as required
            foreach ([MetadataJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataJob.html) item in response)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
    
            // Or iterate over pages (of server-defined size), performing one RPC per page
            foreach ([ListMetadataJobsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ListMetadataJobsResponse.html) page in response.AsRawResponses())
            {
                // Do something with each page of items
                Console.WriteLine("A page of results:");
                foreach ([MetadataJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataJob.html) item in page)
                {
                    // Do something with each item
                    Console.WriteLine(item);
                }
            }
    
            // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
            int pageSize = 10;
            Page<MetadataJob> singlePage = response.ReadPage(pageSize);
            // Do something with the page of items
            Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
            foreach ([MetadataJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataJob.html) item in singlePage)
            {
                // Do something with each item
                Console.WriteLine(item);
            }
            // Store the pageToken, for when the next page is required.
            string nextPageToken = singlePage.NextPageToken;
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    	"google.golang.org/api/iterator"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.ListMetadataJobsRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#ListMetadataJobsRequest.
    	}
    	it := c.ListMetadataJobs(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// TODO: Handle error.
    		}
    		// TODO: Use resp.
    		_ = resp
    
    		// If you need to access the underlying RPC response,
    		// you can do so by casting the `Response` as below.
    		// Otherwise, remove this line. Only populated after
    		// first call to Next(). Not safe for concurrent access.
    		_ = it.Response.(*dataplexpb.ListMetadataJobsResponse)
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[ListMetadataJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataJobsRequest.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    import com.google.cloud.dataplex.v1.[MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob.html);
    
    public class SyncListMetadataJobs {
    
      public static void main(String[] args) throws Exception {
        syncListMetadataJobs();
      }
    
      public static void syncListMetadataJobs() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [ListMetadataJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataJobsRequest.html) request =
              [ListMetadataJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListMetadataJobsRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .setPageSize(883849137)
                  .setPageToken("pageToken873572522")
                  .setFilter("filter-1274492040")
                  .setOrderBy("orderBy-1207110587")
                  .build();
          for ([MetadataJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJob.html) element : catalogServiceClient.listMetadataJobs(request).iterateAll()) {
            // doThingsWith(element);
          }
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the parent location, in the format
     *  `projects/{project_id_or_number}/locations/{location_id}`
     */
    // const parent = 'abc123'
    /**
     *  Optional. The maximum number of metadata jobs to return. The service might
     *  return fewer jobs than this value. If unspecified, at most 10 jobs are
     *  returned. The maximum value is 1,000.
     */
    // const pageSize = 1234
    /**
     *  Optional. The page token received from a previous `ListMetadataJobs` call.
     *  Provide this token to retrieve the subsequent page of results. When
     *  paginating, all other parameters that are provided to the
     *  `ListMetadataJobs` request must match the call that provided the page
     *  token.
     */
    // const pageToken = 'abc123'
    /**
     *  Optional. Filter request. Filters are case-sensitive.
     *  The service supports the following formats:
     *  * `labels.key1 = "value1"`
     *  * `labels:key1`
     *  * `name = "value"`
     *  You can combine filters with `AND`, `OR`, and `NOT` operators.
     */
    // const filter = 'abc123'
    /**
     *  Optional. The field to sort the results by, either `name` or `create_time`.
     *  If not specified, the ordering is undefined.
     */
    // const orderBy = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callListMetadataJobs() {
      // Construct request
      const request = {
        parent,
      };
    
      // Run request
      const iterable = dataplexClient.[listMetadataJobsAsync](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/v1.catalogserviceclient.html)(request);
      for await (const response of iterable) {
          console.log(response);
      }
    }
    
    callListMetadataJobs();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_list_metadata_jobs():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[ListMetadataJobsRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListMetadataJobsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_metadata_jobs](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_list_metadata_jobs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the list_metadata_jobs call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#list_metadata_jobs.
    #
    def list_metadata_jobs
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::ListMetadataJobsRequest.new
    
      # Call the list_metadata_jobs method.
      result = client.list_metadata_jobs request
    
      # The returned object is of type Gapic::PagedEnumerable. You can iterate
      # over elements, and API calls will be issued to fetch pages as needed.
      result.each do |item|
        # Each element is of type ::Google::Cloud::Dataplex::V1::MetadataJob.
        p item
      end
    end

### REST

To get a list of the most recent metadata jobs, use the [`metadataJobs.list` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/list).

## Cancel a metadata job

You can cancel a metadata job that you don't want to run.

**Caution:** If you cancel a metadata import job that is in progress, the changes in the job might be partially applied. We recommend that you reset the state of the entry groups in your project by running another metadata job that reverts the changes from the canceled job.

### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    
    public sealed partial class GeneratedCatalogServiceClientSnippets
    {
        /// <summary>Snippet for CancelMetadataJob</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CancelMetadataJobRequestObject()
        {
            // Create client
            [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_Create)();
            // Initialize request argument(s)
            [CancelMetadataJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelMetadataJobRequest.html) request = new [CancelMetadataJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CancelMetadataJobRequest.html)
            {
                MetadataJobName = [MetadataJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataJobName.html).[FromProjectLocationMetadataJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.MetadataJobName.html#Google_Cloud_Dataplex_V1_MetadataJobName_FromProjectLocationMetadataJob_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[METADATAJOB]"),
            };
            // Make the request
            catalogServiceClient.[CancelMetadataJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CatalogServiceClient.html#Google_Cloud_Dataplex_V1_CatalogServiceClient_CancelMetadataJob_Google_Cloud_Dataplex_V1_CancelMetadataJobRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewCatalogClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_CatalogClient_NewCatalogClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.CancelMetadataJobRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#CancelMetadataJobRequest.
    	}
    	err = c.CancelMetadataJob(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CancelMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelMetadataJobRequest.html);
    import com.google.cloud.dataplex.v1.[CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html);
    import com.google.cloud.dataplex.v1.[MetadataJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJobName.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncCancelMetadataJob {
    
      public static void main(String[] args) throws Exception {
        syncCancelMetadataJob();
      }
    
      public static void syncCancelMetadataJob() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html) catalogServiceClient = [CatalogServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CatalogServiceClient.html).create()) {
          [CancelMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelMetadataJobRequest.html) request =
              [CancelMetadataJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CancelMetadataJobRequest.html).newBuilder()
                  .setName([MetadataJobName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.MetadataJobName.html).of("[PROJECT]", "[LOCATION]", "[METADATAJOB]").toString())
                  .build();
          catalogServiceClient.cancelMetadataJob(request);
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The resource name of the job, in the format
     *  `projects/{project_id_or_number}/locations/{location_id}/metadataJobs/{metadata_job_id}`
     */
    // const name = 'abc123'
    
    // Imports the Dataplex library
    const {CatalogServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [CatalogServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callCancelMetadataJob() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const response = await dataplexClient.cancelMetadataJob(request);
      console.log(response);
    }
    
    callCancelMetadataJob();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_cancel_metadata_job():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CatalogServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CancelMetadataJobRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.CancelMetadataJobRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[cancel_metadata_job](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.catalog_service.CatalogServiceClient.html#google_cloud_dataplex_v1_services_catalog_service_CatalogServiceClient_cancel_metadata_job)(request=request)
    
    

### Ruby

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/dataplex/v1"
    
    ##
    # Snippet for the cancel_metadata_job call in the CatalogService service
    #
    # This snippet has been automatically generated and should be regarded as a code
    # template only. It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    # client as shown in https://cloud.google.com/ruby/docs/reference.
    #
    # This is an auto-generated example demonstrating basic usage of
    # Google::Cloud::Dataplex::V1::CatalogService::Client#cancel_metadata_job.
    #
    def cancel_metadata_job
      # Create a client object. The client can be reused for multiple calls.
      client = Google::Cloud::Dataplex::V1::CatalogService::Client.new
    
      # Create a request. To set request fields, pass in keyword arguments.
      request = Google::Cloud::Dataplex::V1::CancelMetadataJobRequest.new
    
      # Call the cancel_metadata_job method.
      result = client.cancel_metadata_job request
    
      # The returned object is of type Google::Protobuf::Empty.
      p result
    end

### REST

To cancel a metadata job, use the [`metadataJobs.cancel` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/cancel).

## View job logs and troubleshoot

Use Cloud Logging to view logs for a metadata job. For more information, see [Monitor Knowledge Catalog logs](https://docs.cloud.google.com/knowledge-catalog/docs/logging).

You configure the log level when you create a metadata job. The following log levels are available:

  * `INFO`: provides logs at the overall job level. Includes aggregate logs about import items, but doesn't specify which import item has an error.
  * `DEBUG`: provides detailed logs for each import item. Use debug-level logging to troubleshoot issues with specific import items. For example, use debug-level logging to identify resources that are missing from the job scope, entries or aspects that don't conform to the associated entry type or aspect type, or other misconfigurations with the metadata import file.

**Note:** Depending on the size of your metadata job and the number of logs that are generated, debug-level logging might incur additional costs. For more information, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).



## Validation errors

Knowledge Catalog validates the metadata import files against the current metadata in your project. If there is a validation issue, the job status might return one of the following states:

  * `FAILED`: happens when the metadata import file has an error. Knowledge Catalog doesn't import any metadata and the job fails. Examples of errors in the metadata import file include the following: 
    * An item in the file can't be parsed into a valid import item
    * An entry or aspect in the file belongs to an entry group, entry type, or aspect type that isn't part of the job's scope
    * The same entry name is specified more than once in the job
    * An aspect type that is specified in an aspect map or the aspect keys doesn't use the format PROJECT_ID_OR_NUMBER.LOCATION_ID.ASPECT_TYPE_ID@OPTIONAL_PATH
    * A required aspect is marked for deletion
  * `SUCCEEDED_WITH_ERRORS`: happens when the metadata import file can be successfully parsed, but importing an item in the file would cause an entry in your project to be in an inconsistent state. Knowledge Catalog ignores such entries, but imports the rest of the metadata from the file.



Use job logs to troubleshoot the error.

## What's next

  * [Search for data assets in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets)
  * [Manage aspects and enrich metadata](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata)
  * [Manage entries and ingest custom sources](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources)
  * [Export metadata](https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
