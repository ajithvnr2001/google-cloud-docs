---
url: https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-sheets/
title: Import business glossaries from a Google Sheet \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:01.178747+00:00
---

# Import business glossaries from a Google Sheet  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-sheets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import business glossaries from a Google Sheet Stay organized with collections  Save and categorize content based on your preferences. 

The glossary import utility lets you import glossaries, categories, and terms in bulk from a Google Sheet into Knowledge Catalog (formerly Dataplex Universal Catalog). You can use a spreadsheet to collaboratively curate, update, and standardize your business vocabulary at scale before uploading changes to your catalog.

## Before you begin

Before you import glossaries, complete the following prerequisites.

### Set up the service account

To run the import utility using a Google Sheet, you must set up a service account with the necessary permissions to access the Google Sheets API and impersonate your user credentials:

  1. Identify or create a service account.

Select an existing service account or create a new one in the project where you run the import utility. For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts). Note the service account email (for example, `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`).

  2. Configure service account impersonation.

To run the import utility script locally, your user account must have permission to impersonate the service account. Grant your user account the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`) on the service account.

For more information, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

  3. Grant the service account `Editor` access to the Google Sheet.

Open the Google Sheet you want to use for the import process, click **Share** , and add the service account email as an `Editor`. This permission enables the service account to read from or write data to your sheet.




### Create a Cloud Storage bucket

[Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to serve as a staging area for import files.

### Required roles

To ensure that the service account has the necessary permissions to import glossaries from a Google Sheet, ask your administrator to grant the following IAM roles to the service account: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Dataplex Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`) on the project
  * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) on the project
  * [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the project
  * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) on the Cloud Storage bucket



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

To import glossaries, enable the following APIs in your project:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,cloudresourcemanager.googleapis.com,storage.googleapis.com,sheets.googleapis.com)

### Set up the git repository

Clone the `dataplex-labs` repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/dataplex-labs.git
    cd dataplex-labs/dataplex-quickstart-labs/00-resources/scripts/python/business-glossary-import/dataplex-glossary/import

### Install dependencies

Install the required Python dependencies:
    
    
    pip3 install -r requirements.txt
    

If you encounter any issues with the package installation, [set up a new Python development environment](https://docs.cloud.google.com/python/docs/setup).

### Authenticate and configure service account impersonation

Initialize the Google Cloud CLI and authenticate using Application Default Credentials (ADC) with service account impersonation:
    
    
    # Set your service account email address
    SA_EMAIL="SERVICE_ACCOUNT_EMAIL"
    
    # Authenticate ADC using service account impersonation and required scopes
    gcloud auth application-default login \
      --impersonate-service-account="${SA_EMAIL}" \
      --scopes="https://www.googleapis.com/auth/spreadsheets"

Replace SERVICE_ACCOUNT_EMAIL with the service account email ID. For example:

`SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`

## Create and structure the Google Sheet for import

To successfully run a bulk import, you must create a new Google Sheet using a precise column schema so that the import utility can successfully parse and validate your metadata fields. Ensure that you have granted the service account `Editor` access to the Google Sheet.

The first row of the sheet must contain these exact, case-sensitive schema headers:

Field | Required or Optional | Description  
---|---|---  
`id` | Required | A unique identifier for the term or category within the glossary.  
`parent` | Optional | The ID of the parent category. If empty, the item is a root-level child of the glossary. Note that the referenced parent ID must exist in the sheet and must belong to a category.   
`display_name` | Required | The display name of the term or category.  
`description` | Optional | A brief description of the term or category.  
`overview` | Optional | A rich text description of the term or category (supports HTML tags).  
`type` | Required | The row type. Valid values are `TERM` or `CATEGORY`.  
`contact1_email` | Optional | Email address of the primary data steward for the term or category.  
`contact1_name` | Optional | Name of the primary data steward for the term or category.  
`contact2_email` | Optional | Email address of the secondary data steward for the term or category.  
`contact2_name` | Optional | Name of the secondary data steward for the term or category.  
`label1_key` | Optional | Key for the first assigned label.  
`label1_value` | Optional | Value for the first assigned label.  
`label2_key` | Optional | Key for the second assigned label.  
`label2_value` | Optional | Value for the second assigned label.  
**Note:** You can add multiple labels.

## Import glossary from the Google Sheet

After setting up your environment and preparing your Google Sheet, run the `glossary_import.py` script:
    
    
    python3 bg_import/dataplex-glossary/glossary_import.py
    

The `glossary_import` utility parses and validates data from a Google Sheet, converts it into a format compatible with the Knowledge Catalog [`CreateMetadataJob` API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create), and uploads it to a Cloud Storage bucket before triggering the import job. The import utility then prints the result of the `CreateMetadataJob` API execution directly to your terminal. Verify that the job status indicates success.

You can review the execution logs in the `logs/` directory in your local execution path. These logs help you audit the transfer process and identify skipped entries or formatting warnings.

## What's next

  * Learn how to [manage a business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).
  * Learn how to [import glossaries using JSON files](https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-entrylinks-json).
  * Learn how to [export glossaries to a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/export-glossaries-sheets).
  * Learn more about [metadata management](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
