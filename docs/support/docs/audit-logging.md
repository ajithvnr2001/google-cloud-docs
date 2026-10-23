---
url: https://docs.cloud.google.com/support/docs/audit-logging/
title: Cloud Customer Care audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:51.077854+00:00
---

# Cloud Customer Care audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/audit-logging/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Cloud Customer Care audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the audited methods for Cloud Customer Care. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Cloud Customer Care audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="cloudsupport.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Cloud Customer Care generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`DATA_READ` | `google.cloud.support.v2.CaseAttachmentService.DownloadAttachment`  
`google.cloud.support.v2.CaseAttachmentService.GetAttachment`  
`google.cloud.support.v2.CaseAttachmentService.ListAttachments`  
`google.cloud.support.v2.CaseService.GetCase`  
`google.cloud.support.v2.CaseService.ListCases`  
`google.cloud.support.v2.CommentService.GetComment`  
`google.cloud.support.v2.CommentService.ListComments`  
`google.cloud.support.v2.SupportEventSubscriptionService.GetSupportEventSubscription`  
`google.cloud.support.v2.SupportEventSubscriptionService.ListSupportEventSubscriptions`  
`google.cloud.support.v2beta.CaseAttachmentService.DownloadAttachment`  
`google.cloud.support.v2beta.CaseAttachmentService.GetAttachment`  
`google.cloud.support.v2beta.CaseAttachmentService.ListAttachments`  
`google.cloud.support.v2beta.CaseService.GetCase`  
`google.cloud.support.v2beta.CaseService.ListCases`  
`google.cloud.support.v2beta.CommentService.GetComment`  
`google.cloud.support.v2beta.CommentService.ListComments`  
`google.cloud.support.v2beta.FeedService.ShowFeed`  
`google.cloud.support.v2beta.SupportEventSubscriptionService.ListSupportEventSubscriptions`  
`DATA_WRITE` | `google.cloud.support.v2.CaseAttachmentService.CreateAttachment`  
`google.cloud.support.v2.CaseService.CloseCase`  
`google.cloud.support.v2.CaseService.CreateCase`  
`google.cloud.support.v2.CaseService.EscalateCase`  
`google.cloud.support.v2.CaseService.UpdateCase`  
`google.cloud.support.v2.CommentService.CreateComment`  
`google.cloud.support.v2.SupportEventSubscriptionService.CreateSupportEventSubscription`  
`google.cloud.support.v2.SupportEventSubscriptionService.DeleteSupportEventSubscription`  
`google.cloud.support.v2.SupportEventSubscriptionService.UndeleteSupportEventSubscription`  
`google.cloud.support.v2.SupportEventSubscriptionService.UpdateSupportEventSubscription`  
`google.cloud.support.v2beta.CaseAttachmentService.CreateAttachment`  
`google.cloud.support.v2beta.CaseService.CloseCase`  
`google.cloud.support.v2beta.CaseService.CreateCase`  
`google.cloud.support.v2beta.CaseService.EscalateCase`  
`google.cloud.support.v2beta.CaseService.UpdateCase`  
`google.cloud.support.v2beta.CommentService.CreateComment`  
`google.cloud.support.v2beta.SupportEventSubscriptionService.CreateSupportEventSubscription`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Cloud Customer Care.

### `google.cloud.support.v2.CaseAttachmentService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2.CaseAttachmentService`.

#### `CreateAttachment`

  * **Method** : `google.cloud.support.v2.CaseAttachmentService.CreateAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseAttachmentService.CreateAttachment" `  




#### `DownloadAttachment`

  * **Method** : `google.cloud.support.v2.CaseAttachmentService.DownloadAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseAttachmentService.DownloadAttachment" `  




#### `GetAttachment`

  * **Method** : `google.cloud.support.v2.CaseAttachmentService.GetAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseAttachmentService.GetAttachment" `  




#### `ListAttachments`

  * **Method** : `google.cloud.support.v2.CaseAttachmentService.ListAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseAttachmentService.ListAttachments" `  




### `google.cloud.support.v2.CaseService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2.CaseService`.

#### `CloseCase`

  * **Method** : `google.cloud.support.v2.CaseService.CloseCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseService.CloseCase" `  




#### `CreateCase`

  * **Method** : `google.cloud.support.v2.CaseService.CreateCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseService.CreateCase" `  




#### `EscalateCase`

  * **Method** : `google.cloud.support.v2.CaseService.EscalateCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.escalate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseService.EscalateCase" `  




#### `GetCase`

  * **Method** : `google.cloud.support.v2.CaseService.GetCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseService.GetCase" `  




#### `ListCases`

  * **Method** : `google.cloud.support.v2.CaseService.ListCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseService.ListCases" `  




#### `UpdateCase`

  * **Method** : `google.cloud.support.v2.CaseService.UpdateCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CaseService.UpdateCase" `  




### `google.cloud.support.v2.CommentService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2.CommentService`.

#### `CreateComment`

  * **Method** : `google.cloud.support.v2.CommentService.CreateComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CommentService.CreateComment" `  




#### `GetComment`

  * **Method** : `google.cloud.support.v2.CommentService.GetComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CommentService.GetComment" `  




#### `ListComments`

  * **Method** : `google.cloud.support.v2.CommentService.ListComments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.CommentService.ListComments" `  




### `google.cloud.support.v2.SupportEventSubscriptionService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2.SupportEventSubscriptionService`.

#### `CreateSupportEventSubscription`

  * **Method** : `google.cloud.support.v2.SupportEventSubscriptionService.CreateSupportEventSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.supportSubscriptions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.SupportEventSubscriptionService.CreateSupportEventSubscription" `  




#### `DeleteSupportEventSubscription`

  * **Method** : `google.cloud.support.v2.SupportEventSubscriptionService.DeleteSupportEventSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.supportSubscriptions.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.SupportEventSubscriptionService.DeleteSupportEventSubscription" `  




#### `GetSupportEventSubscription`

  * **Method** : `google.cloud.support.v2.SupportEventSubscriptionService.GetSupportEventSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.supportSubscriptions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.SupportEventSubscriptionService.GetSupportEventSubscription" `  




#### `ListSupportEventSubscriptions`

  * **Method** : `google.cloud.support.v2.SupportEventSubscriptionService.ListSupportEventSubscriptions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.supportSubscriptions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.SupportEventSubscriptionService.ListSupportEventSubscriptions" `  




#### `UndeleteSupportEventSubscription`

  * **Method** : `google.cloud.support.v2.SupportEventSubscriptionService.UndeleteSupportEventSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.supportSubscriptions.undelete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.SupportEventSubscriptionService.UndeleteSupportEventSubscription" `  




#### `UpdateSupportEventSubscription`

  * **Method** : `google.cloud.support.v2.SupportEventSubscriptionService.UpdateSupportEventSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.supportSubscriptions.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2.SupportEventSubscriptionService.UpdateSupportEventSubscription" `  




### `google.cloud.support.v2beta.CaseAttachmentService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2beta.CaseAttachmentService`.

#### `CreateAttachment`

  * **Method** : `google.cloud.support.v2beta.CaseAttachmentService.CreateAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseAttachmentService.CreateAttachment" `  




#### `DownloadAttachment`

  * **Method** : `google.cloud.support.v2beta.CaseAttachmentService.DownloadAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseAttachmentService.DownloadAttachment" `  




#### `GetAttachment`

  * **Method** : `google.cloud.support.v2beta.CaseAttachmentService.GetAttachment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseAttachmentService.GetAttachment" `  




#### `ListAttachments`

  * **Method** : `google.cloud.support.v2beta.CaseAttachmentService.ListAttachments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseAttachmentService.ListAttachments" `  




### `google.cloud.support.v2beta.CaseService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2beta.CaseService`.

#### `CloseCase`

  * **Method** : `google.cloud.support.v2beta.CaseService.CloseCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseService.CloseCase" `  




#### `CreateCase`

  * **Method** : `google.cloud.support.v2beta.CaseService.CreateCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseService.CreateCase" `  




#### `EscalateCase`

  * **Method** : `google.cloud.support.v2beta.CaseService.EscalateCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.escalate - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseService.EscalateCase" `  




#### `GetCase`

  * **Method** : `google.cloud.support.v2beta.CaseService.GetCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseService.GetCase" `  




#### `ListCases`

  * **Method** : `google.cloud.support.v2beta.CaseService.ListCases`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseService.ListCases" `  




#### `UpdateCase`

  * **Method** : `google.cloud.support.v2beta.CaseService.UpdateCase`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CaseService.UpdateCase" `  




### `google.cloud.support.v2beta.CommentService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2beta.CommentService`.

#### `CreateComment`

  * **Method** : `google.cloud.support.v2beta.CommentService.CreateComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CommentService.CreateComment" `  




#### `GetComment`

  * **Method** : `google.cloud.support.v2beta.CommentService.GetComment`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CommentService.GetComment" `  




#### `ListComments`

  * **Method** : `google.cloud.support.v2beta.CommentService.ListComments`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.CommentService.ListComments" `  




### `google.cloud.support.v2beta.FeedService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2beta.FeedService`.

#### `ShowFeed`

  * **Method** : `google.cloud.support.v2beta.FeedService.ShowFeed`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.techCases.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.FeedService.ShowFeed" `  




### `google.cloud.support.v2beta.SupportEventSubscriptionService`

The following audit logs are associated with methods belonging to `google.cloud.support.v2beta.SupportEventSubscriptionService`.

#### `CreateSupportEventSubscription`

  * **Method** : `google.cloud.support.v2beta.SupportEventSubscriptionService.CreateSupportEventSubscription`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.supportSubscriptions.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.SupportEventSubscriptionService.CreateSupportEventSubscription" `  




#### `ListSupportEventSubscriptions`

  * **Method** : `google.cloud.support.v2beta.SupportEventSubscriptionService.ListSupportEventSubscriptions`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsupport.supportSubscriptions.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.support.v2beta.SupportEventSubscriptionService.ListSupportEventSubscriptions" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.support.v2.CaseService.SearchCaseClassifications`
  * `google.cloud.support.v2.CaseService.SearchCases`
  * `google.cloud.support.v2beta.CaseService.SearchCaseClassifications`
  * `google.cloud.support.v2beta.CaseService.SearchCases`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
