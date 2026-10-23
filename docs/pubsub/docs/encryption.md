---
url: https://docs.cloud.google.com/pubsub/docs/encryption/
title: Configure message encryption \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:14.369930+00:00
---

# Configure message encryption  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Configure message encryption Stay organized with collections  Save and categorize content based on your preferences. 

By default, Pub/Sub encrypts customer content at rest. Pub/Sub handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Pub/Sub. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you [track key usage](https://docs.cloud.google.com/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Pub/Sub resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## CMEK with Cloud KMS Autokey

You can either create CMEKs manually to protect your Pub/Sub resources or use Cloud KMS Autokey. With Autokey, key rings and keys are generated on demand to support resource creation in Pub/Sub. Service agents that use the keys for encrypt and decrypt operations are created if they don't already exist and are granted the required Identity and Access Management (IAM) roles. For more information, see [Autokey overview](https://docs.cloud.google.com/kms/docs/autokey-overview).

## How CMEK works with Pub/Sub

When you configure Pub/Sub with CMEK, the service automatically encrypts all data using the specified key. Cloud KMS usage for CMEK might incur additional costs depending on your usage patterns.

Every message is encrypted at the following states and layers:

  * [At rest](https://cloud.google.com/security/encryption/default-encryption/)

    * Hardware layer
    * Infrastructure layer
    * Application layer
  * [In transit](https://cloud.google.com/security/encryption-in-transit/)




At the application layer, Pub/Sub individually encrypts incoming messages as soon as the message is received. This implementation adds the following features:

  * Keeps messages encrypted on data-center internal links
  * Enables customer-managed encryption keys (CMEK)

**Note:** Pub/Sub does not encrypt [message attributes](https://docs.cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#google.pubsub.v1.PubsubMessage) at the application layer. Message attributes are still encrypted at the hardware and infrastructure layers.

**Envelope encryption pattern**

Pub/Sub uses the [envelope encryption pattern](https://docs.cloud.google.com/kms/docs/envelope-encryption) with CMEK. In this approach, the messages are not encrypted by Cloud KMS. Instead, Cloud KMS is used to encrypt Data Encryption Keys (DEKs) created by Pub/Sub for each topic. These DEKs are stored only in encrypted, or wrapped, form by Pub/Sub. Before storing a DEK, the service sends the DEK to Cloud KMS to be encrypted with the key encryption key (KEK) specified on the topic. A new DEK is generated for each topic approximately every six hours.

Before Pub/Sub publishes messages to a subscription, it encrypts them using the newest DEK that was generated for the topic. Pub/Sub decrypts the messages shortly before they are delivered to subscribers.

**Cloud KMS key region**

Because Pub/Sub resources are global, we recommend that you use global Cloud KMS keys to configure CMEK-enabled topics. Using a regional Cloud KMS key can introduce unnecessary dependencies on cross-region network links, depending on the locations of a topic's publishers and subscribers.

Use regional Cloud KMS keys only in the following situations:

  * A [message storage policy](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) restricts message storage to that region with `enforceInTransit` enabled.
  * All publisher and subscriber clients use the same [regional endpoint](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#regional-endpoints).



In these situations, all traffic for the topic is routed to the same region. 

## Configure CMEK with Pub/Sub

You can configure CMEK manually or by using Autokey.

### Before you begin

You can configure CMEK for Pub/Sub using the Google Cloud console or the Google Cloud CLI.

Complete the following tasks:

  * Enable the Cloud KMS API.

  * Create a key ring and a key in Cloud KMS. Keys and key rings cannot be deleted.




For instructions on how to accomplish these tasks, [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [Create a key](https://docs.cloud.google.com/kms/docs/create-key).

### Required roles and permissions

Pub/Sub uses a Google Cloud [service agent](https://docs.cloud.google.com/iam/docs/service-agents) to access Cloud KMS. The service agent is maintained internally by Pub/Sub for each project, and is not visible on the **Service Accounts** page in the Google Cloud console by default.

The Pub/Sub service agent has the form `service-${PROJECT_NUMBER}@gcp-sa-pubsub.iam.gserviceaccount.com`.

Pub/Sub requires specific permissions to encrypt and decrypt data using CMEK.

Complete the following steps to set up the required access:

  * Grant the Pub/Sub service agent the Cloud KMS Crypto Key Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role.
        
        gcloud kms keys add-iam-policy-binding CLOUD_KMS_KEY_NAME \
            --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com \
            --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
        

Replace the following:

    * CLOUD_KMS_KEY_NAME: The name of the Cloud KMS key.

The key is of the format `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/CRYPTO_KEY`.

An example is `projects/test-project/locations/us-central1/keyRings/test-keyring/cryptoKeys/test-key`.

    * PROJECT_NUMBER: The project number of the Pub/Sub project.




For more information about granting Identity and Access Management roles, see [Granting roles on a resource](https://docs.cloud.google.com/kms/docs/iam#granting_roles_on_a_resource).

### Configure a topic manually with CMEK

You can manually configure CMEK for a topic using the Google Cloud console or gcloud CLI.

### Console

To create a topic with CMEK, follow these steps:

  1. In the Google Cloud console, go to the Pub/Sub **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Click **Create topic**.

  3. In the **Topic ID** field, enter an ID for your topic.

For more information about naming topics, see the [naming guidelines](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  4. For **Encryption** , click **Cloud KMS key**.

  5. Select the key type. If you don't see the **Select a customer-managed key** dropdown, ensure that you have enabled the Cloud KMS API for the project.

  6. Click **Create topic**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To create a topic with CMEK, run the [`gcloud pubsub topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/create) command:
         
         gcloud pubsub topics create TOPIC_ID --topic-encryption-key=ENCRYPTION_KEY
             

Replace the following:

     * TOPIC_ID: The ID or name of the topic.

For more information about how to name a topic, see [ Guidelines to name a topic, subscription, schema, or snapshot](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

     * ENCRYPTION_KEY: ID of the CMEK to use for the topic.

The format is `projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/CRYPTO_KEY`.




### Update a CMEK topic manually

You have the flexibility to add, change, or remove the CMEK linked to a Pub/Sub topic. You can use gcloud CLI to update the CMEK. However, this change doesn't apply retroactively.

Messages published to the topic before the key changes remain encrypted with the original key, regardless of whether it was a CMEK or Google-owned and Google-managed encryption key. Changing a topic's CMEK does not re-encrypt previously published messages—these messages remain protected with the key that they were originally encrypted with, so message data within a topic might still depend on the previous key for up to 31 days, depending on the message retention duration specified on the topic or any of its subscriptions.

Pub/Sub has a caching mechanism for keys that lasts approximately 30 minutes. It might take up to this duration for Pub/Sub to recognize and start using a new key that was manually changed in the topic configuration.

### Cloud KMS key rotation in Pub/Sub

Key configuration changes such as key rotation within Cloud KMS don't directly trigger the creation of data encryption keys in Pub/Sub. It might take up to 12 hours for Pub/Sub to start using new key versions for encrypting message data.

As with manual configuration changes made to encryption settings in Pub/Sub, these changes don't apply retroactively to messages that were published in the past. Existing messages continue to be protected with previous versions of the cryptographic key. These messages remain protected with the key that they were originally encrypted with, so message data within a topic might still depend on the previous key version for up to 31 days, depending on the message retention duration specified on the topic or any of its subscriptions.

### Configure a topic with Cloud KMS Autokey

For more information on using Cloud KMS Autokey with Pub/Sub, see [Cloud KMS with Autokey](https://docs.cloud.google.com/kms/docs/kms-autokey).

## Audit logs

Cloud KMS produces [audit logs](https://docs.cloud.google.com/pubsub/docs/audit-logging) when keys are enabled, disabled, or used by Pub/Sub to encrypt and decrypt messages. This is useful in debugging issues with publish or delivery availability.

Cloud KMS keys are attached to audit logs for Pub/Sub topic resources. Pub/Sub does not include any other Cloud KMS-related information.

## Pricing and cost

For the following Pub/Sub requests, the use of CMEK incurs charges for access to the Cloud KMS service based on Pub/Sub [pricing](https://cloud.google.com/pubsub/pricing):

  * For each topic using CMEK, a new DEK is encrypted and stored every six hours.

  * The key is used to decrypt DEKs every six minutes. The decryption happens three times, once for every zone in the region where the Pub/Sub service runs.




For example, consider a topic with:

  * At least one subscription

  * Publisher and subscriber clients in the same region




The number of Cloud KMS cryptographic operations can be estimated as: 
    
    
    1 key access for ENCRYPT * (30 days / month * 24 hours / day) / 6 hours
     + 3 key accesses for DECRYPT
       * (30 days / month * 24 hours / day * 60 minutes / hour ) / 6 minutes
       = 21,720 Cloud KMS key access events
    

Given a pricing structure in which cryptographic operations cost $0.03 per 10,000 operations, the above usage would cost approximately $0.07. Refer to [Cloud KMS pricing](https://cloud.google.com/kms/pricing) for the most current pricing information. 

In practice, keys might be fetched more or less frequently depending on access patterns. Use these numbers as estimates only.

## Monitoring and troubleshooting

Issues with key access can have these effects:

  * Delays in message delivery

  * Publish errors




Monitor publish and pull request errors using the following [metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-pubsub), grouped by `response_class` and `response_code`:

  * `topic/send_request_count`
  * `subscription/pull_request_count`
  * `subscription/streaming_pull_response_count`



[StreamingPull response](https://docs.cloud.google.com/pubsub/docs/pull#streamingpull) has a 100% error rate. This is an indication that the stream has ended, not that requests are failing. To monitor StreamingPull, look for the `FAILED_PRECONDITION` response code.

Publishing and message delivery can fail with `FAILED_PRECONDITION` errors for multiple reasons.

  * The Cloud KMS key could be disabled. For details, see Disabling and re-enabling keys on this page.

  * If you are using externally managed keys through Cloud EKM, see the [Cloud EKM error reference](https://docs.cloud.google.com/kms/docs/reference/ekm_errors).




For push subscriptions, there is no way to directly detect CMEK-specific delivery issues. Instead:

  * Monitor the size and age of the backlog of a push subscription using `subscription/num_unacked_messages`.

  * Monitor `subscription/oldest_unacked_message_age` for unusual spikes.

  * Use publish errors and CMEK audit logs to spot issues.




## Disabling and re-enabling keys

There are two ways to prevent Pub/Sub from decrypting your message data:

  * **Recommended:** [Disable the Cloud KMS key](https://docs.cloud.google.com/kms/docs/enable-disable#disable_an_enabled_key_version) you've associated with the topic using Pub/Sub. This approach affects only the Pub/Sub topics and subscriptions that are associated with that specific key.

  * [Revoke the **Pub/Sub CryptoKey Encrypter/Decrypter** role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke_access) from the Pub/Sub service account (`service-$PROJECT_NUMBER@gcp-sa-pubsub.iam.gserviceaccount.com`) using IAM. This approach affects all of the project's Pub/Sub topics and the subscriptions that contain messages encrypted using CMEK.




Although neither operation confirms instantaneous access revocation, IAM changes generally propagate faster. To learn more, see [Cloud KMS resource consistency](https://docs.cloud.google.com/kms/docs/consistency) and [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

When Pub/Sub cannot access a Cloud KMS key, message publishing and delivery with StreamingPull or pull fails with `FAILED_PRECONDITION` errors. Message delivery to push endpoints will stop. To resume delivery and publishing, [restore access](https://docs.cloud.google.com/kms/docs/enable-disable#enable_a_disabled_key_version) to the Cloud KMS key.

Once the Cloud KMS key is accessible to Pub/Sub, publishing is available within 12 hours and message delivery resumes within 2 hours.

Although intermittent outages of less than a minute for Cloud KMS are unlikely to significantly interrupt publishing and delivery, extended Cloud KMS unavailability has the same effect as key revocation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
