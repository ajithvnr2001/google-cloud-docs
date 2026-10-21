---
url: https://docs.cloud.google.com/eventarc/docs/eventarc-regulatory-compliance/
title: Regulatory support in Eventarc \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:41.226453+00:00
---

# Regulatory support in Eventarc  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/eventarc-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Resources ](https://docs.cloud.google.com/eventarc/docs/resources)



Send feedback 

#  Regulatory support in Eventarc Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Eventarc that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Eventarc APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
eventarc.googleapis.com | v1 |  SUPPORTED   
  
### Compliance supported regions

Eventarc is available for Data Boundary for ITAR in the following Google Cloud regions:

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



### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Authentication and authorization | 

  * `channel.cryptoKeyName`
  * `googleApiSource.cryptoKeyName`
  * `kafkaSource.authenticationConfig.saslAuth.usernameSecret`
  * `pipeline.destinations.authenticationConfig.oauthToken.scope`
  * `trigger.serviceAccount`

  
Paging and filtering | 

  * `filter`
  * `orderBy`
  * `pageToken`

  
Parent resource specification | 

  * `parent`

  
Resource configuration - channels | 

  * `channel.provider`
  * `channelConnection.activationToken`
  * `channelConnection.channel`

  
Resource configuration - enrollments | 

  * `enrollment.celMatch`
  * `enrollment.destination`
  * `enrollment.messageBus`

  
Resource configuration - pipelines | 

  * `pipeline.destinations.topic`
  * `pipeline.destinations.workflow`
  * `pipeline.inputPayloadFormat.protobuf.schemaDefinition`

  
Resource configuration - sources | 

  * `googleApiSource.destination`
  * `kafkaSource.brokerUris`
  * `kafkaSource.topics`

  
Resource configuration - triggers | 

  * `trigger.destination.cloudRun.service`
  * `trigger.destination.gke.cluster`
  * `trigger.eventFilters.attribute`

  
Resource identification | 

  * `channelId`
  * `enrollmentId`
  * `googleApiSourceId`
  * `kafkaSourceId`
  * `messageBusId`
  * `pipelineId`

  
Resource naming | 

  * `channel.name`
  * `enrollment.name`
  * `googleApiSource.name`
  * `kafkaSource.name`
  * `messageBus.name`
  * `name`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
