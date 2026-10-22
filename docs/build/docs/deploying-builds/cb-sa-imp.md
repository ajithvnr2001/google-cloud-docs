---
url: https://docs.cloud.google.com/build/docs/deploying-builds/cb-sa-imp/
title: Configure Cloud Build service account impersonation for managed services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:16.260722+00:00
---

# Configure Cloud Build service account impersonation for managed services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/deploying-builds/cb-sa-imp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Configure Cloud Build service account impersonation for managed services Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure your Cloud Build service account to [impersonate service accounts](https://docs.cloud.google.com/iam/docs/service-account-impersonation) for Runtime, Compute Engine, or App Engine so that you can deploy images to managed services.

## Overview

When an image is deployed to specific managed services, the image runs using the identity of the service account for that managed service. Because Cloud Build can deploy new instances or versions automatically, your [specified Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) or the [default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) must be able to impersonate the service account of your managed service. This requirement applies when deploying to the following managed services:

Managed Service | Service Account  
---|---  
App Engine | [App Engine service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts)  
Cloud Run functions | [Runtime service account](https://docs.cloud.google.com/functions/docs/securing/function-identity)  
Cloud Run | [Service identity](https://docs.cloud.google.com/run/docs/configuring/services/service-identity)  
Compute Engine | [Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts)  
  
## Set up service account impersonation

To configure your Cloud Build service account to impersonate another service account, do the following:

###  console 

  1. Go to the _settings_ Cloud Build **Permissions** page.

  2. Select your Cloud Build service account.

  3. Enable the required IAM role for your managed service:

Managed Service | Required Role  
---|---  
App Engine | App Engine Admin ( `roles/appengine.appAdmin` )  
Cloud Run functions | Cloud Functions Developer ( `roles/cloudfunctions.developer` )  
Cloud Run | Cloud Run Admin ( `roles/run.admin` )  
Compute Engine | Compute Instance Admin v1 ( `roles/compute.instanceAdmin.v1` )  
  
Cloud Build shows the **Assign Service Account User Role** panel.

  4. Choose a service account to impersonate. For example, if you plan to deploy to Compute Engine and enabled the Compute Instance Admin v1 role, you would choose the Compute Engine service account that you want your Cloud Build service account to impersonate.

  5. Click **Grant permission**.




###  gcloud CLI 

In the Google Cloud CLI, enter the following:
    
    
      gcloud iam service-accounts add-iam-policy-binding \
            SERVICE_ACCOUNT_TO_IMPERSONATE \
            --member="CLOUD_BUILD_SERVICE_ACCOUNT" \
            --role="roles/iam.serviceAccountUser"
    

Where:

  * SERVICE_ACCOUNT_TO_IMPERSONATE is the service account that you want to impersonate.
  * CLOUD_BUILD_SERVICE_ACCOUNT is your Cloud Build service account.



Cloud Build assigns your Cloud Build service account the Service Account User (`roles/iam.serviceAccountUser`) role for the service account that you want to impersonate.

The Service Account User role lets a principal attach a service account to a resource, allowing your Cloud Build service account to impersonate your chosen managed service account. For more information, see [Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) and [Attach service accounts to resources](https://docs.cloud.google.com/iam/docs/attach-service-accounts) in the IAM documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
