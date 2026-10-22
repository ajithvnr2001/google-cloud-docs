---
url: https://docs.cloud.google.com/kms/docs/monitor-state-changes/
title: Monitor state changes using Pub/Sub \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:51.444035+00:00
---

# Monitor state changes using Pub/Sub  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/monitor-state-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Monitor state changes using Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use [Pub/Sub](https://docs.cloud.google.com/pubsub) to create notifications on state changes for Cloud KMS resources.

## Before you begin

To enable APIs, grant required permissions, and create a Pub/Sub topic, follow the instructions in [Before you begin](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes#before_you_begin) in "Monitoring asset changes".

## Configure a feed

Configure a feed that monitors the type of changes and resources that you are interested in.

### Notify on all resource changes

To create a feed, use the [`gcloud asset feeds create`](https://docs.cloud.google.com/sdk/gcloud/reference/asset/feeds/create) command.
    
    
    gcloud asset feeds create FEED_NAME \
      --project=PROJECT_ID  \
      --asset-types="RESOURCE_TYPE" \
      --pubsub-topic="PUBSUB_TOPIC"
    

Replace the following:

  * `FEED_NAME`: The name to use for your Pub/Sub feed.
  * `PROJECT_ID`: The ID of the Cloud KMS project you want to monitor.
  * `RESOURCE_TYPE`: The types of resource for which you want to receive notifications. Use commas between resource types—for example, `cloudkms.googleapis.com/CryptoKey,cloudkms.googleapis.com/CryptoKeyVersion`. You can notify on any [supported resource type](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types#supported_resource_types), including the following:

    * `cloudkms.googleapis.com/CryptoKey`
    * `cloudkms.googleapis.com/CryptoKeyVersion`
    * `cloudkms.googleapis.com/EkmConnection`
    * `cloudkms.googleapis.com/ImportJob`
    * `cloudkms.googleapis.com/KeyRing`
  * `PUBSUB_TOPIC`: The name of the Pub/Sub topic you created in Before you begin




This creates a notification when resources of the indicated type are created or updated. The notification indicates that the resource has been updated, but does not include detailed information about the update. For example, an update notification for a `CryptoKeyVersion` might mean the version was made primary or that the version was scheduled for destruction. When you receive a notification that a resource has been updated, you should check the resource to find its current state.

**Note:** Cloud KMS does not support resource deletion. Key rings, keys, and key versions can't be deleted. The only way to fully delete Cloud KMS resources is to delete the project that contains them. Scheduling a `CryptoKeyVersion` for destruction and destruction of `CryptoKeyVersion` resources are update operations.

### Notify on specific resource changes

To create a feed with a condition, use the [`gcloud asset feeds create`](https://docs.cloud.google.com/sdk/gcloud/reference/asset/feeds/create) command with the `--condition-expression` flag.
    
    
    gcloud asset feeds create FEED_NAME \
      --project=PROJECT_ID  \
      --asset-types="RESOURCE_TYPE" \
      --pubsub-topic="PUBSUB_TOPIC" \
      --condition-expression="CONDITION_EXPRESSION"
    

Replace the following:

  * `FEED_NAME`: The name to use for your Pub/Sub feed.
  * `PROJECT_ID`: The ID of your Cloud KMS project.
  * `RESOURCE_TYPE`: The type of resource for which you want to receive notifications—for example, `cloudkms.googleapis.com/CryptoKeyVersion`. You can notify on any [supported resource type](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types#supported_resource_types), including the following:

    * `cloudkms.googleapis.com/CryptoKey`
    * `cloudkms.googleapis.com/CryptoKeyVersion`
    * `cloudkms.googleapis.com/EkmConnection`
    * `cloudkms.googleapis.com/ImportJob`
    * `cloudkms.googleapis.com/KeyRing`
  * `PUBSUB_TOPIC`: The name of the Pub/Sub topic you created in Before you begin

  * `CONDITION_EXPRESSION`: A condition expression in [Common Expression Language (CEL)](https://github.com/google/cel-spec). For example, `"folders/FOLDER_NUMBER" in temporal_asset.asset.ancestors` causes the feed to only create notifications when the indicated resource is located within folder `FOLDER_NUMBER`.




This creates a notification when resources of the indicated type that match the specified condition expression are created, deleted, or updated.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
