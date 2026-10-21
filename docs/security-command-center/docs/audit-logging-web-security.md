---
url: https://docs.cloud.google.com/security-command-center/docs/audit-logging-web-security/
title: Web Security Scanner audit logging \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:47.424269+00:00
---

# Web Security Scanner audit logging  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/audit-logging-web-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Web Security Scanner audit logging Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document lists the audited methods for Web Security Scanner. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

To view the Web Security Scanner audit logs, do the following:

  1. In the Google Cloud console, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query**.
         
         protoPayload.serviceName="websecurityscanner.googleapis.com"
           




## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Web Security Scanner generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro). Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.websecurityscanner.v1.WebSecurityScanner.GetScanConfig`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.GetScanRun`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.ListScanConfigs`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.ListScanRuns`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetScanConfig`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetScanRun`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListScanConfigs`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListScanRuns`  
`ADMIN_WRITE` | `google.cloud.websecurityscanner.v1.WebSecurityScanner.CreateScanConfig`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.DeleteScanConfig`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.StartScanRun`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.StopScanRun`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.UpdateScanConfig`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.CreateScanConfig`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.DeleteScanConfig`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.StartScanRun`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.StopScanRun`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.UpdateScanConfig`  
`DATA_READ` | `google.cloud.websecurityscanner.v1.WebSecurityScanner.GetFinding`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.ListCrawledUrls`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.ListFindingTypeStats`  
`google.cloud.websecurityscanner.v1.WebSecurityScanner.ListFindings`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetFinding`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListCrawledUrls`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListFindingTypeStats`  
`google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListFindings`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the [Identity and Access Management documentation](https://docs.cloud.google.com/security-command-center/docs/access-control) for Web Security Scanner.

### `google.cloud.websecurityscanner.v1.WebSecurityScanner`

The following audit logs are associated with methods belonging to `google.cloud.websecurityscanner.v1.WebSecurityScanner`.

#### `CreateScanConfig`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.CreateScanConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.CreateScanConfig" `  




#### `DeleteScanConfig`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.DeleteScanConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.DeleteScanConfig" `  




#### `GetFinding`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.GetFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.results.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.GetFinding" `  




#### `GetScanConfig`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.GetScanConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.GetScanConfig" `  




#### `GetScanRun`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.GetScanRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scanruns.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.GetScanRun" `  




#### `ListCrawledUrls`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.ListCrawledUrls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.crawledurls.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.ListCrawledUrls" `  




#### `ListFindingTypeStats`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.ListFindingTypeStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scanruns.getSummary - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.ListFindingTypeStats" `  




#### `ListFindings`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.ListFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.results.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.ListFindings" `  




#### `ListScanConfigs`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.ListScanConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.ListScanConfigs" `  




#### `ListScanRuns`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.ListScanRuns`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scanruns.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.ListScanRuns" `  




#### `StartScanRun`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.StartScanRun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.StartScanRun" `  




#### `StopScanRun`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.StopScanRun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scanruns.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.StopScanRun" `  




#### `UpdateScanConfig`

  * **Method** : `google.cloud.websecurityscanner.v1.WebSecurityScanner.UpdateScanConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1.WebSecurityScanner.UpdateScanConfig" `  




### `google.cloud.websecurityscanner.v1beta.WebSecurityScanner`

The following audit logs are associated with methods belonging to `google.cloud.websecurityscanner.v1beta.WebSecurityScanner`.

#### `CreateScanConfig`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.CreateScanConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.CreateScanConfig" `  




#### `DeleteScanConfig`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.DeleteScanConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.DeleteScanConfig" `  




#### `GetFinding`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetFinding`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.results.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetFinding" `  




#### `GetScanConfig`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetScanConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetScanConfig" `  




#### `GetScanRun`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetScanRun`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scanruns.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.GetScanRun" `  




#### `ListCrawledUrls`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListCrawledUrls`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.crawledurls.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListCrawledUrls" `  




#### `ListFindingTypeStats`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListFindingTypeStats`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scanruns.getSummary - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListFindingTypeStats" `  




#### `ListFindings`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListFindings`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.results.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListFindings" `  




#### `ListScanConfigs`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListScanConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListScanConfigs" `  




#### `ListScanRuns`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListScanRuns`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `cloudsecurityscanner.scanruns.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.ListScanRuns" `  




#### `StartScanRun`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.StartScanRun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.run - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.StartScanRun" `  




#### `StopScanRun`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.StopScanRun`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scanruns.stop - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.StopScanRun" `  




#### `UpdateScanConfig`

  * **Method** : `google.cloud.websecurityscanner.v1beta.WebSecurityScanner.UpdateScanConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `cloudsecurityscanner.scans.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.websecurityscanner.v1beta.WebSecurityScanner.UpdateScanConfig" `  




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
