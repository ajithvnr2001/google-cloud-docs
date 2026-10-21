---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels
title: REST Resource: projects.notificationChannels \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:47:39.230702+00:00
---

# REST Resource: projects.notificationChannels  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  REST Resource: projects.notificationChannels Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: NotificationChannel
    * JSON representation
  * VerificationStatus
  * Methods



## Resource: NotificationChannel

A `NotificationChannel` is a medium through which an alert is delivered when a policy violation is detected. Examples of channels include email, SMS, and third-party messaging applications. Fields containing sensitive information like authentication tokens or contact info are only partially populated on retrieval.

JSON representation  
---  
      
    
    {
      "type": string,
      "name": string,
      "displayName": string,
      "description": string,
      "labels": {
        string: string,
        ...
      },
      "userLabels": {
        string: string,
        ...
      },
      "verificationStatus": enum ([VerificationStatus](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels#VerificationStatus)),
      "enabled": boolean,
      "creationRecord": {
        object ([MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/MutationRecord))
      },
      "mutationRecords": [
        {
          object ([MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/MutationRecord))
        }
      ]
    }  
  
Fields  
---  
`type` |  `string` The type of the notification channel. This field matches the value of the `[NotificationChannelDescriptor.type](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors#NotificationChannelDescriptor.FIELDS.type)` field.  
`name` |  `string` Identifier. The full REST resource name for this channel. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
    

The `[CHANNEL_ID]` is automatically assigned by the server on creation.  
`displayName` |  `string` An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique name in order to make it easier to identify the channels in your project, though this is not enforced. The display name is limited to 512 Unicode characters.  
`description` |  `string` An optional human-readable description of this notification channel. This description may provide additional details, beyond the display name, for the channel. This may not exceed 1024 Unicode characters.  
`labels` |  `map (key: string, value: string)` Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the `[NotificationChannelDescriptor.labels](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors#NotificationChannelDescriptor.FIELDS.labels)` of the `NotificationChannelDescriptor` corresponding to the `type` field.  
`userLabels` |  `map (key: string, value: string)` User-supplied key/value data that does not need to conform to the corresponding `NotificationChannelDescriptor`'s schema, unlike the `labels` field. This field is intended to be used for organizing and identifying the `NotificationChannel` objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.  
`verificationStatus` |  `enum (`[VerificationStatus](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels#VerificationStatus)`)` Indicates whether this channel has been verified or not. On a `[`notificationChannels.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list#google.monitoring.v3.NotificationChannelService.ListNotificationChannels)` or `[`notificationChannels.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/get#google.monitoring.v3.NotificationChannelService.GetNotificationChannel)` operation, this field is expected to be populated.If the value is `UNVERIFIED`, then it indicates that the channel is non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel works.If the channel is neither `VERIFIED` nor `UNVERIFIED`, it implies that the channel is of a type that does not require verification or that this specific channel has been exempted from verification because it was created prior to verification being required for channels of this type.This field cannot be modified using a standard `[`notificationChannels.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/patch#google.monitoring.v3.NotificationChannelService.UpdateNotificationChannel)` operation. To change the value of this field, you must call `[`notificationChannels.verify`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/verify#google.monitoring.v3.NotificationChannelService.VerifyNotificationChannel)`.  
`enabled` |  `boolean` Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of notifications to a particular channel without removing the channel from all alerting policies that reference the channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the same set of alerting policies on the channel at some point in the future.  
`creationRecord` |  `object (`[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/MutationRecord)`)` Record of the creation of this channel.  
`mutationRecords[]` |  `object (`[MutationRecord](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/MutationRecord)`)` Records of the modification of this channel.  
  
## VerificationStatus

Indicates whether the channel has been verified or not. It is illegal to specify this field in a `[`notificationChannels.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/create#google.monitoring.v3.NotificationChannelService.CreateNotificationChannel)` or an `[`notificationChannels.patch`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/patch#google.monitoring.v3.NotificationChannelService.UpdateNotificationChannel)` operation.

Enums  
---  
`VERIFICATION_STATUS_UNSPECIFIED` | Sentinel value used to indicate that the state is unknown, omitted, or is not applicable (as in the case of channels that neither support nor require verification in order to function).  
`UNVERIFIED` | The channel has yet to be verified and requires verification to function. Note that this state also applies to the case where the verification process has been initiated by sending a verification code but where the verification code has not been submitted to complete the process.  
`VERIFIED` | It has been proven that notifications can be received on this notification channel and that someone on the project has access to messages that are delivered to that channel.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/create)`

|  Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service.  
  
### `[delete](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/delete)`

|  Deletes a notification channel.  
  
### `[get](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/get)`

|  Gets a single notification channel.  
  
### `[getVerificationCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/getVerificationCode)`

|  Requests a verification code for an already verified channel that can then be used in a call to VerifyNotificationChannel() on a different channel with an equivalent identity in the same or in a different project.  
  
### `[list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/list)`

|  Lists the notification channels that have been created for the project.  
  
### `[patch](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/patch)`

|  Updates a notification channel.  
  
### `[sendVerificationCode](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/sendVerificationCode)`

|  Causes a verification code to be delivered to the channel.  
  
### `[verify](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/verify)`

|  Verifies a `NotificationChannel` by proving receipt of the code delivered to the channel as a result of calling `SendNotificationChannelVerificationCode`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
