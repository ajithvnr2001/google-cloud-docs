---
url: https://docs.cloud.google.com/apigee/docs/api-observation/audit-logging/
title: Apigee API Management audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:15:24.139349+00:00
---

# Apigee API Management audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-observation/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee API Management audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Apigee API Management. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Apigee API Management audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="apim.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Apigee API Management generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetEntitlement`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetObservationJob`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetObservationSource`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiObservationTags`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListObservationJobs`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListObservationSources`  
`ADMIN_WRITE` | `google.cloud.apim.v1alpha.ApiDiscoveryObservation.BatchEditTagsApiObservations`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.CreateObservationJob` (LRO)  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.CreateObservationSource` (LRO)  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.DeleteObservationJob` (LRO)  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.DeleteObservationSource` (LRO)  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.DisableObservationJob` (LRO)  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.EnableObservationJob` (LRO)  
`DATA_READ` | `google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetApiObservation`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetApiOperation`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiObservations`  
`google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiOperations`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Apigee API Management.

### `google.cloud.apim.v1alpha.ApiDiscoveryObservation`

The following audit logs are associated with methods belonging to `google.cloud.apim.v1alpha.ApiDiscoveryObservation`.

#### `BatchEditTagsApiObservations`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.BatchEditTagsApiObservations`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apim.apiObservations.batchEditTags - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.BatchEditTagsApiObservations" `  




#### `CreateObservationJob`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.CreateObservationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apim.observationJobs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.CreateObservationJob" `  




#### `CreateObservationSource`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.CreateObservationSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apim.observationSources.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.CreateObservationSource" `  




#### `DeleteObservationJob`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.DeleteObservationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apim.observationJobs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.DeleteObservationJob" `  




#### `DeleteObservationSource`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.DeleteObservationSource`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apim.observationSources.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.DeleteObservationSource" `  




#### `DisableObservationJob`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.DisableObservationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apim.observationJobs.disable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.DisableObservationJob" `  




#### `EnableObservationJob`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.EnableObservationJob`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `apim.observationJobs.enable - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.EnableObservationJob" `  




#### `GetApiObservation`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetApiObservation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.apiObservations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetApiObservation" `  




#### `GetApiOperation`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetApiOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.apiOperations.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetApiOperation" `  




#### `GetEntitlement`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetEntitlement`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.entitlements.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetEntitlement" `  




#### `GetObservationJob`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetObservationJob`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.observationJobs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetObservationJob" `  




#### `GetObservationSource`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetObservationSource`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.observationSources.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.GetObservationSource" `  




#### `ListApiObservationTags`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiObservationTags`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.locations.listApiObservationTags - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiObservationTags" `  




#### `ListApiObservations`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiObservations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.apiObservations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiObservations" `  




#### `ListApiOperations`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.apiOperations.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListApiOperations" `  




#### `ListObservationJobs`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListObservationJobs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.observationJobs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListObservationJobs" `  




#### `ListObservationSources`

  * **Method** : `google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListObservationSources`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `apim.observationSources.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.apim.v1alpha.ApiDiscoveryObservation.ListObservationSources" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.CancelOperation`
  * `google.longrunning.Operations.DeleteOperation`
  * `google.longrunning.Operations.GetOperation`
  * `google.longrunning.Operations.ListOperations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
