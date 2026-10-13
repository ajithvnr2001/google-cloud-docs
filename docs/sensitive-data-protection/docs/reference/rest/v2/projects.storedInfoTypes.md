---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes
title: REST Resource: projects.storedInfoTypes \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:41.301031+00:00
---

# REST Resource: projects.storedInfoTypes  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.storedInfoTypes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: StoredInfoType
    * JSON representation
  * Methods



## Resource: StoredInfoType

StoredInfoType resource message that contains information about the current version and any pending updates.

JSON representation  
---  
      
    
    {
      "name": string,
      "currentVersion": {
        object ([StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeVersion))
      },
      "pendingVersions": [
        {
          object ([StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeVersion))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name.  
`currentVersion` |  `object (`[StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeVersion)`)` Current version of the stored info type.  
`pendingVersions[]` |  `object (`[StoredInfoTypeVersion](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes#StoredInfoType.StoredInfoTypeVersion)`)` Pending versions of the stored info type. Empty if no versions are pending.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/create)`

|  Creates a pre-built stored infoType to be used for inspection.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/delete)`

|  Deletes a stored infoType.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/get)`

|  Gets a stored infoType.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/list)`

|  Lists stored infoTypes.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/patch)`

|  Updates the stored infoType by creating a new version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
