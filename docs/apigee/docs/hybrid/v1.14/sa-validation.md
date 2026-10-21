---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-validation/
title: Service account validation \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:48:36.461273+00:00
---

# Service account validation  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Service account validation Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.14 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.14 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/sa-validation.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-validation.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/sa-validation.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-validation.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/sa-validation.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/sa-validation.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/sa-validation.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/sa-validation.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-validation.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/sa-validation.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/sa-validation.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/sa-validation.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/sa-validation.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/sa-validation.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/sa-validation.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/sa-validation.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/sa-validation.html)



Apigee hybrid provides validation that ensures the location of your service accounts' keys are correct and that the accounts have the proper permissions in your Google Cloud project. This validation is enabled by default.

This section describes how to enable or disable service account validation. In addition, this step ensures that you have the proper APIs enabled for your Google Cloud project so that validation works.

## Enable service account permission validation

**To enable permission validation:**

  1. Be sure the [ Cloud Resource Manager API](https://cloud.google.com/resource-manager/reference/rest/) is enabled for your Google Cloud project: 
     1. Open the [Google Cloud console](https://console.cloud.google.com) and log in with the account you created in [Step 1: Create a Google Cloud account](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-gcpaccount).
     2. Select the project that you created in [Step 2: Create a Google Cloud project](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-gcpproject).
     3. Select **APIs & Services > Library**.
     4. Search for "Cloud Resource Manager".
     5. Locate the **Cloud Resource Manager API** service and click on it.
     6. If it is not enabled, click **Enable**.

You can also enable the API using gcloud:
    
    gcloud services enable cloudresourcemanager.googleapis.com --project GCP_PROJECT_ID

  2. In your overrides file, add the `validateServiceAccounts` property and set it to `true`. For example: 
         
         ...
         # Enables strict validation of service account permissions.
         validateServiceAccounts: true
         ...




When validation is enabled, any time you apply configuration changes to the Apigee hybrid runtime components to your cluster, the Helm chart validates the [service account](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-serviceaccounts) keys that are included in your overrides file.

**NOTE:** Service account JSON key format validation is always performed. You do not have to take any steps to enable this validation and you cannot disable it. 

##  Troubleshooting validation errors 

**Deleting and recreating service accounts:** Note that reusing the name of a deleted service account may result in unexpected behavior. If you create a service account and delete it, always recreate it with a different name than the original SA. For details, see [ Deleting and recreating service accounts](https://cloud.google.com/iam/docs/service-account-overview#deleting-recreating). 

If validation fails, the runtime deployment stops, and `helm upgrade` or `helm install` exits. To troubleshoot service account failure, it's helpful to know that validation checks permissions in this order: 

  1. Permission on the project ID.
  2. (For UDCA and Synchronizer only) If the permission check on the project fails, validation proceeds to check permission against the Apigee environment's [IAM policy](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/setIamPolicy). These SAs are environment scoped and environments support finer-grained permissions. 

To update the IAM policy for a specific environment, go to the hybrid UI. Go to **Admin > Environments > Access**




For example, the following is an error message for a failed permission check: 
    
    
    Invalid Metrics Service Account. Service Account
    "apigee-metrics@hybrid-project.iam.gserviceaccount.com" is **missing 1 or more required
    permissions** [monitoring.metricDescriptors.create monitoring.metricDescriptors.get monitoring.metricDescriptors.list
    monitoring.monitoredResourceDescriptors.get monitoring.monitoredResourceDescriptors.list monitoring.timeSeries.create].
    Visit [Service accounts and roles used by
    hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-serviceaccounts#recommended-sas) for more details on setting up Apigee hybrid service account permissions.

To address this error, add the required roles to the service account. For information on creating and modifying service accounts, see [ Create the service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-about#create-the-service-accounts). To check the required permissions for each Apigee hybrid component, see [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/sa-about#recommended-sas). 

## Disable permission validation

To disable service account permission validation, set the `validationServiceAccounts` property in your overrides file to `false`, as the following example shows:
    
    
    ...
    # Enables strict validation of service account permissions.
    validateServiceAccounts: false
    ...

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
