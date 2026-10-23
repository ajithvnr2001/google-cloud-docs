---
url: https://docs.cloud.google.com/knowledge-catalog/docs/import-entrylinks-sheets/
title: Import entry links from a Google Sheet \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:27.262107+00:00
---

# Import entry links from a Google Sheet  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/import-entrylinks-sheets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import entry links from a Google Sheet Stay organized with collections  Save and categorize content based on your preferences. 

The entry link import utility lets you bulk import entry links from a Google Sheet into Knowledge Catalog (formerly Dataplex Universal Catalog). You can use a spreadsheet to define and update relationships between glossary terms and data assets at scale.

## Before you begin

Before you import entry links into Knowledge Catalog, complete the following prerequisites.

### Set up the service account

To run the import utility using Google Sheets, you must set up a service account with the necessary permissions to access the Google Sheets API and impersonate your user credentials:

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

To ensure that the service account has the necessary permissions to import entry links from a Google Sheet, ask your administrator to grant the following IAM roles to the service account: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Dataplex Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`) on the project
  * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) on the project
  * [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the project
  * [Storage Object Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectAdmin) (`roles/storage.objectAdmin`) on the Cloud Storage bucket
  * [Storage Object Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`) on the Cloud Storage bucket



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

To import entry links, enable the following APIs in your project:

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
    cd dataplex-glossary

If you encounter any issues with the package installation, [set up a new Python development environment](https://docs.cloud.google.com/python/docs/setup).

### Authenticate and configure service account impersonation

Initialize the Google Cloud CLI and authenticate using Application Default Credentials (ADC) with service account impersonation:
    
    
    # Set your service account email address
    SA_EMAIL="SERVICE_ACCOUNT_EMAIL"
    
    # Authenticate ADC using service account impersonation and required scopes
    gcloud init
    gcloud auth login
    gcloud auth application-default login \
      --impersonate-service-account="${SA_EMAIL}" \
      --scopes="https://www.googleapis.com/auth/spreadsheets"

Replace SERVICE_ACCOUNT_EMAIL with the service account email ID. For example:

`SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`

## Cross-project import requirements

To import entry links across multiple Google Cloud projects, ensure your configuration meets the following requirements before running the import utility:

  * Configure cross-project IAM permissions: The service account executing the import script must have sufficient permissions in all target projects.

  * Verify entry existence: The target entries must already exist in their respective Knowledge Catalog projects before you run the import.

  * Grant the Cloud Storage bucket access to Knowledge Catalog service agents: The Knowledge Catalog service accounts in each target project require access to your Cloud Storage buckets.




## Create and structure the Google Sheet for import

To successfully run a bulk import, you must create a new Google Sheet using a precise column schema to define your entry links, including `definition`, `related`, and `synonym` entry link types. This schema lets the import utility parse and validate your metadata fields. Ensure that you have granted the service account `Editor` access to the Google Sheet.

The first row of the sheet must contain these exact, case-sensitive schema headers:

Column header | Required or Optional | Description  
---|---|---  
`entry_link_type` | Required | Value must be `definition`, `related`, or `synonym`.  
`source_entry` | Required | The full resource path of the source entry in the format:  
`projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRYGROUP_NAME/entries/ENTRY_NAME`  
`target_entry` | Required | The full resource path of the target entry in the format:  
`projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRYGROUP_NAME/entries/ENTRY_NAME`  
`source_path` | Optional | Column or field path for definition links (for example, `Schema.column_name`).  
  
## Set up environment variables

Set up the following environment variables:
    
    
    # Set your Google Sheet URL
    export SPREADSHEET_URL="GOOGLE_SHEET_URL"
    
    # Set your bucket name
    export BUCKETS="COMMA_SEPARATED_LIST_OF_BUCKETS"
    
    # Set the project ID
    export USER_PROJECT="USER_PROJECT"

## Import entry links from the Google Sheet

To import the entry links from the Google Sheet into Knowledge Catalog, run the `entrylinks-import.py` script:
    
    
    cd import
    python3 entrylinks-import.py \
      --spreadsheet-url="$SPREADSHEET_URL" \
      --buckets="$BUCKETS" \
      --user-project="$USER_PROJECT"

To run multiple import jobs in parallel, specify multiple Cloud Storage buckets in the `--buckets` parameter. The script splits the metadata into smaller batches and processes them concurrently across the buckets, reducing total ingestion time.

**Note:** Format the list of Cloud Storage buckets as a single, comma-separated string without spaces (for example, `bucket-1,bucket-2,bucket-3`). To prevent rate-limiting on API calls, don't specify more than 20 buckets.

You can review the execution logs in the `logs/` directory in your local execution path. These logs help you audit the transfer process and identify skipped entries or formatting warnings.

## What's next

  * Learn how to [manage a business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).
  * Learn how to [export entry links to a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/export-entrylinks-sheets).
  * Learn how to [import glossaries from a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/import-glossaries-sheets).
  * Learn more about [metadata management](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
