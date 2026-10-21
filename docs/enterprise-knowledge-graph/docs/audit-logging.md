---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/audit-logging/
title: Enterprise Knowledge Graph audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:33:29.300068+00:00
---

# Enterprise Knowledge Graph audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Reference ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/libraries)



Send feedback 

#  Enterprise Knowledge Graph audit logging Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this product or feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes audit logging for Enterprise Knowledge Graph. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Enterprise Knowledge Graph audit logs use the service name `enterpriseknowledgegraph.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="enterpriseknowledgegraph.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Enterprise Knowledge Graph generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.GetEntityReconciliationJob`  
`google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Lookup`  
`google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search`  
`ADMIN_WRITE` | `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.CancelEntityReconciliationJob`  
`google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.CreateEntityReconciliationJob`  
`google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.DeleteEntityReconciliationJob`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Enterprise Knowledge Graph.

### `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService`

The following audit logs are associated with methods belonging to `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService`.

#### `CancelEntityReconciliationJob`

  * **Method** : `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.CancelEntityReconciliationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `enterpriseknowledgegraph.entityReconciliationJobs.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.CancelEntityReconciliationJob" `  




#### `CreateEntityReconciliationJob`

  * **Method** : `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.CreateEntityReconciliationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `enterpriseknowledgegraph.entityReconciliationJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.CreateEntityReconciliationJob" `  




#### `DeleteEntityReconciliationJob`

  * **Method** : `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.DeleteEntityReconciliationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `enterpriseknowledgegraph.entityReconciliationJobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.DeleteEntityReconciliationJob" `  




#### `GetEntityReconciliationJob`

  * **Method** : `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.GetEntityReconciliationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `enterpriseknowledgegraph.entityReconciliationJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.GetEntityReconciliationJob" `  




#### `Lookup`

  * **Method** : `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Lookup`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.lookup - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Lookup" `  




#### `Search`

  * **Method** : `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.search - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.Search" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.ListEntityReconciliationJobs`
  * `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.LookupPublicKg`
  * `google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphService.SearchPublicKg`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
