---
url: https://docs.cloud.google.com/tpu/docs/cmek-tpu-compute/
title: Encrypt a TPU VM boot disk with a customer-managed encryption key (CMEK) with Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:25.235475+00:00
---

# Encrypt a TPU VM boot disk with a customer-managed encryption key (CMEK) with Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/cmek-tpu-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Encrypt a TPU VM boot disk with a customer-managed encryption key (CMEK) with Compute Engine

By default, Cloud TPU encrypts customer content at rest. Cloud TPU handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Cloud TPU. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Cloud TPU resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

To use a CMEK, [create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring#kms-create-key-ring-gcloud). Create your key ring in the same location where you create your TPU VM or slice. For example, a TPU VM in the `us-central1-a` zone can only use a key in the `us-central1` region.

Next, [create a key](https://docs.cloud.google.com/kms/docs/create-key) in your key ring. After creating a CMEK, lets the Compute Engine service account access your key.

## Grant permission to use the key

Grant the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) IAM role on the Cloud KMS key to the [Compute Engine service agent](https://docs.cloud.google.com/iam/docs/service-agents#compute-engine-service-agent) in your Google Cloud project. Granting this role lets the Compute Engine service access and use your encryption key.

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

  * KEY_NAME: The name of your key.
  * LOCATION: The location where you created your key ring.
  * RING_NAME: The name of your key ring.
  * PROJECT_NUMBER: Your Google Cloud project number.
  * KEY_PROJECT_ID: Your key project ID.



### Console

  1. In the Google Cloud console, go to the **Key management** page. 

[Go to Key management](https://console.cloud.google.com/security/kms)

  2. Click the key ring name that contains the key.

  3. Click the key name that you want to modify.

  4. Click **Permissions**.

  5. Click **Grant Access**. The **Grant Access** pane opens.

  6. In the **New principals** field, enter the Compute Engine service agent name:
         
         service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com
         

Replace PROJECT_NUMBER with your Google Cloud project number.

  7. In the **Select a role** menu, select **Cloud KMS CryptoKey Encrypter/Decrypter**.

  8. Click **Save**.




## Create a TPU VM with a CMEK

You can specify a CMEK when creating a TPU VM or an instance template for a managed instance group (MIG) by using the `--boot-disk-kms-key` flag.

### Create a single TPU VM instance with a CMEK

To specify a CMEK when creating a single TPU VM, use the `--boot-disk-kms-key` flag in the `gcloud compute instances create` command:
    
    
      gcloud compute instances create TPU_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --maintenance-policy=TERMINATE \
        --boot-disk-kms-key=projects/KEY_PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
    

Replace the following placeholders:

  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM, for example, `us-central1-b`.
  * KEY_PROJECT_ID: The project that contains the encryption key.
  * REGION: The region where you created your key ring.
  * RING_NAME: The name of your key ring.
  * KEY_NAME: The name of your key.

**Note:** This example creates a TPU VM instance using the on-demand provisioning model. For information about using other provisioning models, see [Plan your TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).

### Create a MIG with a single-host slice with a CMEK

To use a CMEK with a MIG, specify the key when you create the instance template.

  1. Create an instance template using the `--boot-disk-kms-key` flag:
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
             --machine-type=MACHINE_TYPE \
             --maintenance-policy=TERMINATE \
             --image-family=IMAGE_FAMILY \
             --image-project=IMAGE_PROJECT \
             --boot-disk-kms-key=projects/KEY_PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
         

Replace the following placeholders:

     * INSTANCE_TEMPLATE_NAME: A name for your instance template.
     * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
     * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
     * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
     * KEY_PROJECT_ID: The project that contains the encryption key.
     * REGION: The region where you created your key ring.
     * RING_NAME: The name of your key ring.
     * KEY_NAME: The name of your key.
**Note:** This example creates an instance template using the on-demand provisioning model. For information about using other provisioning models, see [Plan your TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).
  2. Create a MIG using the template:
         
         gcloud compute instance-groups managed create MIG_NAME \
             --size=MIG_SIZE \
             --template=INSTANCE_TEMPLATE_NAME \
             --zone=ZONE \
             --size=MIG_SIZE
         

Replace the following placeholders:

     * MIG_NAME: A name for your MIG.
     * MIG_SIZE: The number of TPU VMs in the MIG.
     * INSTANCE_TEMPLATE_NAME: The name of the instance template to use.
     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM, for example, `us-central1-b`.
     * MIG_SIZE: The number of TPU VMs in the MIG. For a single-host TPU VM, set the size to 1.



### Create a MIG with a multi-host slice with a CMEK

When you create a multi-host slice MIG, specify the encryption key in the instance template.

  1. Create the instance template.
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME
             --machine-type=MACHINE_TYPE \
             --maintenance-policy=TERMINATE \
             --image-family=IMAGE_FAMILY \
             --image-project=IMAGE_PROJECT \
             --boot-disk-kms-key=projects/KEY_PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
         

Replace the following placeholders:

     * INSTANCE_TEMPLATE_NAME: A name for your instance template.
     * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
     * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
     * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
     * KEY_PROJECT_ID: The project that contains the encryption key.
     * REGION: The region where you created your key ring.
     * RING_NAME: The name of your key ring.
     * KEY_NAME: The name of your key.
**Note:** This example creates an instance template using the on-demand provisioning model. For information about using other provisioning models, see [Plan your TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).
  2. Create a workload policy.

The following command creates a workload policy:
         
         gcloud compute resource-policies create workload WORKLOAD_POLICY_NAME \
         --type=high-throughput \
         --accelerator-topology=TOPOLOGY
         

Replace the following placeholders:

     * WORKLOAD_POLICY_NAME: The name of your workload policy.
     * TOPOLOGY: The topology of the TPU VMs, for example, `4x4x8`.
  3. Create the MIG.
         
         gcloud compute instance-groups managed create MIG_NAME \
             --size=MIG_SIZE \
             --target-size-policy-mode=bulk \
             --template=INSTANCE_TEMPLATE_NAME \
             --zone=ZONE \
             --default-action-on-vm-failure=do-nothing \
             --workload-policy=WORKLOAD_POLICY_NAME
         

Replace the following placeholders:

     * MIG_NAME: The name of your MIG.
     * MIG_SIZE: The number of VMs in the MIG. This value is validated against the topology specified in the workload policy.
     * INSTANCE_TEMPLATE_NAME: The name of your instance template.
     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for your MIG.
     * WORKLOAD_POLICY_NAME: The name of your workload policy.



For information about creating TPU VMs with CMEKs by using GKE, see [Use customer-managed encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek) in the GKE documentation.

## Deleted or revoked CMEKs

If a CMEK is revoked or deleted, any TPU VM that uses a boot disk encrypted with the deleted or revoked CMEK does not automatically shut down. The TPU VM still accesses data on the encrypted boot disk until you shut down or restart the VM. This lets you recover your data if you restore access to a revoked or deleted key. If you re-enable a key, you can start or repair your TPU VM, and the boot disk successfully decrypts and loads.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
