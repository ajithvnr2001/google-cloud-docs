---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations/
title: Manage long-running operations \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:11.218926+00:00
---

# Manage long-running operations  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-long-running-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Manage long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage the lifecycle of a Financial Services API Long-Running Operation (LRO).

[_Long-Running Operations_](https://google.aip.dev/151) are returned when method calls might take a long time to complete. For example, the Financial Services API creates an LRO every time you call [`projects.locations.instances.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/create). The LRO tracks the status of the processing job.

You can use the [`projects.locations.operations` methods](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations) that the Financial Services API provides to check the status of LROs. You can also list, cancel, or delete LROs.

LROs are managed at the Google Cloud project and location level. When making a request to the API, include the Google Cloud project and the location in which the LRO is running.

The record of an LRO is kept for approximately 30 days after the LRO finishes. You can't view or list an LRO after that point.

## Get details about a long-running operation

Suppose you [created an instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances). The `name` value in the response shows that the Financial Services API created an LRO named `projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID`.

Use the [`projects.locations.operations.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/get) method to check if the instance has been created. If the response contains `"done": false`, repeat the command until the response contains `"done": true`. This operation can take a few minutes to complete.

**Note:** Some operations may take hours to complete.

You can also retrieve the LRO name by listing long-running operations.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `OPERATION_ID`: the identifier for the operation



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
        "createTime": "2023-03-14T15:52:55.358979323Z",
        "endTime": "2023-03-14T16:52:55.358979323Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.financialservices.v1.Instance",
        "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
        "createTime": CREATE_TIME,
        "updateTime": UPDATE_TIME,
        "state": "ACTIVE",
        "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID"
      }
    }
    

## List long-running operations

Use the [`projects.locations.operations.list`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/list) method to list all of the operations in a given location.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the operations; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "operations": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
            "createTime": "2023-03-14T15:52:55.358979323Z",
            "endTime": "2023-03-14T16:52:55.358979323Z",
            "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineConfigs/ENGINE_CONFIG_ID",
            "verb": "create",
            "requestedCancellation": false,
            "apiVersion": "v1"
          },
          "done": false
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/operations/my-other-operation",
          "metadata": {
            "@type": "type.googleapis.com/google.cloud.financialservices.v1.OperationMetadata",
            "createTime": CREATE_TIME,
            "endTime": END_TIME,
            "target": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
            "verb": "create",
            "requestedCancellation": false,
            "apiVersion": "v1"
          },
          "done": true,
          "response": {
            "@type": "type.googleapis.com/google.cloud.financialservices.v1.Instance",
            "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID",
            "createTime": CREATE_TIME,
            "updateTime": UPDATE_TIME,
            "state": "ACTIVE",
            "kmsKey": "projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID"
          }
        }
      ]
    }
    

## Cancel a long-running operation

Use the [`projects.locations.operations.cancel`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/cancel) method to start asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the operation; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `OPERATION_ID`: the identifier for the operation



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID:cancel"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID:cancel" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

## Delete a long-running operation

Use the [`projects.locations.operations.delete`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/delete) method to delete a completed long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the operation; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `OPERATION_ID`: the identifier for the operation



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
