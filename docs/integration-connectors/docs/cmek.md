---
url: https://docs.cloud.google.com/integration-connectors/docs/cmek/
title: Customer-managed encryption keys \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:38.159664+00:00
---

# Customer-managed encryption keys  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customer-managed encryption keys

By default, Integration Connectors encrypts customer content at rest. Integration Connectors handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Integration Connectors. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Integration Connectors resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Before you begin

Ensure that the following tasks are completed before using CMEK for Integration Connectors:

  1. Enable the Cloud KMS API for the project that will store your encryption keys. 

[Enable Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com) **Tip:** You can run Integration Connectors and Cloud KMS in the same Google Cloud project, or in different projects. 

  2. Assign the **Cloud KMS Admin** IAM role or grant the following IAM permissions for the project that will store your encryption keys: 
     * `cloudkms.cryptoKeys.setIamPolicy`
     * `cloudkms.keyRings.create`
     * `cloudkms.cryptoKeys.create`

For information about granting additional roles or permissions, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Caution:** The Cloud KMS Admin role contains permissions for key maintenance and key version destruction. To protect your Cloud KMS resources, this role should only be assigned to individuals responsible for key administration.
  3. Create a [key ring](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key_ring) and a [key](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key). **Note:** The key ring must be created in the same region where you have set up Integration Connectors.



## Add service account to CMEK key

In order to use a CMEK key in Integration Connectors, you must ensure that your default service account (having the format `service-PROJECT_NUMBER@gcp-sa-connectors.iam.gserviceaccount.com`) is added and assigned with the [CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) IAM role for that CMEK key. 

**Note:** The default service account may not exist if you are provisioning the first region. To generate the service account, run the `gcloud beta services identity create --service=connectors.googleapis.com --project=PROJECT_ID` command.

  1. In the Google Cloud console, go to the **Key Inventory** page. 

[Go to Key Inventory page](https://console.cloud.google.com/security/kms/keys)

  2. Select the checkbox for the desired CMEK key. 

The **Permissions** tab in the right window pane becomes available. 

  3. Click **Add principal** , and enter the email address of the default service account. 
  4. Click **Select a role** and select the **Cloud KMS CryptoKey Encrypter/Decrypter** role from the available dropdown list. 
  5. Click **Save**. 



## Enable CMEK encryption for an existing Integration Connectors region

**Caution:**

  * Enabling CMEK encryption for an Integration Connectors region cannot be undone. This also means that you can't change the encryption method for a region if CMEK is already enabled, and the root key resource path cannot be updated or changed dynamically on an existing resource.
  * You can enable CMEK for an Integration Connectors region only when all the connections in that region are `SUSPENDED`. Therefore, before you enable CMEK for an existing region that has connections, you must [suspend all the connections](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection#suspend-a-connection) in the region.



You can use CMEK to encrypt and decrypt the [supported data](https://docs.cloud.google.com/integration-connectors/docs/encryption#data) stored in a region (also referred as location). To enable CMEK encryption for an existing Integration Connectors region, do the following steps:

  1. In the Google Cloud console, go to the **Integration Connectors > Connections** page. 

[Go to all connections](https://console.cloud.google.com/connectors/connections) page. 

  2. Filter the connections for the required **Location**. 

You will get a list of all the connections for the specified location (region).

  3. [Suspend all the connections](https://docs.cloud.google.com/integration-connectors/docs/suspend-resume-connection#suspend-a-connection) in the region.
  4. Go to the **Integration Connectors > Regions** page. This lists all the regions where Integration Connectors is available.
  5. For the region in which you want to enable CMEK, click **Edit encryption** in the **Actions** menu. This shows the **Edit encryption** pane.
  6. Select **Customer-managed encryption key (CMEK)** , and then select the required key from the **Customer-managed key** drop-down list. 

This may prompt you to grant to `cloudkms.cryptoKeyEncrypterDecrypter` role to the service account. Click **Grant**.

  7. Click **Done**.



## Enable CMEK encryption for a new Integration Connectors region

**Caution:** Enabling CMEK encryption for an Integration Connectors region cannot be undone. Additionally, the root key resource path cannot be updated or changed dynamically on an existing resource.

You can use CMEK to encrypt and decrypt the [supported data](https://docs.cloud.google.com/integration-connectors/docs/encryption#data) stored in a region (also referred as location). To enable CMEK encryption for a new Integration Connectors region, do the following steps:

  1. In the Google Cloud console, go to the **Integration Connectors > Regions** page. 

[Go to Regions](https://console.cloud.google.com/connectors/regions) page. 

  2. Click **Provision new region**. This displays the create region page. 
  3. Select the required region from the **Region** drop-down list.
  4. In the **Advanced settings** section, select **Customer-managed encryption key (CMEK)** , and then select the required key from the **Customer-managed key** drop-down list 

This may prompt you to grant to `cloudkms.cryptoKeyEncrypterDecrypter` role to the service account. Click **Grant**.

  5. Click **Done**.



## Key rotation and re-encryption

When a CMEK key is rotated, existing data is not automatically re-encrypted with the new key version, nor does Integration Connectors support manual re-encryption. However, the data remains accessible as long as those previous active key versions are not disabled or destroyed. 

## Cloud KMS quotas and Integration Connectors

When you use CMEK in Integration Connectors, your projects can consume Cloud KMS cryptographic requests quotas. For example, CMEK keys can consume these quotas for each encryption and decryption call.

Encryption and decryption operations using CMEK keys affect Cloud KMS quotas in these ways:

  * For software CMEK keys generated in Cloud KMS, no Cloud KMS quota is consumed.
  * For hardware CMEK keys—sometimes called Cloud HSM keys—encryption and decryption operations count against [Cloud HSM quotas](https://docs.cloud.google.com/kms/quotas#hsm) in the project that contains the key.
  * For external CMEK keys—sometimes called Cloud EKM keys—encryption and decryption operations count against [Cloud EKM quotas](https://docs.cloud.google.com/kms/quotas#ekm) in the project that contains the key.



For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
