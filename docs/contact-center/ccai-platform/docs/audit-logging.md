---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/audit-logging/
title: Audit logging information \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:26.809570+00:00
---

# Audit logging information  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Audit logging information Stay organized with collections  Save and categorize content based on your preferences. 

This page contains information about Cloud Audit logging for `contactcenteraiplatform.googleapis.com` API. For example, entries are logged when Contact Center AI Platform (CCAI Platform) is created or deleted.

This page doesn't describe audit logs for user actions performed on Contact Center AI Platform. For example, when contact center users (admins, managers, agents) sign in, or make changes to settings. To get audit logs for user actions, contact Cloud Support and provide the following:

  * Google Cloud project of the CCAI Platform contact center.

  * CCAI Platform URL for the contact center

  * The region for the CCAI Platform contact center, for example, `us-central1`.

  * The Cloud Storage bucket (`gs://bucketname`) where you want Cloud Support to upload the logs. You will need to grant write access to Cloud Support on this bucket, so they can upload the logs.

The start and end time and date with the time zone (preferably in UTC) within the last 30 days for the window that you want the logs for. Logs older than 30 days are deleted and cannot be provided.




This document lists the audited methods for Google Cloud Contact Center as a Service. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Google Cloud Contact Center as a Service audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="contactcenteraiplatform.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Google Cloud Contact Center as a Service generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.GetContactCenter`  
`google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.ListContactCenters`  
`google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.QueryContactCenterQuota`  
`google.cloud.contactcenteraiplatform.v1alpha1.WorkforceScheduling.GenerateShifts` (LRO)  
`google.longrunning.Operations.GetOperation`  
`google.longrunning.Operations.ListOperations`  
`ADMIN_WRITE` | `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.CreateContactCenter` (LRO)  
`google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.DeleteContactCenter` (LRO)  
`google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.UpdateContactCenter` (LRO)  
`google.longrunning.Operations.CancelOperation`  
`google.longrunning.Operations.DeleteOperation`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Google Cloud Contact Center as a Service.

### `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform`

The following audit logs are associated with methods belonging to `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform`.

#### `CreateContactCenter`

  * **Method** : `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.CreateContactCenter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contactcenteraiplatform.contactCenters.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.CreateContactCenter" `  




#### `DeleteContactCenter`

  * **Method** : `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.DeleteContactCenter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contactcenteraiplatform.contactCenters.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.DeleteContactCenter" `  




#### `GetContactCenter`

  * **Method** : `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.GetContactCenter`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenteraiplatform.contactCenters.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.GetContactCenter" `  




#### `ListContactCenters`

  * **Method** : `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.ListContactCenters`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenteraiplatform.contactCenters.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.ListContactCenters" `  




#### `QueryContactCenterQuota`

  * **Method** : `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.QueryContactCenterQuota`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenteraiplatform.contactCenters.queryQuota - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.QueryContactCenterQuota" `  




#### `UpdateContactCenter`

  * **Method** : `google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.UpdateContactCenter`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contactcenteraiplatform.contactCenters.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenteraiplatform.v1alpha1.ContactCenterAiPlatform.UpdateContactCenter" `  




### `google.cloud.contactcenteraiplatform.v1alpha1.WorkforceScheduling`

The following audit logs are associated with methods belonging to `google.cloud.contactcenteraiplatform.v1alpha1.WorkforceScheduling`.

#### `GenerateShifts`

  * **Method** : `google.cloud.contactcenteraiplatform.v1alpha1.WorkforceScheduling.GenerateShifts`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenteraiplatform.locations.generateShifts - ADMIN_READ`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.contactcenteraiplatform.v1alpha1.WorkforceScheduling.GenerateShifts" `  




### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to `google.longrunning.Operations`.

#### `CancelOperation`

  * **Method** : `google.longrunning.Operations.CancelOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contactcenteraiplatform.operations.cancel - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.CancelOperation" `  




#### `DeleteOperation`

  * **Method** : `google.longrunning.Operations.DeleteOperation`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `contactcenteraiplatform.operations.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.DeleteOperation" `  




#### `GetOperation`

  * **Method** : `google.longrunning.Operations.GetOperation`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenteraiplatform.operations.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.GetOperation" `  




#### `ListOperations`

  * **Method** : `google.longrunning.Operations.ListOperations`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `contactcenteraiplatform.operations.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.longrunning.Operations.ListOperations" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.location.Locations.GetLocation`
  * `google.cloud.location.Locations.ListLocations`
  * `google.longrunning.Operations.WaitOperation`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
