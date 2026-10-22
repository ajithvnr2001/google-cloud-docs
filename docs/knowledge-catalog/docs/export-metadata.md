---
url: https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata/
title: Export metadata \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:24.459154+00:00
---

# Export metadata  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Export metadata Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you export metadata for use in external systems by using a metadata export job. You can then analyze this metadata with tools such as BigQuery, programmatically process large volumes, or integrate it with custom applications.

This document assumes that you're familiar with [Knowledge Catalog metadata concepts](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview), including entry groups, entry types, and aspect types.

## Job scope

The job scope defines the metadata to export. You must provide one of the following job scopes for each metadata export job:

  * **Organization** : exports the metadata that belongs to your organization.
  * **Projects** : exports the metadata that belongs to the specified projects.
  * **Entry groups** : exports the metadata that belongs to the specified entry groups.



You can further restrict the scope by specifying the entry types or aspect types to include in the job. The job exports only the entries and aspects that belong to these entry types and aspect types.

## VPC Service Controls

Knowledge Catalog uses [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to provide additional security for metadata export jobs. The project that the job belongs to determines the VPC Service Controls perimeter, as follows:

  * If you set the job scope to the organization level, the following things happen: 
    * The export scope is the organization that the job belongs to.
    * Only the entries that are within the VPC Service Controls perimeter are exported.
    * Any projects that are within the job's organization but outside the VPC Service Controls perimeter are excluded.
  * If you set the job scope to projects or entry groups, the projects or entry groups must be in the same VPC Service Controls perimeter as the job. If any of the projects or entry groups violate VPC Service Controls rules, the job fails.



## Before you begin

Before you export metadata, complete the tasks in this section.

### Required roles for end users

To get the permissions that you need to manage metadata export jobs, ask your administrator to grant you the following IAM roles: 

  * Create metadata export jobs: 
    * [Dataplex Entry Group Exporter ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryGroupExporter) (`roles/dataplex.entryGroupExporter`) on the organization, the projects, or the entry groups to export
    * [Dataplex Metadata Job Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`) on the project that you run the metadata job in
  * Access the exported results: [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the project or the bucket 
  * View metadata jobs: [Dataplex Metadata Job Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataJobViewer) (`roles/dataplex.metadataJobViewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage metadata export jobs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage metadata export jobs:

  * Export metadata: 
    * `dataplex.metadataJobs.create`
    * `dataplex.entryGroups.export`
    * `dataplex.entryGroups.get`
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.list`
  * Access the exported results: `storage.objects.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required roles for the Knowledge Catalog service account

To ensure that the [Knowledge Catalog service account](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control#service-accounts) has the necessary permissions to access the Cloud Storage bucket, ask your administrator to grant the Knowledge Catalog service account the following permissions on the bucket: `storage.buckets.get`, `storage.objects.get`, and `storage.objects.create`.

### Configure Google Cloud resources

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store the exported results.

The bucket must be in the same [location](https://docs.cloud.google.com/knowledge-catalog/docs/locations) and the same VPC Service Controls perimeter as the metadata job.




## Run a metadata export job

The following sections show how to export metadata with different job scopes.

### Export metadata from your organization

To export the metadata from your organization, use the [`metadataJobs.create` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create) and set the `organizationLevel` boolean to `true`.

Before using any of the request data, make the following replacements: 

  * `JOB_PROJECT`: the Google Cloud project that you run the metadata job in. Provide a project number or project ID.
  * `LOCATION_ID`: the Google Cloud location, such as `us-central1`.
  * `METADATA_JOB_ID`: optional. The metadata job ID.
  * `BUCKET`: the Cloud Storage bucket to export the metadata to.

Optionally, you can include a custom prefix after the bucket name, in the format `gs://BUCKET/PREFIX/`. The maximum length of the custom prefix is 128 characters.




HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID

Request JSON body: 
    
    
    {
      "type": "EXPORT",
      "export_spec": {
        "output_path": "gs://BUCKET/",
        "scope": {
          "organizationLevel": true,
        },
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
         "https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID"

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
        -Uri "https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID" | Select-Object -Expand Content

The response identifies a long-running operation. The exported metadata is saved to a Cloud Storage bucket.

### Export metadata from specific projects

To export metadata from one or more projects, use the [`metadataJobs.create` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create) and provide a list of projects.

Before using any of the request data, make the following replacements: 

  * `JOB_PROJECT`: the Google Cloud project that you run the metadata job in. Provide a project number or project ID.
  * `LOCATION_ID`: the Google Cloud location, such as `us-central1`.
  * `METADATA_JOB_ID`: optional. The metadata job ID.
  * `BUCKET`: the Cloud Storage bucket to export the metadata to.

Optionally, you can include a custom prefix after the bucket name, in the format `gs://BUCKET/PREFIX/`. The maximum length of the custom prefix is 128 characters.

  * `METADATA_SOURCE_PROJECT`: a project whose metadata you want to export. Provide a project number or project ID. The project must be in the same organization and VPC Service Controls perimeter as the metadata job.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID

Request JSON body: 
    
    
    {
      "type": "EXPORT",
      "export_spec": {
        "output_path": "gs://BUCKET/",
        "scope": {
          "projects": [
            "projects/METADATA_SOURCE_PROJECT",
            # Additional projects
          ],
        },
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
         "https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID"

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
        -Uri "https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID" | Select-Object -Expand Content

The response identifies a long-running operation. The exported metadata is saved to a Cloud Storage bucket.

### Export metadata from specific entry groups

To export metadata from specific entry groups, use the [`metadataJobs.create` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create) and provide a list of entry groups.

Before using any of the request data, make the following replacements: 

  * `JOB_PROJECT`: the Google Cloud project that you run the metadata job in. Provide a project number or project ID.
  * `LOCATION_ID`: the Google Cloud location, such as `us-central1`.
  * `METADATA_JOB_ID`: optional. The metadata job ID.
  * `BUCKET`: the Cloud Storage bucket to export the metadata to.

Optionally, you can include a custom prefix after the bucket name, in the format `gs://BUCKET/PREFIX/`. The maximum length of the custom prefix is 128 characters.

  * `ENTRY_GROUP`: the relative resource name of an entry group that is in scope for the job, in the format `projects/PROJECT_ID_OR_NUMBER/locations/LOCATION_ID/entryGroups/ENTRY_GROUP_ID`. The entry group must be in the same project as the metadata job. 



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID

Request JSON body: 
    
    
    {
      "type": "EXPORT",
      "export_spec": {
        "output_path": "gs://BUCKET/",
        "scope": {
          "entryGroups": [
            "ENTRY_GROUP",
            # Additional entry groups
          ],
        },
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
         "https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID"

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
        -Uri "https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID" | Select-Object -Expand Content

The response identifies a long-running operation. The exported metadata is saved to a Cloud Storage bucket.

### Export metadata from specific entry types or aspect types

To export metadata from specific entry types or aspect types, set the primary job scope, such as at the organization level, as shown in the following example. Then, provide a list of entry types, aspect types, or both.

Before using any of the request data, make the following replacements: 

  * `ENTRY_TYPE`: optional. The relative resource name of an entry type that is in scope for the job, in the format `projects/PROJECT_ID_OR_NUMBER/locations/LOCATION_ID/entryTypes/ENTRY_TYPE_ID`. 

  * `ASPECT_TYPE`: optional. The relative resource name of an aspect type that is in scope for the job, in the format `projects/PROJECT_ID_OR_NUMBER/locations/LOCATION_ID/aspectTypes/ASPECT_TYPE_ID`. 



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID

Request JSON body: 
    
    
    {
      "type": "EXPORT",
      "export_spec": {
        "output_path": "gs://BUCKET/",
        "scope": {
          "organizationLevel": true,
          "entry_types": [
            "ENTRY_TYPE",
            # Additional entry types
          ],
          "aspect_types": [
            "ASPECT_TYPE",
            # Additional aspect types
          ]
        },
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
         "https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID"

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
        -Uri "https://dataplex.googleapis.com/v1/projects/JOB_PROJECT/locations/LOCATION_ID/metadataJobs?metadataJobId=METADATA_JOB_ID" | Select-Object -Expand Content

The response identifies a long-running operation. The exported metadata is saved to a Cloud Storage bucket.

## Get details about a metadata job

To get information about a metadata job, such as the status of the job and the number of entries that were exported, use the [`metadataJobs.get` method](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/get).

## Metadata export results

The metadata export job exports a snapshot of your Knowledge Catalog metadata at the time that the metadata job was created.

### Export file contents

The contents of the output file follow the same format as the [metadata import file](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#import-item) that is used for metadata import jobs. You can use the output file directly as the input for a metadata import job.

### Export file location

Knowledge Catalog saves the export result files to a Cloud Storage bucket as objects.

The object path for each output file is constructed by using the bucket name and custom prefix that you specified in the export job, followed by a system-generated path. The system-generated path is designed for integration with BigQuery. The object path uses the following format:
    
    
    gs://BUCKET/PREFIX/year=YYYY/month=MM/day=DD/consumer_project=JOB_PROJECT/job=METADATA_JOB_ID/project=METADATA_SOURCE_PROJECT/entry_group=ENTRY_GROUP/FILE_NUMBER.jsonl
    

Note the following:

  * The system-generated path starts with the standard Hive partition format for the export job's creation date. This format is supported by BigQuery. For more information, see [Loading externally partitioned data](https://docs.cloud.google.com/bigquery/docs/hive-partitioned-loads-gcs#load_hive_partitioned_data).
  * The `consumer_project` parameter is the project where you run the metadata export job. The `project` parameter is the project that contains the metadata that you're exporting.
  * You can reuse a metadata job ID if the previous job was deleted. However, when you delete a job, it doesn't delete the files that were exported by that job. This means that if you reuse a deleted job ID, you might see duplicate job IDs in the output file paths.
  * Each output file is named with a file number, which is an integer starting from `1`.

If a metadata export job contains a large number of entries, then the job splits the results into multiple files to limit the size of each output file. The maximum number of entries in each output file is 1,000,000.




#### Example output files

Here are example output files for a metadata export job that included multiple projects:
    
    
    gs://export-bucket/example-folder/year=2025/month=04/day=13/consumer_project=admin-project/job=example-job/**project=metadata-project-1** /entrygroup=entry-group-1/1.jsonl
    gs://export-bucket/example-folder/year=2025/month=04/day=13/consumer_project=admin-project/job=example-job/**project=metadata-project-2** /entrygroup=entry-group-1/1.jsonl
    gs://export-bucket/example-folder/year=2025/month=04/day=13/consumer_project=admin-project/job=example-job/**project=metadata-project-3** /entrygroup=entry-group-2/1.jsonl

Here are example output files for a metadata export job that contained a large entry group. The results for the entry group were split into multiple files.
    
    
    gs://export-bucket/example-folder/year=2025/month=04/day=13/consumer_project=admin-project/job=another-example-job/project=example-metadata-project/**entrygroup=big-entry-group/1**.jsonl
    gs://export-bucket/example-folder/year=2025/month=04/day=13/consumer_project=admin-project/job=another-example-job/project=example-metadata-project/**entrygroup=big-entry-group/2**.jsonl

## Analyze the exported metadata in BigQuery

If you want to analyze the exported metadata in BigQuery, you can create an external table for the exported metadata. Creating an external table lets you query the exported data without additional data loading or transformation. For example, you can count the number of entries by entry group, find entries that have specific aspects, or perform additional [analysis in BigQuery](https://docs.cloud.google.com/bigquery/docs/query-overview).

Do the following:

  * [Create an external table for Hive partitioned data](https://docs.cloud.google.com/bigquery/docs/external-data-cloud-storage#create-external-table-partitioned). Provide the following information:

    * **Select file from Cloud Storage bucket** : provide the path to the Cloud Storage folder that contains the exported metadata files. To include all files in the bucket, use the asterisk (`*`) wildcard. For example, `gs://export-bucket/example-folder/*`.
    * **File format** : select **JSONL (Newline delimited JSON)**.
    * Select the **Source data partitioning** checkbox, and then for **Select Source URI Prefix** , provide the Cloud Storage URI prefix for the BigQuery table to define partitions. For example, `gs://export-bucket/example-folder/`.
    * **Partition inference mode** : select the **Automatically infer types** option.
    * **Table type** : select the **External table** option.
    * **Schema** : click the **Edit as text** toggle, and then enter the following schema definition for the export files:
          
          [
            {
              "name": "entry",
              "type": "RECORD",
              "mode": "NULLABLE",
              "fields": [
                {
                  "mode": "NULLABLE",
                  "name": "name",
                  "type": "STRING"
                },
                {
                  "mode": "NULLABLE",
                  "name": "entryType",
                  "type": "STRING"
                },
                {
                  "mode": "NULLABLE",
                  "name": "createTime",
                  "type": "STRING"
                },
                {
                  "mode": "NULLABLE",
                  "name": "updateTime",
                  "type": "STRING"
                },
                {
                  "mode": "NULLABLE",
                  "name": "aspects",
                  "type": "JSON"
                },
                {
                  "mode": "NULLABLE",
                  "name": "parentEntry",
                  "type": "STRING"
                },
                {
                  "mode": "NULLABLE",
                  "name": "fullyQualifiedName",
                  "type": "STRING"
                },
                {
                  "mode": "NULLABLE",
                  "name": "entrySource",
                  "type": "RECORD",
                  "fields": [
                    {
                      "mode": "NULLABLE",
                      "name": "resource",
                      "type": "STRING"
                    },
                    {
                      "mode": "NULLABLE",
                      "name": "system",
                      "type": "STRING"
                    },
                    {
                      "mode": "NULLABLE",
                      "name": "platform",
                      "type": "STRING"
                    },
                    {
                      "mode": "NULLABLE",
                      "name": "displayName",
                      "type": "STRING"
                    },
                    {
                      "mode": "NULLABLE",
                      "name": "description",
                      "type": "STRING"
                    },
                    {
                      "mode": "NULLABLE",
                      "name": "labels",
                      "type": "JSON"
                    },
                    {
                      "mode": "REPEATED",
                      "name": "ancestors",
                      "type": "RECORD",
                      "fields": [
                        {
                          "mode": "NULLABLE",
                          "name": "name",
                          "type": "STRING"
                        },
                        {
                          "mode": "NULLABLE",
                          "name": "type",
                          "type": "STRING"
                        }
                      ]
                    },
                    {
                      "mode": "NULLABLE",
                      "name": "createTime",
                      "type": "STRING"
                    },
                    {
                      "mode": "NULLABLE",
                      "name": "updateTime",
                      "type": "STRING"
                    },
                    {
                      "mode": "NULLABLE",
                      "name": "location",
                      "type": "STRING"
                    }
                  ]
                }
              ]
            }
          ]
          




BigQuery creates an external table that contains the exported metadata. The table's schema includes an `entry` schema column, where each row represents one entry. For more information about the fields for an entry, see [`ImportItem`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rpc/google.cloud.dataplex.v1#google.cloud.dataplex.v1.ImportItem). The table's schema also contains the export file partitions, as described in the Export file location section of this document.

After you create the external table, you can [query the table using GoogleSQL syntax](https://docs.cloud.google.com/bigquery/docs/running-queries). For example, to query which entry types were exported, use the following statement:
    
    
    SELECT entry.entryType FROM `example-project.example-dataset.example-table` LIMIT 1000
    

## What's next

  * Learn how to [query BigQuery tables by using GoogleSQL syntax](https://docs.cloud.google.com/bigquery/docs/running-queries).
  * Import metadata into Knowledge Catalog by using a [managed connectivity pipeline](https://docs.cloud.google.com/knowledge-catalog/docs/managed-connectivity-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
