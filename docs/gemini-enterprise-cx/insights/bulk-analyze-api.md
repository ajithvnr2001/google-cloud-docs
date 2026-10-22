---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/bulk-analyze-api/
title: Bulk analyze conversations using the API \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:03.334833+00:00
---

# Bulk analyze conversations using the API  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/bulk-analyze-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Bulk analyze conversations using the API Stay organized with collections  Save and categorize content based on your preferences. 

You have the option to analyze a random subset of the conversations, a filtered subset of conversations or a combination thereof in a single request in Customer Experience Insights.

**Note:** A maximum of 10k conversations can be analyzed per API request. Only one concurrent bulk analysis operation is allowed.

## Prerequisites

  1. Make sure that the [Cloud Storage, Speech-to-Text and Insights APIs](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin) are enabled on your Google Cloud project.
  2. Make sure that your conversation data is uploaded into Customer Experience Insights.



## Sample Commands

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.analyses.create`



### REST

Refer to the [`conversations:bulkAnalyze`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/bulkAnalyze) API endpoint for complete details. See the [`Conversation`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#Conversation) reference documentation for more information about this resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud Platform project ID.
  * ANALYSIS_PERCENTAGE: Percentage of the conversations to randomly analyze.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze

Request JSON body: 
    
    
    {
      "analysisPercentage": ANALYSIS_PERCENTAGE
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID",
    }
    

### (Optional) Analyze conversations using a filter

You can view a full list of filters on the [Conversation filtering](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering) page.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud Platform project ID.
  * ANALYSIS_PERCENTAGE: Percentage of the conversations to randomly analyze. 
  * FILTER: Filter conversations. [API reference](https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-api)

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze

Request JSON body: 
    
    
    {
      "analysisPercentage": ANALYSIS_PERCENTAGE,
      "filter": 'FILTER''
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID",
    }
    

### (Optional) Configure the analysis

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud Platform project ID.
  * ANALYSIS_PERCENTAGE: Percentage of the conversations to randomly analyze. 
  * PHRASE_MATCHER(s): The fully qualified phrase matcher resource names of the phrase matchers you want to use for the phrase matcher annotator. If left empty, all active phrase matchers will run.
  * ISSUE_MODEL(s): The fully qualified resource names of the issue models you want to use for the issue model annotator. Only works if run_issue_model_annotator is true. If left empty, all deployed issue models will run. Currently limited to 1 deployed model.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze

Request JSON body: 
    
    
    {
      "analysisPercentage": ANALYSIS_PERCENTAGE
      "annotatorSelector": {
        "run_interruption_annotator": {true/false},
        "run_silence_annotator": {true/false},
        "run_phrase_matcher_annotator": {true/false},
        "phrase_matchers": PHRASE_MATCHER(s),
        "run_sentiment_annotator": {true/false},
        "run_entity_annotator": {true/false},
        "run_intent_annotator": {true/false},
        "run_issue_model_annotator": {true/false}
        "issue_models": ISSUE_MODEL(s)
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/conversations:bulkAnalyze" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID",
    }
    

### Poll the operation

Creating an analysis returns a long-running operation. Long-running methods are asynchronous, and the operation might not yet be completed when the method returns a response. You can poll the operation to check on its status. See the [long-running operations page](https://docs.cloud.google.com/gemini-enterprise-cx/insights/long-running-operations) for details and code samples.

### Cancel the operation

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenteraiplatform.operations.cancel`



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud Platform project ID.
  * OPERATION_ID: the ID of the conversation you want to analyze. This value was returned when you created the operation.

**Note:** All the examples are using the global Customer Experience Insights instance. Refer to [Regionalization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/docs/regionalization) for instructions on using regional instances. 

HTTP method and URL: 
    
    
    POST https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID:cancel

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID:cancel"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/operations/OPERATION_ID:cancel" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
