---
url: https://docs.cloud.google.com/vision/deprecation/libraries/
title: Alpha client libraries \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:30.637624+00:00
---

# Alpha client libraries  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/deprecation/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)



Send feedback 

#  Alpha client libraries Stay organized with collections  Save and categorize content based on your preferences. 

**Alpha**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides instructions for installing and authenticating with the Cloud Vision Alpha client libraries.

## Installing the Python client library

**Note:** The client libraries have been updated to reflect the latest changes to the Vision Alpha. These changes are not backward-compatible with client libraries version older than 0.30.1. Review the latest code samples in this document for examples of how to call the Vision Alpha using the new client libraries.

### Python
    
    
    pip install https://storage.googleapis.com/api-client-staging/vision-python-q1alpha-mar2019.tar.gz

## Authentication

To use the alpha client library, you must create and activate a service account.

  1. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs).

  2. Create a [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account).

  3. Create a [service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete) and download the JSON key file.

  4. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to your service account key file. This enables your client libraries to use [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) (ADC).
         
         export GOOGLE_APPLICATION_CREDENTIALS=path-to-key-file

  5. Authenticate by running [the following command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login):
         
         gcloud auth login


**Note:** For information about authenticating in other environments, see the [Google Cloud Platform Auth Guide](https://docs.cloud.google.com/docs/authentication#getting_credentials_for_server-centric_flow).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
