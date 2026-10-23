---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/auth/
title: Authenticating to the DLP API \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:17.176313+00:00
---

# Authenticating to the DLP API  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/auth/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Authenticating to the DLP API Stay organized with collections  Save and categorize content based on your preferences. 

You must authenticate to the DLP API in order to use it. The DLP API can handle both API keys and authentication. The main distinction between these two methods is:

  * API keys identify the calling project—the app or site—that is making the call to an API.
  * Auth tokens identify a user—the person—that is using the project.



## Using an API key for unauthenticated access

You can use a Google Cloud console API key to authenticate to the DLP API for some methods, including all [`projects.content.*`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content) and [`projects.image.*`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image) methods.

  1. Follow the instructions to [create an API key for your Google Cloud console project](https://support.google.com/cloud/answer/6158862).
  2. When making any DLP API request, pass your key as the value of a `key` parameter. For example: 
         
         curl https://dlp.googleapis.com/v2/infoTypes?key=[YOUR_API_KEY]




It's important to protect your API keys against unauthorized use. For advice on how to do this, see [Best practices for securely using API keys](https://support.google.com/cloud/answer/6310037).

**Note:** When a Cloud Key Management Service wrapped key is used on [`deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/deidentify) or [`reidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/reidentify) requests, API keys can't be used for authentication. Cloud Key Management Service does not support API keys as an authentication method. For more information, see [Accessing the API](https://docs.cloud.google.com/kms/docs/accessing-the-api).

## Using a service account

To use a service account to authenticate to the DLP API:

  * Follow the instructions to [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account). Select **JSON** as your key type, and grant the user the **DLP User** role (roles/dlp.user).



For more information about granting roles to service accounts, see [Granting Roles to Service Accounts](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts).

**Note:** Granting the user the **Owner** role is not necessary.

Once complete, your service account key is downloaded to your browser's default location.

Next, decide whether you'll provide your service account authentication as a _bearer token_ or using _application default credentials_.

### Bearer tokens using a service account

If you're calling the DLP API directly, such as by making an HTTP request with cURL, you'll pass your authentication as a bearer token in an HTTP Authorization request header. To obtain a bearer token using your service account:

  1. Install the [ Google Cloud CLI](https://docs.cloud.google.com/sdk/downloads#interactive).
  2. Authenticate to your service account, replacing [KEY_FILE] below with the path to your service account key file: 
         
         gcloud auth activate-service-account --key-file [KEY_FILE]

  3. Obtain an authorization token using your service account: 
         
         gcloud auth print-access-token

The command returns an access token value.
  4. When calling the API, pass the token value as a `bearer` token in an `Authorization` header: 
         
         curl -s -H 'Content-Type: application/json' \
           -H 'Authorization: Bearer [ACCESS_TOKEN]' \
           'https://dlp.googleapis.com/v2/infoTypes'




### Application default credentials

If you're using a client library to call the DLP API, use [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) (ADC).

Services using ADC look for credentials within a `GOOGLE_APPLICATION_CREDENTIALS` environment variable. Unless you specifically want to have ADC use other credentials (for example, user credentials), set this environment variable to point to your service account key file.
    
    
    export GOOGLE_APPLICATION_CREDENTIALS=[PATH_TO_KEY_FILE]

### Using Sensitive Data Protection from Compute Engine VMs

In order to access the DLP API from VM instances, select **Allow full access to all Cloud APIs** under the **Identity and API Access** section when creating the VM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
