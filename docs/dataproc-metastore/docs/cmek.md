---
url: https://docs.cloud.google.com/dataproc-metastore/docs/cmek/
title: Encrypt data with customer-managed encryption keys \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:49.932559+00:00
---

# Encrypt data with customer-managed encryption keys  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Guides ](https://docs.cloud.google.com/dataproc-metastore/docs/create-service-cluster)



Send feedback 

#  Encrypt data with customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

By default, Dataproc Metastore encrypts customer content at rest. Dataproc Metastore handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Dataproc Metastore. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Dataproc Metastore resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Before you begin

  * [Enable Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/hms-federation).
  * [Create a Dataproc Metastore service](https://docs.cloud.google.com/dataproc-metastore/docs/enable-service).



### Considerations

Consider the following points when using Dataproc Metastore with CMEK.

**Warning:** If a service remains disabled for more than seven consecutive days, the Dataproc Metastore cannot be recovered and requires manual deletion. To avoid permanent data loss, don't leave CMEK keys in an inaccessible state for an extended time.

If a Cloud KMS key is deleted and can't be recovered, any Dataproc Metastore service encrypted with that key becomes permanently inaccessible.

  * The Cloud Monitoring database doesn't support CMEK encryption. Instead, Google Cloud uses Google encryption keys to protect the names and service configurations of your Dataproc Metastore services.

  * If you want your Dataproc Metastore service to run inside a [VPC Service Controls](https://docs.cloud.google.com/dataproc-metastore/docs/vpc-sc) perimeter, you must add the Cloud Key Management Service (Cloud KMS) API to the perimeter.

  * When you use a [Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm) key, Google has no control over the availability of your externally managed key. If the key becomes unavailable during the Dataproc Metastore service creation period, the service creation fails. After a Dataproc Metastore service is created, if the key becomes unavailable, the service becomes unavailable until the key becomes available again. For more considerations when using external keys, see [Cloud EKM Considerations](https://docs.cloud.google.com/kms/docs/ekm#considerations).




### Limitations

Consider the following limitations when using Dataproc Metastore with CMEK.

  * You can't enable CMEK on an existing service.

  * You can't rotate CMEKs used by a CMEK-enabled service.

  * You can't use CMEKs to encrypt user data in transit, such as user queries and responses.




## Configure CMEK for Dataproc Metastore

If you don't already have a Cloud KMS key, you can create one for your Dataproc Metastore service. Otherwise, you can skip this step and use an existing key.

### Optional: Create a new Cloud KMS key

To create a Cloud KMS key, you first create a key ring and then create a key that's stored inside the key ring.

#### To create a key ring

To create a key ring, run the following [`gcloud kms keyrings create`](https://cloud.google.com/sdk/gcloud/reference/kms/keyrings/create) command.

**Note:** You must create your CMEK key in the same region where your Dataproc Metastore service is located.
    
    
    gcloud kms keyrings create KEY_RING \
      --project=PROJECT_ID \
      --location=LOCATION

Replace the following:

  * `KEY_RING`: a name for your key ring.
  * `PROJECT_ID`: the ID of the Google Cloud project that you want to create the key ring in.
  * `LOCATION`: the region that you want to create the key ring in.



#### To create a key

To create a key that's stored inside your key ring, run the following [`gcloud kms keys create`](https://cloud.google.com/sdk/gcloud/reference/kms/keys/create) command.
    
    
    gcloud kms keys create KEY_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --keyring=KEY_RING \
      --purpose=encryption

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that you created in the preceding step.



### Grant Cloud KMS key permissions

Use the following commands to grant Cloud KMS key permissions for Dataproc Metastore:

  1. Grant permissions to the Dataproc Metastore Service Agent service account:
         
         gcloud kms keys add-iam-policy-binding KEY_NAME \
             --location LOCATION \
             --keyring KEY_RING \
             --member=serviceAccount:$(gcloud beta services identity create \
             --service=metastore.googleapis.com 2>&1 | awk '{print $4}') \
             --role=roles/cloudkms.cryptoKeyEncrypterDecrypter




  1. Grant permissions to the Cloud Storage service account:
         
         gcloud storage service-agent --authorize-cmek projects/KEY_PROJECT/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME




### Create a single-region service with a CMEK key

Use the following steps to configure CMEK encryption for a single-region Dataproc Metastore service.

### Console

  1. In the Google Cloud console, go to the Dataproc Metastore page:

[Go to Dataproc Metastore](https://console.cloud.google.com/dataproc/metastore/services)

  2. At the top of the **Dataproc Metastore** page, click **Create**.

The **Create service** page opens.

  3. Configure your service as needed.

  4. Under **Encryption** , click **Customer-managed encryption key (CMEK)**.

  5. Select the customer-managed key.

  6. Click **Submit**.




Verify the service's encryption configuration:

  1. In the Google Cloud console, go to the Dataproc Metastore page:

[Go to Google Cloud console](https://console.cloud.google.com/dataproc/metastore/services)

  2. On the **Dataproc Metastore** page, click the name of the service you'd like to view.

The **Service detail** page opens.

  3. Under the **Configuration** tab, verify that the details show CMEK is enabled.




### gcloud

  1. To create a single-region service with CMEK encryption, run the Google Cloud [`gcloud metastore services create`](https://docs.cloud.google.com/sdk/gcloud/reference/metastore/services/create) command:
         
         gcloud metastore services create SERVICE \
            --encryption-kms-key=KMS_KEY
         

Replace the following:

     * `SERVICE`: the name of the new service.
     * `KMS_KEY`: the key resource ID.



## Import and export data from and to a CMEK-enabled service

If you want your data to remain encrypted with a customer-managed key during an import, you must set CMEK on the Cloud Storage bucket before importing data from it.

You can import from a non-CMEK-protected Cloud Storage bucket. After importing, the data stored in Dataproc Metastore is protected according to the destination service's CMEK settings.

When exporting, the exported database dump is protected according to the destination storage bucket's CMEK settings.

## What's next

  * [Import metadata into a service](https://docs.cloud.google.com/dataproc-metastore/docs/import-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
