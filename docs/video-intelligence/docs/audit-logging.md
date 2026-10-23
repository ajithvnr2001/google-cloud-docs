---
url: https://docs.cloud.google.com/video-intelligence/docs/audit-logging/
title: Video Intelligence API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:05.302943+00:00
---

# Video Intelligence API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/audit-logging/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Video Intelligence API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Video Intelligence API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Video Intelligence API audit logs use the service name `videointelligence.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="videointelligence.googleapis.com"
      

## Audit logs for each API interface

### `google.cloud.videointelligence.v1.VideoIntelligenceService`

The following audit logs are associated with methods belonging to `google.cloud.videointelligence.v1.VideoIntelligenceService`.

#### `AnnotateVideo`

  * **Method** : `google.cloud.videointelligence.v1.VideoIntelligenceService.AnnotateVideo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.videointelligence.v1.VideoIntelligenceService.AnnotateVideo" `  




### `google.cloud.videointelligence.v1beta2.VideoIntelligenceService`

The following audit logs are associated with methods belonging to `google.cloud.videointelligence.v1beta2.VideoIntelligenceService`.

#### `AnnotateVideo`

  * **Method** : `google.cloud.videointelligence.v1beta2.VideoIntelligenceService.AnnotateVideo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.videointelligence.v1beta2.VideoIntelligenceService.AnnotateVideo" `  




### `google.cloud.videointelligence.v1p1beta1.VideoIntelligenceService`

The following audit logs are associated with methods belonging to `google.cloud.videointelligence.v1p1beta1.VideoIntelligenceService`.

#### `AnnotateVideo`

  * **Method** : `google.cloud.videointelligence.v1p1beta1.VideoIntelligenceService.AnnotateVideo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.videointelligence.v1p1beta1.VideoIntelligenceService.AnnotateVideo" `  




### `google.cloud.videointelligence.v1p2beta1.VideoIntelligenceService`

The following audit logs are associated with methods belonging to `google.cloud.videointelligence.v1p2beta1.VideoIntelligenceService`.

#### `AnnotateVideo`

  * **Method** : `google.cloud.videointelligence.v1p2beta1.VideoIntelligenceService.AnnotateVideo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.videointelligence.v1p2beta1.VideoIntelligenceService.AnnotateVideo" `  




### `google.cloud.videointelligence.v1p3beta1.VideoIntelligenceService`

The following audit logs are associated with methods belonging to `google.cloud.videointelligence.v1p3beta1.VideoIntelligenceService`.

#### `AnnotateVideo`

  * **Method** : `google.cloud.videointelligence.v1p3beta1.AnnotateVideo`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.videointelligence.v1p3beta1.AnnotateVideo" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.videointelligence.v1p3beta1.StreamingVideoIntelligenceService.StreamingAnnotateVideo`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
