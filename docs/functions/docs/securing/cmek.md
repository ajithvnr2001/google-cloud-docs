---
url: https://docs.cloud.google.com/functions/docs/securing/cmek/
title: Protect your data with CMEK \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:05.037575+00:00
---

# Protect your data with CMEK  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/securing/cmek/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Protect your data with CMEK

This page provides supplemental information for protecting your data with customer-managed encryption keys (CMEKs) for functions created using [`gcloud functions`](https://docs.cloud.google.com/sdk/gcloud/reference/functions) commands or the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/reference/rest).

For a detailed description of CMEK, including manual setup, using Autokey, and testing CMEK protection, refer to [Cloud Run documentation](https://docs.cloud.google.com/run/docs/securing/using-cmek).

The following types of Cloud Run functions data are encrypted when using a CMEK:

  * Function source code uploaded for deployment and stored by Google in Cloud Storage, used in the build process.
  * The results of the function build process, including: 
    * The container image built from your function source code.
    * Each instance of the function that is deployed.



The function build process itself is protected by an ephemeral key uniquely generated for each build. See [CMEK compliance in Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/cmek) for more information. Additionally, note the following:

  * File metadata, such as file system paths or modification timestamps, is not encrypted.

  * If a key is disabled, the container image cannot be deployed and new instances cannot start.

  * Cloud Run functions CMEK protection only applies to Google-managed Cloud Run functions resources; you are responsible for protecting data and resources managed by you, such as your source code repositories, [event channels](https://docs.cloud.google.com/eventarc/docs/third-parties/third-parties-overview#subscription-terms) that live in the customer project, or any services used by your functions.




## Before you begin

  1. Create a single-region key to use to encrypt your functions. To learn how to create a key, see [Creating symmetric encryption keys](https://docs.cloud.google.com/kms/docs/creating-keys).

  2. [Create an Artifact Registry repository](https://docs.cloud.google.com/artifact-registry/docs/manage-repos#create) that has [CMEK enabled](https://docs.cloud.google.com/artifact-registry/docs/cmek). You must use the same key for the Artifact Registry repository as you do when enabling CMEK for a function.

  3. For event-driven functions, follow the additional setup steps outlined in [Enable CMEK for a Google channel](https://docs.cloud.google.com/eventarc/docs/use-cmek#enable-cmek-google-channel).




## Granting service accounts access to the key

For all functions, you must grant the following service accounts access to the key:

  * Cloud Run functions service agent (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`)

  * Artifact Registry service agent (`service-PROJECT_NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com`)

  * Cloud Storage service agent (`service-PROJECT_NUMBER@gs-project-accounts.iam.gserviceaccount.com`)

  * Cloud Run service agent (`service-PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com`)

  * Eventarc service agent (`service-PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com`)




To grant these service accounts access to the key, add each service account as a principal of the key and then grant the service account the `Cloud KMS CryptoKey Encrypter/Decrypter` role:

###  Console 

  1. Go to the Cloud Key Management Service page in the Google Cloud console:   
[Go to the Cloud KMS page](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the chosen key.

  3. Click the name of the key to view the key details.

  4. In the **Permissions** tab, click **Grant access**.

  5. In the **New principals** field, enter the email addresses of all three service accounts discussed earlier to assign permissions to all three accounts at once.

  6. In the **Select a role** menu, select **Cloud KMS CryptoKey Encrypter/Decrypter**.

  7. Click **Save**.




###  gcloud 

For each service account discussed earlier, run the following command:
    
    
    gcloud kms keys add-iam-policy-binding KEY \
      --keyring KEY_RING \
      --location LOCATION \
      --member serviceAccount:SERVICE_AGENT_EMAIL \
      --role roles/cloudkms.cryptoKeyEncrypterDecrypter

Replace the following:

  * `KEY`: The name of the key. For example, `my-key`.

  * `KEY_RING`: The name of the key ring. For example, `my-keyring`.

  * `LOCATION`: The location of the key. For example, `us-central1`.

  * `SERVICE_AGENT_EMAIL`: The email address of the service account.




**Important:** Some service agents, such as the Cloud Storage service agent (including its email address), are not initially available when you create a project. Instead, they are activated the first time you access them. For example, to activate the Cloud Storage service agent, you can [retrieve its email address](https://docs.cloud.google.com/storage/docs/getting-service-agent). The service agent must be activated prior to assigning permissions to it.

## Enabling CMEK for a function

After setting up an Artifact Registry repository with CMEK enabled and granting Cloud Run functions access to your key, you're ready to enable CMEK for your function.

To enable CMEK for a function, run the following command:
    
    
    gcloud functions deploy FUNCTION \
        --kms-key=KEY \
        --docker-repository=REPOSITORY \
        --source=YOUR_SOURCE_LOCATION
        FLAGS...
     

Replace the following:

  * `FUNCTION`: The name of the function to enable CMEK on. For example, `cmek-function`.

  * `KEY`: The fully qualified key name, in the following format: `projects/PROJECT_NAME/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME`.

  * `REPOSITORY`: The fully qualified Artifact Registry repository name, in the following format: `projects/PROJECT_NAME/locations/LOCATION/repositories/REPOSITORY`.

  * `YOUR_SOURCE_LOCATION`: When enabling CMEK for a pre-existing function, make sure that the intended source code is being re-deployed by specifying this parameter explicitly.

  * `FLAGS...`: Additional flags that may be required to deploy your function, particularly for create deployments. For details, see [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/docs/deploy#basics).




CMEK is enabled for the function. Optionally, enable [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy) to enforce all new functions to be CMEK compliant.

**Note:** First-time function deployments with CMEK enabled might fail due to IAM propagation delays. If you encounter an error upon deployment, ensure the permissions are set correctly and try again after a short period.

Note that Cloud Run functions always uses the primary version of a key for CMEK protection. You cannot specify a particular key version to use when enabling CMEK for your functions.

If a key is [destroyed](https://docs.cloud.google.com/kms/docs/destroy-restore) or [disabled](https://docs.cloud.google.com/kms/docs/enable-disable), or the requisite permissions on it are revoked, active instances of functions protected by that key are not shut down. Function executions already in progress will continue to run, but new executions will fail as long as Cloud Run functions does not have access to the key.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
