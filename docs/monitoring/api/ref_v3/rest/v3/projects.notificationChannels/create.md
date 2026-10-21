---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/create/
title: Method: projects.notificationChannels.create \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:41:42.145803+00:00
---

# Method: projects.notificationChannels.create  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.notificationChannels.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service.

Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to notificationChannels.create, notificationChannels.delete and notificationChannels.patch.

### HTTP request

`POST https://monitoring.googleapis.com/v3/{name}/notificationChannels`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

This names the container into which the channel will be written, this does not name the newly created channel. The resulting channel's name will have a normalized version of this field as a prefix, but will add `/notificationChannels/[CHANNEL_ID]` to identify the channel. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.notificationChannels.create`

  
  
### Request body

The request body contains an instance of `[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels#NotificationChannel)`.

### Response body

If successful, the response body contains a newly created instance of `[NotificationChannel](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels#NotificationChannel)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
