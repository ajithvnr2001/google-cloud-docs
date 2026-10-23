---
url: https://docs.cloud.google.com/recommender/docs/audit-logging/
title: Recommender audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:09.198296+00:00
---

# Recommender audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Guides ](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Recommender audit logging

This document describes audit logging for Recommender. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Recommender audit logs use the service name `recommender.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="recommender.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Recommender generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.recommender.v1.Recommender.GetInsightTypeConfig`  
`google.cloud.recommender.v1.Recommender.GetRecommenderConfig`  
`google.cloud.recommender.v1beta1.Recommender.GetInsightTypeConfig`  
`google.cloud.recommender.v1beta1.Recommender.GetRecommenderConfig`  
`ADMIN_WRITE` | `google.cloud.recommender.v1.Recommender.UpdateInsightTypeConfig`  
`google.cloud.recommender.v1.Recommender.UpdateRecommenderConfig`  
`google.cloud.recommender.v1beta1.Recommender.UpdateInsightTypeConfig`  
`google.cloud.recommender.v1beta1.Recommender.UpdateRecommenderConfig`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Recommender.

### `google.cloud.recommender.v1.Recommender`

The following audit logs are associated with methods belonging to `google.cloud.recommender.v1.Recommender`.

#### `GetInsightTypeConfig`

  * **Method** : `google.cloud.recommender.v1.Recommender.GetInsightTypeConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recommender.computeInstanceBestPracticeInsightTypeConfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recommender.v1.Recommender.GetInsightTypeConfig" `  




#### `GetRecommenderConfig`

  * **Method** : `google.cloud.recommender.v1.Recommender.GetRecommenderConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recommender.computeInstanceBestPracticeRecommenderConfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recommender.v1.Recommender.GetRecommenderConfig" `  




#### `UpdateInsightTypeConfig`

  * **Method** : `google.cloud.recommender.v1.Recommender.UpdateInsightTypeConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recommender.computeFirewallInsightTypeConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recommender.v1.Recommender.UpdateInsightTypeConfig" `  




#### `UpdateRecommenderConfig`

  * **Method** : `google.cloud.recommender.v1.Recommender.UpdateRecommenderConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recommender.computeInstanceBestPracticeRecommenderConfig.update - ADMIN_WRITE`
    * `recommender.computeInstanceIdleResourceRecommenderConfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recommender.v1.Recommender.UpdateRecommenderConfig" `  




### `google.cloud.recommender.v1beta1.Recommender`

The following audit logs are associated with methods belonging to `google.cloud.recommender.v1beta1.Recommender`.

#### `GetInsightTypeConfig`

  * **Method** : `google.cloud.recommender.v1beta1.Recommender.GetInsightTypeConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recommender.computeFirewallInsightTypeConfigs.get - ADMIN_READ`
    * `recommender.computeInstanceBestPracticeInsightTypeConfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recommender.v1beta1.Recommender.GetInsightTypeConfig" `  




#### `GetRecommenderConfig`

  * **Method** : `google.cloud.recommender.v1beta1.Recommender.GetRecommenderConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `recommender.computeInstanceBestPracticeRecommenderConfig.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recommender.v1beta1.Recommender.GetRecommenderConfig" `  




#### `UpdateInsightTypeConfig`

  * **Method** : `google.cloud.recommender.v1beta1.Recommender.UpdateInsightTypeConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recommender.computeFirewallInsightTypeConfigs.update - ADMIN_WRITE`
    * `recommender.computeInstanceBestPracticeInsightTypeConfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recommender.v1beta1.Recommender.UpdateInsightTypeConfig" `  




#### `UpdateRecommenderConfig`

  * **Method** : `google.cloud.recommender.v1beta1.Recommender.UpdateRecommenderConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `recommender.computeInstanceBestPracticeRecommenderConfig.update - ADMIN_WRITE`
    * `recommender.spendBasedCommitmentRecommenderConfig.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.recommender.v1beta1.Recommender.UpdateRecommenderConfig" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.recommender.v1.Recommender.GetInsight`
  * `google.cloud.recommender.v1.Recommender.GetRecommendation`
  * `google.cloud.recommender.v1.Recommender.ListInsights`
  * `google.cloud.recommender.v1.Recommender.ListRecommendations`
  * `google.cloud.recommender.v1.Recommender.MarkInsightAccepted`
  * `google.cloud.recommender.v1.Recommender.MarkRecommendationClaimed`
  * `google.cloud.recommender.v1.Recommender.MarkRecommendationDismissed`
  * `google.cloud.recommender.v1.Recommender.MarkRecommendationFailed`
  * `google.cloud.recommender.v1.Recommender.MarkRecommendationSucceeded`
  * `google.cloud.recommender.v1beta1.Recommender.GetInsight`
  * `google.cloud.recommender.v1beta1.Recommender.GetRecommendation`
  * `google.cloud.recommender.v1beta1.Recommender.ListInsightTypes`
  * `google.cloud.recommender.v1beta1.Recommender.ListInsights`
  * `google.cloud.recommender.v1beta1.Recommender.ListLocations`
  * `google.cloud.recommender.v1beta1.Recommender.ListRecommendations`
  * `google.cloud.recommender.v1beta1.Recommender.ListRecommenders`
  * `google.cloud.recommender.v1beta1.Recommender.MarkInsightAccepted`
  * `google.cloud.recommender.v1beta1.Recommender.MarkRecommendationClaimed`
  * `google.cloud.recommender.v1beta1.Recommender.MarkRecommendationDismissed`
  * `google.cloud.recommender.v1beta1.Recommender.MarkRecommendationFailed`
  * `google.cloud.recommender.v1beta1.Recommender.MarkRecommendationSucceeded`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
