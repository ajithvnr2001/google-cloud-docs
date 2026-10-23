---
url: https://docs.cloud.google.com/spectrum-access-system/docs/authorization-and-authentication/
title: Set up authorization and authentication \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:04.856055+00:00
---

# Set up authorization and authentication  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/authorization-and-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Set up authorization and authentication Stay organized with collections  Save and categorize content based on your preferences. 

We recommend that you use a service account for authentication when you integrate with the Google Spectrum Access System (SAS) Portal API.

## Set up a service account

To use a service account for authentication, complete the following steps:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account).
  2. [Create your service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and select **JSON** as your key type.

After you complete this step, your service account key is downloaded to your browser's default location.

  3. [Grant the **Project Owner** role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to the service account.




## Obtain a bearer token

You need to provide your service account authentication as a bearer token. If you call the SAS Portal API directly, such as by making an HTTP request with `curl`, you pass your authentication as a bearer token in the `Authorization` header.

To obtain a bearer token with your service account, follow these steps:

  1. [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

  2. In the gcloud CLI, authenticate to your service account:
         
         gcloud auth activate-service-account --key-file ${KEY_FILE}
         

Replace `${KEY_FILE}` with the path to your service account key file.

  3. Use your service account to obtain an authorization token:
         
         gcloud auth print-access-token
         

The command returns an access token value.

  4. When you use the API, pass the token value as a bearer token in an `Authorization` header. The following code sample shows how to pass the token value as a bearer token:
         
         curl -X GET -H "X-Goog-User-Project: ${CLIENT_PROJECT}" \
          -H "Content-Type: application/json" \
          -H "Authorization: Bearer ${TOKEN}" \
          "https://sasportal.googleapis.com/v1alpha1/customers"
         

Replace the following:

     * `${CLIENT_PROJECT}`: the [ID of the Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) from which you make the requests
     * `${TOKEN}`: the authorization token



## What's next

  * To get an overview of the SAS Portal API, see [Google SAS Portal API overview](https://docs.cloud.google.com/spectrum-access-system/docs/overview-api).
  * For information about each API, see the [Customers](https://docs.cloud.google.com/spectrum-access-system/docs/customers-api) and [Device Manager](https://docs.cloud.google.com/spectrum-access-system/docs/device-manager-api) API pages.
  * For examples of how to use the API, see [API code samples](https://docs.cloud.google.com/spectrum-access-system/docs/samples).
  * For reference documentation, see [APIs and reference](https://docs.cloud.google.com/spectrum-access-system/docs/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
