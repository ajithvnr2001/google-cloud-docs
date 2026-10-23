---
url: https://docs.cloud.google.com/secure-source-manager/docs/cmek/
title: Encrypt data with customer-managed encryption keys \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:45.416285+00:00
---

# Encrypt data with customer-managed encryption keys  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Encrypt data with customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

By default, Secure Source Manager encrypts customer content at rest. Secure Source Manager handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Secure Source Manager. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Secure Source Manager resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

Cloud KMS can run in a separate project where you centrally manage keys for multiple projects, or the same Google Cloud project as Secure Source Manager. To support separation of duties and greater control over access to keys, we recommend that you create and manage keys in a separate project that doesn't include other Google Cloud resources.

You assign a Cloud KMS key when you create an instance. You can't change the encryption mechanism of an existing instance. If you have a CMEK-encrypted instance, you can't change the encryption mechanism to Google default encryption or assign a different Cloud Key Management Service key for encryption.

The instance must be created in the same [location](https://docs.cloud.google.com/secure-source-manager/docs/locations) as the Cloud KMS key.

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Secure Source Manager resources or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation in Secure Source Manager. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

## Cloud KMS quotas and Secure Source Manager

When you use CMEK in Secure Source Manager, your projects can consume Cloud KMS cryptographic requests quotas. CMEK-encrypted instances consume these quotas at creation time. Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## Create a CMEK key and grant permissions

The following instructions explain how to create a key and grant the Secure Source Manager service account permissions on the key.

  1. Create a Cloud KMS key:

###  Manually 

     1. In the Google Cloud project where you want to manage your keys:

        1. [Enable the Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com&redirect=https://console.cloud.google.com/).

        2. Create a key ring and a key using one of the following options:

        * Create the [key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [key](https://docs.cloud.google.com/kms/docs/create-key) directly in Cloud KMS.
        * Use an externally-managed key. [Create the external key](https://docs.cloud.google.com/kms/docs/ekm-internet#create_external_key) and then [create an Cloud EKM key](https://docs.cloud.google.com/kms/docs/ekm) to make the key available through Cloud KMS.

The Cloud KMS [key location](https://docs.cloud.google.com/kms/docs/locations) must match the [location](https://docs.cloud.google.com/secure-source-manager/docs/locations) of the project where you want to create the Secure Source Manager instance.

###  Using Autokey 

     1. If you haven't already done so, [enable Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey).

     2. Create a new Cloud KMS Autokey [`KeyHandle`](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles):
            
            curl -H "Content-Type: application/json" \
                -H "X-Goog-User-Project: PROJECT" \
                -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                -X POST https://cloudkms.googleapis.com/v1/projects/PROJECT/locations/LOCATION/keyHandles \
                -d '{"resource_type_selector": "securesourcemanager.googleapis.com/Instance"}'
            

Replace the following:

        * PROJECT: the project ID of the project where Cloud KMS Autokey is enabled and where you want to deploy a Secure Source Manager instance
        * LOCATION: the [`KeyHandle`](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles) location. It must match the [location](https://docs.cloud.google.com/secure-source-manager/docs/locations) where you want to deploy a Secure Source Manager instance

The output is similar to the following:
    
    {
      "name": "projects/PROJECT/locations/LOCATION/operations/OPERATION",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.CreateKeyHandleMetadata"
      }
    }
    

Make note of the OPERATION from the output. You need this value to get the resource ID of the created key.

     3. Find the Cloud KMS key associated with the key handle:
            
            curl -H "X-Goog-User-Project: PROJECT" \
                -H "Authorization: Bearer $(gcloud auth print-access-token)" \
                -X GET https://cloudkms.googleapis.com/v1/projects/PROJECT/locations/LOCATION/operations/OPERATION
            

Replace the following:

        * PROJECT: the project ID of the project where Cloud KMS Autokey is enabled and where you want to deploy a Secure Source Manager instance
        * LOCATION: the [`KeyHandle`](https://docs.cloud.google.com/kms/docs/resource-hierarchy#key_handles) location. It must match the [location](https://docs.cloud.google.com/secure-source-manager/docs/locations) where you want to deploy a Secure Source Manager instance
        * OPERATION: The identifier of the key handle request operation from the output of the previous step

The output is similar to the following:
    
    {
      "name": "projects/PROJECT/locations/LOCATION/operations/OPERATION",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.kms.v1.KeyHandle",
        "name": "projects/PROJECT/locations/LOCATION/keyHandles/KEY_HANDLE",
        "kmsKey": "projects/PROJECT/locations/LOCATION/keyRings/autokey/cryptoKeys/KEY_NAME",
        "resourceTypeSelector": "securesourcemanager.googleapis.com/Instance"
      }
    }
    

The value of the `kmsKey` element in the output is the full resource ID of the key created by Cloud KMS Autokey for this resource. You can use this resource ID the same way you would use the resource ID for any other Cloud KMS resource.

  2. If you are creating your first Secure Source Manager instance in your project, you will need to manually create the Secure Source Manager service agent by running the following command:
         
         gcloud beta services identity create \
         --service=securesourcemanager.googleapis.com \
         --project=PROJECT
         

Where `PROJECT` is the project ID of the project where you will create your Secure Source Manager instance.

Once you create the Secure Source Manager service agent, you must grant the Secure Source Manager Service Agent role (`roles/securesourcemanager.serviceAgent`) to the principal `service-PROJECT-NUMBER@gcp-sa-sourcemanager.iam.gserviceaccount.com` or the instance creation will fail.

  3. Grant the [CryptoKey Encrypter/Decrypter IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the Secure Source Manager service account. Grant this permission on the key you created.

###  Console 

     1. Go to the **Key management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

     2. Select the key ring you want to use, open the **Key ring details** page, then select the key you created.

     3. Grant access to the Secure Source Manager service account:

        1. Click **ADD PRINCIPLE**.
        2. Add the Secure Source Manager service account. The service account is **service- PROJECT-NUMBER@gcp-sa-sourcemanager.iam.gserviceaccount.com**, where PROJECT-NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Secure Source Manager is enabled.
        3. In **Select a role** , select **Cloud KMS** > **Cloud KMS CryptoKey Encrypter/Decrypter**.
        4. Click **SAVE**.
     4. Repeat the previous step to grant access to the account that will create the Secure Source Manager instance.

     5. Return to the **[Key management](https://console.cloud.google.com/security/kms)** page, select your key ring and open the **Key ring details** page. Then select the key again.

     6. Select the **SHOW INFO PANEL**. You should see roles on the **Role/Member** column.

###  gcloud 

     1. Run the following command to grant access to the Secure Source Manager service account:
            
            gcloud kms keys add-iam-policy-binding [--project=PROJECT] \
                   KEY_NAME --location LOCATION --keyring=KEY_RING \
                   --member serviceAccount:service-PROJECT_NUMBER@gcp-sa-sourcemanager.iam.gserviceaccount.com \
                   --role roles/cloudkms.cryptoKeyEncrypterDecrypter
            

Replace the following:

        * PROJECT: the ID of the project that contains the key
        * KEY_NAME: the key name
        * LOCATION: the key location. The [key location](https://docs.cloud.google.com/kms/docs/locations) must match the [location](https://docs.cloud.google.com/secure-source-manager/docs/locations) of the project where you want to deploy a Secure Source Manager instance
        * KEY_RING: the key ring name
        * PROJECT_NUMBER: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project with Secure Source Manager enabled
     2. Repeat the previous step to grant access to the account that will create the Secure Source Manager instance.

For more information about this command see the [gcloud kms keys add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding) documentation.




## Remove access

There are several ways to remove access to a CMEK-encrypted repository:

  * Revoke the Cloud KMS CryptoKey Encrypter/Decrypter [role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined_roles) from the **Secure Source Manager service account** using the [Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) or the [gcloud CLI](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoking-gcloud-manual).
  * [Temporarily disable](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) the CMEK key.
  * [Permanently destroy](https://docs.cloud.google.com/kms/docs/destroy-restore#schedule_a_key_version_for_destruction_destroy_a_key_version) the CMEK key.



We recommend that you revoke the permissions from the Secure Source Manager service account before disabling or destroying a key. Changes to permissions are consistent within seconds, so you can observe the impacts of disabling or destroying a key.

When you disable or destroy the encryption key for an instance, you lose the ability to view or retrieve data from the instance. All data stored in the instance becomes inaccessible, including code history, pull requests, and issues.

Users with the Secure Source Manager Instance Manager [role](https://docs.cloud.google.com/secure-source-manager/docs/access-control#predefined-roles) or Instance Owner role can delete the instance.

## CMEK organization policies

Secure Source Manager supports [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that can require CMEK protection.

Policies can limit which Cloud KMS CryptoKeys can be used for CMEK protection.

  * When Secure Source Manager API is in the `Deny` policy list of services of constraint `constraints/gcp.restrictNonCmekServices`, Secure Source Manager refuses to create new instances that aren't CMEK-protected.

  * When `constraints/gcp.restrictCmekCryptoKeyProjects` is configured, Secure Source Manager creates CMEK-protected instances that are protected by a CryptoKey from an allowed project, folder, or organization.




For more about configuring organization policies, see [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

## What's next?

  * [Deploy an instance encrypted with CMEK](https://docs.cloud.google.com/secure-source-manager/docs/deploy-access-instance#api)
  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek)
  * Learn more about [Google default encryption](https://docs.cloud.google.com/docs/security/encryption/default-encryption)
  * Learn more about [Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
