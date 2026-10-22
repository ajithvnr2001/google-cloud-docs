---
url: https://docs.cloud.google.com/application-integration/docs/cmek/
title: Customer-managed encryption keys \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:19.896285+00:00
---

# Customer-managed encryption keys  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Customer-managed encryption keys

By default, Application Integration encrypts customer content at rest. Application Integration handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Application Integration. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Application Integration resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

**Tip:** When you use Google-owned and Google-managed encryption keys in Application Integration, your tenant projects consumes Cloud KMS cryptographic requests quotas. For more information about the quotas and limits, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas). 

## Before you begin

Ensure that the following tasks are completed before using CMEK for Application Integration:

  1. Enable the Cloud KMS API for the project that will store your encryption keys. 

[Enable Cloud KMS API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com) **Tip:** You can run Application Integration and Cloud Key Management Service in the same Google Cloud project, or in different projects.

     * If you use CMEK in a different project (shared or key-hosting project) than the one where you have set up Application Integration:
       1. Enable the following API in the shared or key-hosting project: 
          * [Cloud Key Management Service API](https://console.cloud.google.com/apis/library/cloudkms.googleapis.com)
       2. Grant the following IAM role on the CMEK key to the Application Integration [default service account](https://docs.cloud.google.com/application-integration/docs/access-control-iam#sa) in the shared or key-hosting project: 
          * [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms)
**Note:** To enable role assignment for the default service account, you must verify the CMEK key at least once, even if the first attempt fails.
  2. Assign the **Cloud KMS Admin** IAM role to the individuals managing the CMEK keys. Additionally, grant the following IAM permissions for the project that stores your encryption keys: 
     * `cloudkms.cryptoKeys.setIamPolicy`
     * `cloudkms.keyRings.create`
     * `cloudkms.cryptoKeys.create`
     * `cloudkms.cryptoKeyVersions.useToEncrypt`
**Caution:** The Cloud KMS Admin role contains permissions for key maintenance and key version destruction. To protect your Cloud KMS resources, this role should only be assigned to individuals responsible for key administration.

For information about granting additional roles or permissions, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  3. Create a [key ring](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key_ring) and a [key](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key). **Note:** The key ring and CMEK key must be created in the same region where you have set up Application Integration.



## Add service account to CMEK key

In order to use a CMEK key in Application Integration, you must ensure that your [default service account](https://docs.cloud.google.com/application-integration/docs/access-control-iam#sa) is added and assigned with the [CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) IAM role for that CMEK key. 

  1. In the Google Cloud console, go to the **Key Inventory** page. 

[Go to Key Inventory page](https://console.cloud.google.com/security/kms/keys)

  2. Select the checkbox for the desired CMEK key. 

The **Permissions** tab in the right window pane becomes available. 

  3. Click **Add principal** , and enter the email address of the default service account. 
  4. Click **Select a role** and select the **Cloud KMS CryptoKey Encrypter/Decrypter** role from the available dropdown list. 
  5. Click **Save**. 



## Enable CMEK encryption for an Application Integration region

CMEK can be used to encrypt and decrypt [data stored](https://docs.cloud.google.com/application-integration/docs/encryption#data) on PDs within the scope of the provisioned region. **Caution:** Enabling CMEK encryption for an Application Integration region cannot be undone. This also means that you can't change the encryption method for a region if CMEK is already enabled, and the root key resource path cannot be updated or changed dynamically on an existing resource.  To enable CMEK encryption for an Application Integration region in your Google Cloud project, perform the following steps: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration ](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Regions**. 

The **Regions** page appears, listing the provisioned regions for Application Integration. 

  3. For the existing integration that you want to use CMEK, click  more_vert **Actions** and select **Edit encryption**.
  4. In the **Edit encryption pane** , expand the **Advanced settings** section.
  5. Select **Use a Customer-managed encryption key (CMEK)** , and do the following: 
     1. Select a CMEK key from the available drop-down list. The CMEK keys listed in the drop-down are based on the provisioned region. To create a new key, see Create new CMEK key. 
     2. Click **Verify** to check if your default service account has cryptokey access to the selected CMEK key.
     3. If the verification for the selected CMEK key fails, click **Grant** to assign the [CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) IAM role to the default service account. 
  6. Click **Done**.



### Create new CMEK

You can create a new CMEK key if you don't want to use your existing key, or if you don't have a key in the specified region. **Note:** You can only use a [symmetric encryption key](https://docs.cloud.google.com/kms/docs/algorithms#symmetric_encryption_algorithms) in Application Integration.  To create a new symmetric encryption key, perform the following steps in the **Create a new key** dialog: 

  1. Select Key ring: 
     1. Click **Key ring** and choose an existing key ring in the specified region.
     2. If you want to create a new key ring for your key, click the **Create key ring** toggle and do the following steps: 
        1. Click **Key ring name** and enter a name of your key ring.
        2. Click **Key ring location** and choose the regional location of your key ring. **Note:** For CMEK encryption, your key ring must be created in the same region where you have set up Application Integration.
     3. Click **Continue**.
  2. Create Key: 
     1. Click **Key name** and enter a name for your new key.
     2. Click **Protection level** and select either **Software** or **HSM**. 

For information about protection levels, see [Cloud KMS protection levels](https://cloud.google.com/kms/docs/protection-levels). 

  3. Review your key and key ring details, and click **Continue**.
  4. Click **Create**.

**Note:** You must enable CMEK in a region before creating or publishing integrations in that region. Failure to do so may result in errors.

## Key rotation and re-encryption

When a CMEK key is rotated, existing data is not automatically re-encrypted with the new key version, nor does Application Integration support manual re-encryption. However, the data remains accessible as long as those previous active key versions are not disabled or destroyed. 

## Encrypted data

The following table lists the data encrypted in Application Integration: 

Resource | Encrypted data  
---|---  
Integration details  | 

  * Task configuration parameters 
  * Task configuration descriptions

  
Integration execution information  | 

  * Request parameters 
  * Response parameters 
  * Task execution details

  
Authentication profile credentials | 

  * Username and passwords 
  * API keys 
  * [OAuth 2.0 authorization code](https://cloud.google.com/application-integration/docs/configuring-auth-profile#oauth2-code)
  * [OAuth 2.0 client credentials](https://cloud.google.com/application-integration/docs/configuring-auth-profile#oauth2-client)
  * [OAuth 2.0 resource owner password credentials](https://cloud.google.com/application-integration/docs/configuring-auth-profile#oauth2-owner)
  * [Auth tokens](https://cloud.google.com/application-integration/docs/configuring-auth-profile#auth-token)
  * [JWT tokens](https://cloud.google.com/application-integration/docs/configuring-auth-profile#jwt)
  * [Service accounts](https://cloud.google.com/application-integration/docs/configuring-auth-profile#service-account)
  * [SSL/TLS client certificates](https://cloud.google.com/application-integration/docs/configuring-auth-profile#client-certificate)
  * [Google OIDC ID tokens](https://cloud.google.com/application-integration/docs/configuring-auth-profile#googleOIDC)

  
Approval/Suspension task details | Approval or suspension configurations   
  
## Cloud KMS quotas and Application Integration

When you use CMEK in Application Integration, your projects can consume Cloud KMS cryptographic requests quotas. For example, CMEK keys can consume these quotas for each encryption and decryption call.

Encryption and decryption operations using CMEK keys affect Cloud KMS quotas in these ways:

  * For software CMEK keys generated in Cloud KMS, no Cloud KMS quota is consumed.
  * For hardware CMEK keys—sometimes called Cloud HSM keys—encryption and decryption operations count against [Cloud HSM quotas](https://docs.cloud.google.com/kms/quotas#hsm) in the project that contains the key.
  * For external CMEK keys—sometimes called Cloud EKM keys—encryption and decryption operations count against [Cloud EKM quotas](https://docs.cloud.google.com/kms/quotas#ekm) in the project that contains the key.



For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
