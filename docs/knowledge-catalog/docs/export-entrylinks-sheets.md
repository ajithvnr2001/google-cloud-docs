---
url: https://docs.cloud.google.com/knowledge-catalog/docs/export-entrylinks-sheets/
title: Export entry links to a Google Sheet \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:04.539725+00:00
---

# Export entry links to a Google Sheet  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/export-entrylinks-sheets/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Export entry links to a Google Sheet Stay organized with collections  Save and categorize content based on your preferences. 

The entry link export utility lets you extract entry links—the relationships between glossary terms and data assets—from Knowledge Catalog (formerly Dataplex Universal Catalog) into a Google Sheet. You can then audit existing links, back up your metadata, or prepare a template for bulk updates.

## Before you begin

Before you export entry links to a Google Sheet, complete the following prerequisites.

### Set up the service account

To run the export utility, you must set up a service account with the necessary permissions to access the Google Sheets API and impersonate your user credentials:

  1. Identify or create a service account.

Select an existing service account or create a new one in the project where you run the import utility. For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts). Note the service account email (for example, `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`).

  2. Configure service account impersonation.

To run the export utility script locally, your user account must have permission to impersonate the service account. Grant your user account the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`) on the service account.

For more information, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

  3. Grant the service account `Editor` access to the Google Sheet.

Open the Google Sheet you want to use for the import process, click **Share** , and add the service account email as an `Editor`. This permission enables the service account to read from or write data to your sheet.




### Required roles

To ensure that the service account has the necessary permissions to export entry links to a Google Sheet, ask your administrator to grant the following IAM roles to the service account: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Dataplex Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.admin) (`roles/dataplex.admin`) on the project
  * [Dataplex Catalog Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) on the project
  * [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Enable APIs

To export entry links, enable the following APIs in your project:

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,cloudresourcemanager.googleapis.com,storage.googleapis.com,sheets.googleapis.com)

### Set up the git repository

Clone the `dataplex-labs` repository:
    
    
    git clone https://github.com/GoogleCloudPlatform/dataplex-labs.git
    cd dataplex-labs/dataplex-quickstart-labs/00-resources/scripts/python/business-glossary-import/dataplex-glossary/export

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

## Set up the target Google Sheet for export

Create an empty Google Sheet or use an existing one. The export script writes to the first sheet. Ensure that you have granted the service account `Editor` access to the Google Sheet.

## Set up environment variables

Set up the following environment variables:
    
    
    # Set your glossary URL
    export GLOSSARY_URL="GLOSSARY_URL"
    
    # Set your Google Sheet URL
    export SPREADSHEET_URL="GOOGLE_SHEET_URL"
    
    # Set the project ID
    export USER_PROJECT="USER_PROJECT"

## Export entry links to the Google Sheet

To export entry links in a glossary to the Google Sheet, run the following script:
    
    
    cd export
    python3 entrylinks-export.py \
      --glossary-url="$GLOSSARY_URL" \
      --spreadsheet-url="$SPREADSHEET_URL" \
      --user-project="$USER_PROJECT"

You can review the execution logs in the `logs/` directory in your local execution path. These logs help you audit the transfer process and identify skipped entries or formatting warnings.

## Verify the exported entry links data

The export script populates the Google Sheet with the following columns:

Column header | Description  
---|---  
`entry_link_type` | The type of entry link (`definition`, `related`, or `synonym`).  
`source_entry` | The full resource path of the source entry.  
`target_entry` | The full resource path of the target entry.  
`source_path` | Column or field path for definition links.  
  
## What's next

  * Learn how to [manage a business glossary](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries).
  * Learn how to [import entry links from a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/import-entrylinks-sheets).
  * Learn how to [export glossaries to a Google Sheet](https://docs.cloud.google.com/knowledge-catalog/docs/export-glossaries-sheets).
  * Learn more about [metadata management](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
