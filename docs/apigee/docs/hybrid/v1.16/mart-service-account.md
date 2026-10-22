---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/mart-service-account/
title: Configure the MART service account \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:24.189067+00:00
---

# Configure the MART service account  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/mart-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure the MART service account Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

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

MART and Apigee Connect require a Google Cloud service account for authentication.

**Note:** Installations on AKS, EKS, or GKE using Workload Identity Federation for GKE do not require a Google Cloud service account key file (`.json`). See [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-federated).

  1. Locate the key file for the `apigee-mart` service account. The file should have a `.json` extension. It should reside in the `apigee-org` directory or a subdirectory. 
     * **PROD** installations: `apigee-mart.json`
     * **NON-PROD** installations: `apigee-non-prod.json`
  2. If you do not see the MART service account file, create and download it with the `create-service-account` utility: 
     1. Make sure your `PROJECT_ID` environment variable is set: 
            
            echo $PROJECT_ID

Define it if needed:
            
            export PROJECT_ID=my-project-id

     2. Create the MART service account. You can find the `create-service-account` tool in: 
            
            APIGEE_HELM_CHARTS_HOME/
            └── apigee-operator/
                └── etc/
                    └── tools/
                        └── create-service-account
            
            
            

**Note:** See [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/create-service-account).

### PROD
            
            create-service-account \
              --env prod \
              --profile apigee-mart \
              --dir PATH_TO_apigee-org_CHART_DIR

### NON-PROD
            
            $HYBRID_FILES/tools/create-service-account \
              --env non-prod \
              --profile apigee-mart \
              --dir PATH_TO_apigee-org_CHART_DIR/

  3. Edit your `overrides.yaml` file and add the key file path to the `connectAgent` and `mart.serviceAccountPath` properties: 

### PROD
         
         connectAgent:
           **serviceAccountPath: path_to_apigee-mart.json**
         
         mart:
           **serviceAccountPath: path_to_apigee-mart.json**

### NON-PROD
         
         connectAgent:
           **serviceAccountPath: path_to_apigee-non-prod.json**
         
         mart:
           **serviceAccountPath: path_to_apigee-non-prod.json**

For example: 
         
         ...
               connectAgent:
                 **serviceAccountPath: /apigee/hybrid/helm-charts/apigee-org/apigee-mart.json**
         
               mart:
                 **serviceAccountPath: /apigee/hybrid/helm-charts/apigee-org/apigee-mart.json**
               ...

  4. Apply your changes: 
         
         helm upgrade ORG_NAME apigee-org/ \
           --namespace apigee \
           --atomic \
           -f OVERRIDES_FILE.yaml
         

**Note:** If you see an error saying `Error: UPGRADE FAILED: "_ORG_NAME_ " has no deployed releases`, replace `upgrade` with `install` and try the command again.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
