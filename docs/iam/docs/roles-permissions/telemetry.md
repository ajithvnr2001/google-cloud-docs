---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry/
title: Telemetry API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:22:18.626939+00:00
---

# Telemetry API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Telemetry API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Telemetry API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Telemetry API roles

Role | Permissions  
---|---  
  
#### Telemetry Admin 

(`roles/telemetry.admin`) Admin role for telemetry  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `telemetry.*`

  * `telemetry.consumers.getIamPolicy`
  * `telemetry.consumers.setIamPolicy`
  * `telemetry.consumers.writeLogs`
  * `telemetry.consumers.writeMetrics`
  * `telemetry.consumers.writeTraces`
  * `telemetry.traces.write`

  
  
#### Telemetry Editor 

(`roles/telemetry.editor`) Editor role for telemetry  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `telemetry.traces.write`  
  
#### Consumer Admin Beta

(`roles/telemetry.consumerAdmin`) Grants permission management access to consumer resources.  |  `telemetry.consumers.getIamPolicy` `telemetry.consumers.setIamPolicy`  
  
#### Cloud Telemetry Logs Writer 

(`roles/telemetry.logsWriter`) Access to write logs.  |  `logging.logEntries.create`  
  
#### Cloud Telemetry Metrics Writer 

(`roles/telemetry.metricsWriter`) Access to write metrics.  |  `monitoring.timeSeries.create`  
  
#### Integrated Service Telemetry Logs Writer Beta

(`roles/telemetry.serviceLogsWriter`) Allows an onboarded service to write log data to a destination.  |  `telemetry.consumers.writeLogs`  
  
#### Integrated Service Telemetry Metrics Writer Beta

(`roles/telemetry.serviceMetricsWriter`) Allows an onboarded service to write metrics data to a destination.  |  `telemetry.consumers.writeMetrics`  
  
#### Integrated Service Telemetry Writer Beta

(`roles/telemetry.serviceTelemetryWriter`) Allows an onboarded service to write all telemetry data to a destination.  |  `telemetry.consumers.writeLogs` `telemetry.consumers.writeMetrics` `telemetry.consumers.writeTraces`  
  
#### Integrated Service Telemetry Traces Writer Beta

(`roles/telemetry.serviceTracesWriter`) Allows an onboarded service to write trace data to a destination.  |  `telemetry.consumers.writeTraces`  
  
#### Cloud Telemetry Traces Writer 

(`roles/telemetry.tracesWriter`) Access to write trace spans.  |  `telemetry.traces.write`  
  
#### Cloud Telemetry Writer 

(`roles/telemetry.writer`) Full access to write all telemetry data.  |  `logging.logEntries.create` `monitoring.timeSeries.create` `telemetry.traces.write`  
  
## Telemetry API permissions

Permission | Included in roles  
---|---  
  
#### `telemetry.consumers.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Telemetry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.admin) (`roles/telemetry.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Consumer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.consumerAdmin) (`roles/telemetry.consumerAdmin`)   
  
#### `telemetry.consumers.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Telemetry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.admin) (`roles/telemetry.admin`)  [Consumer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.consumerAdmin) (`roles/telemetry.consumerAdmin`)   
  
#### `telemetry.consumers.writeLogs`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Telemetry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.admin) (`roles/telemetry.admin`)  [Integrated Service Telemetry Logs Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.serviceLogsWriter) (`roles/telemetry.serviceLogsWriter`)  [Integrated Service Telemetry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.serviceTelemetryWriter) (`roles/telemetry.serviceTelemetryWriter`)   
  
#### `telemetry.consumers.writeMetrics`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Telemetry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.admin) (`roles/telemetry.admin`)  [Integrated Service Telemetry Metrics Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.serviceMetricsWriter) (`roles/telemetry.serviceMetricsWriter`)  [Integrated Service Telemetry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.serviceTelemetryWriter) (`roles/telemetry.serviceTelemetryWriter`)   
  
#### `telemetry.consumers.writeTraces`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Telemetry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.admin) (`roles/telemetry.admin`)  [Integrated Service Telemetry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.serviceTelemetryWriter) (`roles/telemetry.serviceTelemetryWriter`)  [Integrated Service Telemetry Traces Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.serviceTracesWriter) (`roles/telemetry.serviceTracesWriter`)   
  
#### `telemetry.traces.write`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Trace Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.admin) (`roles/cloudtrace.admin`)  [Telemetry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.admin) (`roles/telemetry.admin`)  [Telemetry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.editor) (`roles/telemetry.editor`)  [Cloud Trace Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`)  [Firebase App Hosting Compute Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseapphosting#firebaseapphosting.computeRunner) (`roles/firebaseapphosting.computeRunner`)  [Cloud Telemetry Traces Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.tracesWriter) (`roles/telemetry.tracesWriter`)  [Cloud Telemetry Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.writer) (`roles/telemetry.writer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI Reasoning Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.reasoningEngineServiceAgent) (`roles/aiplatform.reasoningEngineServiceAgent`) 
  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [Kubernetes Engine Default Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAgent) (`roles/container.defaultNodeServiceAgent`) 
  * [Database Insights Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.serviceAgent) (`roles/databaseinsights.serviceAgent`) 
  * [Firebase AI Logic Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseml#firebaseml.serviceAgent) (`roles/firebaseml.serviceAgent`) 
  * [Firebase Telemetry Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasetelemetry#firebasetelemetry.serviceAgent) (`roles/firebasetelemetry.serviceAgent`) 
  * [Mesh Data Plane Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/anthosservicemesh#meshdataplane.serviceAgent) (`roles/meshdataplane.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
