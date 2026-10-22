---
url: https://docs.cloud.google.com/pubsub/docs/pubsub-regulatory-compliance/
title: Regulatory support in Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:37.859599+00:00
---

# Regulatory support in Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/pubsub-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Resources ](https://docs.cloud.google.com/pubsub/docs/resources)



Send feedback 

#  Regulatory support in Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations, and APIs in Pub/Sub that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary For FedRAMP High  
  
---  
  
## Data Boundary For FedRAMP High

### Supported services

The following table lists the Pub/Sub APIs and versions that meet the requirements of Data Boundary For FedRAMP High. | Service | Version | Status  
---|---|---  
pubsub.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Pub/Sub is available for Data Boundary For FedRAMP High in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### Management tools

The following table describes how management tools support Data Boundary For FedRAMP High with Pub/Sub.

Tool | Description  
---|---  
Google Cloud SDK | You must use Google Cloud SDK version 403.0.0 or later to help ensure data regionalization for FedRAMP High technical data. To verify your current Google Cloud SDK version, run `gcloud --version`, and then run `gcloud components update` to update to the latest version.  
Administrator controls | By default, non-compliant APIs are disabled. However, administrators with sufficient permissions can enable a non-compliant API. When non-compliance APIs are enabled, you are notified in the Assured Workloads Monitoring page.  
  
### Affected features

The following table describes which features are affected by Data Boundary For FedRAMP High:

Feature | Description  
---|---  
Single Message Transforms (SMTs) | This feature is not supported for FedRAMP High compliance and should not be used. It is disabled by default under Assured Workloads folders.  
  
### Applicable settings

The following table describes the organization policy constraints and product settings that apply to Data Boundary For FedRAMP High. By default, these are set by Assured Workloads. If you change these settings, you must first consider how that change impacts your compliance status. For instructions on configuring organization policies, see [Creating and managing organization policies](https://cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

Setting | Required value  
---|---  
[pubsub.managed.disableTopicMessageTransforms](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `True`

  
[pubsub.managed.disableSubscriptionMessageTransforms](https://cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) | 

  * `True`

  
  
### API fields for sensitive data

#### Resource: No resource

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary For FedRAMP High.

API Method | Protected fields  
---|---  
Service: `pubsub.googleapis.com` REST API: `POST` `/v1/{project=projects/*}:testMessageTransforms` RPC methods:

  * `google.pubsub.v1.Transform.TestMessageTransforms`

| 

  * `message.data`

  
  
#### Resource: pubsub.googleapis.com/Topic

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary For FedRAMP High.

API Method | Protected fields  
---|---  
Service: `pubsub.googleapis.com` REST API: `POST` `/v1/{topic=projects/*/topics/*}:publish` RPC methods:

  * `google.pubsub.v1.Publisher.Publish`

| 

  * `messages.data`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Data ingestion source | 

  * `ingestionDataSourceSettings.awsKinesis.streamArn`
  * `ingestionDataSourceSettings.awsMsk.clusterArn`
  * `ingestionDataSourceSettings.awsMsk.gcpServiceAccount`
  * `ingestionDataSourceSettings.azureEventHubs.eventHub`
  * `ingestionDataSourceSettings.cloudStorage.bucket`
  * `ingestionDataSourceSettings.confluentCloud.bootstrapServer`

  
Message metadata | 

  * `ackIds`
  * `messages.attributes.key`
  * `messages.attributes.value`
  * `messages.messageId`
  * `messages.orderingKey`
  * `subscription`

  
Message transformation | 

  * `messageTransforms.aiInference.endpoint`
  * `messageTransforms.aiInference.unstructuredInference.parameters.fields.key`
  * `messageTransforms.aiInference.unstructuredInference.parameters.fields.value.stringValue`
  * `messageTransforms.schemaEncoding.firstRevisionId`
  * `messageTransforms.schemaEncoding.lastRevisionId`
  * `messageTransforms.schemaEncoding.schema`

  
Pagination and filtering | 

  * `filter`
  * `pageToken`

  
Push configuration | 

  * `cloudStorageConfig.filenamePrefix`
  * `pubsubliteExportConfig.topic`
  * `pushConfig.attributes.key`
  * `pushConfig.attributes.value`
  * `pushConfig.oidcToken.audience`
  * `pushConfig.pushEndpoint`

  
Resource identification | 

  * `name`
  * `parent`
  * `project`
  * `schemaId`
  * `subscription`
  * `topic`

  
Schema definition | 

  * `schema.definition`
  * `schema.name`
  * `schema.tags.key`
  * `schema.tags.value`
  * `tags.key`
  * `tags.value`

  
Schema settings | 

  * `schemaSettings.firstRevisionId`
  * `schemaSettings.lastRevisionId`
  * `schemaSettings.schema`

  
Subscription configuration | 

  * `bigqueryConfig.table`
  * `cloudStorageConfig.bucket`
  * `cloudStorageConfig.filenameDatetimeFormat`
  * `cloudStorageConfig.filenameSuffix`
  * `deadLetterPolicy.deadLetterTopic`
  * `pubsubExportConfig.topic`

  
Topic configuration | 

  * `kmsKeyName`
  * `labels.key`
  * `labels.value`
  * `revisionId`
  * `snapshot`
  * `updateMask.paths`

  
  
### References

  * [Assured Workloads Monitoring](https://cloud.google.com/assured-workloads/docs/monitor-folder)
  * [Pub/Sub APIs overview](https://cloud.google.com/pubsub/docs/reference/service_apis_overview)

  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
