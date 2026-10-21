---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek/
title: Customer-managed encryption keys \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:14.591414+00:00
---

# Customer-managed encryption keys  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

By default, Agent Search encrypts customer content at rest. Agent Search handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Agent Search. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Agent Search resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

When a CMEK key is registered, Agent Search calls Cloud KMS periodically to maintain a logically isolated instance of your data. This happens even if the CMEK config isn't set as the default and there are no apps or data connectors using it. The usage comes from setting up and running the instance, not from the volume of data or number of users accessing it. See [Cloud Key Management Service pricing](https://docs.cloud.google.com/kms/pricing).

To completely shut off all Cloud KMS usage, you must unregister your Cloud KMS key, disable the key, or revoke its permissions. Disabling the Agent Search API doesn't delete your CmekConfig or your data, and you continue to be billed for CMEK usage.

**Note:** Apps or data stores in US or EU regions require data encryption.**Note:** Agent Search data at rest uses [Google-owned and Google-managed encryption key (GMEK) by default](https://docs.cloud.google.com/docs/security/encryption/default-encryption). CMEK, as described on this page, lets you use your own keys instead of the GMEK keys.**Note:** If you want to ensure that your Agent Search resources are always protected by CMEK, we strongly recommend that you configure a CMEK organization policy. For more information, see [Organization policy constraints](https://docs.cloud.google.com/kms/docs/org-policy-constraints).

## Limitations of Cloud KMS in Agent Search

The following limitations apply to CMEK (Cloud KMS) keys in Agent Search:

  * Keys that are already applied to an app or data connector can't be changed, although key versions can be rotated.


  * CMEK-protection with Agent Search is not integrated with [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview) search.


  * You must use US or EU multi-region apps and data stores (not global ones). For more information about multi-regions and data residency, including limits associated with using non-global locations, see [locations](https://docs.cloud.google.com/generative-ai-app-builder/docs/locations).


  * If you need to register more than one key for a project, contact your Google account team to request a quota increase for CMEK configurations, providing a justification for why you need more than one key.

The following limitations apply to EKM or HSM with CMEK:

    * Your EKM and HSM quota for encrypt and decrypt calls should have at least 1,000 QPM of headroom. For how to check your quotas, see [Check your Cloud KMS quotas](https://docs.cloud.google.com/kms/docs/monitor-adjust-quotas#check_your_quotas).

    * If using EKM, the key must be reachable for more than 90% of any time window of longer than 30 seconds. If the key isn't reachable for this amount of time, it can negatively impact indexing and search freshness.

    * If there are billing issues, persistent out-of-quota issues, or persistent unreachability issues for more than 12 hours, the service automatically turns down the CmekConfig associated with the EKM or HSM key.



  * Apps or data connectors created before a key is registered to the project can't be protected by the key.


  * You can't [tune search models](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search) for apps and data connectors that are protected by keys.


  * For apps with multiple data connectors, if one data connector uses a CMEK configuration, all other data connectors must also use the same CMEK configuration.


  * For Agent Search, Enterprise edition is required. For information about Enterprise edition, see [About advanced features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features).

  * [First-party connectors](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es) are not CMEK-compliant except for the "import-once" and "periodic" apps and data connectors for BigQuery and Cloud Storage.

  * Healthcare search apps and data connectors, and third-party connectors are CMEK-compliant. For general information about healthcare apps and data connectors, see [Create a healthcare search app or data connector](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc). For information about making third-party connectors CMEK-compliant, see About single-region keys for third-party connectors.

  * Keys don't apply to the following RAG APIs because these APIs don't store content at rest: [check grounding](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding), [grounded generation](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen), and [ranking](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking).



  * You can use Terraform to configure CMEK for Agent Search. See [google_discovery_engine_cmek_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_cmek_config).



## About single-region keys for third-party connectors

If you use third-party connectors and want to use your own keys to protect the connected data, then you need to create three supplemental single-region keys in addition to the multi-region key. The commands for creating keys are given in the following procedure, Register your Cloud KMS key.

The single keys need to be created for the following regions:

Multi-region | Single-regions  
---|---  
`eu` | `europe-west1` | `europe-west4` | `europe-north1`  
`us` | `us-east1` | `us-central1` | `us-west1`  
  
## Before you begin

Make sure you satisfy the following prerequisites:

  * Create a multi-region symmetric Cloud KMS key. See [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [Create a key](https://docs.cloud.google.com/kms/docs/create-key) in the Cloud KMS documentation.

    * Set the rotation period to **Never (Manual rotation)**.

    * For **Location** , select **Multi-region** , and select **europe** or **us** from the drop-down.



  * The CryptoKey Encrypter/Decrypter IAM role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the key has been granted to the Discovery Engine service agent. The service agent account has an email address that uses the following format: `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com`. For general instructions on how to add a role to a service agent, see [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

  * The CryptoKey Encrypter/Decrypter IAM role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the key has been granted to the Cloud Storage service agent. If this role is not granted, data import for CMEK-protected apps and data connectors will fail because Discovery Engine is not able to make the CMEK-protected, temporary bucket and directory that is required for importing.

  * Don't create any apps or data connectors that you want managed by your key until after you have completed the key registration instructions on this page.



  * Enterprise edition features are turned on for the app. See [Turn Enterprise edition on or off](https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-edition).



## Register your Cloud KMS key

To encrypt data using CMEK, you must register your multi-region key. Optionally, if your data needs single-region keys, for example, when using third-party connectors, you also need to register your single-region keys.

#### Before you begin

Make sure of the following:

  * The region isn't already protected by a key. The procedure below fails if a key is already registered for the region through the REST command. To determine if there is an active key in Agent Search for a location, see View Cloud KMS keys.


  * You have the [Discovery Engine Admin](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control#discoveryengine.admin) (`roles/discoveryengine.admin`) role.



#### Procedure

### REST

To register your own key for Agent Search, follow these steps:

  1. Call the [`UpdateCmekConfig`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.cmekConfigs/patch) method with the key that you want to register.
         
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
     * `PROJECT_ID`: the ID of your project that contains the app or data connector.
     * `LOCATION`: the multi-region of your app or data connector: `us` or `eu`.
     * `CMEK_CONFIG_ID`: set a unique ID for the CmekConfig resource, for example, `default_cmek_config`.
     * `SET_DEFAULT`: set to `true` to use the key as the default key for subsequent apps and data connectors created in the multi-region.

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
    

  2. Verify that your key is ready to use before you create any apps or data connectors. A registered key can't protect resources until it's ready. It typically takes a few minutes to register a key. See Verify that your Cloud KMS key is ready to use.

To track the registration operation, you can record the `name` value returned by the method and follow [Get details about a long-running operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/long-running-operations#get-details).

After the key is ready, new apps and data connectors in that multi-region are protected by the key. For general information about creating apps, see [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest).

  3. Create the app. For links to instructions for creating various apps, see [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest).




### Console

**Note:** When you use the console to register the keys, you cannot modify or remove keys from a location using the console. You need to call the [`DeleteCmekConfig`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.cmekConfigs/delete) method to unregister your Cloud KMS key.

#### Procedure

To register your own key for Agent Search, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. Click **Settings** , and select the **CMEK** tab.

  3. Click **Add key** for the **us** or **eu** location.

![Click add key for a location.](https://docs.cloud.google.com/gemini/enterprise/docs/images/cmek-images/kms-key-first-party-connectors.png)Click add key.
     1. Click the **Select a Cloud KMS key** drop-down, and select the key.

        * If the key is in a different project, click **Switch project** , click your project name, type the name of the key you created, and select the key.

        * If you know the resource name of the key, click **Enter manually** , paste the key resource name, and click **Save**.

     2. Click **OK > Save**.

  4. Verify that your key is ready to use before you create any apps or data connectors. A registered key can't protect resources until it's ready. See Verify that your Cloud KMS key is ready to use.

  5. Create the app. For links to instructions for creating various apps, see [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest).




This registers your key, creating a CmekResource called `default_cmek_config`.

It can take several hours for the ingested data to show up in search results.

**Note:** After you create the app or data stores, verify that they are protected by the keys. For more information, see verify that an app or data connector is protected by a Cloud KMS key.

## View Cloud KMS keys

To view a registered key for Agent Search, do one of the following:

  * If you have the CmekConfig resource name, call the [`GetCmekConfig`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.cmekConfigs/get) method:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cmekConfigs/CMEK_CONFIG_ID"
        

Replace the following:

    * `LOCATION`: the multi-region of your app or data connector: `us` or `eu`.
    * `PROJECT_ID`: the ID of your project that contains the data.
    * `CMEK_CONFIG_ID`: the ID of the CmekConfig resource. If you registered your key using the console, the ID is `default_cmek_config`.

An example curl call and response looks like this: 
    
    $ curl -X GET
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    "https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-123/locations/us/cmekConfigs/default_cmek_config"
    
    
    * * *
    
    
    {
      "name":
      "projects/my-ai-app-project-123/locations/us/cmekConfigs/default_cmek_config",
      "kmsKey": "projects/key-project-456/locations/us/keyRings/my-key-ring/cryptoKeys/my-key",
      "kmsKeyVersion": "projects/key-project-456/locations/us/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/2",
      "state": "ACTIVE",
      "isDefault": true,
      "lastRotationTimestampMicros": "1788220800000000"
    }
    

  * If you don't have the CmekConfig resource name, call the [`ListCmekConfigs`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.cmekConfigs/list) method:
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cmekConfigs"
        

Replace the following:

    * `LOCATION`: the multi-region of your app or data connector: `us` or `eu`.
    * `PROJECT_ID`: the ID of your project that contains the data.

An example curl call and response looks like this: 
    
    $ curl -X GET
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    "https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-123/locations/us/cmekConfigs"
    
    
    * * *
    
    
    {
      "cmek_configs": [
        {
          "name":
          "projects/my-ai-app-project-123/locations/us/cmekConfigs/default_cmek_config",
          "kmsKey": "projects/key-project-456/locations/us/keyRings/my-key-ring/cryptoKeys/my-key",
          "kmsKeyVersion": "projects/key-project-456/locations/us/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/2",
          "state": "ACTIVE",
          "isDefault": true,
          "lastRotationTimestampMicros": "1788220800000000"
        }
      ]
    }
    




## Verify that your Cloud KMS key is ready to use

After you register a key, you must verify that it's ready to use before it can protect any resources:

  1. View your registered Cloud KMS keys. See View Cloud KMS keys.

  2. Review the output from the command. The CmekConfig is ready for use if all of the following values are in the output:

     * `"state": "ACTIVE"`
     * `"isDefault": true`

If `"isDefault": true`, then the key is automatically applied to protect new apps and data connectors.




You can also check that a default CMEK configuration is set (that is, `"isDefault": true`) using the Google Cloud console:

  1. In the Google Cloud console, go to the **AI Applications** page.

  2. Click **Settings** , and select the **CMEK** tab.

  3. Check that the configuration status for your location shows your registered key.




## Unregister your Cloud KMS key

To unregister your key from Agent Search, follow these steps:

  1. Call the `DeleteCmekConfig` method with the CmekConfig resource name that you want to unregister.
         
         curl -X DELETE \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cmekConfigs/CMEK_CONFIG_ID"
         

Replace the following:

     * `LOCATION`: the multi-region of your app or data connector: `us` or `eu`.
     * `PROJECT_ID`: the ID of your project that contains the app or data connector.
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
    

  2. Optional: Record the `name` value returned by the method and follow the instructions in [Get details about a long-running operation](https://docs.cloud.google.com/generative-ai-app-builder/docs/long-running-operations#get-details) to see when the operation is complete.

Deleting a CmekConfig is a long-running operation that can take up to a couple of days to complete. This is because the underlying encrypted resources are fully deprovisioned before the CmekConfig is removed.


**Note:** A CmekConfig resource can only be deleted if no Agent Search resources are being protected by that CmekConfig resource.

## Verify that an app or data connector is protected by a key

Apps and data connectors that are created after your key is registered are protected by the key. If you want to confirm that a particular app or data connector is protected by your key, follow these steps:

### Verify using the Google Cloud console

  1. To verify whether a data connector is protected by a key:

     1. In the Google Cloud console, go to the **AI Applications** page.

     2. Click **Data stores** , and select your data connector.

     3. Check that the **KMS key** field shows your registered key.




### Verify using the CLI / API

  1. To verify for a data store:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "x-goog-user-project: PROJECT_ID" \
         "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/dataStores/DATA_STORE_ID"
         

Replace the following:

     * `LOCATION`: the multi-region of your project: `us` or `eu`.
     * `PROJECT_ID`: the ID of your project that contains the app or data connector.
     * `DATA_STORE_ID`: the ID of the data store associated with your app or data connector.

An example curl call looks like this: 
    
    curl -X GET
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json"
    -H "x-goog-user-project: my-ai-app-project-123"
    "https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-123/locations/us/collections/default_collection/dataStores/my-data-store-1"
    

  2. To verify for an app:
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "x-goog-user-project: PROJECT_ID" \
         "https://LOCATION-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/ENGINE_ID"
         

Replace the following:

     * `LOCATION`: the multi-region of your project: `us` or `eu`.
     * `PROJECT_ID`: the ID of your project that contains the app.
     * `ENGINE_ID`: the ID of your app.

An example curl call looks like this: 
    
    curl -X GET
    -H "Authorization: Bearer $(gcloud auth print-access-token)"
    -H "Content-Type: application/json"
    -H "x-goog-user-project: my-ai-app-project-123"
    "https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-123/locations/us/collections/default_collection/engines/my-app"
    

  3. Review the output from the command: If the `cmekConfig` field is in the output and the `kmsKey` field shows the key that you registered, then the app or data connector is protected by the key.

An example response for a data store looks like this:
         
         {
          "name": "projects/969795412903/locations/us/collections/default_collection/dataStores/my-data-store-1",
          "displayName": "my-data-store-1",
          "industryVertical": "GENERIC",
          "createTime": "2023-09-05T21:20:21.520552Z",
          "solutionTypes": [
            "SOLUTION_TYPE_SEARCH"
          ],
          "defaultSchemaId": "default_schema",
          "cmekConfig": {
            "name": "projects/969795412903/locations/us/collections/default_collection/dataStores/my-data-store-1/cmekConfigs/default_cmek_config",
            "kmsKey": "projects/my-ai-app-project-123/locations/us/keyRings/my-key-ring/cryptoKeys/my-key"
          }
         }
         

An example response for an app looks like this:
         
         {
           "name": "projects/969795412903/locations/us/collections/default_collection/engines/my-app",
           "displayName": "my-app",
           "dataStoreIds": [
             "my-data-store-1"
           ],
           "solutionType": "SOLUTION_TYPE_SEARCH",
           "searchEngineConfig": {
             "searchTier": "SEARCH_TIER_STANDARD"
           },
           "industryVertical": "GENERIC",
           "appType": "APP_TYPE_INTRANET",
           "cmekConfig": {
            "name": "projects/969795412903/locations/us/collections/default_collection/dataStores/my-data-store-1/cmekConfigs/default_cmek_config",
            "kmsKey": "projects/my-ai-app-project-123/locations/us/keyRings/my-key-ring/cryptoKeys/my-key"
          }
         }
         




## Other data protected by the Cloud KMS key

In addition to data in the apps and data connectors, your keys can protect other types of app-owned core information held by Agent Search, such as the session data generated during [search with follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#commands_for_follow-up_questions). This kind of core information is CMEK-protected if the apps and data connectors are CMEK-protected.

Although you can't run a specific command to verify that sessions are protected, you can verify if the app is protected. Run the Verify that an app or data connector is protected by a key command for the app to see the key in the cmekConfig resource. Then you'll know that the session data is protected.

## Rotate Cloud KMS keys

You can't change which key protects an existing app or data connector, but you can rotate that key to a new key version. When you make a new version of a registered key the primary version, Agent Search detects the change and re-encrypts your data with the new key version automatically. You don't need to call a Agent Search method to start a rotation.

For general information about rotating keys, see [Key rotation](https://docs.cloud.google.com/kms/docs/key-rotation) in the Cloud KMS guide.

**Important:** Do not rotate keys on apps or data connectors associated with recommendations or with any apps that need analytics, and don't rotate the single-region keys used for third-party connectors. See Limitations of Cloud KMS in Agent Search.

To rotate a key, follow these steps:

  1. Create a new key version and make it the primary version. For instructions, see [Rotate a key](https://docs.cloud.google.com/kms/docs/rotate-key) in the Cloud KMS guide.

Leave the previous key version enabled. Re-encryption starts automatically after Agent Search detects the new primary version.

  2. Confirm that Agent Search detected the new key version. To view your CmekConfig, see View Cloud KMS keys. Check the following fields in the output:

     * `kmsKeyVersion` shows the new key version.
     * `state` is `ACTIVE`.
     * `lastRotationTimestampMicros` shows when the rotation started.
  3. Keep the previous key version enabled for at least 30 days after `kmsKeyVersion` shows the new key version.

**Caution:** Agent Search doesn't report when the re-encryption of all underlying storage is complete. If you disable or destroy the previous key version before the re-encryption is complete, the data that is still encrypted under that version becomes inaccessible.
  4. Disable the previous key version, and make sure that everything is working as before. See [Enable and disable key versions](https://docs.cloud.google.com/kms/docs/enable-disable) in the Cloud KMS guide.

  5. When you are certain that no problems were caused by disabling the previous key version, destroy it. See [Destroy and restore key versions](https://docs.cloud.google.com/kms/docs/destroy-restore) in the Cloud KMS guide.

**Tip:** Destruction is scheduled rather than immediate. While a key version is scheduled for destruction, it behaves as if it were disabled, and you can restore it to cancel the destruction.



## If a Cloud KMS key is disabled or revoked

If a key is [disabled](https://docs.cloud.google.com/kms/docs/enable-disable) or permissions for the key are revoked, the app or data connector stops ingesting data and stops serving data within 15 minutes. You may re-enable your key within 30 days to resume operations before the CMEK config expires and any associated data is permanently deleted. However, re-enabling a key or restoring permissions takes a long time. It can take up to 24 hours before the app or data connector can resume serving data.

Therefore, don't disable a key unless necessary. Disabling and enabling a key on an app or data connector is a time-consuming operation. For example, repeatedly switching a key between disabled and enabled means it will take a long time for the app or data connector to reach a protected state. Disabling a key and re-enabling it immediately afterward could result in days of downtime because the key is first disabled from the app or data connector and subsequently re-enabled.

## Troubleshoot: KMS key projects not found error

**Symptom:** When you try to create an app or data connector using a KMS key, you receive an error similar to the following:

`KMS key projects/[...] not found for location: [...] and project number: [...]`

**Issue:** This error message can be misleading. It doesn't necessarily mean that the key doesn't exist. Instead, it might indicate that the KMS key hasn't been registered for use with Agent Search in the specified location.

**Solution:** To resolve this issue, register your key by following the steps in Register your Cloud KMS key. After the registration is complete, you can create apps or data connectors protected by that key.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
