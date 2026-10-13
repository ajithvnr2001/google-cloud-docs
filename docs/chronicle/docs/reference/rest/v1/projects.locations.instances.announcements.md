---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.announcements
title: REST Resource: projects.locations.instances.announcements \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:35.799555+00:00
---

# REST Resource: projects.locations.instances.announcements  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.announcements

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.announcements Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Announcement
    * JSON representation
  * Methods



## Resource: Announcement

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Announcements - Chronicle SOAR Announcements.

JSON representation  
---  
      
    
    {
      "name": string,
      "updateTime": string,
      "content": string,
      "expireTime": string,
      "title": string,
      "author": string,
      "lastAuthor": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the Announcement. Format: projects/{project}/locations/{location}/instances/{instance}/announcements/{announcement}  
`updateTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Last update time of the announcement.  
`content` |  `string` Required. The announcement content, limited to 500 characters.  
`expireTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The announcement expiration time, must be a future time.  
`title` |  `string` Required. The announcement title. The title must be at least 3 characters and limited to 100 characters.  
`author` |  `string` Output only. The user who created the announcement.  
`lastAuthor` |  `string` Output only. The last user who edited the announcement.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.announcements/create)`

|  Creates a new announcement.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.announcements/delete)`

|  Deletes an announcement.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.announcements/get)`

|  Gets a specific announcement.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.announcements/list)`

|  Lists announcements for a specific instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.announcements/patch)`

|  Updates an existing announcement.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
