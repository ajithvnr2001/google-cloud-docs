---
url: https://docs.cloud.google.com/managed-spark/docs/guides/cmek-serverless/
title: Use CMEK with Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:23.561790+00:00
---

# Use CMEK with Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/cmek-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Use CMEK with Managed Service for Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

By default, Managed Service for Apache Spark encrypts customer content at rest. Managed Service for Apache Spark handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Managed Service for Apache Spark. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Managed Service for Apache Spark resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

When you use Managed Service for Apache Spark, data is stored on disks on the underlying serverless infrastructure and in a Cloud Storage [staging bucket](https://docs.cloud.google.com/managed-spark/docs/concepts/buckets). This data is encrypted using a Google-generated data encryption key (DEK) and key encryption key (KEK). If you want control of your KEK, you can use a customer-managed encryption key (CMEK) instead of [default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption). When you use a CMEK, you create the key and manage access to it, and you can revoke access to it to prevent decryption of your DEKs and data.

## Use CMEK

Follow the steps in this section to use CMEK to encrypt data that Managed Service for Apache Spark writes to persistent disk and to the Managed Service for Apache Spark staging bucket.

Beginning April 23, 2024: 

  * Managed Service for Apache Spark also uses your CMEK to encrypt batch job arguments. The [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) IAM role must be assigned to the Managed Service for Apache Spark Service Agent service account to enable this behavior. If the [Managed Service for Apache Spark Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) is not attached to the Managed Service for Apache Spark Service Agent service account, then add the `serviceusage.services.use` permission to a custom role attached to the Managed Service for Apache Spark Service Agent service account . The Cloud KMS API must be enabled on the project that runs Managed Service for Apache Spark resources.
  * [`batches.list`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches/list) returns an `unreachable` field that lists any batches with job arguments that couldn't be decrypted. You can issue [`batches.get`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.batches/get) requests to obtain more information on unreachable batches.
  * The key (CMEK) must be located in the same location as the encrypted resource. For example, the CMEK used to encrypt a batch that runs in the `us-central1` region must also be located in the `us-central1` region.



You can use Cloud Key Management Service to create and manage key rings and keys, or use [Cloud KMS Autokey](https://docs.cloud.google.com/kms/docs/kms-autokey) for simplified auto-creation of key rings and keys.

### Using Cloud KMS Autokey

  1. [Enable Autokey](https://docs.cloud.google.com/kms/docs/enable-autokey) on the folder that contains your project.
  2. [Create a key handle](https://docs.cloud.google.com/kms/docs/create-key). When you create the key handle, specify `dataproc.googleapis.com/Batch` or `dataproc.googleapis.com/Session` as the `--resource-type`. Autokey generates a key and assigns it to the key handle.
  3. Grant permissions to service accounts and configure your batch or session workload by following steps 4 and 5 in the Manually create and use keys section that follows. When you submit your workload, specify the key handle resource name in place of the key resource name in the `kmsKey` field.



### Manually create and use keys

Follow these steps to manually create Cloud KMS keys and use them with Managed Service for Apache Spark.

  1. Create a key using the [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs/creating-keys).

  2. Copy the resource name. ![Copy the resource name.](https://docs.cloud.google.com/static/managed-spark/docs/images/copy-key.png) The resource name is is constructed as follows: 
         
         projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING_NAME/cryptoKeys/KEY_NAME
         

  3. Enable the Compute Engine, Managed Service for Apache Spark, and Cloud Storage Service Agent service accounts to use your key:

     1. See [Protect resources by using Cloud KMS keys > Required Roles](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#required-roles) to assign the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role to the [Compute Engine Service Agent service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account). If this service account is not listed on the IAM page in Google Cloud console, click **Include Google-provided role grants** to list it.
     2. Assign the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) role to the [Managed Service for Apache Spark Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity). You can use the Google Cloud CLI to assign the role:
            
            gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
             --member serviceAccount:service-PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com \
             --role roles/cloudkms.cryptoKeyEncrypterDecrypter
            

Replace the following:

`KMS_PROJECT_ID`: the ID of your Google Cloud project that runs Cloud KMS. This project can also be the project that runs Managed Service for Apache Spark resources.

`PROJECT_NUMBER`: the project number (not the project ID) of your Google Cloud project that runs Managed Service for Apache Spark resources.

     3. Enable the Cloud KMS API on the project that runs Managed Service for Apache Spark resources.

     4. If the [Managed Service for Apache Spark Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) is not attached to the [Managed Service for Apache Spark Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity), then add the `serviceusage.services.use` permission to the custom role attached to the Managed Service for Apache Spark Service Agent service account. If the Managed Service for Apache Spark Service Agent role is attached to the Managed Service for Apache Spark Service Agent service account, you can skip this step.

     5. Follow the steps to [add your key on the bucket](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#set-default-key).

  4. When you [submit a batch workload](https://docs.cloud.google.com/managed-spark/docs/quickstarts/spark-batch#submit_a_spark_batch_workload):

     1. Specify your key in the batch [`kmsKey`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.kms_key) parameter.
     2. Specify the name of your Cloud Storage bucket in the batch [`stagingBucket`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.staging_bucket) parameter.
  5. When you [create an interactive session or session template](https://docs.cloud.google.com/managed-spark/docs/guides/create-serverless-sessions-templates):

     1. Specify your key in the session [`kmsKey`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.kms_key) parameter.
     2. Specify the name of your Cloud Storage bucket in the session [`stagingBucket`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/EnvironmentConfig#ExecutionConfig.FIELDS.staging_bucket) parameter.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
