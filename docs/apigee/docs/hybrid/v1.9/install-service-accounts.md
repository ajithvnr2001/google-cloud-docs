---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts/
title: Step 4: Create service accounts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:09:24.349605+00:00
---

# Step 4: Create service accounts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 4: Create service accounts Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-service-accounts.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-service-accounts.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-service-accounts.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-service-accounts.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-service-accounts.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-service-accounts.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-service-accounts.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-service-accounts.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-service-accounts.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-service-accounts.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-service-accounts.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-service-accounts.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-service-accounts.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-service-accounts.html)



This step explains how to create the Google Cloud service accounts that are required for Apigee hybrid to operate. 

## Create the service accounts

Apigee hybrid uses Google Cloud [ service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) to allow hybrid components to communicate by making authorized API calls. 

In this step, you use an Apigee hybrid command-line tool to create a set of service accounts and download the service account private key files.

In a production hybrid environment Apigee recommends using a separate service account for each component. For the purposes of this tutorial, you can create a single service account named "apigee-non-prod" that you can use for all components. 

To learn more about service accounts and read the full list of service accounts recommended for production environments, see the following: 

  * [About service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-about)
  * [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-about#recommended-sas)



Apigee provides a tool, `create-service-account`, that creates the service accounts, assigns the roles to the service accounts, and creates and downloads the key files for the service account in a single command. 

  * To learn more about `create-service-account` and all its options see, [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/create-service-account).
  * To learn about the related Google Cloud concepts, see [Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts) and [Creating and managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).


  1. Make sure your **HYBRID_FILES** and **PROJECT_ID** environment variables are set. 

**PROJECT_ID** must be set to your Google cloud project ID, because the `create-service-account` tool reads the **PROJECT_ID** environment variable to create the service accounts in the correct project.
         
         echo $HYBRID_FILES
         echo $PROJECT_ID

  2. Create a _non-prod_ service account with the following command. This command creates a single service account named `apigee-non-prod` for use in non-production environments and places the downloaded key file in the `$HYBRID_FILES/service-accounts` directory. 
         
         $HYBRID_FILES/tools/create-service-account --env non-prod --dir $HYBRID_FILES/service-accounts

**Note:** If you would prefer to create all the individual service accounts for a production environment, use the following command: 
         
         $HYBRID_FILES/tools/create-service-account **--env prod** --dir $HYBRID_FILES/service-accounts

If you see the following prompt, enter `y`: 
         
         [INFO]: gcloud configured project ID is project_id.
          Enter: y to proceed with creating service account in project: project_id
          Enter: n to abort.

If this is the first time you are creating an SA with a particular name assigned, then the tool creates it without further prompts. 

If, however, you see the following message and prompt, enter `y` to generate new keys:
         
         [INFO]: Service account apigee-non-prod@project_id.iam.gserviceaccount.com already exists.
         ...
          [INFO]: The service account might have keys associated with it. It is recommended to use existing keys.
          Press: y to generate new keys.(this does not deactivate existing keys)
          Press: n to skip generating new keys.

**Note:** The Cloud Pub/Sub API must be enabled in the Google Cloud project that owns the service account for Synchronizer. To see if you enabled this API, see [Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-enableapi). 
  3. Verify that the service account key was created using the following command. You are responsible for storing these private keys securely. The key filenames are prefixed with the name of your Google Cloud project. 
         
         ls $HYBRID_FILES/service-accounts

The result should look something like the following: 
         
         project_id-apigee-non-prod.json


**Tip:** Apigee hybrid includes a validator that checks your service accounts' key files and permissions when [apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cli-reference) applies the Apigee hybrid runtime components to your cluster. This validation is enabled by default. For more information, see [Service account validation](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-validation). 

You now have created service accounts and assigned the roles needed by the Apigee hybrid components. Next, create the TLS certificates required by the hybrid ingress gateway. 

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-cert-manager) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-apigeectl) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts) [(NEXT) Step 5: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-configure-cluster) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-hybrid-runtime) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-expose-apigee-ingress) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
