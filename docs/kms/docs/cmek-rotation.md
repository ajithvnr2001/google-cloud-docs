---
url: https://docs.cloud.google.com/kms/docs/cmek-rotation/
title: CMEK key rotation \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:28.746594+00:00
---

# CMEK key rotation  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/cmek-rotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  CMEK key rotation Stay organized with collections  Save and categorize content based on your preferences. 

Customer-managed encryption keys (CMEKs) let you protect data in supported Google Cloud services with a cryptographic key that you control in Cloud KMS. You can configure automatic key rotation on a set schedule, or you can rotate your keys manually. This document explains what happens in a CMEK-integrated service when the underlying Cloud KMS key is rotated.

## How key rotation works with CMEK

When you rotate a key in Cloud KMS, Cloud KMS creates a new version of that key. The new key version becomes the primary version and can be used to encrypt the data encryption keys (DEKs) that protect your data. Previous key versions are kept active and are available for decrypting DEKs that were encrypted with them. This process ensures that you can always access your older data.

Different CMEK-integrated services handle key rotation differently, but there are three main patterns:

  * **New key version protects all data** : When the service detects that a new key version has become primary, the service automatically re-encrypts DEKs that were encrypted with the previous key version. DEKs that protect both new data and existing data are encrypted with the current primary key version. Re-encrypting existing DEKs might take some time to complete, but then the previous key version is no longer used.
  * **New key version is used going forward** : When the service detects that a new key version has become primary, subsequent encryption requests use the new key version. DEKs that protect data for this resource use a mix of current and previous key versions.
  * **New key version is not used** : The service continues to encrypt DEKs with the original key version that was configured when the resource was created, regardless of whether new primary key versions exist.



## Service-specific behavior after key rotation

The following table shows service-specific rotation behavior for resources that can be protected with CMEKs. The following table describes the rotation details for each resource type or set of resource types: 

  * **Can inherit key** : Whether the resource can inherit a key from a parent resource.
  * **Can use unique key** : Whether the resource can use its own unique key, not inherited from a parent resource.
  * **Can change key** : Whether you can select a new CMEK to protect the resource while you update the resource.
  * **New data** : Whether new DEKs are encrypted with the primary key version or the original key version that was primary when CMEK was configured for the resource.
  * **Existing data** : Whether existing DEKs are re-encrypted with the primary key version or remain encrypted with the original key version that was primary when CMEK was configured for the resource.



**Filter by:** Rotation pattern AnyNew key version protects all dataNew key version is used going forwardNew key version is not usedKey inheritance pattern AnyResource can inherit keysUse inherited or unique keysResource only inherits keysResource can't inherit keysChange CMEK on update AnyCan change CMEKCan't change CMEKClear all   


Service and Resources | Can inherit key | Can use unique key | Can change key | New data | Existing data  
---|---|---|---|---|---  
Agent Retrieval

  * `vectorsearch.googleapis.com/Collection`
  * `vectorsearch.googleapis.com/Index`

| No  | Yes  | No  |  Uses new primary key version  |  Uses original key version   
Application Integration

  * `integrations.googleapis.com/IntegrationVersion`
  * `integrations.googleapis.com/AuthConfig`
  * `integrations.googleapis.com/Execution`
  * `integrations.googleapis.com/Suspension`
  * `integrations.googleapis.com/TestCase`
  * `integrations.googleapis.com/Template`

| No  | Yes  | Yes  |  Uses new primary key version  |  Uses original key version   
BigQuery

  * `bigquery.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Table`

| Yes  | Yes  | Yes  |  Uses new primary key version  |  Uses original key version   
Cloud Storage

  * `storage.googleapis.com/Bucket`

| No  | Yes  | Yes  |  Uses new primary key version  |  Uses original key version   
Cloud Storage

  * `storage.googleapis.com/Object`

| Yes  | Yes  | No  | _N/A: this resource is immutable._ |  Uses original key version   
Conversational Analytics API

  * `geminidataanalytics.googleapis.com/Conversation`
  * `geminidataanalytics.googleapis.com/DataAgent`

| No  | Yes  | No  |  Uses new primary key version  |  Uses original key version   
Customer Experience Insights

  * `contactcenterinsights.googleapis.com/*`

**Note:** Customer Experience Insights uses one key per project per region; this key is inherited by all resources in that region.  | Yes  | No  | No  | _Unknown_ | _Unknown_  
Dataflow

  * `dataflow.googleapis.com/Job`

| No  | Yes  | No  |  Uses new primary key version  |  Uses new primary key version   
Eventarc Advanced

  * `eventarc.googleapis.com/MessageBus`
  * `eventarc.googleapis.com/Pipeline`
  * `eventarc.googleapis.com/GoogleApiSource`

| No  | Yes  | Yes  |  Uses original key version  |  Uses original key version   
Eventarc Standard

  * `eventarc.googleapis.com/Channel`

| No  | Yes  | Yes  |  Uses original key version  |  Uses original key version   
Eventarc Standard

  * `eventarc.googleapis.com/Trigger`

| Yes  | No  | Yes  |  Uses original key version  |  Uses original key version   
Filestore

  * `file.googleapis.com/instance`
  * `file.googleapis.com/backup`

| No  | Yes  | No  |  Uses new primary key version  |  Uses original key version   
Firestore

  * `firestore.googleapis.com/Database`
  * `datastore.googleapis.com/Database`

| No  | Yes  | No  |  Uses new primary key version  |  Uses new primary key version   
Gemini Code Assist

  * `cloudaicompanion.googleapis.com/CodeRepositoryIndex`

| No  | Yes  | No  |  Uses original key version  |  Uses original key version   
Pub/Sub

  * `pubsub.googleapis.com/Topic`

| No  | Yes  | Yes  |  Uses new primary key version  |  Uses original key version   
Secure Source Manager

  * `securesourcemanager.googleapis.com/Instance`

| No  | Yes  | No  |  Uses original key version  |  Uses original key version   
Spanner

  * `storage.googleapis.com/instances.databases`
  * `storage.googleapis.com/instances.backups`

| Yes  | Yes  | No  |  Uses new primary key version  |  Uses original key version   
Speech-to-Text

  * `speech.googleapis.com/Config`

| No  | Yes  | Yes  |  Uses new primary key version  |  Uses original key version   
Speech-to-Text

  * `speech.googleapis.com/CustomClass`
  * `speech.googleapis.com/Endpoint`
  * `speech.googleapis.com/Model`
  * `speech.googleapis.com/PhraseSet`
  * `speech.googleapis.com/Recognizer`

| Yes  | No  | Yes  |  Uses new primary key version  |  Uses original key version   
Workflows

  * `workflows.googleapis.com/Workflow`

| No  | Yes  | Yes  |  Uses original key version  |  Uses original key version   
Workflows

  * `workflowexecutions.googleapis.com/Execution`

| Yes  | No  | No  |  Uses original key version  |  Uses original key version   
  
## What's next

  * Learn how to [rotate a key](https://docs.cloud.google.com/kms/docs/rotate-key).
  * Read the [Customer-managed encryption keys (CMEK) overview](https://docs.cloud.google.com/kms/docs/cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
