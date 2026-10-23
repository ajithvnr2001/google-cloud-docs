---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job/
title: Send inspection results to Knowledge Catalog as aspects \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:38.106545+00:00
---

# Send inspection results to Knowledge Catalog as aspects  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Send inspection results to Knowledge Catalog as aspects Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to inspect a BigQuery table for sensitive data and send the inspection results to Knowledge Catalog. This action automatically adds an _aspect_ to the [Knowledge Catalog entry](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entries) that's associated with your BigQuery table.

This document also provides example queries that you can use to find data across your organization and projects with specific aspect values.

This feature is useful if you want to enrich your metadata in Knowledge Catalog with sensitive data classifications from Sensitive Data Protection inspection jobs.

The generated aspects include the following details:

  * The name of the inspection job
  * The information types ([_infoTypes_](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference)) that were detected in the table



## About Knowledge Catalog

[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview) provides a unified inventory of Google Cloud resources.

Knowledge Catalog lets you use _aspects_ to add business and technical metadata to your data to capture context and knowledge about your resources. You can then search and discover data across your organization and enable data governance over your data assets. For more information, see [Aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#aspects).

## How it works

To automatically create Knowledge Catalog aspects based on inspection job results, follow this high-level workflow:

  1. Create or edit an inspection job that inspects a BigQuery table. For instructions, see [Inspect a BigQuery table](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#inspect_a_table).

  2. In the **Add actions** step, enable **Publish to Knowledge Catalog**.




Sensitive Data Protection adds or updates the `Sensitive Data Protection job result` aspect of the [Knowledge Catalog entry](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entries) associated with the BigQuery table. You can then search Knowledge Catalog for all data in your organization or project with specific aspect values. For example queries, see Example search queries in this document.

The resulting Knowledge Catalog aspect is stored in the same project and region as the BigQuery table.

**Note:** When you enable the **Publish to Knowledge Catalog** action in an existing job trigger, Sensitive Data Protection applies this action to the job trigger's new inspection jobs only and not to past inspection jobs.

## Aspect fields

The `Sensitive Data Protection job result` aspect has the following fields:

Job Name
    The full resource name of the inspection job—for example, `projects/example-project/locations/us/dlpJobs/i-8992079400000000000`.
InfoType Counts
    InfoType names that the inspection job searched for—as specified in the inspection configuration—and the count of findings for each infoType. An infoType that has no findings has a count of `0`.
End Time
    The date and time that the inspection job ended.
Is Full Scan
    Whether the inspection job scanned all the rows in the table. If sampling is enabled in the inspection job, for example, then the value of this field is `False`.
Has Findings
    Whether the inspection job detected any of the infoTypes that it scanned for.

## Enable the Dataplex API

The Dataplex API must be enabled in each project that contains data that you want to add aspects for. This section describes how to enable the Dataplex API in a single project or in all projects in an organization or folder.

### Enable the Dataplex API in a single project

  1. Select the project in which you want to enable the Dataplex API.

[Go to project selector](https://console.cloud.google.com/projectselector2)

  2. Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)




### Enable the Dataplex API in all projects in an organization or folder

This section provides a script that searches for all projects in an organization or folder and enables the Dataplex API in each of those projects.

To get the permissions that you need to enable the Dataplex API in all projects in an organization or folder, ask your administrator to grant you the following IAM roles: 

  * [Cloud Asset Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`) on the organization or folder
  * [DLP User ](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.user) (`roles/dlp.user`) on each project in which you want to enable the Dataplex API



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to enable the Dataplex API in all projects in an organization or folder. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to enable the Dataplex API in all projects in an organization or folder:

  * To search for all projects in an organization or folder: `cloudasset.assets.searchAllResources` on the organization or folder 
  * To enable the Dataplex API: `serviceusage.services.use` on each project in which you want to enable the Dataplex API 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To enable the Dataplex API in all projects in an organization or folder, follow these steps:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following script:
         
         #!/bin/bash
         
         RESOURCE_ID="RESOURCE_ID"
         
         gcloud asset search-all-resources \
             --scope="RESOURCE_TYPE/$RESOURCE_ID" \
             --asset-types="cloudresourcemanager.googleapis.com/Project" \
             --format="value(name)" |
             while read project_name; do
               project_id=$(echo "$project_name" | sed 's|.*/||')
               gcloud services enable "dataplex.googleapis.com" --project="$project_id"
             done
         

Replace the following:

     * `RESOURCE_ID`: the organization number or folder number of the resource that contains the projects
     * `RESOURCE_TYPE`: the type of the resource that contains the projects—`organizations` or `folders`



## Roles and permissions for viewing aspects

To get the permissions that you need to search for aspects associated with your BigQuery table, ask your administrator to grant you the following IAM roles on the table: 

  * [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`)
  * [BigQuery Data Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataViewer) (`roles/bigquery.dataViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to search for aspects associated with your BigQuery table. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to search for aspects associated with your BigQuery table:

  * View Knowledge Catalog entries: 
    * `dataplex.entries.list`
    * `dataplex.entries.get`
  * View BigQuery datasets and tables: 
    * `bigquery.datasets.get`
    * `bigquery.tables.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about the permissions required to use Knowledge Catalog, see [Knowledge Catalog IAM permissions](https://docs.cloud.google.com/dataplex/docs/iam-permissions).

## Configure and run a Sensitive Data Protection inspection job

You can configure and run a Sensitive Data Protection inspection job by using the Google Cloud console or the DLP API.

### Console

  1. In the Google Cloud console, go to the **Create job or job trigger** page.

[Go to Create job or job trigger](https://console.cloud.google.com/security/sensitive-data-protection/create/job;source=7)

  2. Select your project.
  3. Enter the required inspection job details and the details of the BigQuery table that you want to inspect. For instructions, see [Inspect a BigQuery table](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#inspect_a_table). For a full list of information types that Sensitive Data Protection can inspect for, see [InfoType detector reference](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference).
  4. For **Add actions** , enable **Publish to Knowledge Catalog**.
  5. Click **Create**. The job runs immediately.



### REST

The following example sends a [`projects.locations.dlpJobs.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/create) request to inspect a BigQuery table and send the results to Knowledge Catalog.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID. Project IDs are alphanumeric strings 
  * `LOCATION`: the region or multi-region where you want to process the request—for example, `europe-west1` or `us`. For available locations, see [Sensitive Data Protection locations](https://docs.cloud.google.com/sensitive-data-protection/docs/locations). 
  * `BIGQUERY_DATASET_NAME`: name of the BigQuery dataset that contains the table to inspect 
  * `BIGQUERY_TABLE_NAME`: name of the BigQuery table to inspect 



HTTP method and URL: 
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/dlpJobs

Request JSON body: 
    
    
    {
                  "inspectJob":
                  {
                    "storageConfig":
                    {
                      "bigQueryOptions":
                      {
                        "tableReference":
                        {
                          "projectId": "PROJECT_ID",
                          "datasetId": "BIGQUERY_DATASET_NAME",
                          "tableId": "BIGQUERY_TABLE_NAME"
                        }
                      }
                    },
                    "inspectConfig":
                    {
                      "infoTypes":
                      [
                        {
                          "name": "EMAIL_ADDRESS"
                        },
                        {
                          "name": "PERSON_NAME"
                        },
                        {
                          "name": "US_SOCIAL_SECURITY_NUMBER"
                        },
                        {
                          "name": "PHONE_NUMBER"
                        }
                      ],
                      "includeQuote": true,
                      "minLikelihood": "UNLIKELY",
                      "limits":
                      {
                        "maxFindingsPerRequest": 100
                      }
                    },
                    "actions":
                    [
                      {
                        "publishFindingsToDataplexCatalog": {}
                      }
                    ]
                  }
                }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `inspect-request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @inspect-request.json \  
         "https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/dlpJobs"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `inspect-request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile inspect-request.json `  
        -Uri "https://dlp.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION/dlpJobs" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/dlpJobs/JOB_ID",
      "type": "INSPECT_JOB",
      "state": "PENDING",
      "inspectDetails": {
        "requestedOptions": {
          "snapshotInspectTemplate": {},
          "jobConfig": {
            "storageConfig": {
              "bigQueryOptions": {
                "tableReference": {
                  "projectId": "PROJECT_ID",
                  "datasetId": "BIGQUERY_DATASET_NAME",
                  "tableId": "BIGQUERY_TABLE_NAME"
                }
              }
            },
            "inspectConfig": {
              "infoTypes": [
                {
                  "name": "EMAIL_ADDRESS"
                },
                {
                  "name": "PERSON_NAME"
                },
                {
                  "name": "US_SOCIAL_SECURITY_NUMBER"
                },
                {
                  "name": "PHONE_NUMBER"
                }
              ],
              "minLikelihood": "UNLIKELY",
              "limits": {
                "maxFindingsPerRequest": 100
              },
              "includeQuote": true
            },
            "actions": [
              {
                "publishFindingsToDataplexCatalog": {}
              }
            ]
          }
        },
        "result": {}
      },
      "createTime": "2025-09-09T00:29:55.951374Z",
      "lastModified": "2025-09-09T00:29:58.022967Z"
    }
    

For information about how to get the inspection job results using the DLP API, see [Get a job](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#get-job).

## Example search queries

This section provides example search queries that you can use in Knowledge Catalog to find data in your organization or project with specific aspect values.

You can find only the data that you have access to. Data access is controlled through IAM permissions. For more information, see Roles and permissions for viewing aspects in this document.

You can enter these example queries in the **Search** field on the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

For information about how to form the queries, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

### Find the entries of all tables that have the Sensitive Data Protection job result aspect
    
    
    aspect:sensitive-data-protection-job-result
    

### Find the entries of inspected tables that have findings
    
    
    aspect:sensitive-data-protection-job-result.hasFindings=True
    

### Find the entries of inspected tables that have no findings
    
    
    aspect:sensitive-data-protection-job-result.hasFindings=False
    

### Find the entries of tables that were inspected fully

The following query returns the entries of tables that Sensitive Data Protection inspected row by row.
    
    
    aspect:sensitive-data-protection-job-result.isFullScan=True
    

### Find the entries of tables that weren't inspected fully

The following query returns the entries of tables that Sensitive Data Protection inspected through sampling.
    
    
    aspect:sensitive-data-protection-job-result.isFullScan=False
    

## Migrate to the Publish to Knowledge Catalog action

To migrate a job trigger that is configured to use the deprecated **Publish to Data Catalog** action, follow these steps:

  1. Edit the job trigger that is configured to publish inspection results to Data Catalog. For information about how to open and edit a job trigger, see [Update an existing job trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers#update_an_existing_job_trigger).
  2. Enable **Publish to Knowledge Catalog**.
  3. Click **Save**. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
