---
url: https://docs.cloud.google.com/vision-ai/docs/manage-searchconfig-api/
title: Manage search config \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:27.183239+00:00
---

# Manage search config  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/manage-searchconfig-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Manage search config Stay organized with collections  Save and categorize content based on your preferences. 

## Restriction

If there is a facet property in search config, its mapped fields should always match those in search criteria property. These fields should be the existing data schema with the same type, granularity, and search strategy.

## Create a search config

### REST

To create a `SearchConfig` resource, send a POST request by using the [`projects.locations.corpora.searchConfigs.create`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs/create) method. 

Here is the example of how to create a search config with customized search criteria. 

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG: The name of your target `SearchConfig`. 
    * The `SearchConfig` in this example is `person`.



HTTP method and URL: 
    
    
    POST https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** person

Request JSON body: 
    
    
    {
       "search_criteria_property": {
         "mapped_fields": "player",
         "mapped_fields": "coach",
         "mapped_fields": "cheerleader",
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** person"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs**?search_config_id=** person" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/person",
      "searchCriteriaProperty":
        {
          "mappedFields": [
            "player",
            "coach",
            "cheerleader"
          ]
        }
    }
    

## Update a search config

### REST

To update a `SearchConfig` resource, send a POST request by using the [`projects.locations.corpora.searchConfigs.patch`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs/patch) method. 

Here is the example of how to create a search config with customized search criteria. 

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT: Your Google Cloud [project ID or project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG_ID: The ID of your target `SearchConfig`. 
  * `"mappedFields"`: One or more existing user-given annotation keys.



HTTP method and URL: 
    
    
    PATCH https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID

Request JSON body: 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID1",
      "searchCriteriaProperty": {
        "mappedFields": "dataschema2"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID1",
      "searchCriteriaProperty": {
        "mappedFields": [
          "dataschema2"
        ]
      }
    }
    

## Get a search config

The following example shows you how to retrieve an existing `SearchConfig` that makes it easier to search for people in warehouse-stored data.

### REST

To get details about a `SearchConfig`, send a GET request by using the [projects.locations.corpora.searchConfigs.get](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs/get) method. 

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG: The name of your target `SearchConfig`. 
    * The `SearchConfig` in this example is `person`.



HTTP method and URL: 
    
    
    GET https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/person"
      "facet_property": {
        // Top-level facet group name.
        "display_name": "Person",
        // Each mapped_field will be displayed in the UI as a selectable value
        // under "Person".
        "mapped_fields": "player",
        // The maximum number of mapped_fields to be displayed.
        "result_size": 2,
        // The facet type is a singular value. In this case, type string.
        "bucket_type": FACET_BUCKET_TYPE_VALUE
      }
    }
    

## List search configs

The following example shows you how to list all previously created [`SearchConfig`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs) resources.

You can specify the number of search configs listed by setting the `page_size` field in your request.

### REST

To list all search configs, send a GET request by using the [`projects.locations.corpora.searchConfigs.list`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs/list) method. 

In this example, the `page_size` field is set to 2, limiting the response to two search configs. If the page size is not specified, the default value of 25 is used. 

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * PAGE_SIZE: (_Optional_) The number of results to return. 



HTTP method and URL: 
    
    
    GET https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs?page_size=2

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs?page_size=2"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs?page_size=2" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "next_page_token": "xyz",
      "search_configs": {
        "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/person",
        "facet_property": {
          // Top-level facet group name.
          "display_name": "Person",
          // Each mapped_field will be displayed in the console as a selectable value
          // under "Person".
          "mapped_fields": "player",
          // The maximum number of mapped_fields to be displayed.
          "result_size": 2,
          // The facet type is a singular value. In this case, type string.
          "bucket_type": FACET_BUCKET_TYPE_VALUE
        }
      },
      "search_configs": {
        "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/location",
        "facet_property": {
          // Top-level facet group name.
          "display_name": "location",
          // Each mapped_field will be displayed in the console as a selectable value
          // under "location".
          "mapped_fields": "city",
          // The maximum number of mapped_fields to be displayed.
          "result_size": 2,
          // The facet type is a singular value. In this case, type string.
          "bucket_type": FACET_BUCKET_TYPE_VALUE
        }
      }
    }
    

The response only contains two `SearchConfigs` because in the request, the `page_size=2` field is set. To view the next page of search configs, include the previous response's `next_page_token` setting in your next request:

  * https://warehouse-visionai.googleapis.com/v1alpha/[...]/searchConfigs**?page_size= 2&page_token='xyz'**



## Delete a search config

### REST & CMD LINE

The following code sample uses the [`projects.locations.corpora.searchConfigs.delete`](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.corpora.searchConfigs/delete) method to delete a `SearchConfig`. The `SearchConfig` must exist for this request to succeed.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * CORPUS_ID: The ID of your target corpus.
  * SEARCHCONFIG_ID: The ID of your target `SearchConfig`. 



HTTP method and URL: 
    
    
    DELETE https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://warehouse-visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/corpora/CORPUS_ID/searchConfigs/SEARCHCONFIG_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
