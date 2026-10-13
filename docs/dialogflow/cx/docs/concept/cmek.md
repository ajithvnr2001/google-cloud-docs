---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek/
title: Customer-managed encryption keys (CMEK) \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:54.135596+00:00
---

# Customer-managed encryption keys (CMEK)  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By default, Dialogflow CX encrypts customer content at rest. Dialogflow CX handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. Google default encryption uses the same hardened key management systems that we use for our own encrypted data. These systems include strict key access controls and auditing.

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Dialogflow CX. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Dialogflow CX resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Protected data

You can protect all Dialogflow CX agent [data at rest](https://en.wikipedia.org/wiki/Data_at_rest) with CMEKs.

## Limitations

  * Key rotation is supported, but data re-encryption isn't. Re-encrypting previously encrypted data with a new key version isn't supported.
  * The following [regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#avail) are not supported: 
    * `global`
  * One key should be used per project location.
  * To [restore an agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export) with CMEK enabled, you must choose the Cloud Storage option.
  * Existing resources in non-CMEK integrated projects can't be CMEK integrated retroactively. Instead, export and restore resources in a new project for CMEK.
  * [Vertex AI Agent Builder](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction) has some [Cloud Key Management Service limitations](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek#limitations).



## Create keys

To create keys, use Cloud KMS. For instructions, see [Creating symmetric keys](https://docs.cloud.google.com/kms/docs/creating-keys). When creating or choosing a key, ensure that you configure the following:

  * Select the [location](https://docs.cloud.google.com/dialogflow/cx/docs/how/region) that you use for your agent, because requests fail if the locations don't match.



## Identify Dialogflow service account

To identify the Dialogflow service account:

  1. Open the [Conversational Agents console](https://conversational-agents.cloud.google.com).
  2. Select your project.
  3. Select your agent.
  4. In the navigation menu, click **Settings** , and then go to the **Security** tab.
  5. Click **Manage Security Settings** to be redirected to the [CCAI console](https://ccai.cloud.google.com/projects).
  6. On the CCAI console, go to the **CMEK** tab.
  7. Click **Check or create service account**.
  8. Note the service account name displayed (e.g., `service-665989447347@gcp-sa-ccai-cmek.IAM.gserviceaccount.com`).



## Grant Permissions to the service account

To grant permissions to the service account:

  1. Go to the [Cloud KMS page](https://cloud.google.com/kms).
  2. Select the key ring that you created.
  3. Select the key that you created within that key ring.
  4. Go to the **Permissions** tab.
  5. Click **Grant Access**.
  6. In the **New principals** field, enter the Dialogflow service account that you identified in the previous step.
  7. In the **Select a role** list, select **Cloud KMS CryptoKey Encrypter/Decrypter**.
  8. Click **Save**.



## Copy the key resource name

To copy the key resource name:

  1. Go to the KMS key details page.
  2. Click the **Action** menu and select **Copy resource name**.



This action copies the full path of your KMS key (for example, `projects/<var>PROJECT_ID</var>/locations/<var>LOCATION_ID</var>/keyRings/<var>KEY_RING</var>/cryptoKeys/<var>KEY_ID</var>`).

## Enable CMEK in Dialogflow

To enable CMEK in Dialogflow:

  1. Return to the **CMEK** tab in the CCAI console.
  2. Paste the copied key resource name into the **Key** field for the location where you want to enable CMEK.
  3. Click **Save**.



This initiates a long-running operation (LRO) to enable CMEK for the chosen location. This process takes 2-3 minutes.

## Configure an agent to use your keys

When you create an agent, specify its [location](https://docs.cloud.google.com/dialogflow/cx/docs/how/region) and whether to use a Google-managed encryption key or a CMEK for that location.

**Caution:** You can't change encryption key settings for a location once it has been specified. To change a location, you need to create a new project with the selected location and [import](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export) existing agents to the new project.

### Using CLI to set up CMEK

Alternatively, you can use the following commands to set up CMEK. This is helpful when setting it up for multiple regions.

**Note:** The CCAI CMEK service account is not visible in your project Identity and Access Management (IAM).

  1. Use Google Cloud CLI to create the CCAI CMEK service account for your project. For more information, see the [gcloud services identity documentation](https://cloud.google.com/sdk/gcloud/reference/beta/services/identity/create).
         
         gcloud beta services identity create --service=dialogflow.googleapis.com --project=PROJECT_ID

The service account is created. It isn't returned in the create response, but it has the following format:
         
         service-PROJECT_NUMBER@gcp-sa-ccai-cmek.iam.gserviceaccount.com

  2. Grant the CCAI CMEK service account the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role to allow the service to encrypt and decrypt with your key.
         
         gcloud kms keys add-iam-policy-binding KMS_KEY_ID \
          --project=PROJECT_ID \
          --location=LOCATION_ID \
          --keyring=KMS_KEY_RING \
          --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-ccai-cmek.iam.gserviceaccount.com \
          --role=roles/cloudkms.cryptoKeyEncrypterDecrypter




### Using API to configure a key and check settings

  1. To configure a key for Dialogflow CX location, call the `InitializeEncryptionSpec` API and provide the following variables:

     * `PROJECT_ID`: The Google Cloud project ID.
     * `LOCATION_ID`: The location you select to enable CMEK in Dialogflow CX.
     * `KMS_KEY_RING`: The key ring within which your KMS key was created. The location in the key ring, such as `projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KMS_KEY_RING`, must match the location where you're enabling CMEK.
     * `KMS_KEY_ID`: The name of your KMS key that is used to encrypt and decrypt Dialogflow CX data in the selected location.

For example:
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d "{ encryption_spec: { kms_key: 'projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KMS_KEY_RING/cryptoKeys/KMS_KEY_ID' } }" \
        "https://LOCATION_ID-dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/encryptionSpec:initialize"

The JSON response is similar to the following:
    
    {
       "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"
     }

  2. To get the long-running operation (LRO) result, call the `GetOperation` API.

For example:
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             "https://LOCATION_ID-dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID"

  3. To retrieve the encryption key configured for a location, call the `GetEncryptionSpec` API.

For example:
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             "https://LOCATION_ID-dialogflow.googleapis.com/v2/projects/PROJECT_ID/locations/LOCATION_ID/encryptionSpec"




## Revoke keys

To revoke Dialogflow CX access to the key, you can [disable the KMS key version](https://docs.cloud.google.com/kms/docs/IAM#revoking_access_to_a_resource) or [remove](https://docs.cloud.google.com/kms/docs/IAM#revoking_access_to_a_resource) the service account's [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role from the KMS key.

After key revocation, the encrypted data becomes inaccessible to Dialogflow CX, and the service is no longer operational until the key permissions are reinstated.

**Caution:** If the key is revoked for more than 30 days, the Dialogflow CX data encrypted by that key is lost.

[ Previous arrow_back  Agent collaboration  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-collaboration)

[ Next Security settings  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/security-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
