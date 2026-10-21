---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/synchronizer-access/
title: Configure the Synchronizer \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:29:42.356230+00:00
---

# Configure the Synchronizer  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/synchronizer-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure the Synchronizer Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/synchronizer-access.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/synchronizer-access.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/synchronizer-access.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/synchronizer-access.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/synchronizer-access.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/synchronizer-access.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/synchronizer-access.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/synchronizer-access.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/synchronizer-access.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/synchronizer-access.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/synchronizer-access.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/synchronizer-access.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/synchronizer-access.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/synchronizer-access.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/synchronizer-access.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/synchronizer-access.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/synchronizer-access.html)



This section describes the Synchronizer.

## Synchronizer overview

In Apigee hybrid, the Synchronizer's primary job is to poll and download the runtime contracts which are supplied by the management plane. Information communicated by contract includes API proxies, API products, caches, and virtual hosts. Synchronizer by default stores environment configuration data in the Cassandra database.

Synchronizer instances running in the runtime-plane are expected to poll the management plane on a regular basis, download the contracts and make the same available to local runtime instances.

One Synchronizer can support many Message Processors deployed in the same pod.

## Enable Synchronizer access

You must grant the [Synchronizer](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/what-is-hybrid#synchronizer) permission to pull down Apigee artifacts, such as proxy bundles and resources from the management plane. You must call an Apigee API to authorize the Synchronizer to pull artifacts down from the management plane to the runtime plane. 

  1. Ensure that you have enabled the Apigee API as explained in the Google Cloud setup steps. For details, see [Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-enableapi).
  2. Locate the **write-enabled Google Cloud service account key** (a JSON file) that you downloaded as part of [Create service accounts and credentials](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-service-accounts). The service account has the **Apigee Org Admin** role and is the one named "apigee-org-admin". If you did not previously create this service account, you must do so before continuing. 
  3. Use the Apigee Org Admin service account key to generate an OAuth 2.0 access token. This token is required to authenticate the [Apigee APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest). 

Use [gcloud](https://docs.cloud.google.com/sdk/docs) to obtain an OAuth 2.0 access token, passing the service account credentials JSON file that you downloaded using `GOOGLE_APPLICATION_CREDENTIALS` environment variable:
         
         export GOOGLE_APPLICATION_CREDENTIALS=your_sa_credentials_file.json
         gcloud auth application-default print-access-token

An OAuth2.0 token is returned.

For more information, see [gcloud beta auth application-default print-access-token](https://docs.cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/print-access-token).

  4. Copy the OAuth 2.0 token returned and store it in a variable, such as `TOKEN`. For example: 
         
         export TOKEN=ya29....Ts13inj3LrqMJlztwygtM

  5. Call the [setSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setSyncAuthorization) API to enable the required permissions for Synchronizer: **TIP:** If your are using Terraform, you can use the [`google_apigee_sync_authorization` Terraform attribute](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_sync_authorization) instead of calling the `setSyncAuthorization` API. **IMPORTANT:** Be sure that the service account name that you add to this API has the **Apigee Synchronizer Manager** role. For more information about service accounts, see [Create service accounts and credentials](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-service-accounts). 

### No data residency
         
         curl -X POST -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/YOUR_ORG_NAME:setSyncAuthorization" \
            -d '{"identities":["serviceAccount:SYNCHRONIZER_MANAGER_SERVICE_ACCOUNT_NAME"]}'
         

Where:

     * `YOUR_ORG_NAME`: The name of the hybrid organization.
     * `SYNCHRONIZER_MANAGER_SERVICE_ACCOUNT_NAME`: The name of a service account with the **Apigee Synchronizer Manager** role. The name is formed like an email address. For example: `my-synchronizer-manager-service_account@my_project_id.iam.gserviceaccount.com`

Example:
    
    curl -X POST -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type:application/json" \
      "https://apigee.googleapis.com/v1/organizations/my_org:setSyncAuthorization" \
       -d '{"identities":["serviceAccount:my-synchronizer-manager-service_account@my_project_id.iam.gserviceaccount.com"]}'
    

### Data residency
    
    curl -X POST -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type:application/json" \
      "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/YOUR_ORG_NAME:setSyncAuthorization" \
       -d '{"identities":["serviceAccount:SYNCHRONIZER_MANAGER_SERVICE_ACCOUNT_NAME"]}'
    

Where:

     * `YOUR_ORG_NAME`: The name of the hybrid organization.
     * `CONTROL_PLANE_LOCATION`: The location for your control plane data if your hybrid installation uses [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). This is location where customer core content like proxy bundles are stored. For a list see [Available Apigee API control plane regions](https://cloud.devsite.corp.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).
     * `SYNCHRONIZER_MANAGER_SERVICE_ACCOUNT_NAME`: The name of a service account with the **Apigee Synchronizer Manager** role. The name is formed like an email address. For example: `my-synchronizer-manager-service_account@my_project_id.iam.gserviceaccount.com`

Example:
    
    curl -X POST -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type:application/json" \
      "https://us-apigee.googleapis.com/v1/organizations/my_org:setSyncAuthorization" \
       -d '{"identities":["serviceAccount:my-synchronizer-manager-service_account@my_project_id.iam.gserviceaccount.com"]}'
    

For more information on this API, see [setSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setSyncAuthorization) API.

  6. To verify that the service account was set, call the following API to get a list of service accounts: 

### No data residency
         
         curl -X POST -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/your_org_name:getSyncAuthorization" \
            -d ''

### Data residency
         
         curl -X POST -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type:application/json" \
           "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/your_org_name:getSyncAuthorization" \
            -d ''

The output looks similar to the following:
         
         {
            "identities":[
               "serviceAccount:my-synchronizer-manager-service_account@my_project_id.iam.gserviceaccount.com"
            ],
            "etag":"BwWJgyS8I4w="
         }




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
