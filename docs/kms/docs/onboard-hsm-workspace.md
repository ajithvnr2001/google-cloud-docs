---
url: https://docs.cloud.google.com/kms/docs/onboard-hsm-workspace/
title: Onboard to Cloud HSM for Google Workspace \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:35.570307+00:00
---

# Onboard to Cloud HSM for Google Workspace  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/onboard-hsm-workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Onboard to Cloud HSM for Google Workspace Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to onboard Cloud HSM for Google Workspace (CHGWS), the encryption key service for Google Workspace offered by Cloud Key Management Service (Cloud KMS). Cloud HSM for Google Workspace provides enhanced privacy controls for Google Workspace, helping you achieve regulatory standards such as [DISA IL5](https://cloud.google.com/security/compliance/disa#services-in-scope) and elevate data security. Cloud HSM is a standards-aligned, highly available, and fully managed key management service operated at cloud scale with hardware-backed keys stored in FIPS 140-2 Level 3 compliant HSMs (hardware security modules).

CHGWS is compatible with both Multi-tenant Cloud HSM and Single-tenant Cloud HSM keys.

For more information, see [Cloud HSM for Google Workspace](https://docs.cloud.google.com/kms/docs/hsm-for-workspace).

## Automated onboarding support

The Google Workspace Admin console has an automated onboarding process that is considerably faster than onboarding manually. However, automated onboarding is only supported if you meet all of the following criteria:

  * You're setting up Google Workspace client-side encryption (CSE) for the first time.
  * You're using Google Identity as your identity provider (IdP).
  * You're using Multi-tenant Cloud HSM keys.



If you meet all these criteria, go to the Admin console and complete the [automated onboarding process](https://knowledge.workspace.google.com/admin/security/set-up-cse-simplified).

You'll have to onboard manually if you meet any of the following criteria:

  * You use a third-party IdP.
  * You use Single-tenant Cloud HSM.
  * You plan to migrate keys from another key service.
  * You want to modify an existing Cloud HSM for Google Workspace configuration.



If you meet any of these criteria, follow the setup instructions in this document.

## Before you begin

Before you onboard Cloud HSM for Google Workspace, complete the following prerequisites:

  * Set up a Google Workspace.
  * Enable Google Workspace Client-side Encryption (CSE) in your Google Workspace.
  * Configure your Identity Provider (IdP) in Google Workspace CSE. Note the Client ID for your IdP. If you use Google Identity Platform, find the Client ID in your Google Cloud project.
  * Optional: If you allow access to CSE-encrypted content on platform applications other than web (such as mobile or desktop), add the client IDs for those platforms in your IdP settings in the Google Workspace Admin Console. Note all client IDs for this IdP. If you use Google Identity Platform, find these client IDs in your Google Cloud project. For other Identity Providers, create these client IDs separately.



## Compatible locations

You can store your Cloud KMS keys in any regional or multi-regional location within the **US** or **Europe** geographic areas. Cloud HSM for Google Workspace supports both Multi-tenant Cloud HSM and Single-tenant Cloud HSM keys. To find a specific location, visit [Cloud KMS Locations](https://docs.cloud.google.com/kms/docs/locations) and filter by your HSM type.

Cloud HSM for Google Workspace automatically provides the endpoint in one of the following multi-regions closest to your key location:

  * us
  * eur3



## Set up a Google Cloud project for Cloud KMS

Cloud HSM for Google Workspace endpoints rely on Cloud KMS keys for cryptographic operations. Set up a new Google Cloud project to host the Cloud KMS keys.

  1. [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project). This is your key project. Make note of the project ID and project number; you need these to complete the setup.

**Important:** We strongly recommend that you use a dedicated Google Cloud project that only contains CHGWS keys. This gives you greater control over billing. For more information, see Manage billing.
  2. [Enable billing on the project that you created.](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project)

  3. Enable the Cloud KMS API in your Google Cloud key project.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

  4. In the Google Cloud console, click terminal **Activate Cloud Shell**.

  5. Verify that you are in the correct project by comparing your project ID with the project ID in the Cloud Shell prompt.

  6. Using Cloud Shell, create the Cloud HSM for Google Workspace service account:
         
         gcloud beta services identity create \
             --service=cloudkmskacls-pa.googleapis.com
         

Note the service identity created by this command. You need the service identity name in the next step.

  7. Grant the **CHGWS key Service Agent** role to the service account that you created:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudkmskacls.iam.gserviceaccount.com \
             --role=roles/cloudkmskacls.serviceAgent
         

Replace the following:

     * `PROJECT_ID`: The project ID of your key project.
     * `PROJECT_NUMBER`: The project number of your key project.



## Manage CHGWS service endpoint

The following sections show you how to set up and manage your CHGWS endpoints.

### Set up Cloud KMS keys

Set up the Cloud KMS resources for your CHGWS key service endpoint.

  1. Create a key ring in one of the supported regions:
         
         gcloud kms keyrings create KEY_RING --location LOCATION
         

     * Replace `KEY_RING` with the name that you want to use for your CHGWS key ring—for example, `CHGWS_KEY_RING`.
     * Replace `LOCATION` with the location where you want to create your key ring—for example, `us`.
  2. Create a Cloud HSM key.

###  Multi-tenant Cloud HSM 

To create a key with the `hsm` protection level:
         
         gcloud kms keys create KEY_NAME \
             --protection-level "hsm" \
             --keyring KEY_RING \
             --location LOCATION \
             --purpose "encryption" \
             --rotation-period ROTATION_PERIOD \
             --next-rotation-time NEXT_ROTATION_TIME
         

Replace the following:

     * `KEY_NAME`: The name that you want to use for your key—for example, `CHGWS_KEY`.
     * `KEY_RING`: The name of your key ring—for example, `CHGWS_KEY_RING`.
     * `LOCATION`: The location where you created your key ring—for example, `us`.
     * `ROTATION_PERIOD`: The frequency at which you want to rotate your keys—for example, `7d`.
     * `NEXT_ROTATION_TIME`: The date and time when the next key rotation occurs—for example, `2024-03-20T01:00:00`.

###  Single-tenant Cloud HSM 

To create a key with the `hsm_single_tenant` protection level, you must first have a Single-tenant Cloud HSM instance provisioned in the same location.

     1. **Create and provision a Single-tenant Cloud HSM instance:** Follow the instructions in the [Create and manage a Single-tenant Cloud HSM instance](https://docs.cloud.google.com/kms/docs/create-manage-single-tenant-hsm) guide. Make note of the provisioned Instance ID. You use it in the next step.

     2. **Create a key:**
            
            gcloud kms keys create KEY_NAME \
                --protection-level "hsm_single_tenant" \
                --keyring KEY_RING \
                --location LOCATION \
                --purpose "encryption" \
                --crypto-key-backend "projects/PROJECT_ID/locations/LOCATION/singleTenantHsmInstances/INSTANCE_NAME" \
                --rotation-period ROTATION_PERIOD \
                --next-rotation-time NEXT_ROTATION_TIME
            

Replace the following:

        * `KEY_NAME`: The name that you want to use for your key—for example, `CHGWS_KEY`.
        * `KEY_RING`: The name of your key ring—for example, `CHGWS_KEY_RING`.
        * `LOCATION`: The location where you created your key ring—for example, `us`.
        * `PROJECT_ID`: The project ID of your key project.
        * `INSTANCE_NAME`: The name of the Single-tenant Cloud HSM instance where you want to create the key.
        * `ROTATION_PERIOD`: The frequency at which you want to rotate your keys—for example, `7d`.
        * `NEXT_ROTATION_TIME`: The date and time when the next key rotation occurs—for example, `2024-03-20T01:00:00`.

For more details on key creation options, see [Creating keys](https://docs.cloud.google.com/kms/docs/create-key).




### Request onboarding and endpoint creation

To request onboarding and endpoint creation, contact your account representative for assistance with submitting an endpoint onboarding request. In the request, include the following information:

  * **Google Workspace details**

    * **Google Workspace ID** : Your Google Workspace ID. Find your Google Workspace ID by following the instructions at [Find your customer ID](https://support.google.com/a/answer/10070793).

    * **Google Workspace administrator email addresses** : Provide a comma-separated list of administrator email addresses.

  * **Identity Provider (IdP) details**

    * **Primary Identity Provider (IdP) details** :

      * **IdP JSON Web Key Set (JWKS) URL** : For Google Identity Platform, use `https://www.googleapis.com/oauth2/v3/certs`.
      * **JSON Web Token (JWT) token issuer** : For Google Identity Platform, use `https://accounts.google.com`.
      * **JWT audience** : Your IdP's Client ID for web applications.
      * **Additional JWT audiences** : Optional. Provide client IDs for non-web platform applications if configured. For Google Identity Platform, use the client IDs given in [If you'll use Google identity for CSE](https://support.google.com/a/answer/10743588).
    * **Guest IdP details** : Optional. Complete this section if you're using a guest IdP.

      * **Guest IdP JWKS URL** : The JWKS URL of your guest IdP.
      * **Guest JWT token issuer** : The JWT token issuer of your guest IdP.
      * **Guest JWT audience** : Your guest IdP's Client ID for web applications, except for Google Meet.
      * **Guest additional JWT audiences** : Optional. If you configure a Google Meet web client ID or other non-web platform application client IDs, provide client IDs for each. For Google Identity Platform, use the client IDs given in [If you'll use Google identity for CSE](https://support.google.com/a/answer/10743588).
**Important:** Verify that your IdP JWKS URL is publicly accessible. Confirm the JWT Token Issuer and JWT Audience values with your IdP administrator.
  * **CSE Key details**

    * **Google Cloud Project ID** : `PROJECT_ID`
    * **Google Cloud Project Number** : `PROJECT_NUMBER`
    * **Cloud KMS keyring name** : `KEY_RING`
    * **Cloud KMS keyring location** : `LOCATION`
    * **Cloud KMS key name** : `KEY_NAME`
    * **Cloud KMS key protection level** : either `hsm` or `hsm_single_tenant`
    * **CHGWS Base URL** : Optional. A list of URLs to enable key migration. If you set up CHGWS for the first time for this Google Workspace, leave this field blank.
  * **Additional Details**

    * **Customer Name** : Provide customer name.
    * **Expected number of users** : Provide the expected number of users in your Google Workspace instance.



### Configure CHGWS endpoint in Google Workspace CSE

Configure Google Workspace CSE to use the CHGWS URL generated when you created the CHGWS endpoint. Follow the instructions at [Add and manage key services for client-side encryption](https://support.google.com/a/answer/10742487).

### Key Service Migration

CHGWS provides flexibility to move your key service to or from CHGWS. To start a key service migration, contact your account representative for assistance with submitting a migration request. In the request, include the following information:

  * **Endpoint ID** : The endpoint ID of CHGWS.
  * **Key Service URL** : A list of URLs to enable key service migration.

    * If you migrate to Cloud HSM for Google Workspace, then provide the base URL of each key service endpoint that you migrate from.
    * If you migrate from Cloud HSM for Google Workspace, provide the base URLs of the key service endpoints that you want to migrate to.
**Important:** If you migrate between two different Cloud HSM for Google Workspace endpoints, submit two separate requests: one _from_ the previous endpoint and the other _to_ the new endpoint.



### Delete or disable endpoints

Delete or disable operations on the Cloud HSM for Google Workspace endpoint are not directly supported. However, you can disable a Cloud HSM for Google Workspace endpoint by disabling all backing Cloud KMS key versions.

  * For each Cloud KMS key version backing the endpoint, run the following command:
        
        gcloud kms keys versions disable KEY_VERSION --keyring \
            KEY_RING --location LOCATION --key KEY_NAME
        

Replace the following:

    * `KEY_VERSION`: The version of the key that you want to disable—for example, `1`.
    * `KEY_RING`: The name of the key ring—for example, `CHGWS_KEY_RING`.
    * `LOCATION`: The location where you want to disable—for example, `us`.
    * `KEY_NAME`: The name of the key—for example, `CHGWS_KEY`.



### Enable endpoints

If you've disabled a CHGWS endpoint by disabling all key versions of the backing Cloud KMS key, then you can re-enable the CHGWS endpoint. To re-enable the endpoint, enable all active versions of the backing Cloud KMS key by using the following gcloud CLI command:

  * For each Cloud KMS key version backing the endpoint, run the following command:
        
        gcloud kms keys versions enable KEY_VERSION --keyring \
            KEY_RING --location LOCATION --key KEY_NAME
        

Replace the following:

    * `KEY_VERSION`: The version of the key that you want to enable—for example, `1`.
    * `KEY_RING`: The name of the key ring—for example, `CHGWS_KEY_RING`.
    * `LOCATION`: The location where you want to enable—for example, `us`.
    * `KEY_NAME`: The name of the key—for example, `CHGWS_KEY`.



## Manage billing for CHGWS

Billing begins as soon as you are provided with the CHGWS endpoint requested in your onboarding request. From that point on, recurring subscription charges for Cloud HSM for Google Workspace continue as long as billing remains enabled on the Google Cloud project, even if you disable the CHGWS endpoint. This section explains how you can stop accruing charges for Cloud HSM for Google Workspace and how you can resume them.

### Disable/Enable project billing

You can [disable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) for the project that contains your Cloud KMS keys for Cloud HSM for Google Workspace. Disabling billing makes all chargeable services within the project stop working. After the project level billing is disabled, expect the Cloud HSM for Google Workspace subscription charges to stop within 24 hours.

When you want to resume using Cloud HSM for Google Workspace, you can [re-enable billing on the project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project). After billing is re-enabled, your subscription fees resume and your CHGWS endpoint and Cloud KMS keys function normally again.

### Request manual deactivation or activation

If you need to disable the CHGWS endpoint while keeping other project resources active, file a request similar to the onboarding request. Provide Google Workspace details, CHGWS endpoint ID, and other relevant details and describe your requirement. Manual tickets can take 48 hours to be completed by the CHGWS team. After the request is completed, expect the Cloud HSM for Google Workspace subscription charges to stop within 24 hours.

You can re-enable the CHGWS endpoint and its billing by creating a similar request.

### Delete or restore the project

You can [delete the project](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects) that contains your Cloud KMS keys for Cloud HSM for Google Workspace. Deleting a project stops all services within the project. You can [recover a deleted project](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects#restoring_a_project) within 30 days of deletion. However, Cloud KMS keys in the project can't be recovered, so all the documents and other data that are encrypted with keys in the restored project remain permanently crypto-shredded. Restoring a deleted project resumes the subscription charges of Cloud HSM for Google Workspace even though the Cloud KMS keys remain unrecoverable.

**Warning:** Deleting a project involves significant risk of permanent data loss if the resources in the project are still in use. Don't delete a project without making a data recovery or migration plan if it contains resources that you might still need.

## What's next

  * Learn more about [Cloud HSM for Google Workspace](https://docs.cloud.google.com/kms/docs/hsm-for-workspace).
  * Review the [best practices for Cloud HSM for Google Workspace](https://docs.cloud.google.com/kms/docs/hsm-for-workspace-best-practices).
  * Learn more about [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service).
  * Learn how to [add and manage key services for client-side encryption](https://support.google.com/a/answer/10742487).
  * Learn how to [automatically set up Client-side encryption for the first time](https://knowledge.workspace.google.com/admin/security/set-up-cse-simplified).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
