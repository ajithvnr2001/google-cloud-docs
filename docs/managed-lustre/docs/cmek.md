---
url: https://docs.cloud.google.com/managed-lustre/docs/cmek/
title: Customer-managed encryption keys for Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:58.194727+00:00
---

# Customer-managed encryption keys for Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Customer-managed encryption keys for Managed Lustre Stay organized with collections  Save and categorize content based on your preferences. 

By default, Google Cloud Managed Lustre encrypts customer content at rest. Managed Lustre handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Managed Lustre. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Managed Lustre resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

The following Managed Lustre data is protected by CMEK:

  * File data
  * File system metadata, such as filenames

When you use CMEK in Managed Lustre, your projects can consume Cloud KMS cryptographic requests quotas. CMEK-encrypted instances consume quotas when reading or writing data in Managed Lustre. Encryption and decryption operations using CMEK keys affect Cloud KMS quotas only if you use hardware (Cloud HSM) or external (Cloud EKM) keys. For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas). 

## Limitations

The following limitations apply:

  * Dynamic provisioning of CMEK-protected Managed Lustre instances is not supported in Google Kubernetes Engine, but static provisioning is supported.

  * Cluster Toolkit does not support CMEK-protected Managed Lustre instances. 

  * When creating a CMEK-protected Managed Lustre instance within a VPC Service Controls perimeter, your Cloud KMS key must be either:

    * Within the same VPC Service Controls perimeter; or
    * Accessible through an egress rule. See [Use VPC Service Controls with customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/managed-lustre/docs/vpc-sc#vpcsc-cmek) for details.



## Create a Cloud KMS key

Before creating a CMEK-enabled Lustre instance, you must have a Cloud KMS key ring and a Cloud KMS key.

Managed Lustre supports three [protection levels](https://docs.cloud.google.com/kms/docs/protection-levels):

  * Software (`SOFTWARE`)
  * Hardware (`HSM`)
  * External over the internet (`EXTERNAL`)



When creating your key, we recommend creating your Cloud KMS key in a different project from the project containing your Managed Lustre instance. See [Separation of duties](https://docs.cloud.google.com/kms/docs/separation-of-duties).

The Cloud KMS key must be created in the same region as the Managed Lustre instance you are creating.

To create a key:

  1. If you don't already have one, [create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring).
  2. [Create a Cloud KMS key](https://docs.cloud.google.com/kms/docs/create-key).



## Grant IAM permissions to the Managed Lustre service agent

Managed Lustre uses a [service agent](https://docs.cloud.google.com/managed-lustre/docs/access-control#service-agent) to access your resources and perform actions on your behalf. To use CMEK, you must grant the service agent the `roles/cloudkms.cryptoKeyEncrypterDecrypter` IAM role on your Cloud KMS key.

**Google Cloud console users**

If you'll be creating your CMEK-protected Managed Lustre instance using the Google Cloud console, you can skip this section. The Google Cloud console grants the required permissions as part of the instance creation flow.

Jump to Create a CMEK-enabled Managed Lustre instance.

If you don't know your project's service agent identity, see [Create or retrieve the service agent identity](https://docs.cloud.google.com/managed-lustre/docs/access-control#get-service-agent).

### Grant permissions to the service agent

To grant the role to the service agent, use the `gcloud kms keys add-iam-policy-binding` command:
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
      --keyring=KEY_RING \
      --location=REGION \
      --project=KMS_PROJECT_ID \
      --member=serviceAccount:SERVICE_AGENT_IDENTITY \
      --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    

Replace the following variables:

  * KEY_NAME: The name of your Cloud KMS key.
  * KEY_RING: The name of the key ring that contains the key.
  * REGION: The region where your key ring is located.
  * KMS_PROJECT_ID: The ID of the project that contains your Cloud KMS key.
  * SERVICE_AGENT_IDENTITY: The Managed Lustre service agent identity (`service-<var>PROJECT_NUMBER</var>@gcp-sa-lustre.iam.gserviceaccount.com`).



## Create a CMEK-enabled Managed Lustre instance

To create a Managed Lustre instance protected by CMEK:

###  gcloud 

To create a CMEK-protected instance using `gcloud`, follow the steps in [Create an instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance#create_an_instance). Specify the key identifier as the value of `--kms-key-name` as shown below:
    
    
    gcloud lustre instance create INSTANCE_ID \
      --filesystem=FILESYSTEM_NAME \
      --per-unit-storage-throughput=PERF_TIER \
      --capacity-gib=CAPACITY_GIB \
      --location=ZONE \
      --network=NETWORK_NAME \
      --project=PROJECT_ID \
      --kms-key-name=projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY_NAME
    

The Cloud KMS key must exist in the same region as the Managed Lustre instance you are creating.

###  REST 

To create a CMEK-protected instance using the REST API, follow the steps in [Create an instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance#create_an_instance). Specify the key identifier as the value of `kmsKey` as shown below:
    
    
    POST https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances?instanceId=INSTANCE_NAME
    Authorization: Bearer AUTH_TOKEN
    {
      "filesystem": "FILESYSTEM_NAME",
      "perUnitStorageThroughput": PERF_TIER,
      "capacityGib": CAPACITY_GIB,
      "network": "NETWORK_NAME",
      "kmsKey": "projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
    }
    

The Cloud KMS key must exist in the same region as the Managed Lustre instance you are creating.

See the [`Instance` resource reference documentation](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances#Instance) for a full list of fields and their descriptions.

###  Google Cloud console

To create a CMEK-protected instance using the Google Cloud console, follow the steps in [Create an instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance#create_an_instance). While on the **Create instance** page of the Google Cloud console:

  1. From the **Encryption** section, select **Cloud KMS key**.

  2. Select **Cloud KMS** as the Key management type, and select your key. If your key is in a different project (recommended), click **Switch project** , select the key project, and select your key. The Cloud KMS key must exist in the same region as the Managed Lustre instance you are creating.

  3. If your Managed Lustre service agent does not have the required permissions to use CMEK, you're prompted to grant the `cloudkms.cryptoKeyEncrypterDecrypter` role. Click **Grant** to apply the role.




If the Cloud KMS key isn't available, or there are permission issues when you initiate the create operation, the operation fails and returns a `FAILED_PRECONDITION` error.

## Key management

Cloud Key Management Service keys can be rotated, disabled, re-enabled, or destroyed. They can become unavailable for various reasons.

### Rotate a key

You can rotate your Cloud KMS key. Rotating a key creates a new _key version_.

  * Rotating a key does not re-encrypt the data in your Managed Lustre instance. Managed Lustre does not support decrypting or re-encrypting data.

  * The existing capacity of your Managed Lustre instance continues to be encrypted by the version of the key in use when the instance was created.

  * When you increase your instance's storage capacity, the new capacity is protected by the key version that is primary when you make the capacity increase request, and any data that is written to that capacity is protected by that key version.




This means that you can have multiple key versions encrypting your Managed Lustre instance, if you have increased the instance's capacity after rotating the key version.

### Disable a key

You can disable a key version. During the time that **any key version used by your Managed Lustre instance** is disabled, the instance is suspended. To resume your instance, return all key versions that protect your instance to an available state. See Unavailable keys for information about suspended instances.

See [Enable and disable key versions](https://docs.cloud.google.com/kms/docs/enable-disable) for more information.

### Re-enable a key

If a key version is disabled, you can re-enable it through the Cloud KMS API. See [Enable and disable key versions](https://docs.cloud.google.com/kms/docs/enable-disable).

To resume the Managed Lustre instance, all versions of the key that are encrypting storage capacity must be enabled or restored.

After all required keys return to the `ENABLED` state, Managed Lustre automatically detects key changes and restarts the instance. The instance state becomes `ACTIVE` and the Managed Lustre service resumes normal operation. You can perform I/O and all other long-running operations.

### Destroy a key

Cloud KMS key versions can be destroyed, meaning that the key material is permanently deleted.

Cloud KMS keys cannot be destroyed immediately; instead, you must schedule a key version for destruction. During the scheduled duration, you can restore a key version to cancel its destruction. See [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore) for more details.

A key version that is scheduled for destruction is unavailable; any Managed Lustre instances protected by that key version are suspended. See Unavailable keys for information about suspended instances.

Once a key version is destroyed, it cannot be restored. Your instance remains suspended permanently. The only operation available on the Managed Lustre instance is deleting the instance.

### Unavailable keys

A key can become unavailable for the following reasons:

  * The key is disabled.
  * The key is destroyed or scheduled to be destroyed.
  * The required permissions are removed from the service agent.
  * Billing is disabled on the Cloud KMS key's project and remains disabled for more than one hour.
  * An external key remains unreachable for more than one hour.



In these cases, within a few minutes of the event, the Managed Lustre instance is shut down and its instance state is set to `SUSPENDED`.

A `SUSPENDED` instance can be recovered by making the key available again.

Possible suspension reasons are as follows:

Action on key | Instance state | Suspension reason | Can be re-enabled  
---|---|---|---  
Disable | `SUSPENDED` | `KEY_DISABLE` | Yes  
Schedule for destruction | `SUSPENDED` | `KEY_DESTROY_SCHEDULED` | Yes  
Destroy | `SUSPENDED` | `KEY_DESTROY` | No  
Remove permission | `SUSPENDED` | `PERMISSION_DENIED` | Yes  
Disable billing for 1h | `SUSPENDED` | `BILLING_DISABLED` | Yes  
EKM key unreachable for 1h | `SUSPENDED` | `EKM_KEY_UNREACHABLE` | Yes  
  
When an instance is suspended:

  * Long-running operations, such as instance updates and import/export, are blocked and return a `FAILED_PRECONDITION` error.
  * I/O operations stop responding until server nodes are shut down. This occurs within 30 minutes.
  * The only allowed long-running operation is `DeleteInstance`.



Instances that have been suspended for longer than four months may not be able to be resumed.

### Billing for suspended instances

If a Managed Lustre instance enters the `SUSPENDED` state due to key unavailability, you continue to accrue charges for the instance. The suspension state does not pause billing. To stop incurring charges for the instance, you must delete it.

You are also billed separately by Cloud KMS for any key versions in use.

### View key usage and list key versions

You can view the Google Cloud resources within your organization that are protected by your Cloud KMS keys. See [View key usage](https://docs.cloud.google.com/kms/docs/view-key-usage) for details.

To view the full list of key versions used by your Managed Lustre instance, use the `gcloud kms inventory search-protected-resources` command:
    
    
    gcloud kms inventory search-protected-resources \
      --keyname=projects/KMS_PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
      --scope=organizations/ORGANIZATION_ID \
      --filter="name:projects/PROJECT_ID/locations/REGION/instances/INSTANCE_ID" \
      --flatten="cryptoKeyVersions" \
      --format="value(cryptoKeyVersions)"
    

Where:

  * ORGANIZATION_ID is the numerical ID of your organization. See [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



You can also view key information from the **Key Inventory** page.

[Go to Key Inventory](https://console.cloud.google.com/security/kms/keys)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
