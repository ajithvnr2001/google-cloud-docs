---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek/
title: Customer-managed encryption keys (CMEK) \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:03.733873+00:00
---

# Customer-managed encryption keys (CMEK)  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By default, Gemini Data Analytics encrypts customer content at rest. Gemini Data Analytics handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Gemini Data Analytics. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Gemini Data Analytics resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

This page describes how to use customer-managed encryption keys (CMEK) to protect data that is used by the Conversational Analytics API. The Conversational Analytics API is a product within the Gemini Data Analytics service (`geminidataanalytics.googleapis.com`). 

## CMEK for Conversational Analytics API resources

When you configure CMEK for a Conversational Analytics API resource, the specified Cloud KMS key encrypts the sensitive data at rest. You can configure CMEK for `DataAgent` and `Conversation` resources independently.

**Important:** You can configure CMEK only when creating resources. To use CMEK, you must specify the `kms_key` field when you create a `DataAgent` or `Conversation` resource. You can't add or change a Cloud KMS key on an existing resource.

CMEK for the Conversational Analytics API is available only in regional and multi-regional locations, not in the `global` location. For the locations that each data source supports, see [Supported data locations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency#supported-data-locations).

## What is protected with CMEK

CMEK for the Conversational Analytics API protects the following data at rest:

  * For `DataAgent` resources, all customer core content within the `data_analytics_agent` field is protected. This content includes the `staging_context`, `published_context`, and `last_published_context` fields, as well as the `system_instruction` and `example_queries` fields.
  * For `Conversation` resources, all message and state history data is protected.



The following data isn't encrypted with the customer's CMEK key. Instead, this data is protected by Google default encryption:

  * For `DataAgent` resources, Google default encryption protects metadata fields such as `name`, `display_name`, `description`, `labels`, `create_time`, `update_time`, `delete_time`, `purge_time`, and `kms_key`.
  * For `Conversation` resources, Google default encryption protects metadata fields such as `name`, `agents`, `labels`, `create_time`, `last_used_time`, and `kms_key`.



## Limitations

CMEK for the Conversational Analytics API has the following limitations:

  * CMEK must be configured when the resource is created. It can't be added to or changed on an existing resource.
  * CMEK organization policies aren't supported.
  * The Cloud KMS key and the Conversational Analytics API resource must be in the same location.
  * The `global` region isn't supported.
  * You can use only one CMEK per project per region for all `Conversation` resources within that project and region.



## Before you begin

Before you can use CMEK with Conversational Analytics API, complete the following steps:

  1. Enable the required APIs within the Google Cloud console or the Google Cloud CLI.

###  Console 

Enable the following APIs in the Google Cloud console for your Google Cloud project.

[ Enable the Gemini Data Analytics API](https://console.cloud.google.com/apis/enableflow?apiid=geminidataanalytics.googleapis.com)

[Enable the Gemini for Google Cloud API](https://console.cloud.google.com/apis/enableflow?apiid=cloudaicompanion.googleapis.com)

[ Enable the Cloud Key Management Service API](https://console.cloud.google.com/apis/enableflow?apiid=cloudkms.googleapis.com)

**Tip:** When you enable an API, you might need to refresh the Google Cloud console page to confirm that it's enabled.

###  gcloud 

With the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk), run the following [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) commands to enable the Gemini Data Analytics API, the Gemini for Google Cloud API, and the Cloud Key Management Service API, respectively:
         
         gcloud services enable geminidataanalytics.googleapis.com --project=project_id
         gcloud services enable cloudaicompanion.googleapis.com --project=project_id
         gcloud services enable cloudkms.googleapis.com --project=project_id
         

In the previous sample gcloud CLI commands, replace `project_id` with your Google Cloud project ID.

  2. Create a Cloud KMS key ring and key in the same location as your Conversational Analytics API resources. For more information, see [Create a key](https://docs.cloud.google.com/kms/docs/create-key).

  3. Create the Google-managed [service agents](https://docs.cloud.google.com/iam/docs/service-agents), also known as _per-product per-project service accounts (P4SAs)_ , if they don't already exist. These service agents are required to allow the services that are involved in protecting your Conversational Analytics API resources with CMEK to access your Cloud KMS key.

Run the following `gcloud` commands to create the service agents: 
         
         gcloud beta services identity create --service=geminidataanalytics.googleapis.com --project PROJECT_ID
         gcloud beta services identity create --service=cloudaicompanion.googleapis.com --project PROJECT_ID
         

Replace `PROJECT_ID` with your Google Cloud project ID.
  4. Grant the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role in Identity and Access Management (IAM) to both service agents that you created in the previous step to enable the Gemini Data Analytics service to use your Cloud KMS key for encrypting and decrypting your Conversational Analytics API data.

Grant the permission to the Gemini Data Analytics service agent:
         
         gcloud kms keys add-iam-policy-binding KEY_NAME \
           --location KEY_LOCATION \
           --keyring KEY_RING_NAME \
           --member
         serviceAccount:service-PROJECT_NUMBER@gcp-sa-geminidataanalytics.iam.gserviceaccount.com \
           --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
           --project KMS_PROJECT_ID
         

Grant the permission to the Gemini for Google Cloud API service agent:
         
         gcloud kms keys add-iam-policy-binding KEY_NAME \
           --location KEY_LOCATION \
           --keyring KEY_RING_NAME \
           --member
         serviceAccount:service-PROJECT_NUMBER@gcp-sa-cloudaicompanion.iam.gserviceaccount.com \
           --role roles/cloudkms.cryptoKeyEncrypterDecrypter \
           --project KMS_PROJECT_ID
         

In the previous code examples, replace the sample values as follows:

     * `KEY_NAME`: The name of your Cloud KMS key.
     * `KEY_LOCATION`: The region of your key ring (for example, `us-east4`).
     * `KEY_RING_NAME`: The name of your key ring.
     * `PROJECT_NUMBER`: Your Google Cloud project number where you are creating API resources.
     * `KMS_PROJECT_ID`: The project ID where the key was created. This can be the same as the project where you are creating API resources.



## Protect resources with CMEK

This section shows how to protect a new `DataAgent` or `Conversation` resource with CMEK by using the REST API to specify a Cloud KMS key in the `kms_key` field during resource creation.

You can enable CMEK only when you create a `DataAgent` or `Conversation` resource.

**Important:** You can't add or change a Cloud KMS key on an existing resource.

A CMEK key must be in the same region as the resource that it protects. For more information, see Limitations.

### Protect a `DataAgent` resource with CMEK

To protect a new `DataAgent` resource with CMEK, specify a Cloud KMS key in the `kms_key` field when you create the data agent.

### Python SDK

The following example shows how to specify a Cloud KMS key when you create a `DataAgent` resource with the Python SDK. For an example of a complete `create` request, see [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#create_a_data_agent).
    
    
    # Define the KMS key.
    billing_project = "BILLING_PROJECT_ID"
    key_ring = "KEY_RING_NAME"
    key_name = "KEY_NAME"
    key_project = "KMS_PROJECT_ID" # Project where the key was created
    location = "LOCATION" # Region of your key ring
    
    if key_project == "":
      key_project = billing_project
    
    kms_key_data_agent = f"projects/{key_project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key_name}"
    
    data_agent = geminidataanalytics.DataAgent()
    data_agent.data_analytics_agent.published_context = published_context
    data_agent.kms_key = kms_key_data_agent
    

In the previous example, replace values as follows:

  * `BILLING_PROJECT_ID`: Your billing project ID.
  * `KEY_RING_NAME`: The name of your Cloud KMS key ring.
  * `KEY_NAME`: The name of your Cloud KMS key.
  * `KMS_PROJECT_ID`: The project ID where the key was created. If left empty, `billing_project` is used.
  * `LOCATION`: The region of your key ring.



### HTTP

The following example shows how to specify a Cloud KMS key in the request body when you create a `DataAgent` resource with HTTP and Python. For an example of a complete `create` request, see [Build a data agent using HTTP and Python](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#create_a_data_agent).
    
    
    data_agent_payload = {
          "name": f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}",
          "description": "This is the description of data_agent_1.",
          # If using CMEK, include the kms_key field.
          "kms_key": f"projects/{key_project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key_name}",
          "data_analytics_agent": {
              "published_context": {
                  "datasource_references": looker_data_source,
                  "system_instruction": system_instruction,
              }
          }
      }
    

In the previous example, replace values as follows:

  * `KMS_PROJECT_ID`: The project ID where the key was created.
  * `LOCATION`: The region of your key ring.
  * `KEY_RING_NAME`: The name of your Cloud KMS key ring.
  * `KEY_NAME`: The name of your Cloud KMS key.



### Protect a `Conversation` resource with CMEK

To protect a new `Conversation` resource with CMEK, specify a Cloud KMS key in the `kms_key` field when you create the conversation.

### Python SDK

The following example shows how to specify a Cloud KMS key when you create a `Conversation` resource with the Python SDK. For an example of a complete `create` request, see [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#create_a_conversation).
    
    
    # Define the KMS key.
    billing_project = "BILLING_PROJECT_ID"
    key_ring = "KEY_RING_NAME"
    key_name = "KEY_NAME"
    key_project = "KMS_PROJECT_ID" # Project where the key was created
    location = "LOCATION" # Region of your key ring
    
    if key_project == "":
      key_project = billing_project
    
    kms_key_conversation = f"projects/{key_project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key_name}"
    
    conversation = geminidataanalytics.Conversation()
    conversation.agents = [f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"]
    conversation.kms_key = kms_key_conversation
    

In the previous example, replace values as follows:

  * `BILLING_PROJECT_ID`: Your billing project ID.
  * `KEY_RING_NAME`: The name of your Cloud KMS key ring.
  * `KEY_NAME`: The name of your Cloud KMS key.
  * `KMS_PROJECT_ID`: The project ID where the key was created. If left empty, `billing_project` is used.
  * `LOCATION`: The region of your key ring.



### HTTP

The following example shows how to specify a Cloud KMS key in the request body when you create a `Conversation` resource with HTTP and Python. For an example of a complete `create` request, see [Build a data agent using HTTP and Python](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#create_a_conversation).
    
    
    conversation_payload = {
        "agents": [
            f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
        ],
        "name": f"projects/{billing_project}/locations/{location}/conversations/{conversation_id}",
        # If using CMEK, include the kms_key field.
        "kms_key": f"projects/{key_project}/locations/{location}/keyRings/{key_ring_name}/cryptoKeys/{key_name}"
    }
    

In the previous example, replace values as follows:

  * `KMS_PROJECT_ID`: The project ID where the key was created.
  * `LOCATION`: The region of your key ring.
  * `KEY_RING_NAME`: The name of your Cloud KMS key ring.
  * `KEY_NAME`: The name of your Cloud KMS key.



## Troubleshooting

This section covers common issues and important considerations when you're using CMEK with the Conversational Analytics API.

### Key state changes

If a Cloud KMS key version that protects a Conversational Analytics API resource becomes unavailable, you lose access to the data that is encrypted by that key. If you attempt to access protected data while the key is unavailable, such as by reading a `DataAgent` resource's context or accessing `Conversation` history, then the request fails. The error that is returned depends on why the key is unavailable:

  * If the key version is [disabled](https://docs.cloud.google.com/kms/docs/enable-disable) or [destroyed](https://docs.cloud.google.com/kms/docs/destroy-restore), the operation typically fails with a `FAILED_PRECONDITION` error.
  * If the `cloudkms.cryptoKeyEncrypterDecrypter` IAM role is revoked from the `gcp-sa-geminidataanalytics` or `gcp-sa-cloudaicompanion` service agent, the operation typically fails with a `PERMISSION_DENIED` or `NOT_FOUND` error.



Even when the key is unavailable, you can still perform operations that don't require decrypting the content, such as deleting the `DataAgent` or `Conversation` resource.

To restore access to encrypted data, re-enable the key and ensure that the service agents have the required IAM permissions, as described in Before you begin.

### Cloud KMS quotas and the Conversational Analytics API

When you use CMEK in the Conversational Analytics API, your projects can consume Cloud KMS cryptographic requests quotas. For example, reading a `DataAgent` resource or accessing `Conversation` history that is protected by CMEK requires Cloud KMS to decrypt the data. 

Encryption and decryption operations using CMEK keys affect Cloud KMS quotas in these ways:

  * For software CMEK keys generated in Cloud KMS, no Cloud KMS quota is consumed.
  * For hardware CMEK keys—sometimes called Cloud HSM keys—encryption and decryption operations count against [Cloud HSM quotas](https://docs.cloud.google.com/kms/quotas#hsm) in the project that contains the key.
  * For external CMEK keys—sometimes called Cloud EKM keys—encryption and decryption operations count against [Cloud EKM quotas](https://docs.cloud.google.com/kms/quotas#ekm) in the project that contains the key.



For more information, see [Cloud KMS quotas](https://docs.cloud.google.com/kms/quotas).

## What's next

  * Learn how to [Enable the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api).
  * Learn about [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).
  * Learn how to [Authenticate and connect to a data source with the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication).
  * Learn more about [Cloud KMS](https://docs.cloud.google.com/kms/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
