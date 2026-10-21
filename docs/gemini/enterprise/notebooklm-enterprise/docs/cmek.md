---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/cmek/
title: Customer-managed encryption keys \u00a0|\u00a0 Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:14.260048+00:00
---

# Customer-managed encryption keys  |  Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)



Send feedback 

#  Customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

By default, Gemini Notebook Enterprise encrypts customer content at rest. Gemini Notebook Enterprise handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Gemini Notebook Enterprise. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Gemini Notebook Enterprise resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

When a CMEK key is registered, Gemini Notebook Enterprise calls Cloud KMS periodically to maintain a logically isolated instance of your data. This happens even if the CMEK config isn't set as the default and there are no apps or data connectors using it. The usage comes from setting up and running the instance, not from the volume of data or number of users accessing it. See [Cloud Key Management Service pricing](https://docs.cloud.google.com/kms/pricing).

To completely shut off all Cloud KMS usage, you must unregister your Cloud KMS key, disable the key, or revoke its permissions. Disabling the Gemini Notebook Enterprise API doesn't delete your CmekConfig or your data, and you continue to be billed for CMEK usage.

**Note:** Instances in US or EU regions require data encryption.**Note:** Gemini Notebook Enterprise data at rest uses [Google-owned and Google-managed encryption key (GMEK) by default](https://docs.cloud.google.com/docs/security/encryption/default-encryption). CMEK, as described on this page, lets you use your own keys instead of the GMEK keys.**Note:** If you want to ensure that your Gemini Notebook Enterprise resources are always protected by CMEK, we strongly recommend that you configure a CMEK organization policy. For more information, see [Organization policy constraints](https://docs.cloud.google.com/kms/docs/org-policy-constraints).

## Limitations of Cloud KMS in Gemini Notebook Enterprise

The following limitations apply to CMEK (Cloud KMS) keys in Gemini Notebook Enterprise:

  * Keys that are already applied to an instance can't be changed, although key versions can be rotated.

  * You can't change the encryption settings of notebooks after creation. An unprotected notebook can't later be protected, and protection can't be removed.



  * CMEK-protection with Gemini Notebook Enterprise is not integrated with [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) search.


  * You must use US or EU multi-region instances (not global ones). For more information about multi-regions and data residency, including limits associated with using non-global locations, see [locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations).


  * If you need to register more than one key for a project, contact your Google account team to request a quota increase for CMEK configurations, providing a justification for why you need more than one key.

The following limitations apply to EKM or HSM with CMEK:

    * Your EKM and HSM quota for encrypt and decrypt calls should have at least 1,000 QPM of headroom. For how to check your quotas, see [Check your Cloud KMS quotas](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas#check_your_quotas).

    * If using EKM, the key must be reachable for more than 90% of any time window of longer than 30 seconds. If the key isn't reachable for this amount of time, it can negatively impact indexing and search freshness.

    * If there are billing issues, persistent out-of-quota issues, or persistent unreachability issues for more than 12 hours, the service automatically turns down the CmekConfig associated with the EKM or HSM key.



  * You can use Terraform to configure CMEK for Gemini Notebook Enterprise. See [google_discovery_engine_cmek_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_cmek_config).

**Note:** The [Podcast API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api) (deprecated) is a standalone component, separate from Gemini Notebook Enterprise. Podcasts generated using the Podcast API aren't protected by CMEK. However, all podcasts created from within Gemini Notebook Enterprise notebooks are CMEK-protected.

## Before you begin

Make sure you satisfy the following prerequisites:

  * Create a multi-region symmetric Cloud KMS key. See [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [Create a key](https://docs.cloud.google.com/kms/docs/create-key) in the Cloud KMS documentation.

    * Set the rotation period to **Never (Manual rotation)**.

    * For **Location** , select **Multi-region** , and select **europe** or **us** from the drop-down.



  * The CryptoKey Encrypter/Decrypter IAM role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the key has been granted to the Discovery Engine service agent. The service agent account has an email address that uses the following format: `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`. For general instructions on how to add a role to a service agent, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

  * The CryptoKey Encrypter/Decrypter IAM role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the key has been granted to the Cloud Storage service agent. If this role is not granted, data import for CMEK-protected instances will fail because Discovery Engine is not able to make the CMEK-protected, temporary bucket and directory that is required for importing.

  * Don't set up any instances that you want managed by your key until after you have completed the key registration instructions on this page.




## Register your Cloud KMS key

To encrypt data using CMEK, you must register your multi-region key. Optionally, if your data needs single-region keys, for example, when using third-party connectors, you also need to register your single-region keys.

#### Before you begin

Make sure of the following:

  * The region isn't already protected by a key. The procedure below fails if a key is already registered for the region through the REST command. To determine if there is an active key in Gemini Notebook Enterprise for a location, see View Cloud KMS keys.


  * You have the [Gemini Notebook Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) role.



#### Procedure

### REST

To register your own key for Gemini Notebook Enterprise, follow these steps:

  1. Call the [`UpdateCmekConfig`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs/patch) method with the key that you want to register.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{"kmsKey":"projects/KMS_PROJECT_ID/locations/KMS_LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"}' \
         "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cmekConfigs/CMEK_CONFIG_ID?set_default=SET_DEFAULT"
         

Replace the following:

     * `KMS_PROJECT_ID`: the ID of your project that contains the key. The project number won't work.
     * `KMS_LOCATION`: the multi-region of your key: `us` or `europe`.
     * `KEY_RING`: the name of the key ring that holds the key.
     * `KEY_NAME`: the name of the key.
     * `PROJECT_ID`: the ID of your project that contains the instance.
     * `LOCATION`: the multi-region of your instance: `us` or `eu`.
     * `CMEK_CONFIG_ID`: set a unique ID for the CmekConfig resource, for example, `default_cmek_config`.
     * `SET_DEFAULT`: set to `true` to use the key as the default key for subsequent instances created in the multi-region.

**Important:** SET_DEFAULT is required to automatically apply the CmekConfig on subsequent resources.

#### Example command and result
    
    $ curl -X PATCH
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json"
    -d '{"kmsKey":"projects/key-project-456/locations/us/keyRings/my-key-ring/cryptoKeys/my-key"}'
    "https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-123/locations/us/cmekConfigs/default_cmek_config?set_default=true"
    
    
    * * *
    
    
    {
     "name": "projects/my-ai-app-project-123/locations/us/operations/update-cmek-config-56789",
     "metadata": {
      "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.UpdateCmekConfigMetadata"
     }
    }
    

  2. Wait up to 24 hours for your registered key to be ready for use with Gemini Notebook Enterprise. A registered key can't protect notebooks until it is ready. If you open the UI during this 24-hour window, you might encounter errors, or new notebooks might not be protected by the key. After 24 hours, confirm the key is active by following the steps in Verify that Gemini Notebook Enterprise is protected by a key.

  3. Set up the instance. For instructions, see [Set up Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-notebooklm).




### Console

**Note:** When you use the console to register the keys, you cannot modify or remove keys from a location using the console. You need to call the [`DeleteCmekConfig`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs/delete) method to unregister your Cloud KMS key.

#### Procedure

To register your own key for Gemini Notebook Enterprise, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click **Settings** , and select the **CMEK** tab.

  3. Click **Add key** for the **us** or **eu** location.

![Click add key for a location.](https://docs.cloud.google.com/gemini/enterprise/docs/images/cmek-images/kms-key-first-party-connectors.png)Click add key.
     1. Click the **Select a Cloud KMS key** drop-down, and select the key.

        * If the key is in a different project, click **Switch project** , click your project name, type the name of the key you created, and select the key.

        * If you know the resource name of the key, click **Enter manually** , paste the key resource name, and click **Save**.

     2. Click **OK > Save**.

  4. Verify that your key is ready to use before you set up an instance. A registered key can't protect notebooks until it's ready. It can take up to 24 hours for your registered key to be ready for use with Gemini Notebook Enterprise. See Verify that Gemini Notebook Enterprise is protected by a key.

  5. Set up the instance. For instructions, see [Set up Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-notebooklm).




This registers your key, creating a CmekResource called `default_cmek_config`.

It can take several hours for the ingested data to show up in search results.

**Note:** After you set up the instances, verify that they are protected by the keys. For more information, see verify that the instance is protected by a Cloud KMS key.

## Unregister your Cloud KMS key

To unregister your key from Gemini Notebook Enterprise, follow these steps:

  1. Call the `DeleteCmekConfig` method with the CmekConfig resource name that you want to unregister.
         
         curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cmekConfigs/CMEK_CONFIG_ID"
         

Replace the following:

     * `LOCATION`: the multi-region of your instance: `us` or `eu`.
     * `PROJECT_ID`: the ID of your project that contains the instance.
     * `CMEK_CONFIG_ID`: the ID of the CmekConfig resource. If you registered your key using the console, the ID is `default_cmek_config`.

An example curl call and response looks like this: 
    
    $ curl -X DELETE
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    "https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-123/locations/us/cmekConfigs/default_cmek_config"
     
    {
     "name": "projects/my-ai-app-project-123/locations/us/operations/delete-cmek-config-56789",
     "metadata": {
      "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.DeleteCmekConfigMetadata"
     }
    }
    

  2. Optional: Record the `name` value returned by the method and follow the instructions in [Get details about a long-running operation](https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations#get-details) to see when the operation is complete.

Deleting a CmekConfig is a long-running operation that can take up to a couple of days to complete. This is because the underlying encrypted resources are fully deprovisioned before the CmekConfig is removed.


**Note:** A CmekConfig resource can only be deleted if no Gemini Notebook Enterprise resources are being protected by that CmekConfig resource.

## Verify that Gemini Notebook Enterprise is protected by a key

**Important:** Only those notebooks created after the key is registered are protected by the key.

Because it can take up to 24 hours for a registered key to be ready for use with Gemini Notebook Enterprise, users who open the app before the key is ready might encounter errors, or new notebooks might not be protected by the key.

**Important:** If your users see the "Failed to fetch project" error, don't try to re-register keys or change permissions. The error resolves automatically once the provisioning is complete.

If you want to confirm that your key is ready to use and that Gemini Notebook Enterprise is protected by your key, follow these steps:

  1. Call the `ListCmekConfigs` method:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cmekConfigs"
         

Replace the following:

     * `LOCATION`: the multi-region of your instance: `us` or `eu`.
     * `PROJECT_ID`: the ID of your Google Cloud project that contains the data.

#### Example command and result
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://us-discoveryengine.googleapis.com/v1alpha/projects/my-project-123/locations/us/cmekConfigs"
    
    
    * * *
    
    
    {
      "cmekConfigs": [
        {
        "name": "projects/123456/locations/us/cmekConfigs/cmek-config-1",
        "kmsKey": "projects/key-project-456/locations/us/keyRings/my-key-ring/cryptoKeys/my-key",
        **"state": "ACTIVE",
        "isDefault": true,**
        "kmsKeyVersion": "projects/key-project-456/locations/us/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/1",
        **"notebooklmState": "NOTEBOOK_LM_READY"**
        }
      ]
    }
    
    

  2. Review the output from the command.

If the provisioning process is still ongoing, the output contains `"notebooklmState": NOTEBOOK_LM_NOT_READY`.

The CmekConfig is ready for use if all of the following are in the output:

     * `"state": "ACTIVE"`
     * `"isDefault": true`
     * `"notebooklmState": NOTEBOOK_LM_READY`



## Rotate Cloud KMS keys

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can't change which key protects an existing instance, but you can rotate that key to a new key version. When you make a new version of a registered key the primary version, Gemini Notebook Enterprise detects the change and re-encrypts your data with the new key version automatically. You don't need to call a Gemini Notebook Enterprise method to start a rotation.

For general information about rotating keys, see [Key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) in the Cloud KMS guide.

To rotate a key, follow these steps:

  1. Create a new key version and make it the primary version. For instructions, see [Rotate a key](https://docs.cloud.google.com/kms/docs/rotate-key) in the Cloud KMS guide.

Leave the previous key version enabled. Re-encryption starts automatically after Gemini Notebook Enterprise detects the new primary version.

  2. Confirm that Gemini Notebook Enterprise detected the new key version. To view your CmekConfig, see Verify that Gemini Notebook Enterprise is protected by a key. Check the following fields in the output:

     * `kmsKeyVersion` shows the new key version.
     * `state` is `ACTIVE`.
     * `lastRotationTimestampMicros` shows when the rotation started.
  3. Keep the previous key version enabled for at least 30 days after `kmsKeyVersion` shows the new key version.

**Caution:** Gemini Notebook Enterprise doesn't report when the re-encryption of all underlying storage is complete. If you disable or destroy the previous key version before the re-encryption is complete, the data that is still encrypted under that version becomes inaccessible.
  4. Disable the previous key version, and make sure that everything is working as before. See [Enable and disable key versions](https://docs.cloud.google.com/kms/docs/enable-disable) in the Cloud KMS guide.

  5. When you are certain that no problems were caused by disabling the previous key version, destroy it. See [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore) in the Cloud KMS guide.

**Tip:** Destruction is scheduled rather than immediate. While a key version is scheduled for destruction, it behaves as if it were disabled, and you can restore it to cancel the destruction.



## If a Cloud KMS key is disabled or revoked

If a key is [disabled](https://docs.cloud.google.com/kms/docs/enable-disable) or permissions for the key are revoked, the instance stops ingesting data and stops serving data within 15 minutes. You may re-enable your key within 30 days to resume operations before the CMEK config expires and any associated data is permanently deleted. However, re-enabling a key or restoring permissions takes a long time. It can take up to 24 hours before the instance can resume serving data.

Therefore, don't disable a key unless necessary. Disabling and enabling a key on an instance is a time-consuming operation. For example, repeatedly switching a key between disabled and enabled means it will take a long time for the instance to reach a protected state. Disabling a key and re-enabling it immediately afterward could result in days of downtime because the key is first disabled from the instance and subsequently re-enabled.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
