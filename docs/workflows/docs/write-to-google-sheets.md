---
url: https://docs.cloud.google.com/workflows/docs/write-to-google-sheets/
title: Write to Google Sheets from a workflow \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:35.730909+00:00
---

# Write to Google Sheets from a workflow  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/write-to-google-sheets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Write to Google Sheets from a workflow Stay organized with collections  Save and categorize content based on your preferences. 

[Workflows connectors](https://docs.cloud.google.com/workflows/docs/connectors) let you automate querying a BigQuery dataset and writing the results to a [Google Sheets](https://developers.google.com/sheets) spreadsheet. Connectors simplify calling Google Cloud APIs by handling authentication and request formatting within your workflow.

## Before you begin

Before trying out the example in this document, ensure that you have completed the following.

  1. Enable the Compute Engine, Google Drive, Google Sheets, and Workflows APIs.

###  Console 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,drive.googleapis.com,sheets.googleapis.com,workflows.googleapis.com)

###  gcloud 
         
         gcloud services enable \
             compute.googleapis.com \
             drive.googleapis.com \
             sheets.googleapis.com \
             workflows.googleapis.com

  2. Make note of the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) service account as you will associate it with the example workflow for testing purposes. New projects that have enabled the Compute Engine API have this service account created with the IAM basic Editor role, and with the following email format:
         
         PROJECT_NUMBER-compute@developer.gserviceaccount.com

You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or you can retrieve your project number:
         
         gcloud projects describe PROJECT_ID

For production environments, we strongly recommend [creating a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and granting it one or more IAM roles that contain the [minimum permissions required](https://docs.cloud.google.com/iam/docs/understanding-service-accounts#granting_minimum) and follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  3. Create a new folder in Google Drive. This folder is used to store your spreadsheet. By setting up a permission for the shared folder, your workflow is allowed to write to the spreadsheet.

     1. Go to [drive.google.com](https://drive.google.com/).
     2. Click **New > New folder**.
     3. Enter a name for the folder.
     4. Click **Create**.
     5. Right-click your new folder and select **Share**.
     6. Add the email address for the Compute Engine default service account.

This gives the service account access to the folder. When you associate the service account with your workflow, the workflow will have edit access to any file in the folder. [Learn more about sharing files, folders & drives](https://developers.google.com/drive/api/guides/manage-sharing).

     7. Select the **Editor** role.

     8. Clear the **Notify people** checkbox.

     9. Click **Share**.




## Create a spreadsheet

You can create a spreadsheet in either one of the following ways:

  * Create a spreadsheet using Google Sheets
  * Create a spreadsheet using the Google Sheets API connector



There's no option to create a spreadsheet directly within a specified folder using the Google Sheets API. However, there are alternatives, including moving the spreadsheet to a specific folder after you create it, as is done in the following examples. For more information, see [Work with Google Drive folders](https://developers.google.com/sheets/api/guides/create#work_with_folders).

### Create a spreadsheet using Google Sheets

When you create a spreadsheet through Google Sheets, it's saved in Google Drive. By default, the spreadsheet is saved to your root folder on Drive.

  1. Go to [sheets.google.com](https://sheets.google.com/).

  2. Click **New** ![Plus](https://lh3.googleusercontent.com/anBD83lVdJYMSbLhOXIulHzmEGPr0uJRfiomsujvgYDHF0UlSHRhpJWca3hcw68T5A=w36-h36).

This creates and opens your new spreadsheet. Every spreadsheet has a unique [`spreadsheetId`](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets) value, containing letters, numbers, hyphens, or underscores. You can find the spreadsheet ID in a Google Sheets URL:

`https://docs.google.com/spreadsheets/d/spreadsheetId/edit#gid=0`

  3. Note this ID as it will be needed when you create your workflow.

  4. Move the spreadsheet to the Google Drive folder that you created previously:

     1. In the spreadsheet, select **File > Move**.
     2. Navigate to the folder you created.
     3. Click **Move**.



### Create a spreadsheet using the Google Sheets API connector

You can use the [Google Sheets API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/sheets/Overview) to create a spreadsheet. As Workflows uses the service account as the trigger identity, the spreadsheet is created in the service account's Google Drive root folder. You can then move the spreadsheet to another folder.

In the following workflow, the `spreadsheetId` is retrieved from the `resp` result:

### YAML
    
    
    main:
      steps:
        - init:
            assign:
              - folder_id: 'FOLDER_ID'
              - drive_url: 'https://www.googleapis.com/drive/v3/files/'
              - drive_auth_scope: 'https://www.googleapis.com/auth/drive'
        - create_sheet:
            call: googleapis.sheets.v4.spreadsheets.create
            args:
              body: null
              connector_params:
                scopes: 'https://www.googleapis.com/auth/drive'
            result: resp
        - get_sheet_info:
            call: http.get
            args:
              url: '${drive_url + resp.spreadsheetId}'
              query:
                fields: parents
              auth:
                type: OAuth2
                scopes: '${drive_auth_scope}'
            result: sheet_info
        - move_sheet:
            call: http.patch
            args:
              url: '${drive_url + resp.spreadsheetId}'
              query:
                addParents: '${folder_id}'
                removeParents: '${sheet_info["body"]["parents"][0]}'
              auth:
                type: OAuth2
                scopes: '${drive_auth_scope}'
            result: resp
        - return:
            return: '${resp}'

### JSON
    
    
    {
      "main": {
        "steps": [
          {
            "init": {
              "assign": [
                {
                  "folder_id": "FOLDER_ID"
                },
                {
                  "drive_url": "https://www.googleapis.com/drive/v3/files/"
                },
                {
                  "drive_auth_scope": "https://www.googleapis.com/auth/drive"
                }
              ]
            }
          },
          {
            "create_sheet": {
              "call": "googleapis.sheets.v4.spreadsheets.create",
              "args": {
                "body": null,
                "connector_params": {
                  "scopes": "https://www.googleapis.com/auth/drive"
                }
              },
              "result": "resp"
            }
          },
          {
            "get_sheet_info": {
              "call": "http.get",
              "args": {
                "url": "${drive_url + resp.spreadsheetId}",
                "query": {
                  "fields": "parents"
                },
                "auth": {
                  "type": "OAuth2",
                  "scopes": "${drive_auth_scope}"
                }
              },
              "result": "sheet_info"
            }
          },
          {
            "move_sheet": {
              "call": "http.patch",
              "args": {
                "url": "${drive_url + resp.spreadsheetId}",
                "query": {
                  "addParents": "${folder_id}",
                  "removeParents": "${sheet_info[\"body\"][\"parents\"][0]}"
                },
                "auth": {
                  "type": "OAuth2",
                  "scopes": "${drive_auth_scope}"
                }
              },
              "result": "resp"
            }
          },
          {
            "return": {
              "return": "${resp}"
            }
          }
        ]
      }
    }

Replace `FOLDER_ID` with the ID of the folder to which you want to move the spreadsheet. Every Drive folder has a unique ID, containing letters, numbers, hyphens, or underscores. You can find the folder ID in the folder URL:

`https://drive.google.com/drive/folders/FOLDER_ID/edit#gid=0`

For more information, see [Create and populate folders](https://developers.google.com/drive/api/guides/folder).

The output from the workflow should be similar to the following where the `id` value is the `spreadsheetId`:
    
    
    "body": {
        "id": "spreadsheetId",
        "kind": "drive#file",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "name": "Untitled spreadsheet"
      }
    

## Explore the BigQuery public dataset

BigQuery hosts a number of [public datasets](https://docs.cloud.google.com/bigquery/public-data) that are available to the general public to query.

In BigQuery, you can run an [interactive (on-demand) query job](https://docs.cloud.google.com/bigquery/docs/running-queries). For example, the following query returns the 100 most popular names in a specific dataset and writes the output to a temporary table. This is the query that your workflow will run.

### Console

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Enter the following BigQuery SQL query in the **Query editor** text area:
         
         SELECT name, gender, SUM(number) AS total
         FROM `bigquery-public-data.usa_names.usa_1910_2013`
         GROUP BY name, gender
         ORDER BY total DESC
         LIMIT 100
         

  3. Click **Run**.




### bq

In your terminal, enter the following `bq query` command to run an interactive query using standard SQL syntax:
    
    
        bq query \
        --use_legacy_sql=false \
        'SELECT
          name, gender, SUM(number) AS total
        FROM
          `bigquery-public-data.usa_names.usa_1910_2013`
        GROUP BY
          name, gender
        ORDER BY
          total DESC
        LIMIT 100'

## Deploy a workflow that writes to Sheets

Deploy a workflow that queries a BigQuery dataset using the [BigQuery API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/Overview) and that writes the results to a Sheets spreadsheet using the [Google Sheets API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/sheets/Overview).

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click add **Create**.

  3. Enter a name for the new workflow: `read-bigquery-write-sheets`.

  4. In the **Region** list, select **us-central1 (Iowa)**.

  5. For the **Service account** , select the Compute Engine default service account (`PROJECT_NUMBER-compute@developer.gserviceaccount.com`).

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:
         
         main:
             steps:
             - init:
                 assign:
                 # Replace with your sheetId and make sure the service account
                 # for the workflow has write permissions to the sheet
                 - sheetId: "1D8n7uoU8kGwQvR4rcLkF10CdAfnUKE2o0yl6P-Z7nfM"
                 - limit: 100
             - runQuery:
                 call: googleapis.bigquery.v2.jobs.query
                 args:
                     projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                     body:
                         useLegacySql: false
                         # Query name and gender of most popular names
                         query: ${"SELECT name, gender, SUM(number) AS total
                             FROM `bigquery-public-data.usa_names.usa_1910_2013`
                             GROUP BY name, gender
                             ORDER BY total DESC
                             LIMIT " + limit}
                 result: queryResult
             - init_header_row:
                 assign:
                 - rows:
                     - ["Name", "Gender", "Total"]
             - process_query_result:
                 for:
                     value: row
                     in: ${queryResult.rows}
                     steps:
                     - process_each_row:
                         assign:
                         - name: ${row.f[0].v}
                         - gender: ${row.f[1].v}
                         - total: ${row.f[2].v}
                         - row: ["${name}", "${gender}", "${total}"]
                         - rows: ${list.concat(rows, row)}
             - clear_existing_values:
                 call: googleapis.sheets.v4.spreadsheets.values.clear
                 args:
                     range: "Sheet1"
                     spreadsheetId: ${sheetId}
                 result: clearResult
             - update_sheet:
                 call: googleapis.sheets.v4.spreadsheets.values.update
                 args:
                     range: ${"Sheet1!A1:C" + (limit + 1)}
                     spreadsheetId: ${sheetId}
                     valueInputOption: RAW
                     body:
                         majorDimension: "ROWS"
                         values: ${rows}
                 result: updateResult
             - returnResult:
                 return: ${updateResult}

  8. Replace the placeholder `sheetId` value with your `spreadsheetId`.

  9. Click **Deploy**.




### gcloud

  1. Create a source code file for your workflow:
         
         touch read-bigquery-write-sheets.yaml

  2. In a text editor, copy the following workflow to your source code file:
         
         main:
             steps:
             - init:
                 assign:
                 # Replace with your sheetId and make sure the service account
                 # for the workflow has write permissions to the sheet
                 - sheetId: "1D8n7uoU8kGwQvR4rcLkF10CdAfnUKE2o0yl6P-Z7nfM"
                 - limit: 100
             - runQuery:
                 call: googleapis.bigquery.v2.jobs.query
                 args:
                     projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                     body:
                         useLegacySql: false
                         # Query name and gender of most popular names
                         query: ${"SELECT name, gender, SUM(number) AS total
                             FROM `bigquery-public-data.usa_names.usa_1910_2013`
                             GROUP BY name, gender
                             ORDER BY total DESC
                             LIMIT " + limit}
                 result: queryResult
             - init_header_row:
                 assign:
                 - rows:
                     - ["Name", "Gender", "Total"]
             - process_query_result:
                 for:
                     value: row
                     in: ${queryResult.rows}
                     steps:
                     - process_each_row:
                         assign:
                         - name: ${row.f[0].v}
                         - gender: ${row.f[1].v}
                         - total: ${row.f[2].v}
                         - row: ["${name}", "${gender}", "${total}"]
                         - rows: ${list.concat(rows, row)}
             - clear_existing_values:
                 call: googleapis.sheets.v4.spreadsheets.values.clear
                 args:
                     range: "Sheet1"
                     spreadsheetId: ${sheetId}
                 result: clearResult
             - update_sheet:
                 call: googleapis.sheets.v4.spreadsheets.values.update
                 args:
                     range: ${"Sheet1!A1:C" + (limit + 1)}
                     spreadsheetId: ${sheetId}
                     valueInputOption: RAW
                     body:
                         majorDimension: "ROWS"
                         values: ${rows}
                 result: updateResult
             - returnResult:
                 return: ${updateResult}

  3. Replace the placeholder `sheetId` value with your `spreadsheetId`.

  4. Deploy the workflow by entering the following command:
         
         gcloud workflows deploy read-bigquery-write-sheets \
             --source=read-bigquery-write-sheets.yaml \
             --location=us-central1 \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com

Replace `PROJECT_NUMBER` with your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console.




## Execute the workflow and verify the results

Executing a workflow runs the current workflow definition associated with the workflow.

  1. Run the workflow:

### Console

     1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

     2. On the **Workflows** page, select the **read-bigquery-write-sheets** workflow to go to its details page.

     3. On the **Workflow details** page, click _play_arrow_ **Execute**.

     4. Click **Execute** again.

     5. View the results of the workflow in the **Output** pane.

The output should be similar to the following:
            
            {
            "spreadsheetId": "1pgkNY7mWICA6o6INUNLHGnmk0Tdioh0nUghZPOYPpZA",
            "updatedCells": 303,
            "updatedColumns": 3,
            "updatedRange": "Sheet1!A1:C101",
            "updatedRows": 101
            }
            

### gcloud

     1. Open a terminal.

     2. Execute the workflow:
            
            gcloud workflows run read-bigquery-write-sheets

The execution results should be similar to the following:
            
            Waiting for execution [4dcf737b-69d9-4081-b8d9-86d39ae86bd1] to complete...done.     
            argument: 'null'
            duration: 3.131912897s
            endTime: '2023-01-25T14:59:46.818828242Z'
            name: projects/918619793306/locations/us-central1/workflows/read-bigquery-write-sheets/executions/4dcf737b-69d9-4081-b8d9-86d39ae86bd1
            result: '{"spreadsheetId":"1pgkNY7mWICA6o6INUNLHGnmk0Tdioh0nUghZPOYPpZA","updatedCells":303,"updatedColumns":3,"updatedRange":"Sheet1!A1:C101","updatedRows":101}'
            startTime: '2023-01-25T14:59:43.686915345Z'
            state: SUCCEEDED
            

  2. Verify that the workflow has written the results of the query to your spreadsheet. For example, the number of columns and rows in the spreadsheet should match the `updatedColumns` and `updatedRows` values.




## What's next

  * [Trigger a workflow from Google Sheets](https://docs.cloud.google.com/workflows/docs/tutorials/trigger-workflow-from-sheets).
  * [Pause and resume a workflow using callbacks and Google Sheets](https://docs.cloud.google.com/workflows/docs/tutorials/workflow-waits-callback-sheets).
  * [Explore the Google Workspace Learning Center](https://support.google.com/a/users#topic=11499463).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
