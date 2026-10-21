---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/mart-service-account/
title: Configure the MART service account \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:53:11.854465+00:00
---

# Configure the MART service account  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/mart-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure the MART service account Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/mart-service-account.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/mart-service-account.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/mart-service-account.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/mart-service-account.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/mart-service-account.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/mart-service-account.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/mart-service-account.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/mart-service-account.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/mart-service-account.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/mart-service-account.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/mart-service-account.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/mart-service-account.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/mart-service-account.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/mart-service-account.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/mart-service-account.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/mart-service-account.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/mart-service-account.html)



This topic explains how to configure the MART service account. 

## Adding the MART service account 

MART requires a Google Cloud service account for authentication.

**Note:** Installations on GKE using workload identity do not require a Google Cloud service account. See [Enabling Workload Identity with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/enable-workload-identity).

  1. Locate the key file for the `apigee-mart` service account. The file should have a `.json` extension. 
         
         ls $HYBRID_FILES/service-accounts

     * **PROD** installations: `apigee-mart.json`
     * **NON-PROD** installations: `apigee-non-prod.json`
  2. If you do not see the MART service account file, create and download it with the `create-service-account` utility: 
     1. Make sure your `PROJECT_ID` environment variable is set: 
            
            echo $PROJECT_ID

Define it if needed:
            
            export PROJECT_ID=my-project-id

     2. Create the MART service account: 

### PROD
            
            $HYBRID_FILES/tools/create-service-account \
              --env prod \
              --profile apigee-mart \
              --dir $HYBRID_FILES/service-accounts

### NON-PROD
            
            $HYBRID_FILES/tools/create-service-account \
              --env non-prod \
              --profile apigee-mart \
              --dir $HYBRID_FILES/service-accounts

  3. Edit your `overrides.yaml` file and add the key file path to the `mart.serviceAccountPath` property: 

### PROD
         
         ...
         mart:
           **serviceAccountPath: path_to_apigee-mart.json**
         ...

### NON-PROD
         
         ...
         mart:
           **serviceAccountPath: path_to_apigee-non-prod.json**
         ...

For example: 
         
         ...
         mart:
           **serviceAccountPath: /apigee/hybrid/hyprid-files/service-accounts/apigee-mart.json**
         ...

  4. Apply your changes with `apigeectl apply`: 
         
         $APIGEECTL_HOME/apigeectl apply -f overrides/overrides.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
