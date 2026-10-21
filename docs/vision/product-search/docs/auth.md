---
url: https://docs.cloud.google.com/vision/product-search/docs/auth/
title: Authenticating to the Cloud Vision API \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:10:14.167981+00:00
---

# Authenticating to the Cloud Vision API  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/auth/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



Send feedback 

#  Authenticating to the Cloud Vision API Stay organized with collections  Save and categorize content based on your preferences. 

## Using a service account

Using a service account to authenticate is the preferred method. To use a service account to authenticate to the Vision API:

  1. Follow the instructions to [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account). Select **JSON** as your key type.



Once complete, your service account key is downloaded to your browser's default location.

Next, decide whether you'll provide your service account authentication as a **bearer token** or using **application default credentials**.

### Bearer tokens

If you're calling the Vision API directly, such as by making an HTTP request with cURL, you'll pass your authentication as a bearer token in an `Authorization` header. To obtain a bearer token using your service account:

  1. [Install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads#interactive).
  2. Authenticate to your service account, replacing `KEY_FILE` below with the path to your service account key file:
         
         gcloud auth activate-service-account --key-file KEY_FILE
         

  3. Obtain an authorization token using your service account:
         
         gcloud auth print-access-token
         

The command returns an access token value.

  4. When calling the API, obtain an authorization token using your service account in an `Authorization` header:
         
         curl -s -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json" \
         "https://vision.googleapis.com/v1/images:annotate" -d @request.json
         




### Application default credentials

If you're using a client library to call the Vision API, use [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) (ADC). Services using ADC look for credentials within a `GOOGLE_APPLICATION_CREDENTIALS` environment variable. Unless you specifically wish to have ADC use other credentials (for example, user credentials), we recommend you set this environment variable to point to your service account key file.
    
    
    export GOOGLE_APPLICATION_CREDENTIALS=_PATH_TO_KEY_FILE_
    

Replace `PATH_TO_KEY_FILE` with the path to your JSON service account file. `GOOGLE_APPLICATION_CREDENTIALS` should be written out as-is (it's not a placeholder in the example above).

## Using an API key

You can use a Google Cloud console API key to authenticate to the Vision API.

To do so:

  1. Follow the instructions to [create an API key for your Google Cloud console project](https://support.google.com/cloud/answer/6158862?hl=en).

  2. When making any Vision API request, pass your key as the value of a `key` parameter. For example:
         
         POST https://vision.googleapis.com/v1/images:annotate?key=YOUR_API_KEY
         




Make sure to read [Best practices for securely using API keys](https://support.google.com/cloud/answer/6310037?hl=en&ref_topic=6262490) to prevent unauthorized use of your API key.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
