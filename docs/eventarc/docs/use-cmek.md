---
url: https://docs.cloud.google.com/eventarc/docs/use-cmek/
title: Use customer-managed encryption keys \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:53.018977+00:00
---

# Use customer-managed encryption keys  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Use customer-managed encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

By default, Eventarc encrypts customer content at rest. Eventarc handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Eventarc. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Eventarc resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

Customer-managed encryption keys are stored as software keys, in a [Cloud HSM cluster](https://docs.cloud.google.com/kms/docs/hsm), or [externally using Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

Cloud KMS produces audit logs when keys are enabled, disabled, or used by Eventarc Advanced resources to encrypt and decrypt messages. For more information, see the [Cloud KMS audit logging information](https://docs.cloud.google.com/kms/docs/audit-logging).

## What is protected with CMEK

**Note:** Enabling a channel with CMEK protects the Pub/Sub topic used as a transport layer by Eventarc Standard. However, the CMEK key is not displayed through the Google Cloud console. You can use the Google Cloud CLI to [verify that a CMEK key is enabled for a Pub/Sub topic](https://docs.cloud.google.com/eventarc/docs/troubleshooting#pubsub-topic-cmek-key).

You can configure CMEK for a channel that Eventarc Standard uses and encrypt the events that pass through the channel. Enabling a channel with CMEK protects the data associated with it by using an encryption key that only you can access.

When you enable CMEK for the Google channel in a Google Cloud project, all Eventarc Standard triggers for Google event types in that project and region are fully encrypted with that CMEK key. _CMEK keys can't be applied on a per-trigger basis._

## Before you begin

Before using this feature in Eventarc, you should:

###  Console 

  1. Enable the Cloud KMS and Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com,eventarc.googleapis.com)

  2. [Create a key ring](https://docs.cloud.google.com/kms/docs/creating-keys#kms-create-key-ring-console).
  3. [Create a key for a specified key ring](https://docs.cloud.google.com/kms/docs/creating-keys#kms-create-symmetric-encrypt-decrypt-console).



###  gcloud 

  1. Update `gcloud` components. 
         
         gcloud components update

  2. Enable the Cloud KMS and Eventarc APIs for the project that will store your encryption keys. 
         
         gcloud services enable cloudkms.googleapis.com eventarc.googleapis.com

  3. [Create a key ring](https://docs.cloud.google.com/kms/docs/creating-keys#kms-create-key-ring-gcloud).
  4. [Create a key for a specified key ring](https://docs.cloud.google.com/kms/docs/creating-keys#kms-create-symmetric-encrypt-decrypt-gcloud).



For information on all flags and possible values, run the command with the `--help` flag.

###  Terraform 

  1. Enable the Cloud KMS and Eventarc APIs for the project that will store your encryption keys by configuring the [`google_project_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/google_project_service) resource:
         
         # Enable Cloud KMS API
         resource "google_project_service" "cloudkms" {
           service            = "cloudkms.googleapis.com"
           disable_on_destroy = false
         }
         
         # Enable Eventarc API
         resource "google_project_service" "eventarc" {
           service            = "eventarc.googleapis.com"
           disable_on_destroy = false
         }

  2. Create a key ring and key by configuring the [`google_kms_key_ring`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_key_ring) and [`google_kms_crypto_key`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_crypto_key) resources:
         
         resource "random_id" "default" {
           byte_length = 8
         }
         
         # Create a Cloud KMS key ring
         resource "google_kms_key_ring" "default" {
           name     = "${random_id.default.hex}-example-keyring"
           location = "us-central1"
         }
         
         # Create a Cloud KMS key
         resource "google_kms_crypto_key" "default" {
           name            = "example-key"
           key_ring        = google_kms_key_ring.default.id
           rotation_period = "7776000s"
         }




For more information about using Terraform, see the [Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform) documentation.

Note that Cloud KMS and Eventarc are regionalized services. The region for the Cloud KMS key and the protected Eventarc channel must be the same.

## Grant the Eventarc service account access to a key

To grant the Eventarc service account access to the Cloud KMS key, add the service account as a principal of the key, and grant the service account the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) role:

###  Console 

When you enable CMEK for a Google or third-party channel through the console, you are prompted to grant the **Cloud KMS CryptoKey Encrypter/Decrypter** role to the service account. For more information, in this document, see Enable CMEK for Google event types or Enable CMEK for a third-party event channel.

###  gcloud 
    
    
     gcloud kms keys add-iam-policy-binding KEY_NAME \
         --keyring RING_NAME \
         --location LOCATION \
         --member serviceAccount:SERVICE_AGENT_EMAIL \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter

Replace the following:

  * `KEY_NAME`: the name of the key. For example, `my-key`.
  * `RING_NAME`: the name of the key ring. For example, `my-keyring`.
  * `LOCATION`: the location of the key. For example, `us-central1`.
  * `SERVICE_AGENT_EMAIL`: the email address of the service account with the `eventarc.serviceAgent`role.

For example, `service-PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com`. For more information, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents).




###  Terraform 

  1. Generate the service identity for the Eventarc service by configuring the [`google_project_service_identity`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/project_service_identity) resource:
         
         resource "google_project_service_identity" "eventarc_sa" {
           provider = google-beta
           project  = data.google_project.default.project_id
           service  = "eventarc.googleapis.com"
         }

  2. Grant the Cloud KMS role to the Eventarc service account by configuring the [`google_kms_crypto_key_iam_member`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_kms_crypto_key_iam) resource:
         
         # Grant service account access to Cloud KMS key
         resource "google_kms_crypto_key_iam_member" "default" {
           crypto_key_id = google_kms_crypto_key.default.id
           role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
           member        = "serviceAccount:${google_project_service_identity.eventarc_sa.email}"
         }




## Enable CMEK for Google event types

Eventarc triggers that [route Google event types](https://docs.cloud.google.com/eventarc/docs/event-types#directly-from-a-google-cloud-source) publish events to a virtual channel referred to as a _Google channel_ that is project and regional-specific. This virtual channel is available in all Eventarc regions.

When you enable CMEK for the Google channel in a Google Cloud project, all Eventarc triggers for Google event types in that project and region are fully encrypted with that CMEK key. You can add multiple CMEK keys, and associate each with a specific region for the Google channel. CMEK keys can't be applied on a per-trigger basis.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. Click a channel with a Google **Provider**.

  3. In the **Edit channel** page, select the **Use a customer-managed encryption key (CMEK)** checkbox.

  4. Click **Add encryption key**.

  5. Select a **Region** and, in the **CMEK encryption key** list, select a key ring that you have created for the region. Note that you can add only one encryption key per region for a channel.

  6. Optional: To manually enter the resource name of the key, in the **CMEK encryption key** list, click **Don't see your key? Enter key resource name** , and enter the key name in the specified format.

  7. If prompted, grant the `cloudkms.cryptoKeyEncrypterDecrypter` role to the Eventarc service account with the `eventarc.serviceAgent` role.

  8. Optional: Click **Add encryption key** to add another key ring that you have created for a different region.

  9. Click **Save**.




###  gcloud 
    
    
     gcloud eventarc google-channels update \
         --location=LOCATION \
         --crypto-key=KEY

Replace the following:

  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the Google channel to be protected. It must match the location of the key used. Note that you can add only one encryption key per region for a channel.
  * `KEY`: the fully qualified Cloud KMS key name in the format `projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`.



###  Terraform 

Enable CMEK for the `GoogleChannelConfig` resource in a given project and location by configuring the [`google_eventarc_google_channel_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_google_channel_config) resource:
    
    
    # Specify a CMEK key for the `GoogleChannelConfig` resource
    resource "google_eventarc_google_channel_config" "default" {
      location        = "us-central1"
      name            = "googleChannelConfig"
      crypto_key_name = google_kms_crypto_key.default.id
      depends_on      = [google_kms_crypto_key_iam_member.default]
    }

###  REST 

You can update the `GoogleChannelConfig` resource using the [`projects.locations.updateGoogleChannelConfig`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations/updateGoogleChannelConfig) method and specify a CMEK key for a given project and location.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the Google channel to be protected. It must match the location of the key used—for example, `us-central1`. Note that you can add only one encryption key per region for a channel.
  * `KEY_NAME`: the name of the key—for example, `my-key`.
  * `RING_NAME`: the name of the key ring—for example, `my-keyring`.



Request JSON body: 
    
    
    {
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleChannelConfig"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleChannelConfig" | Select-Object -Expand Content

If successful, the response body contains an updated instance of [`GoogleChannelConfig`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/GoogleChannelConfig): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/googleChannelConfig",
      "updateTime": "2025-03-05T17:56:54.106390447Z",
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    

**Note:** To protect the Google channel in the `eu` multi-region, you must use a Cloud KMS key from `europe` since Cloud KMS uses a different name to represent the same multi-region. For more information, see [Cloud KMS multi-regional](https://docs.cloud.google.com/kms/docs/locations#multi_regional) and [Eventarc multi-regional](https://docs.cloud.google.com/eventarc/docs/locations#gcs-triggers) locations.

If you are creating Pub/Sub triggers using your own existing topics, for comprehensive CMEK protection, we recommend that you also configure the KMS key on the topic. For more information, see [Configuring Pub/Sub topics](https://docs.cloud.google.com/pubsub/docs/encryption#configuring_topics).

## Verify Cloud KMS usage

To verify that the channel is now CMEK-compliant:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click a trigger that lists a Google Cloud source as its **Event provider** and a **Region** that you have protected using CMEK.

  3. On the **Trigger details** page, the **Encryption** status displays, the message, `Events encrypted using Customer-managed encryption keys`.




###  gcloud 

To confirm the CMEK key, you can use the [`google-channels describe`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-channels/describe) command.
    
    
     gcloud eventarc google-channels describe \
         --location=LOCATION

The output should be similar to the following:
    
    
     cryptoKeyName: projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
     name: projects/PROJECT_ID/locations/LOCATION/googleChannelConfig
     updateTime: '2022-06-28T17:24:56.365866104Z'

The `cryptokeyName` value shows the Cloud KMS key used for the Google channel.

###  Terraform 

To confirm the CMEK key, you can use the Terraform `state show` command.
    
    
    terraform state show google_eventarc_google_channel_config.default

The output should be similar to the following:
    
    
    # google_eventarc_google_channel_config.default:
    resource "google_eventarc_google_channel_config" "default" {
        crypto_key_name = "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
        id              = "projects/PROJECT_ID/locations/LOCATION/googleChannelConfig"
        location        = "LOCATION"
        name            = "projects/PROJECT_ID/locations/LOCATION/googleChannelConfig"
        project         = "PROJECT_ID"
        update_time     = "2025-03-24T17:15:08.809635011Z"
    }

###  REST 

To confirm the CMEK key, you can retrieve the `GoogleChannelConfig` resource using the [`projects.locations.getGoogleChannelConfig`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations/getGoogleChannelConfig) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the protected Google channel.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleChannelConfig"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleChannelConfig" | Select-Object -Expand Content

If successful, the response body contains an instance of [`GoogleChannelConfig`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/GoogleChannelConfig): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/googleChannelConfig",
      "updateTime": "2025-03-05T17:56:54.106390447Z",
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    

## Enable CMEK for a third-party channel

An Eventarc channel for third parties is a resource through which non-Google Cloud entities that offer an Eventarc source can interact with destinations. This channel is specific to a region and you can add only one key per third-party channel. 

To enable CMEK for a third-party channel:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. Click a channel with a third-party **Provider**.

  3. In the **Channel details** page, click edit **Edit**.

  4. In the **Edit channel** page, for **Encryption** , select **Cloud KMS key**.

  5. In the **Key type** list, select a method to manage your keys.

You can manage your keys manually or you can use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) which lets you generate key rings and keys on-demand. If the Autokey option is disabled, it isn't yet integrated with the current resource type.

  6. In the **Select a Cloud KMS key** list, select a key. Note that you can add only one encryption key per region for a channel.

  7. Optional: To manually enter the resource name of the key, in the **Select a Cloud KMS key** list, click **Enter key manually** , and enter the key name in the specified format.

  8. If prompted, grant the [`cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) to the [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#eventarc-service-agent).

  9. Click **Save**.




###  gcloud 
    
    
     gcloud eventarc channels update CHANNEL_NAME \
         --location=LOCATION \
         --crypto-key=KEY

Replace the following:

  * `CHANNEL_NAME`: the name of the third-party channel. To create a new third-party channel, see [Create a channel](https://docs.cloud.google.com/eventarc/standard/docs/third-parties/create-channels#create-channel).
  * `LOCATION`: the region of the third-party channel to be protected. It must match the location of the key.
  * `KEY`: the fully qualified Cloud KMS key name in the format `projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`.



###  Terraform 

Specify a CMEK key for a third-party channel by configuring the [`google_eventarc_channel`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_channel) resource. For example:
    
    
    resource "google_eventarc_channel" "default" {
      location        = "us-central1"
      name            = "CHANNEL_NAME"
      crypto_key_name = google_kms_crypto_key.default.id
    }

Replace `CHANNEL_NAME` with the name of the third-party channel.

###  REST 

You can update a `Channel` resource using the [`projects.locations.channels.patch`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels/patch) method and specify a CMEK key for a given project and location.

Before using any of the request data, make the following replacements: 

  * `CHANNEL_NAME`: the channel name.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the channel to be protected. It must match the location of the key used—for example, `us-central1`. Note that you can add only one encryption key per region for a channel.
  * `KEY_NAME`: the name of the key—for example, `my-key`.
  * `RING_NAME`: the name of the key ring—for example, `my-keyring`.



Request JSON body: 
    
    
    {
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME?updateMask=cryptoKeyName"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME?updateMask=cryptoKeyName" | Select-Object -Expand Content

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.operations#Operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Verify Cloud KMS usage

To verify that the channel is now CMEK-compliant:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Triggers** page.

[Go to Triggers](https://console.cloud.google.com/eventarc/triggers)

  2. Click a trigger with a third-party source as its **Event provider** and a **Region** that you have protected using CMEK.

  3. In the **Trigger details** page, the status of **Encryption** displays the message, `Events encrypted using Customer-managed encryption keys`.




###  gcloud 
    
    
     gcloud eventarc channels describe CHANNEL_NAME \
         --location=LOCATION

The output should be similar to the following:
    
    
     createTime: '2022-06-28T18:05:52.403999904Z'
     cryptoKeyName: projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
     name: projects/PROJECT_ID/locations/LOCATION/googleChannelConfig
     pubsubTopic: projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID
     state: ACTIVE
     uid: 5ea277f9-b4b7-4e7f-a8e0-6ca9d7204fa3
     updateTime: '2022-06-28T18:09:18.650727516Z'

The `cryptokeyName` value shows the Cloud KMS key used for the third-party channel.

###  Terraform 

To confirm the CMEK key, you can use the Terraform `state show` command.
    
    
    terraform state show google_eventarc_channel.default

The output should be similar to the following:
    
    
    # google_eventarc_channel.default:
    resource "google_eventarc_channel" "default" {
    create_time     = "2025-03-31T13:07:44.721274062Z"
    crypto_key_name = "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    id              = "projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME"
    location        = "LOCATION"
    name            = "CHANNEL_NAME"
    project         = "PROJECT_ID"
    pubsub_topic    = "projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID"
    state           = "ACTIVE"
    uid             = "406302e9-1d41-4479-8f4f-2524a803790e"
    update_time     = "2025-03-31T13:07:49.708241490Z"
    }

###  REST 

To confirm the CMEK key for a channel, you can retrieve a `Channel` resource using the [`projects.locations.channels.get`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels/get) method.

Before using any of the request data, make the following replacements: 

  * `CHANNEL_NAME`: the channel name.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the protected channel.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME" | Select-Object -Expand Content

If successful, the response body contains an instance of [`Channel`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels#Channel): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME",
      "uid": "12f941a6-196a-457b-bfdb-ca21138859d0",
      "createTime": "2025-01-29T15:05:12.113912689Z",
      "updateTime": "2025-01-29T15:05:17.210986285Z",
      "pubsubTopic": "projects/PROJECT_ID/topics/TOPIC_ID",
      "state": "ACTIVE",
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    

## Display the key used for a channel

You can describe an Eventarc channel and display the Cloud KMS key being used for the channel.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. Click a channel name.

  3. Any CMEK encryption keys being used for the channel are displayed.




###  gcloud 

Based on the type of channel, run the following command:

###  Google channel 
    
    
    gcloud eventarc google-channels describe \
        --location=LOCATION

###  Third-party channel 
    
    
    gcloud eventarc channels describe CHANNEL_NAME \
        --location=LOCATION

The output should contain a line similar to the following:
    
    
    cryptoKeyName: projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME

The `cryptoKeyName` value shows the Cloud KMS key being used for the channel.

###  Terraform 

Based on the type of channel, run the following command:

###  Google channel 
    
    
    terraform state show google_eventarc_google_channel_config.default

###  Third-party channel 
    
    
    terraform state show google_eventarc_channel.default

The output should contain a line similar to the following:
    
    
    crypto_key_name= "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"

The `crypto_key_name` value shows the Cloud KMS key being used for the channel.

###  REST 

Based on the type of channel, make the following request:

###  Google channel 

To confirm the CMEK key for a given project and location, you can retrieve the `GoogleChannelConfig` resource using the [`projects.locations.getGoogleChannelConfig`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations/getGoogleChannelConfig) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the protected Google channel.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleChannelConfig"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleChannelConfig" | Select-Object -Expand Content

If successful, the response body contains an instance of [`GoogleChannelConfig`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/GoogleChannelConfig): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/googleChannelConfig",
      "updateTime": "2025-03-05T17:56:54.106390447Z",
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    

###  Third-party channel 

To confirm the CMEK key for a given project and location, you can retrieve a `Channel` resource using the [`projects.locations.channels.get`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels/get) method.

Before using any of the request data, make the following replacements: 

  * `CHANNEL_NAME`: the channel name.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the protected channel.



To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME" | Select-Object -Expand Content

If successful, the response body contains an instance of [`Channel`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels#Channel): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME",
      "uid": "12f941a6-196a-457b-bfdb-ca21138859d0",
      "createTime": "2025-01-29T15:05:12.113912689Z",
      "updateTime": "2025-01-29T15:05:17.210986285Z",
      "pubsubTopic": "projects/PROJECT_ID/topics/TOPIC_ID",
      "state": "ACTIVE",
      "cryptoKeyName": "projects/PROJECT_ID/locations/LOCATION/keyRings/RING_NAME/cryptoKeys/KEY_NAME"
    }
    

## Disable CMEK

You can disable the CMEK protection associated with a channel. The events that are delivered through such channels are still protected by [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/docs/security/encryption/default-encryption). To delete the CMEK protection associated with a channel:

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Channels** page.

[Go to Channels](https://console.cloud.google.com/eventarc/channels)

  2. Based on the type of channel, complete the following steps:

###  Google channel 

     1. Click a channel with a Google **Provider**.
     2. On the **Edit channel** page, hold the pointer over the **CMEK encryption key** list to see the delete **Delete item** button.
     3. Click delete **Delete item**.
     4. Click **Save**.

You might need to refresh the page to enable the **Use a customer-managed encryption key (CMEK)** checkbox.

### Third-party channel

     1. Click a channel with a third-party **Provider**.
     2. On the **Channel details** page, click edit **Edit**.
     3. On the **Edit channel** page, for **Encryption** , select **Google-managed encryption key**.
     4. Click **Save**.




###  gcloud 

Based on the type of channel, run the following command:

###  Google channel 
    
    
    gcloud eventarc google-channels \
        update --clear-crypto-key

###  Third-party channel 
    
    
    gcloud eventarc channels CHANNEL_NAME \
        update --clear-crypto-key

###  Terraform 

Based on the type of channel, clear the `crypto_key_name` value by not specifying it when configuring the Terraform resource:

###  Google channel 
    
    
    resource "google_eventarc_google_channel_config" "default" {
      location        = "us-central1"
      name            = "googleChannelConfig"
    }

###  Third-party channel 
    
    
    resource "google_eventarc_channel" "default" {
      location        = "us-central1"
      name            = "CHANNEL_NAME"
    }

###  REST 

Based on the type of channel, make the following request:

###  Google channel 

To delete the CMEK key, you can update the `GoogleChannelConfig` resource for a given project and location using the [`projects.locations.updateGoogleChannelConfig`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations/updateGoogleChannelConfig) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the protected Google channel to be protected.



Request JSON body: 
    
    
    {
      "cryptoKeyName": ""
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "cryptoKeyName": ""
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleChannelConfig"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "cryptoKeyName": ""
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/googleChannelConfig" | Select-Object -Expand Content

If successful, the response body contains an updated instance of [`GoogleChannelConfig`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/GoogleChannelConfig): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/googleChannelConfig",
      "updateTime": "2025-03-05T17:56:54.106390447Z"
    }
    

###  Third-party channel 

To delete the CMEK key, you can update a `Channel` resource for a given project and location using the [`projects.locations.channels.patch`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.channels/patch) method.

Before using any of the request data, make the following replacements: 

  * `CHANNEL_NAME`: the channel name.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [region](https://docs.cloud.google.com/eventarc/docs/locations) of the protected channel.



Request JSON body: 
    
    
    {
      "cryptoKeyName": ""
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "cryptoKeyName": ""
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME?updateMask=cryptoKeyName"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "cryptoKeyName": ""
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://eventarc.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME?updateMask=cryptoKeyName" | Select-Object -Expand Content

If successful, the response body contains a newly created instance of [`Operation`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.operations#Operation): 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.eventarc.v1.OperationMetadata",
        "createTime": "2024-01-25T17:17:45.782370139Z",
        "target": "projects/PROJECT_ID/locations/LOCATION/channels/CHANNEL_NAME",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

## Apply a CMEK organization policy

Eventarc is integrated with two [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) to help ensure CMEK usage across an organization:

  * `constraints/gcp.restrictNonCmekServices` is used to require CMEK protection.
  * `constraints/gcp.restrictCmekCryptoKeyProjects` is used to limit which Cloud KMS keys are used for CMEK protection.

**Note:** CMEK organization policies only apply to newly created resources within supported Google Cloud services. For more information, see [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) and [CMEK organization policies](https://docs.cloud.google.com/kms/docs/cmek-org-policy).

This integration lets you specify the following encryption compliance requirements for Eventarc resources in your organization:

  * Require CMEKs for new Eventarc resources
  * Restrict Cloud KMS keys for an Eventarc project



### Considerations when applying organization policies

Before applying any CMEK organization policies, you should be aware of the following.

  * **Prepare for a propagation delay**

After you set or update an organization policy, it can take up to 15 minutes for the new policy to take effect.

  * **Consider existing resources**

Existing resources are not subject to newly created organization policies. For example, an organization policy does not retroactively apply to existing pipelines. Those resources are still accessible without a CMEK and, if applicable, are still encrypted with existing keys.

  * **Verify required permissions to set an organization policy**

The permission to set or update the organization policy might be difficult to acquire for testing purposes. You must be granted the [Organization Policy Administrator role](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#required-roles), which can only be granted at the organization level (rather than the project or folder level).

Although the role must be granted at the organization level, it is still possible to specify a policy that only applies to a specific project or folder.




### Require CMEKs for new Eventarc resources

You can use the `constraints/gcp.restrictNonCmekServices` constraint to require that CMEKs be used to protect new Eventarc resources in an organization.

If set, this organization policy causes all resource creation requests without a specified Cloud KMS key to fail.

After you set this policy, it applies only to new resources in the project. Any existing resources without Cloud KMS keys applied continue to exist and are accessible without issue.

**Important:** Before setting this policy, make sure to enable CMEK for the Google channel in a Google Cloud project so that all Eventarc triggers for Google event types in that project and region are fully encrypted with that CMEK key. In this document, see Enable CMEK for Google event types.

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. Using the **Filter** , search for the following constraint:
         
         constraints/gcp.restrictNonCmekServices
         

  3. In the Name column, click **Restrict which services may create resources without CMEK**.

  4. Click edit **Manage Policy**.

  5. On the **Edit policy** page, under **Policy source** , select **Override parent's policy**.

  6. Under **Rules** , click **Add a rule**.

  7. In the **Policy values** list, select **Custom**.

  8. In the **Policy type** list, select **Deny**.

  9. In the **Custom values** field, enter the following:
         
         is:eventarc.googleapis.com
         

  10. Click **Done** , and then click **Set policy**.




###  gcloud 

  1. Create a temporary file `/tmp/policy.yaml` to store the policy:
         
         name: projects/PROJECT_ID/policies/gcp.restrictNonCmekServices
           spec:
             rules:
             - values:
                 deniedValues:
                 - is:eventarc.googleapis.com

Replace `PROJECT_ID` with the ID of the project where you are applying this constraint.

  2. Run the [`org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) command:
         
         gcloud org-policies set-policy /tmp/policy.yaml




To verify that the policy is successfully applied, you can try to create an Eventarc Standard channel in the project. The process fails unless you specify a Cloud KMS key.

### Restrict Cloud KMS keys for an Eventarc project

You can use the `constraints/gcp.restrictCmekCryptoKeyProjects` constraint to restrict the Cloud KMS keys that you can use to protect a resource in an Eventarc project.

For example, you can specify a rule similar to the following: "For applicable Eventarc resources in `projects/my-company-data-project`, Cloud KMS keys used in this project must come from `projects/my-company-central-keys` OR `projects/team-specific-keys`."

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies/list)

  2. Using the **Filter** , search for the following constraint:
         
         constraints/gcp.restrictCmekCryptoKeyProjects
         

  3. In the Name column, click **Restrict which projects may supply KMS CryptoKeys for CMEK**.

  4. Click edit **Manage Policy**.

  5. On the **Edit policy** page, under **Policy source** , select **Override parent's policy**.

  6. Under **Rules** , click **Add a rule**.

  7. In the **Policy values** list, select **Custom**.

  8. In the **Policy type** list, select **Allow**.

  9. In the **Custom values** field, enter the following:
         
         under:projects/KMS_PROJECT_ID
         

Replace `KMS_PROJECT_ID` with the ID of the project where the Cloud KMS keys you want to use are located.

For example, `under:projects/my-kms-project`.

  10. Click **Done** , and then click **Set policy**.




###  gcloud 

  1. Create a temporary file `/tmp/policy.yaml` to store the policy:
         
         name: projects/PROJECT_ID/policies/gcp.restrictCmekCryptoKeyProjects
           spec:
             rules:
             - values:
                 allowedValues:
                 - under:projects/KMS_PROJECT_ID

Replace the following

     * `PROJECT_ID`: the ID of the project where you are applying this constraint.
     * `KMS_PROJECT_ID`: the ID of the project where the Cloud KMS keys you want to use are located.
  2. Run the [`org-policies set-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-policy) command:
         
         gcloud org-policies set-policy /tmp/policy.yaml




To verify that the policy is successfully applied, you can try to create an Eventarc Standard channel using a Cloud KMS key from a different project. The process will fail.

## Disabling and enabling Cloud KMS keys

A key version stores the cryptographic key material that you use to encrypt, decrypt, sign, and verify data. You can disable this key version so that data that was encrypted with the key can't be accessed.

When Eventarc cannot access Cloud KMS keys, event publishing with channels fails with `FAILED_PRECONDITION` errors and event delivery stops. You can enable a key in the _Disabled_ state so that the encrypted data can be accessed again.

### Disable Cloud KMS keys

To prevent Eventarc from using the key to encrypt or decrypt your event data, do any of the following:

  * We recommend [disabling the key version](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) you have configured for the channel. This affects only the Eventarc channels and triggers that are associated with the specific key.
  * Optional: [Revoke the `cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) from the Eventarc service account. This affects all the project's Eventarc channels and triggers that support events encrypted using CMEK.



Although neither operation guarantees instantaneous access revocation, Identity and Access Management (IAM) changes generally propagate faster. For more information, see [Cloud KMS resource consistency](https://docs.cloud.google.com/kms/docs/consistency) and [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### Re-enable Cloud KMS keys

To resume event delivery and publishing, [restore access](https://docs.cloud.google.com/kms/docs/enable-disable#enable_a_disabled_key_version) to Cloud KMS.

## Pricing

This integration does not incur additional costs beyond the key operations, which are billed to your Google Cloud project. The use of CMEK for a channel incurs charges for access to the Cloud KMS service based on [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing).

For more information on the most current pricing information, see [Cloud KMS Pricing](https://cloud.google.com/kms/pricing).

## What's next

  * [Troubleshoot CMEK issues](https://docs.cloud.google.com/eventarc/docs/troubleshoot-cmek)
  * [Recommended practices for using CMEKs](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices)
  * [Use CMEK with Eventarc Advanced](https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
