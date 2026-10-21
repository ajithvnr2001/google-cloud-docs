---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-service-accounts/
title: Step 4: Create service accounts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:39:51.764910+00:00
---

# Step 4: Create service accounts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 4: Create service accounts Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.11 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.11 keyboard_arrow_down

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

## Overview

Apigee hybrid uses Google Cloud [ service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) to allow hybrid components to communicate by making authorized API calls. 

### Production vs. non-production environments

This guide refers to _Production_ ("Prod") and _Non-production_ ("Non-prod") installations. A production installation is tuned for greater usage capacity, storage, and scalability. A non-production installation uses fewer resources and is mainly for learning and demonstration purposes. 

When you create and configure service accounts for Apigee hybrid, it is important to be aware of the type of installation you are targeting. 

For _production_ installations, we recommend creating a separate service account for each Apigee hybrid component. For example, runtime, mart, metrics, udca, and so on each get their own service account. 

For _non-prod_ installations, you can create a single service account that applies to all the components. 

To learn more about the service accounts used by Apigee and the roles they are assigned, see [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/sa-about#recommended-sas). 

### Workload Identity on GKE

For Apigee hybrid installations on GKE, Google Cloud offers an option called [workload identity](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity) to authenticate hybrid runtime components. This option does not use downloaded certificate files to authenticate the service accounts, Instead, it associates the Google Cloud service accounts that you create in this step with Kubernetes service accounts in the Kubernetes cluster. 

Workload Identity is only available on GKE installations.

## Create the service accounts

### `create-service-account`

Use the `create-service-account` tool in the following circumstances:

  * You are installing on a platform other than GKE
  * You are installing on GKE but do not plan to use workload identity.



Otherwise, skip to Create service accounts in the Google Cloud console or with `gcloud`. 

  1. Make sure your **HYBRID_FILES** and **PROJECT_ID** environment variables are set. 

**PROJECT_ID** must be set to your Google cloud project ID, because the `create-service-account` tool reads the **PROJECT_ID** environment variable to create the service accounts in the correct project.
         
         echo $HYBRID_FILES
         echo $PROJECT_ID

  2. Create the service account with the following command: 

### Non-prod

This command creates a single service account named `apigee-non-prod` for use in a non-production installation and downloads the key file for the service account in the `$HYBRID_FILES/service-accounts` directory.
         
         $HYBRID_FILES/tools/create-service-account --env non-prod --dir $HYBRID_FILES/service-accounts

### Production

This command creates all the individual service accounts for a _production_ installation and downloads the key files for the service accounts in the `$HYBRID_FILES/service-accounts` directory.
         
         $HYBRID_FILES/tools/create-service-account --env prod --dir $HYBRID_FILES/service-accounts

If you see the following prompt, enter `y`: 
         
         [INFO]: gcloud configured project ID is project_id.
         Enter: y to proceed with creating service account in project: project_id
         Enter: n to abort.

If you are installing Apigee hybrid on a platform other than GKE, or if you are installing on GKE but do not want to use workload identity, Use the Apigee provided tool, create-service-account, to create the service accounts, assign the roles to the service accounts, and create and download the key files for the service account in a single command. 

If this is the first time you are creating a particular service account, then the tool creates it without further prompts. 

If, however, you see the following message and prompt, enter `y` to generate new keys:
         
         [INFO]: Service account apigee-non-prod@project_id.iam.gserviceaccount.com already exists.
         ...
         [INFO]: The service account might have keys associated with it. It is recommended to use existing keys.
         Press: y to generate new keys.(this does not deactivate existing keys)
         Press: n to skip generating new keys.

**Note:** The Cloud Pub/Sub API must be enabled in the Google Cloud project that owns the service account for Synchronizer. To see if you enabled this API, see [Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-enableapi). 
  3. Verify that the service account key was created using the following command. You are responsible for storing these private keys securely. The key filenames are prefixed with the name of your Google Cloud project. 
         
         ls $HYBRID_FILES/service-accounts

The result should look something like the following: 
         
         project_id-apigee-non-prod.json

**Tip:** Apigee hybrid includes a validator that checks your service accounts' key files and permissions when [apigeectl](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cli-reference) applies the Apigee hybrid runtime components to your cluster. This validation is enabled by default. For more information, see [Service account validation](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/sa-validation). 
     * To learn more about `create-service-account` and all its options see, [`create-service-account`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/create-service-account).
     * To learn about the related Google Cloud concepts, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) and [Creating and managing service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).



If you plan to use [workload identity](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/enable-workload-identity) on GKE to authenticate hybrid runtime components, you do not need to create and download certificate files for the service accounts. Therefore, do not use the `create-service-account` tool. Instead, create the service accounts in the Google Cloud console or with the IAM API in `gcloud`. 

Follow the instructions in [Create service accounts using](https://docs.cloud.google.com/docs/service-accounts-create#iam-service-accounts-create-console) to create the following service accounts and assign the following roles to them: 

### Console

### **Non-prod**

For non-production installations:

Service account name | IAM roles  
---|---  
`apigee-non-prod` | 

  * Apigee Analytics Agent
  * Apigee Connect Agent
  * Apigee Runtime Agent
  * Apigee Synchronizer Manager
  * Logs Writer
  * Monitoring Metric Writer
  * Storage Object Admin

  
  
### **Production**

For production installations:

**Production installations**  
---  
Service account name | IAM roles  
`apigee-cassandra` | Storage Object Admin  
`apigee-logger` | Logs Writer  
`apigee-mart` | Apigee Connect Agent  
`apigee-metrics` | Monitoring Metric Writer  
`apigee-runtime` | _No role required_  
`apigee-synchronizer` | Apigee Synchronizer Manager  
`apigee-udca` | Apigee Analytics Agent  
`apigee-watcher` | Apigee Runtime Agent  
  
Use the following commands to create the service accounts and assign the IAM roles. 

### `gcloud`

### **Non-prod**

For non-production installations:

  1. Create the `apigee-non-prod` service account: 
         
         gcloud iam service-accounts create apigee-non-prod \
           --display-name="apigee-non-prod" \
           --project=$PROJECT_ID

  2. Assign the IAM roles to the service account: 
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/storage.objectAdmin"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/apigeeconnect.Agent"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.metricWriter"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/apigee.synchronizerManager"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/apigee.analyticsAgent"
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/apigee.runtimeAgent"

  3. Verify the role bindings: 
         
         gcloud projects get-iam-policy ${PROJECT_ID} \
           --flatten="bindings[].members" \
           --format='table(bindings.role)' \
           --filter="bindings.members:apigee-non-prod@$PROJECT_ID.iam.gserviceaccount.com"




### **Production**

For production installations:

Use the following commands to create each service account and assign the corresponding IAM role. 

  1. **`apigee-cassandra`** service account: 
         
         gcloud iam service-accounts create apigee-cassandra \
           --display-name="apigee-cassandra" \
           --project=$PROJECT_ID
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-cassandra@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/storage.objectAdmin"

  2. **`apigee-logger`** service account: 
         
         gcloud iam service-accounts create apigee-logger \
           --display-name="apigee-logger" \
           --project=$PROJECT_ID
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-logger@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"

  3. **`apigee-mart`** service account: 
         
         gcloud iam service-accounts create apigee-mart \
           --display-name="apigee-mart" \
           --project=$PROJECT_ID
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-mart@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/apigeeconnect.Agent"

  4. **`apigee-metrics`** service account: 
         
         gcloud iam service-accounts create apigee-metrics \
           --display-name="apigee-metrics" \
           --project=$PROJECT_ID
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-metrics@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/monitoring.metricWriter"

  5. **`apigee-runtime`** service account: 
         
         gcloud iam service-accounts create apigee-runtime \
           --display-name="apigee-runtime" \
           --project=$PROJECT_ID

  6. **`apigee-synchronizer`** service account: 
         
         gcloud iam service-accounts create apigee-synchronizer \
           --display-name="apigee-synchronizer" \
           --project=$PROJECT_ID
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-synchronizer@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/apigee.synchronizerManager"

  7. **`apigee-udca`** service account: 
         
         gcloud iam service-accounts create apigee-udca \
           --display-name="apigee-udca" \
           --project=$PROJECT_ID
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-udca@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/apigee.analyticsAgent"

  8. **`apigee-watcher`** service account: 
         
         gcloud iam service-accounts create apigee-watcher \
           --display-name="apigee-watcher" \
           --project=$PROJECT_ID
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
           --member="serviceAccount:apigee-watcher@$PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/apigee.runtimeAgent"




To learn more about creating service accounts with `gcloud`, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating). 

You now have created service accounts and assigned the roles needed by the Apigee hybrid components. Next, create the TLS certificates required by the hybrid ingress gateway. 

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-cert-manager) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-apigeectl) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-service-accounts) [(NEXT) Step 5: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-configure-cluster) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-check-cluster) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-hybrid-runtime) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-workload-identity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
