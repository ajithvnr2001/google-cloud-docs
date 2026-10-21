---
url: https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-entrylinks-json/
title: Import business glossaries and entry links using JSON files \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:03.633308+00:00
---

# Import business glossaries and entry links using JSON files  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-entrylinks-json/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import business glossaries and entry links using JSON files Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you bulk import glossaries, categories, terms, and entry links using the Dataplex API. You can use this process to migrate metadata from other cataloging tools or perform bulk updates to your existing glossaries.

## Before you begin

Before you start the import process, complete the following prerequisites:

### Create a Cloud Storage bucket

[Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to serve as a staging area where you upload JSON files for import.

### Required roles

To get the permissions that you need to import glossaries and entry links using JSON files, ask your administrator to grant you the following IAM roles: 

  * [Dataplex Metadata Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.metadataEditor) (`roles/dataplex.metadataEditor`) on the project
  * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the bucket containing your import files



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

To import glossaries and entry links, enable the Dataplex API in your project.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,cloudresourcemanager.googleapis.com,storage.googleapis.com)

## Import glossaries using JSON files

To import glossaries, categories, and terms by uploading JSON files to Cloud Storage, complete the following tasks.

### Create a target glossary

Create a target glossary to import metadata.
    
    
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl -X POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/glossaries?glossary_id=GLOSSARY_ID -d "$(cat<<EOF
    
    {
       "displayName": "DISPLAY_NAME",
       "description": "DESCRIPTION"
    }
    EOF
    )"

Replace the following:

  * `PROJECT_ID`: the project ID in which you're creating the glossary
  * `LOCATION_ID`: the location in which you want to create the glossary
  * `GLOSSARY_ID`: the glossary ID
  * `DISPLAY_NAME`: the display name of the glossary
  * `DESCRIPTION`: the description of the glossary



### Prepare JSON files

Create a newline-delimited JSON file with glossary, categories, and terms that you want to upload to the Cloud Storage bucket.

Use the following JSON schema to structure your import files:
    
    
       {"entry":{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID","entryType":"projects/dataplex-types/locations/global/entryTypes/glossary-category","aspects":{"dataplex-types.global.glossary-category-aspect":{"data":{}},"dataplex-types.global.overview":{"data":{"content":"CONTENT"}},"dataplex-types.global.contacts":{"data":{"identities":[{role: "steward", name: "CONTACT_DISPLAY_NAME", id: "CONTACT_EMAIL"}]}}},"parentEntry":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","entrySource":{"resource":"projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID","displayName":"CATEGORY_NAME","description":"CATEGORY_DESCRIPTION","ancestors":[{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary"}]}}}
       {"entry":{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM1_ID","entryType":"projects/dataplex-types/locations/global/entryTypes/glossary-term","aspects":{"dataplex-types.global.glossary-term-aspect":{"data":{}},"dataplex-types.global.overview":{"data":{"content":"TERM1_CONTENT"}},"dataplex-types.global.contacts":{"data":{"identities":[{role: "steward", name: "CONTACT_DISPLAY_NAME", id: "CONTACT_EMAIL"}]}}},"parentEntry":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","entrySource":{"resource":"projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM1_ID","displayName":"TERM1_DISPLAY_NAME","description":"TERM1_DESCRIPTION","ancestors":[{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary"},{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary-category"}]}}}
       {"entry":{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM2_ID","entryType":"projects/dataplex-types/locations/global/entryTypes/glossary-term","aspects":{"dataplex-types.global.glossary-term-aspect":{"data":{}},"dataplex-types.global.overview":{"data":{"content":"TERM1_CONTENT"}},"dataplex-types.global.contacts":{"data":{"identities":[{role: "steward", name: "CONTACT_DISPLAY_NAME", id: "CONTACT_EMAIL"}]}}},"parentEntry":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","entrySource":{"resource":"projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/terms/TERM2_ID","displayName":"TERM2_DISPLAY_NAME","description":"TERM2_DESCRIPTION","ancestors":[{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary"},{"name":"projects/PROJECT_NUMBER/locations/LOCATION_ID/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION_ID/glossaries/GLOSSARY_ID/categories/CATEGORY_ID","type":"projects/dataplex-types/locations/global/entryTypes/glossary-category"}]}}}

### Import glossary, categories, and terms

Import the glossary, categories, and terms into the Cloud Storage bucket:
    
    
    # Set GCURL alias
    alias gcurl='curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"'
    
    gcurl https://DATAPLEX_API/metadataJobs?metadata_job_id=JOB_ID -d "$(cat<<EOF
    {
       "type":"IMPORT",
       "import_spec":{
          "log_level":"DEBUG",
          "source_storage_uri":"gs://STORAGE_BUCKET/",
          "entry_sync_mode":"FULL",
          "aspect_sync_mode":"INCREMENTAL",
          "scope":{
             "glossaries": "GLOSSARY_NAME"
          }
       }
    }
    EOF
    )"

Replace `DATAPLEX_API` with the Dataplex API endpoint of the format `dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID`.

## Import entry links using JSON files

To bulk import entry links by uploading JSON files to Cloud Storage, complete the following tasks.

### Prepare JSON files

Create a newline-delimited JSON file with the entry links that you want to upload to the Cloud Storage bucket.

Use the following JSON schema to structure your import files:

Sample format for links between terms
    
    
       {"entryLink":{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entryLinks/el-import-0606e3f2-8206-4f3a-aba9-32c6196f6048","entryLinkType":"projects/dataplex-types/locations/global/entryLinkTypes/synonym","entryReferences":[{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-1"},{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-2"}]}}
       {"entryLink":{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entryLinks/el-import-2f7408e3-af3d-405d-81bb-861cf9ec5146","entryLinkType":"projects/dataplex-types/locations/global/entryLinkTypes/related","entryReferences":[{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-1"},{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-2"}]}}
       

Sample format for links between terms and data assets
    
    
       {"entryLink":{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entryLinks/el-import-0606e3f2-8206-4f3a-aba9-32c6196f6048","entryLinkType":"projects/dataplex-types/locations/global/entryLinkTypes/definition","entryReferences":[{"name":"projects/PROJECT_NUMBER/locations/global/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/global/glossaries/import-glossary/terms/term-1"},{"name":"projects/PROJECT_NUMBER/locations/us-central1/entryGroups/entry-group-1/entries/entry-1"}]}}
       

### Import links between terms as synonym or related terms

To initiate a metadata import job that establishes `synonym` or `related` connections between your catalog terms, use the following command:
    
    
    gcurl https://DATAPLEX_API/metadataJobs?metadata_job_id=JOB_ID -d "$(cat<<EOF
       {
          "type":"IMPORT",
          "import_spec":{
             "log_level":"DEBUG",
             "source_storage_uri":"gs://STORAGE_BUCKET/",
             "entry_sync_mode":"FULL",
             "aspect_sync_mode":"INCREMENTAL",
             "scope":{
                "entry_groups":[  "projects/PROJECT_ID/locations/LOCATION_ID/entryGroups/@dataplex"
                ],
                "entry_link_types":[
                   "projects/dataplex-types/locations/global/entryLinkTypes/synonym",
                   "projects/dataplex-types/locations/global/entryLinkTypes/related"
                ],
                "referenced_entry_scopes":[
                   "PROJECT_IDS"
                ]
             }
          }
       }
    EOF
    )"

Replace `DATAPLEX_API` with `dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID`.

### Import links between terms and specific data assets or columns

To create a link between glossary terms and data assets, run the import job for each entry group to which the entry for the data asset belongs. All definition entry links are created in this entry group.

**Note:** Make sure the import file in the Cloud Storage bucket contains a file for links in one entry group. To create a link between a term and entry for the data asset in another entry group, provide a new file in the Cloud Storage bucket.
    
    
       gcurl https://DATAPLEX_API/metadataJobs?metadata_job_id=JOB_ID -d "$(cat<<EOF
       {
       "type":"IMPORT",
       "import_spec":{
          "log_level":"DEBUG",
          "source_storage_uri":"gs://STORAGE_BUCKET/",
          "entry_sync_mode":"FULL",
          "aspect_sync_mode":"INCREMENTAL",
          "scope":{
             "entry_groups":[  "projects/PROJECT_ID/locations/ENTRY_GROUP_LOCATION_ID/entryGroups/@dataplex"
             ],
             "entry_link_types":[
                "projects/dataplex-types/locations/global/entryLinkTypes/definition"
             ],
             "referenced_entry_scopes":[
                "PROJECT_IDS"
             ]
          }
       }
       }
    EOF
    )"

Replace `DATAPLEX_API` with `dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID`.

## Monitor the import job status

  1. To get the status of the `import` operation, run the following command:
         
         gcurl https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/operations/operation-OPERATION_ID

Replace `OPERATION_ID` with the ID of the operation.

  2. To get the status of the metadata job, run the following command:
         
         gcurl -X GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/metadataJobs/JOB_ID




## What's next

  * Learn how to [manage business glossaries in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).
  * Learn how to [import glossaries from a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-sheets).
  * Learn more about [metadata management](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
