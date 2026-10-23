---
url: https://docs.cloud.google.com/translate/docs/advanced/labels/
title: Reporting usage with labels (Advanced) \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:03.483573+00:00
---

# Reporting usage with labels (Advanced)  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/advanced/labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ Guides ](https://docs.cloud.google.com/translate/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reporting usage with labels (Advanced)

The Cloud Translation API supports adding user-defined labels (key-value pairs) to `TranslateText`, `BatchTranslateText` and `DetectLanguage` requests. Information about a request's usage is forwarded to the billing system where you can break down your billing charges by filtering by label.

## Use case

An important use case for labels involves customers who provide translation services to many clients. A single project can be used for multiple clients. For billing purposes it's important to associate specific requests with their respective clients. That's where labels come in. When making a call on behalf of a client, you label the request with a client specific label. These labels are then available for filtering purposes in the **Reports** section of the Google Cloud.

## Requirements for labels

The labels applied to a request must meet the following requirements:

  * Each request can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters, and cannot be empty. Values can be empty, and have a maximum length of 63 characters.
  * Keys and values contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique within a single request (for example, `{'country':'india'}` is fine, but `{'country':'india','country':'sweden'}` is not allowed).
  * Keys must start with a lowercase letter or international character.



## Labels and billing

In Cloud Translation, you can use labels to organize [fees](https://cloud.google.com/translate/pricing) by billing account. You aren't changed for the use of Cloud Translation labels.

Fees are associated with the billing account of the project that contains the request. Or, if a custom or Neural Machine Translation (NMT) model is used, fees are associated with the [project that contains the model](https://cloud.google.com/translate/pricing#charged-projects).

For billing purposes, all billable requests can have labels of their own. These billable requests include batch translation, detect language, and translate text.

## Creating and managing labels using the Cloud Translation API

Use the Cloud Translation API to add labels to a request. 

### REST

In the following example, the labels `{'country':'russia'}`,`{'env':'test'}` are added to the `translateText` request. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER_OR_ID`: the numeric or alphanumeric ID of your Google Cloud project



HTTP method and URL: 
    
    
    POST https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID:translateText

Request JSON body: 
    
    
    {
      source_language_code: 'en',
      target_language_code: 'ru',
      contents: 'Dr. Watson, come here!',
      labels: {'country':'russia','env':'test'}
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_NUMBER_OR_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID:translateText"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_NUMBER_OR_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://translation.googleapis.com/v3/projects/PROJECT_NUMBER_OR_ID:translateText" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "translations": [
        {
          "translatedText": "Доктор Ватсон, иди сюда!"
        }
      ]
    }
    

## Pricing report

Go to the [Google Cloud](https://console.cloud.google.com/billing) billing console **Reports** view to use these labels as filters for request usage.

  1. From the dashboard, click the hamburger icon on the upper left-hand side and select "Billing" from the drop-down. If you have multiple billing accounts a page appears that asks you to make a selection. Click "Go to linked billing account."
  2. From the Billing page, select **Reports** in the left-hand nav.
  3. Use the filters in the right-hand nav to check usage of requests.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
