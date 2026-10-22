---
url: https://docs.cloud.google.com/assured-workloads/access-approval/docs/audit-logging/
title: Access Approval audit logging information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:35.078759+00:00
---

# Access Approval audit logging information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/access-approval/docs/audit-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud provider access management ](https://docs.cloud.google.com/assured-workloads/cloud-provider-access-management/docs)
  * [ Access Approval ](https://docs.cloud.google.com/assured-workloads/access-approval/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access Approval audit logging information 

This document lists the audited methods for Access Approval. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Access Approval audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="accessapproval.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Access Approval generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_WRITE` | `google.cloud.accessapproval.v1.AccessApproval.ApproveApprovalRequest`  
`google.cloud.accessapproval.v1.AccessApproval.DeleteAccessApprovalSettings`  
`google.cloud.accessapproval.v1.AccessApproval.DismissApprovalRequest`  
`google.cloud.accessapproval.v1.AccessApproval.InvalidateApprovalRequest`  
`google.cloud.accessapproval.v1.AccessApproval.UpdateAccessApprovalSettings`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Access Approval.

### `google.cloud.accessapproval.v1.AccessApproval`

The following audit logs are associated with methods belonging to `google.cloud.accessapproval.v1.AccessApproval`.

#### `ApproveApprovalRequest`

  * **Method** : `google.cloud.accessapproval.v1.AccessApproval.ApproveApprovalRequest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accessapproval.requests.approve - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.accessapproval.v1.AccessApproval.ApproveApprovalRequest" `  




#### `DeleteAccessApprovalSettings`

  * **Method** : `google.cloud.accessapproval.v1.AccessApproval.DeleteAccessApprovalSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accessapproval.settings.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.accessapproval.v1.AccessApproval.DeleteAccessApprovalSettings" `  




#### `DismissApprovalRequest`

  * **Method** : `google.cloud.accessapproval.v1.AccessApproval.DismissApprovalRequest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accessapproval.requests.dismiss - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.accessapproval.v1.AccessApproval.DismissApprovalRequest" `  




#### `InvalidateApprovalRequest`

  * **Method** : `google.cloud.accessapproval.v1.AccessApproval.InvalidateApprovalRequest`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accessapproval.requests.invalidate - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.accessapproval.v1.AccessApproval.InvalidateApprovalRequest" `  




#### `UpdateAccessApprovalSettings`

  * **Method** : `google.cloud.accessapproval.v1.AccessApproval.UpdateAccessApprovalSettings`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `accessapproval.settings.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.accessapproval.v1.AccessApproval.UpdateAccessApprovalSettings" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.accessapproval.v1.AccessApproval.GetAccessApprovalServiceAccount`
  * `google.cloud.accessapproval.v1.AccessApproval.GetAccessApprovalSettings`
  * `google.cloud.accessapproval.v1.AccessApproval.GetApprovalRequest`
  * `google.cloud.accessapproval.v1.AccessApproval.ListApprovalRequests`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
