---
url: https://docs.cloud.google.com/video-stitcher/docs/audit-logging/
title: Video Stitcher API audit logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:31.135650+00:00
---

# Video Stitcher API audit logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/audit-logging/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Guides ](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



Send feedback 

#  Video Stitcher API audit logging Stay organized with collections  Save and categorize content based on your preferences. 

This document describes audit logging for Video Stitcher API. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Video Stitcher API audit logs use the service name `videostitcher.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="videostitcher.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Video Stitcher API generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`ADMIN_READ` | `google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveConfig`  
`google.cloud.video.stitcher.v1.VideoStitcherService.GetVodConfig`  
`google.cloud.video.stitcher.v1.VideoStitcherService.ListLiveConfigs`  
`google.cloud.video.stitcher.v1.VideoStitcherService.ListVodConfigs`  
`ADMIN_WRITE` | `google.cloud.video.stitcher.v1.VideoStitcherService.CreateLiveConfig`  
`google.cloud.video.stitcher.v1.VideoStitcherService.CreateVodConfig`  
`google.cloud.video.stitcher.v1.VideoStitcherService.DeleteLiveConfig`  
`google.cloud.video.stitcher.v1.VideoStitcherService.DeleteVodConfig`  
`google.cloud.video.stitcher.v1.VideoStitcherService.UpdateLiveConfig`  
`google.cloud.video.stitcher.v1.VideoStitcherService.UpdateVodConfig`  
`DATA_READ` | `google.cloud.video.stitcher.v1.VideoStitcherService.GetCdnKey`  
`google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveAdTagDetail`  
`google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveSession`  
`google.cloud.video.stitcher.v1.VideoStitcherService.GetSlate`  
`google.cloud.video.stitcher.v1.VideoStitcherService.GetVodAdTagDetail`  
`google.cloud.video.stitcher.v1.VideoStitcherService.GetVodSession`  
`google.cloud.video.stitcher.v1.VideoStitcherService.GetVodStitchDetail`  
`google.cloud.video.stitcher.v1.VideoStitcherService.ListCdnKeys`  
`google.cloud.video.stitcher.v1.VideoStitcherService.ListLiveAdTagDetails`  
`google.cloud.video.stitcher.v1.VideoStitcherService.ListSlates`  
`google.cloud.video.stitcher.v1.VideoStitcherService.ListVodAdTagDetails`  
`google.cloud.video.stitcher.v1.VideoStitcherService.ListVodStitchDetails`  
`DATA_WRITE` | `google.cloud.video.stitcher.v1.VideoStitcherService.CreateCdnKey`  
`google.cloud.video.stitcher.v1.VideoStitcherService.CreateSlate`  
`google.cloud.video.stitcher.v1.VideoStitcherService.DeleteCdnKey`  
`google.cloud.video.stitcher.v1.VideoStitcherService.DeleteSlate`  
`google.cloud.video.stitcher.v1.VideoStitcherService.UpdateCdnKey`  
`google.cloud.video.stitcher.v1.VideoStitcherService.UpdateSlate`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Video Stitcher API.

### `google.cloud.video.stitcher.v1.VideoStitcherService`

The following audit logs are associated with methods belonging to `google.cloud.video.stitcher.v1.VideoStitcherService`.

#### `CreateCdnKey`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.CreateCdnKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.cdnKeys.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.CreateCdnKey" `  




#### `CreateLiveConfig`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.CreateLiveConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `videostitcher.liveConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.CreateLiveConfig" `  




#### `CreateSlate`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.CreateSlate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.slates.create - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.CreateSlate" `  




#### `CreateVodConfig`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.CreateVodConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `videostitcher.vodConfigs.create - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.CreateVodConfig" `  




#### `DeleteCdnKey`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.DeleteCdnKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.cdnKeys.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.DeleteCdnKey" `  




#### `DeleteLiveConfig`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.DeleteLiveConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `videostitcher.liveConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.DeleteLiveConfig" `  




#### `DeleteSlate`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.DeleteSlate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.slates.delete - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.DeleteSlate" `  




#### `DeleteVodConfig`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.DeleteVodConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `videostitcher.vodConfigs.delete - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.DeleteVodConfig" `  




#### `GetCdnKey`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetCdnKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.cdnKeys.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetCdnKey" `  




#### `GetLiveAdTagDetail`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveAdTagDetail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.liveAdTagDetails.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveAdTagDetail" `  




#### `GetLiveConfig`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.liveConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveConfig" `  




#### `GetLiveSession`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.liveSessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetLiveSession" `  




#### `GetSlate`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetSlate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.slates.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetSlate" `  




#### `GetVodAdTagDetail`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetVodAdTagDetail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.vodAdTagDetails.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetVodAdTagDetail" `  




#### `GetVodConfig`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetVodConfig`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.vodConfigs.get - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetVodConfig" `  




#### `GetVodSession`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetVodSession`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.vodSessions.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetVodSession" `  




#### `GetVodStitchDetail`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.GetVodStitchDetail`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.vodStitchDetails.get - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.GetVodStitchDetail" `  




#### `ListCdnKeys`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.ListCdnKeys`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.cdnKeys.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.ListCdnKeys" `  




#### `ListLiveAdTagDetails`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.ListLiveAdTagDetails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.liveAdTagDetails.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.ListLiveAdTagDetails" `  




#### `ListLiveConfigs`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.ListLiveConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.liveConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.ListLiveConfigs" `  




#### `ListSlates`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.ListSlates`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.slates.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.ListSlates" `  




#### `ListVodAdTagDetails`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.ListVodAdTagDetails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.vodAdTagDetails.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.ListVodAdTagDetails" `  




#### `ListVodConfigs`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.ListVodConfigs`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.vodConfigs.list - ADMIN_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.ListVodConfigs" `  




#### `ListVodStitchDetails`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.ListVodStitchDetails`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.vodStitchDetails.list - DATA_READ`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.ListVodStitchDetails" `  




#### `UpdateCdnKey`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.UpdateCdnKey`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.cdnKeys.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.UpdateCdnKey" `  




#### `UpdateLiveConfig`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.UpdateLiveConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `videostitcher.liveConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.UpdateLiveConfig" `  




#### `UpdateSlate`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.UpdateSlate`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `videostitcher.slates.update - DATA_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.UpdateSlate" `  




#### `UpdateVodConfig`

  * **Method** : `google.cloud.video.stitcher.v1.VideoStitcherService.UpdateVodConfig`  

  * **Audit log type** : [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)  

  * **Permissions** : 
    * `videostitcher.vodConfigs.update - ADMIN_WRITE`
  * **Method is a long-running or streaming operation** : [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)   

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.video.stitcher.v1.VideoStitcherService.UpdateVodConfig" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.video.stitcher.v1.VideoStitcherService.CreateLiveSession`
  * `google.cloud.video.stitcher.v1.VideoStitcherService.CreateVodSession`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
