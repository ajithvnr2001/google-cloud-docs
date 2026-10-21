---
url: https://docs.cloud.google.com/alloydb/docs/cancel-import/
title: Cancel an import operation \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:17.302360+00:00
---

# Cancel an import operation  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/cancel-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Cancel an import operation Stay organized with collections  Save and categorize content based on your preferences. 

To stop an in-progress CSV or SQL import and free up cluster resources, you can cancel the AlloyDB for PostgreSQL import operation using the Google Cloud CLI or the REST API.

## Before you begin

To cancel the import of data, find the ID of the import operation that you want to cancel. To find the ID, do one of the following:

  * Follow the instructions in [Import a CSV file](https://docs.cloud.google.com/alloydb/docs/import-csv-file) or [Import a SQL file](https://docs.cloud.google.com/alloydb/docs/import-sql-file). The operation ID is returned in the `name` field of the response.
  * Make an [`operations.list`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/list) call on the AlloyDB cluster.



## Cancel the import operation

You can use the Google Cloud CLI or REST API commands to cancel an import operation.

###  gcloud 

Use the [`gcloud alloydb operations cancel`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/cancel) command to cancel the operation:
    
    
    gcloud alloydb operations cancel OPERATION_ID --region=REGION

Replace the following:

  * `OPERATION_ID`: the ID of the operation. For more information, see Before you begin.
  * `REGION`: the region in which the AlloyDB cluster is deployed.



###  REST v1 

Use the following HTTP method and URL:
    
    
    POST https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID:cancel

For more information, see [`operations.cancel`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.operations/cancel).

Before you use any of the request data, make the following replacements:

  * PROJECT_ID: the project ID.
  * REGION: the region in which the AlloyDB cluster is deployed.
  * OPERATION_ID: the ID of the import operation. For more information, see Before you begin.

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

The following command assumes that you signed into the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
        
        curl -X POST \
                 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                 -H "Content-Type: application/json; charset=utf-8" \
                 -d @request.json \
                 "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID:cancel"
        

#### PowerShell (Windows)

The following command assumes that you signed into the Google Cloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json` and execute the following command:
        
        $cred = gcloud auth print-access-token
        $headers = @{ "Authorization" = "Bearer $cred" }
        
        Invoke-WebRequest `
          -Method POST `
          -Headers $headers `
          -ContentType: "application/json; charset=utf-8" `
          -InFile request.json `
          -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID:cancel"| Select-Object -Expand Content
        

This REST API call doesn't return any response. For more information about checking the cancellation status of the import, see Check the cancelled status.




## Check the cancelled status

You can use the gcloud CLI or REST API commands to check the status of a cancelled import operation.

###  gcloud 

Use the [`gcloud alloydb operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/describe) command to check the status of the cancelled operation.
    
    
    gcloud alloydb operations describe OPERATION_ID --region=REGION

Replace the following:

  * `OPERATION_ID`: the ID of the cancelled operation. For more information, see Before you begin.
  * `REGION`: the region in which the AlloyDB cluster is deployed.



###  REST v1 

Run the following:
    
    
    GET https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID
    

For more information, see [`operations.get`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.operations/get).

Before you use any of the request data, make the following replacements:

  * REGION: the region in which the AlloyDB cluster is deployed.
  * PROJECT_ID: the project ID.
  * OPERATION_ID: the ID of the import operation. For more information, see Before you begin.



To send your request, expand one of these options:

#### _curl (Linux, macOS, or Cloud Shell)_

The following command assumes that you signed into the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically signs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list).

Execute the following command:
    
    
      curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID"
     

#### _PowerShell (Windows)_

The following command assumes that you signed into the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command:
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method GET `
      -Headers $headers `
      -Uri "https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/operations/OPERATION_ID" | Select-Object -Expand Content
    

If successful, the response body contains an instance of [`Operation`](https://docs.cloud.google.com/alloydb/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation). 

## What's next

  * Learn how to [import a CSV file](https://docs.cloud.google.com/alloydb/docs/import-csv-file).
  * Learn how to [import a SQL file](https://docs.cloud.google.com/alloydb/docs/import-sql-file).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
