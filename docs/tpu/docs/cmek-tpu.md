---
url: https://docs.cloud.google.com/tpu/docs/cmek-tpu/
title: Encrypt a TPU VM boot disk with a customer-managed encryption key (CMEK) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:14.199602+00:00
---

# Encrypt a TPU VM boot disk with a customer-managed encryption key (CMEK)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/cmek-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Encrypt a TPU VM boot disk with a customer-managed encryption key (CMEK)

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

By default, Cloud TPU encrypts customer content at rest. Cloud TPU handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Cloud TPU. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Cloud TPU resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

To use a CMEK, you need to [create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring#kms-create-key-ring-gcloud). You must create your key ring in the same location as where you plan to create your Cloud TPU. For example, a Cloud TPU in the `us-central1-a` zone can only use a key in the `us-central1` region.

Next, [create a key](https://docs.cloud.google.com/kms/docs/create-key) in your key ring. After creating a CMEK, you will need to grant the Compute Engine service account access to your key.

## Grant permission to use the key

You must grant the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) IAM role on the Cloud KMS key to the [Compute Engine service agent](https://docs.cloud.google.com/iam/docs/service-agents#compute-engine-service-agent) in your Google Cloud project. Granting this role allows the Compute Engine service to access and use your encryption key.

To grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role to the Compute Engine service agent, select one of the following options:

### gcloud

Run the following command:
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
        --location LOCATION \
        --keyring RING_NAME \
        --member serviceAccount:service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
        --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
        --project KEY_PROJECT_ID
    

Replace the following:

  * `KEY_NAME`: the name of your key.
  * `LOCATION`: the location where you created your key ring.
  * `RING_NAME`: the name of your key ring.
  * `PROJECT_NUMBER`: your Google Cloud project number.
  * `KEY_PROJECT_ID`: your key project ID.



### Console

  1. In the Google Cloud console, go to the **Key management** page. 

[Go to Key management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key.

  3. Click the name of the key that you want to modify.

  4. Click the **Permissions** tab.

  5. Click person_add **Grant access**. The **Grant access to key** pane opens.

  6. In the **New principals** field, enter the name of the Compute Engine service agent:
         
         service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with your Google Cloud project number.

  7. In the **Select a role** menu, select **Cloud KMS CryptoKey Encrypter/Decrypter**.

  8. Click **Save**.




## Create a TPU VM with a CMEK

You can specify a CMEK when creating a TPU VM by using the TPU API or the Queued Resources API.

### TPU API

To specify a CMEK when creating a TPU VM by using the Cloud TPU API, use the `--boot-disk` argument to the `tpu-vm create` command to specify the encryption key to use:
    
    
    gcloud compute tpus tpu-vm create TPU_NAME \
        --zone ZONE \
        --boot-disk kms-key=projects/PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME \
        --version=TPU_RUNTIME_VERSION \
        --accelerator-type=ACCLERATOR_TYPE
    

Replace the following:

  * `TPU_NAME`: the name of your TPU VM.
  * `ZONE`: the [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) where you plan to create your Cloud TPU.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the region where you created your key ring.
  * `RING_NAME`: the name of your key ring.
  * `KEY_NAME`: the name of your key.
  * `TPU_RUNTIME_VERSION`: the Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions).
  * `ACCELERATOR_TYPE`: the accelerator type for your Cloud TPU that you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).



### Queued Resources API

To specify a CMEK when creating a TPU VM by using the Queued Resources API, use the `--bootdisk` argument to the `queued-resources create` command to specify the encryption key to use:
    
    
    gcloud compute tpus queued-resources create QUEUED_RESOURCE_ID \
        --zone ZONE \
        --node-id NODE_ID \
        --boot-disk kms-key=projects/PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME \
        --runtime-version=TPU_RUNTIME_VERSION \
        --accelerator-type=ACCLERATOR_TYPE
    

Replace the following:

  * `QUEUED_RESOURCE_ID`: the user-assigned ID of the queued resource request.
  * `ZONE`: the [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) where you plan to create your Cloud TPU.
  * `NODE_ID`: the user-assigned ID of the Cloud TPU which is created when the queued resource request is allocated.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the region where you created your key ring.
  * `RING_NAME`: the name of your key ring.
  * `KEY_NAME`: the name of your key.
  * `TPU_RUNTIME_VERSION`: the Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions).
  * `ACCELERATOR_TYPE`: the accelerator type for your Cloud TPU that you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).



For information about creating TPU VMs with CMEKs by using GKE, see [Use customer-managed encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek) in the GKE documentation.

## Deleted or revoked CMEKs

If a CMEK is revoked or deleted, any TPU VM that uses a boot disk encrypted with the deleted or revoked CMEK, won't be automatically shut down. The TPU VM will still be able to access data on the encrypted boot disk until the VM is shut down or restarted. This lets you recover your data if you restore access to a revoked or deleted key. If you re-enable a key, you can start or repair your TPU VM, and the boot disk will be successfully decrypted and loaded.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
