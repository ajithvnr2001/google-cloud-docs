---
url: https://docs.cloud.google.com/migration-center/docs/export-collected-data/
title: Export data to Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:39.686481+00:00
---

# Export data to Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/export-collected-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Export data to Migration Center Stay organized with collections  Save and categorize content based on your preferences. 

After you've collected the data about your assets, you can then export it to Migration Center where you can do the following:

  * [View the collected assets in one place](https://docs.cloud.google.com/migration-center/docs/view-assets)
  * [View and understand insights that Migration Center generates about your infrastructure](https://docs.cloud.google.com/migration-center/docs/view-and-understand-insights)
  * [Create groups of assets](https://docs.cloud.google.com/migration-center/docs/create-groups)
  * [Generate total cost of ownership (TCO) reports](https://docs.cloud.google.com/migration-center/docs/generate-tco-report) for your infrastructure



This document describes how to export the data to Migration Center for an online assessment by using the Migration Center discovery client CLI.

## Before you begin

  1. Complete the steps to discover assets in your infrastructure.
  2. From the Google Cloud console, [activate Migration Center](https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center#activate-migration-center).
  3. Enable the Cloud Resource Manager API.

[Enable the API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com)




### Review required roles and permissions

To get the permissions that you need to export the collected data to Migration Center, ask your administrator to grant you the Migration Center Admin (`migrationcenter.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to export the collected data to Migration Center. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to export the collected data to Migration Center:

  * `resourcemanager.projects.get`
  * `migrationcenter.sources.create`
  * `migrationcenter.sources.get`
  * `migrationcenter.assets.reportFrames`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Set up authentication to Migration Center

To export the collected data to Migration Center, you need to set up authentication to Migration Center with one of the following methods:

  * Using a service account.
  * Using a personal account.



We recommend you to create a service account from the Cloud Shell in the Google Cloud console, which has the Google Cloud CLI already installed. Alternatively, if you want to use your personal account, then you need to [install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

#### Set up authentication using a service account

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  1. If you have the [required permissions](https://docs.cloud.google.com/iam/docs/service-accounts-create#permissions), then [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating):
         
         gcloud iam service-accounts create SA_NAME \
             --description='SA_DESCRIPTION' \
             --display-name='SA_DISPLAY_NAME'
         

Replace the following:

     * SA_NAME: the name you want for the service account
     * SA_DESCRIPTION: an optional description for the service account
     * SA_DISPLAY_NAME: the display name for the service account
  2. To grant the service account the required permissions, assign the [`migrationcenter.admin` role](https://docs.cloud.google.com/migration-center/docs/roles-and-permissions#migrationcenter.admin):
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member='serviceAccount:SA_NAME@PROJECT_ID.iam.gserviceaccount.com' \
             --role='roles/migrationcenter.admin'
         

Replace PROJECT_ID with the name of your project.

  3. [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating):
         
         gcloud iam service-accounts keys create ~/sa-private-key.json \
          --iam-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
          --billing-project PROJECT_ID
         

The key is saved in the specified path: `~/sa-private-key.json`.

**Note:** It is recommended that you set an [expiration date](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#key-expiry) for the service account key. If you don't set an expiration date for the service account key, the generated key has no expiration date and you must delete it manually. For more information, see the [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).
  4. Copy the key file to the machine where you want to run the `mcdc` CLI.




#### Set up authentication using a personal account

  * Provide your user credentials to [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials):
        
        gcloud --project PROJECT_ID auth application-default login
        

Replace PROJECT_ID with the name or ID of your project.




## Export the collected data

After the data collection and authentication setup to Migration Center is complete, you can proceed to exporting the collected data to Migration Center.

  * To export the collected data from your workstation to Migration Center, run the following command:

### Linux
        
        ./mcdc export mc --project PROJECT_ID

### Windows
        
        mcdc.exe export mc --project PROJECT_ID

Replace PROJECT_ID with the name of your project.

  * If you've set up authentication to Migration Center using a service account key, then you need to provide the path to the JSON key file using the `--json-key` flag:

### Linux
        
        ./mcdc export mc --project PROJECT_ID --json-key PATH_TO_JSON_KEY

### Windows
        
        mcdc.exe export mc --project PROJECT_ID --json-key PATH_TO_JSON_KEY

Replace PATH_TO_JSON_KEY with the path to the JSON key file.

Optionally, if you want to wait for Migration Center to finish processing the assets, and check whether all the work is done successfully, then use the `--wait` flag with the `export` command.




After the export is complete, the discovery client prints a link that you can follow to see your assets in Migration Center.

## What's next

  * Learn how to [manage the `mcdc` CLI](https://docs.cloud.google.com/migration-center/docs/manage-collector-cli).
  * Learn how to [view the collected assets in Migration Center](https://docs.cloud.google.com/migration-center/docs/view-assets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
