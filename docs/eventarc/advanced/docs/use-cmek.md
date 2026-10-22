---
url: https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek/
title: Use customer-managed encryption keys (CMEK) \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:20.293984+00:00
---

# Use customer-managed encryption keys (CMEK)  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/use-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Use customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

By default, Eventarc encrypts customer content at rest. Eventarc handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Eventarc. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Eventarc resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

Customer-managed encryption keys are stored as software keys, in a [Cloud HSM cluster](https://docs.cloud.google.com/kms/docs/hsm), or [externally using Cloud External Key Manager](https://docs.cloud.google.com/kms/docs/ekm).

## What is protected with CMEK

You can configure CMEK to encrypt the event messages that pass through the following Eventarc Advanced resources:

  * `MessageBus`—An Eventarc Advanced bus
  * `Pipeline`—An Eventarc Advanced pipeline
  * `GoogleApiSource`—An Eventarc Advanced resource which represents a subscription to Google API events for a particular bus



For more information, see the [Eventarc Advanced overview](https://docs.cloud.google.com/eventarc/advanced/docs/overview).

When you enable CMEK for a resource, it protects the data associated with the resource in that region by using an encryption key that only you can access.

Cloud KMS and Eventarc are regionalized services. The region for the Cloud KMS key and the protected Eventarc Advanced resource must be the same.

## Before you begin

Before using this feature in Eventarc, you must perform the following actions:

###  Console 

  1. Enable the Cloud KMS and Eventarc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com,eventarc.googleapis.com)

  2. [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring#kms-create-key-ring-console).
  3. [Create a key for a specified key ring](https://docs.cloud.google.com/kms/docs/creating-keys#kms-create-symmetric-encrypt-decrypt-console).



###  gcloud 

  1. Update `gcloud` components. 
         
         gcloud components update

  2. Enable the Cloud KMS and Eventarc APIs for the project that will store your encryption keys. 
         
         gcloud services enable cloudkms.googleapis.com eventarc.googleapis.com

  3. [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring#kms-create-key-ring-gcloud).
  4. [Create a key for a specified key ring](https://docs.cloud.google.com/kms/docs/creating-keys#kms-create-symmetric-encrypt-decrypt-gcloud).



For information on all flags and possible values, run the command with the `--help` flag.

###  Terraform 

  1. Enable the Cloud KMS and Eventarc APIs for the project that will store your encryption keys by configuring the [`google_project_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/google_project_service) resource:
         
         resource "google_project_service" "apis" {
           for_each = toset([
             "cloudkms.googleapis.com",
             "eventarc.googleapis.com",
             "eventarcpublishing.googleapis.com"
           ])
           service            = each.key
           disable_on_destroy = false
         }

  2. Create a key ring and key by configuring the [`google_kms_key_ring`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_key_ring) and [`google_kms_crypto_key`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/kms_crypto_key) resources. For example:
         
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

## Grant the Eventarc service account access to a key

To grant the Eventarc service account access to the Cloud KMS key, add the service account as a principal of the key, and grant the service account the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms) role:

###  Console 

When you enable CMEK for a bus or pipeline using the Google Cloud console, you are prompted to grant the **Cloud KMS CryptoKey Encrypter/Decrypter** role to the service account. For more information, in this document, see Enable CMEK for a bus or Enable CMEK for a pipeline.

###  gcloud 
    
    
     gcloud kms keys add-iam-policy-binding KEY_NAME \
         --keyring KEY_RING \
         --location REGION \
         --member serviceAccount:SERVICE_AGENT_EMAIL \
         --role roles/cloudkms.cryptoKeyEncrypterDecrypter

Replace the following:

  * `KEY_NAME`: the name of the key—for example, `my-key`
  * `KEY_RING`: the name of the key ring—for example, `my-keyring`
  * `REGION`: the location of the key—for example, `us-central1`
  * `SERVICE_AGENT_EMAIL`: the email address of the service account with the `eventarc.serviceAgent`role

For example, `service-PROJECT_NUMBER@gcp-sa-eventarc.iam.gserviceaccount.com`. For more information, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents).




###  Terraform 

  1. Generate the service identity for the Eventarc service by configuring the [`google_project_service_identity`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/project_service_identity) resource:
         
         # Generate service identity for Eventarc service
         resource "google_project_service_identity" "default" {
           provider   = google-beta
           project    = data.google_project.project.project_id
           service    = "eventarc.googleapis.com"
           depends_on = [google_project_service.apis]
         }

  2. Grant the Cloud KMS role to the Eventarc service account by configuring the [`google_kms_crypto_key_iam_member`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_kms_crypto_key_iam) resource:
         
         # Grant service account access to Cloud KMS key
         resource "google_kms_crypto_key_iam_member" "default" {
           crypto_key_id = google_kms_crypto_key.default.id
           role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
           member        = "serviceAccount:${google_project_service_identity.default.email}"
           depends_on    = [time_sleep.default]
         }




Note that the [`time_sleep`](https://registry.terraform.io/providers/hashicorp/time/latest/docs/resources/sleep) resource adds a delay to allow for service agent and IAM permissions [propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Enable CMEK for a bus

When you enable CMEK for an Eventarc Advanced bus, all messages that pass through the bus are fully encrypted with that CMEK key.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

  2. You can [create a bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus) or, if you are updating a bus, click the name of the bus.

  3. In the **Bus details** page, click edit **Edit**.

  4. In the **Edit bus** page, for **Encryption** , select **Cloud KMS key**.

  5. In the **Key type** list, select a method to manage your keys.

You can manage your keys manually or you can use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) which lets you generate key rings and keys on-demand. If the Autokey option is disabled, it isn't yet integrated with the current resource type.

  6. In the **Select a Cloud KMS key** list, select a key.

  7. Optional: To manually enter the resource name of the key, in the **Select a Cloud KMS key** list, click **Enter key manually** , and enter the key name in the specified format.

  8. If prompted, grant the [`cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) to the [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#eventarc-service-agent).

  9. Click **Save**.




###  gcloud 

Use the [`gcloud eventarc message-buses update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/update) command to enable CMEK for your bus:
    
    
    gcloud eventarc message-buses update BUS_NAME \
        --location=REGION \
        --crypto-key=KEY

Replace the following:

  * `BUS_NAME`: the ID or fully qualified identifier of your bus
  * `REGION`: a [supported Eventarc Advanced location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions)
  * `KEY`: the fully qualified Cloud KMS key name in the format `projects/PROJECT_NAME/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`

The `REGION` of the key must match the [location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) of the bus to be protected.




###  Terraform 

Enable CMEK for your bus by configuring the [`google_eventarc_message_bus`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_message_bus) resource. For example:
    
    
    # Enable CMEK for an Eventarc Advanced bus
    resource "google_eventarc_message_bus" "default" {
      location        = "us-central1"
      message_bus_id  = "example-bus"
      crypto_key_name = google_kms_crypto_key.default.id
      depends_on      = [google_kms_crypto_key_iam_member.default]
    }

### Verify Cloud KMS usage

Verify that the bus is now CMEK-compliant.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

  2. Click the name of the bus that you have protected using CMEK.

  3. On the **Bus details** page, the **Encryption** status indicates the customer-managed encryption key in use. You can click the key to go to it in the Security Command Center.

Otherwise, the status message is `Event messages encrypted using Google-managed encryption keys`.




###  gcloud 

Use the [`gcloud eventarc message-buses describe`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/describe) command to describe your bus:
    
    
     gcloud eventarc message-buses describe BUS_NAME \
         --location=REGION

The output should be similar to the following:
    
    
     cryptoKeyName: projects/PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
     name: projects/PROJECT_ID/locations/REGION/messageBuses/BUS_NAME
     updateTime: '2022-06-28T17:24:56.365866104Z'

The `cryptoKeyName` value shows the Cloud KMS key used for the bus.

###  Terraform 

To confirm the CMEK key, you can use the Terraform `state show` command.
    
    
    terraform state show google_eventarc_message_bus.default

The output should be similar to the following:
    
    
    resource "google_eventarc_message_bus" "default" {
        create_time           = "2026-03-02T21:24:11.493277339Z"
        crypto_key_name       = "projects/PROJECT_ID/locations/us-central1/keyRings/adffca5e8fbc2cca-example-keyring/cryptoKeys/example-key"
        effective_annotations = {}
        effective_labels      = {
            "goog-terraform-provisioned" = "true"
        }
        id                    = "projects/PROJECT_ID/locations/us-central1/messageBuses/example-bus"
        location              = "us-central1"
        message_bus_id        = "example-bus"
        name                  = "projects/PROJECT_ID/locations/us-central1/messageBuses/example-bus"
        project               = "PROJECT_ID"
        terraform_labels      = {
            "goog-terraform-provisioned" = "true"
        }
        uid                   = "771501be-36ac-4336-93e3-f04604e2523e"
        update_time           = "2026-03-02T21:24:29.933105970Z"
    
        logging_config {
            log_severity = "NONE"
        }
    }

### Disable CMEK for a bus

You can disable the CMEK protection associated with a bus. The events that are delivered through the bus are still protected by [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

**Caution:** Disabling CMEK can result in the loss of events stored in Eventarc Advanced at the time of the change. It is the customer's responsibility to ensure that it is safe to disable CMEK. Google is not responsible for outages, loss of data, or compliance issues which result from disabling CMEK for a bus.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

  2. Click the name of the bus.

  3. In the **Bus details** page, click edit **Edit**.

  4. On the **Edit bus** page, for **Encryption** , select **Google-managed encryption key**.

  5. Click **Save**.




###  gcloud 

Use the [`gcloud eventarc message-buses update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/message-buses/update) command to disable CMEK for your bus:
    
    
    gcloud eventarc message-buses update BUS_NAME \
        --location=REGION \
        --clear-crypto-key

###  Terraform 

You can update the bus in place by clearing the `crypto_key_name` value and not specifying it in the Terraform configuration file. For example:
    
    
      # Disable CMEK for an Eventarc Advanced bus
      resource "google_eventarc_message_bus" "default" {
        location        = "us-central1"
        message_bus_id  = "example-bus"
      }
    

## Enable CMEK for a pipeline

When you enable CMEK for an Eventarc Advanced pipeline, all messages that pass through the pipeline are fully encrypted with that CMEK key.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. You can [create a pipeline](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment) or, if you are updating a pipeline, click the name of the pipeline.

  3. In the **Pipeline details** page, click edit **Edit**.

  4. In the **Edit pipeline** page, for **Encryption** , select **Cloud KMS key**.

  5. In the **Key type** list, select a method to manage your keys.

You can manage your keys manually or you can use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) which lets you generate key rings and keys on-demand. If the Autokey option is disabled, it isn't yet integrated with the current resource type.

  6. In the **Select a Cloud KMS key** list, select a key.

  7. Optional: To manually enter the resource name of the key, in the **Select a Cloud KMS key** list, click **Enter key manually** , and enter the key name in the specified format.

  8. If prompted, grant the [`cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) to the [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#eventarc-service-agent).

  9. Click **Save**.




###  gcloud 

Use the [`gcloud eventarc pipelines update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/update) command to enable CMEK for a pipeline:
    
    
     gcloud eventarc pipelines update PIPELINE_NAME \
         --location=REGION \
         --crypto-key=KEY

Replace the following:

  * `PIPELINE_NAME`: the ID or fully qualified identifier of your pipeline
  * `REGION`: a [supported Eventarc Advanced location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions)
  * `KEY`: the fully qualified Cloud KMS key name in the format `projects/PROJECT_NAME/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`

The `REGION` of the key must match the [location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) of the pipeline to be protected.




###  Terraform 

Enable CMEK for your pipeline by configuring the [`google_eventarc_pipeline`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_pipeline) resource. For example:
    
    
    # Enable CMEK for an Eventarc Advanced pipeline
    resource "google_eventarc_pipeline" "default" {
      location    = "us-central1"
      pipeline_id = "example-pipeline"
      destinations {
        http_endpoint {
          uri = google_cloud_run_v2_service.default.uri
        }
        authentication_config {
          google_oidc {
            service_account = google_service_account.default.email
          }
        }
      }
      crypto_key_name = google_kms_crypto_key.default.id
      depends_on      = [google_kms_crypto_key_iam_member.default]
    }

### Verify Cloud KMS usage

Verify that the pipeline is now CMEK-compliant.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. Click the name of the pipeline that you have protected using CMEK.

  3. On the **Pipeline details** page, the **Encryption** status indicates the customer-managed encryption key in use. You can click the key to go to it in the Security Command Center.

Otherwise, the status message is `Event messages encrypted using Google-managed encryption keys`.




###  gcloud 

Use the [`gcloud eventarc pipelines describe`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/describe) command to verify CMEK for your pipeline:
    
    
     gcloud eventarc pipelines describe PIPELINE_NAME \
         --location=REGION

The output should be similar to the following:
    
    
     createTime: '2022-06-28T18:05:52.403999904Z'
     cryptoKeyName: projects/PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
     destinations: ...
     name: projects/PROJECT_ID/locations/REGION/pipelines/PIPELINE_NAME
     uid: 5ea277f9-b4b7-4e7f-a8e0-6ca9d7204fa3
     updateTime: '2022-06-28T18:09:18.650727516Z'

The `cryptoKeyName` value shows the Cloud KMS key used for the pipeline.

###  Terraform 

To confirm the CMEK key, you can use the Terraform `state show` command.
    
    
    terraform state show google_eventarc_pipeline.default

The output should be similar to the following:
    
    
    resource "google_eventarc_pipeline" "default" {
        create_time           = "2026-03-02T21:24:32.651373287Z"
        crypto_key_name       = "projects/PROJECT_ID/locations/us-central1/keyRings/adffca5e8fbc2cca-example-keyring/cryptoKeys/example-key"
        effective_annotations = {}
        effective_labels      = {
            "goog-terraform-provisioned" = "true"
        }
        id                    = "projects/PROJECT_ID/locations/us-central1/pipelines/example-pipeline"
        location              = "us-central1"
        name                  = "projects/PROJECT_ID/locations/us-central1/pipelines/example-pipeline"
        pipeline_id           = "example-pipeline"
        project               = "PROJECT_ID"
        terraform_labels      = {
            "goog-terraform-provisioned" = "true"
        }
        uid                   = "124e444d-55ca-4c99-8529-395bda80c82b"
        update_time           = "2026-03-02T21:28:26.699657974Z"
    
        destinations {
            authentication_config {
                google_oidc {
                    service_account = "eventarc-advanced-sa@PROJECT_ID.iam.gserviceaccount.com"
                }
            }
            http_endpoint {
                uri = "https://example-service-hk27nrrura-uc.a.run.app"
            }
        }
    
        retry_policy {
            max_attempts    = 5
            max_retry_delay = "60s"
            min_retry_delay = "1s"
        }
    }

### Disable CMEK for a pipeline

You can disable the CMEK protection associated with a pipeline. The events that are delivered through the pipeline are still protected by [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

**Caution:** Disabling CMEK can result in the loss of events stored in Eventarc Advanced at the time of the change. It is the customer's responsibility to ensure that it is safe to disable CMEK. Google is not responsible for outages, loss of data, or compliance issues which result from disabling CMEK for a pipeline.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Pipelines** page.

[Go to Pipelines](https://console.cloud.google.com/eventarc/pipelines)

  2. Click the name of the pipeline.

  3. In the **Pipeline details** page, click edit **Edit**.

  4. On the **Edit pipeline** page, for **Encryption** , select **Google-managed encryption key**.

  5. Click **Save**.




###  gcloud 

Use the [`gcloud eventarc pipelines update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/pipelines/update) command to disable CMEK for your pipeline:
    
    
    gcloud eventarc pipelines update PIPELINE_NAME \
        --location=REGION \
        --clear-crypto-key

###  Terraform 

You can update the pipeline in place by clearing the `crypto_key_name` value and not specifying it in the Terraform configuration file. For example:
    
    
      # Disable CMEK for an Eventarc Advanced pipeline
      resource "google_eventarc_pipeline" "default" {
        location    = "us-central1"
        pipeline_id = "example-pipeline"
        destinations {
          http_endpoint {
            uri = google_cloud_run_v2_service.default.uri
          }
          authentication_config {
            google_oidc {
              service_account = google_service_account.default.email
            }
          }
        }
      }
    

## Enable CMEK for Google API sources

When you enable CMEK for a `GoogleApiSource` resource, all messages that are collected for that resource are fully encrypted with the CMEK key.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

  2. You can [create a bus](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus) or, if you are updating a bus, click the name of the bus.

  3. In the **Bus details** page, click edit **Edit**.

  4. To add a message source, click add **Add source**.

If a message source already exists, you must first delete it and then add a new message source.

  5. In the **Add message source** pane, for the Google API message provider, accept the default of `google-api-source`.

  6. For **Encryption** , select **Cloud KMS key** and do the following:

     1. In the **Key type** list, select a method to manage your keys.

You can manage your keys manually or you can use [Autokey](https://docs.cloud.google.com/kms/docs/autokey-overview) which lets you generate key rings and keys on-demand. If the Autokey option is disabled, it isn't yet integrated with the current resource type.

     2. In the **Select a Cloud KMS key** , select a key.

You must select a region before you can view your customer-managed keys.

     3. Optional: To manually enter the resource name of the key, in the **Select a Cloud KMS key** list, click **Enter key manually** , and enter the key name in the specified format.

     4. If prompted, grant the [`cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) to the [Eventarc Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#eventarc-service-agent).

  7. Click **Create**.

This enables the automatic collection of events coming directly from Google sources, and all event messages are fully encrypted with the CMEK key.

Only events from resources in the same Google Cloud project as the `GoogleApiSource` are published. For more information, see [Publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources).

  8. Click **Save**.




###  gcloud 

Use the [`gcloud eventarc google-api-sources update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/update) command to enable CMEK for your `GoogleApiSource` resource:
    
    
    gcloud eventarc google-api-sources update GOOGLE_API_SOURCE_NAME \
        --location=REGION \
        --crypto-key=KEY

Replace the following:

  * `GOOGLE_API_SOURCE_NAME`: the ID or fully qualified identifier of your `GoogleApiSource` resource
  * `REGION`: a [supported Eventarc Advanced location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions)
  * `KEY`: the fully qualified Cloud KMS key name in the format `projects/PROJECT_NAME/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME`

The `REGION` of the key must match the [location](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions) of the resource to be protected.




###  Terraform 

Enable CMEK for your Google API sources by configuring the [`google_eventarc_google_api_source`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_google_api_source) resource. For example:
    
    
    # Enable CMEK for Google API sources
    resource "google_eventarc_google_api_source" "default" {
      location             = "us-central1"
      google_api_source_id = "example-google-api-source"
      destination          = google_eventarc_message_bus.default.id
      crypto_key_name      = google_kms_crypto_key.default.id
      depends_on           = [google_kms_crypto_key_iam_member.default]
    }

### Verify Cloud KMS usage

Verify that the resource is now CMEK-compliant.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

  2. Click the name of the bus whose message source you have protected using a Cloud KMS key.

  3. In the **Bus details** page, click edit **Edit**.

The key that is encrypting your message source should be listed. You can click the key to go to it in the Security Command Center.

Otherwise, the **Encryption** status message is `Event messages encrypted using Google-managed encryption keys`.




###  gcloud 

Use the [`gcloud eventarc google-api-sources describe`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/describe) command to verify CMEK for your `GoogleApiSource` resource:
    
    
      gcloud eventarc google-api-sources describe GOOGLE_API_SOURCE_NAME \
          --location=REGION

The output should be similar to the following:
    
    
      createTime: '2022-06-28T18:05:52.403999904Z'
      cryptoKeyName: projects/PROJECT_ID/locations/REGION/keyRings/RING_NAME/cryptoKeys/KEY_NAME
      destination: projects/PROJECT_ID/locations/REGION/messageBuses/BUS_NAME
      name: projects/PROJECT_ID/locations/REGION/googleApiSources/GOOGLE_API_SOURCE_NAME
      uid: 5ea277f9-b4b7-4e7f-a8e0-6ca9d7204fa3
      updateTime: '2022-06-28T18:09:18.650727516Z'

The `cryptoKeyName` value shows the Cloud KMS key used for the resource.

###  Terraform 

To confirm the CMEK key, you can use the Terraform `state show` command.
    
    
    terraform state show google_eventarc_google_api_source.default

The output should be similar to the following:
    
    
    resource "google_eventarc_google_api_source" "default" {
        create_time           = "2026-03-02T21:24:32.019246933Z"
        crypto_key_name       = "projects/PROJECT_ID/locations/us-central1/keyRings/adffca5e8fbc2cca-example-keyring/cryptoKeys/example-key"
        destination           = "projects/PROJECT_ID/locations/us-central1/messageBuses/example-bus"
        effective_annotations = {}
        effective_labels      = {
            "goog-terraform-provisioned" = "true"
        }
        google_api_source_id  = "example-google-api-source"
        id                    = "projects/PROJECT_ID/locations/us-central1/googleApiSources/example-google-api-source"
        location              = "us-central1"
        name                  = "projects/PROJECT_ID/locations/us-central1/googleApiSources/example-google-api-source"
        project               = "PROJECT_ID"
        terraform_labels      = {
            "goog-terraform-provisioned" = "true"
        }
        uid                   = "5c79b6e1-8377-48bd-b5d1-61f04ec07e29"
        update_time           = "2026-03-02T21:24:38.051947964Z"
    
        logging_config {
            log_severity = "NONE"
        }
    }

### Disable CMEK for Google API sources

You can disable the CMEK protection associated with Google API sources. The events that are collected through the `GoogleApiSource` resource are still protected by [Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

**Caution:** Disabling CMEK can result in the loss of events stored in Eventarc Advanced at the time of the change. It is the customer's responsibility to ensure that it is safe to disable CMEK. Google is not responsible for outages, loss of data, or compliance issues which result from disabling CMEK for Google API sources.

###  Console 

  1. In the Google Cloud console, go to the **Eventarc** > **Bus** page.

[Go to Bus](https://console.cloud.google.com/eventarc/buses)

  2. Click the name of the bus whose message source you have protected using CMEK.

  3. In the **Bus details** page, click edit **Edit**.

  4. To delete the message source that is encrypted by a Cloud KMS key, click delete **Delete resource**.

  5. If necessary, re-add the message source.




###  gcloud 

Use the [`gcloud eventarc google-api-sources update`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/update) command to disable CMEK for your `GoogleApiSource` resource:
    
    
    gcloud eventarc google-api-sources update GOOGLE_API_SOURCE_NAME \
        --location=REGION \
        --clear-crypto-key

###  Terraform 

You can update the `GoogleApiSource` resource in place by clearing the `crypto_key_name` value and not specifying it in the Terraform configuration file. For example:
    
    
      # Disable CMEK for Google API sources
      resource "google_eventarc_google_api_source" "default" {
        location             = "us-central1"
        google_api_source_id = "example-google-api-source"
        destination          = google_eventarc_message_bus.default.id
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




To verify that the policy is successfully applied, you can try to create an Eventarc Advanced pipeline in the project. The process fails unless you specify a Cloud KMS key.

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




To verify that the policy is successfully applied, you can try to create an Eventarc Advanced pipeline using a Cloud KMS key from a different project. The process will fail.

## Disabling and enabling Cloud KMS keys

A key version stores the cryptographic key material that you use to encrypt, decrypt, sign, and verify data. You can disable this key version so that data that was encrypted with the key can't be accessed.

When Eventarc cannot access Cloud KMS keys, event routing fails with `FAILED_PRECONDITION` errors and event delivery stops. You can enable a key in the _Disabled_ state so that the encrypted data can be accessed again.

### Disable Cloud KMS keys

To prevent Eventarc from using the key to encrypt or decrypt your event data, do any of the following:

  * We recommend [disabling the key version](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) you have configured for the bus or pipeline. This affects only the Eventarc Advanced bus or pipeline that is associated with the specific key.
  * Optional: [Revoke the `cloudkms.cryptoKeyEncrypterDecrypter` role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) from the Eventarc service account. This affects all the project's Eventarc resources that support events encrypted using CMEK.



Although neither operation guarantees instantaneous access revocation, Identity and Access Management (IAM) changes generally propagate faster. For more information, see [Cloud KMS resource consistency](https://docs.cloud.google.com/kms/docs/consistency) and [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

### Re-enable Cloud KMS keys

To resume event delivery and routing, [restore access](https://docs.cloud.google.com/kms/docs/enable-disable#enable_a_disabled_key_version) to Cloud KMS.

## Audit logging and troubleshooting

Cloud KMS produces audit logs when keys are enabled, disabled, or used by Eventarc Advanced resources to encrypt and decrypt messages. For more information, see the [Cloud KMS audit logging information](https://docs.cloud.google.com/kms/docs/audit-logging).

To resolve issues that you might encounter when using Cloud KMS with Eventarc, see [Troubleshoot issues](https://docs.cloud.google.com/eventarc/advanced/docs/troubleshoot).

To resolve issues that you might encounter when using externally managed keys through Cloud External Key Manager (Cloud EKM), see [Cloud EKM error reference](https://docs.cloud.google.com/kms/docs/reference/ekm_errors).

## Pricing

The bus integration does not incur additional costs beyond the key operations, which are billed to your Google Cloud project. The use of CMEK for a pipeline incurs charges for access to the Cloud KMS service based on [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing).

For more information on the most current pricing information, see [Cloud KMS Pricing](https://cloud.google.com/kms/pricing).

## What's next

  * [Recommended practices for using CMEKs](https://docs.cloud.google.com/kms/docs/cmek-recommended-practices)
  * [Use CMEK with Eventarc Standard](https://docs.cloud.google.com/eventarc/docs/use-cmek)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
