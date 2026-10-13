---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessLabels
title: REST Resource: projects.locations.instances.dataAccessLabels \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:06.862015+00:00
---

# REST Resource: projects.locations.instances.dataAccessLabels  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessLabels

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.dataAccessLabels Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DataAccessLabel
    * JSON representation
  * Methods



## Resource: DataAccessLabel

A DataAccessLabel is a label on events to define user access to data.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "author": string,
      "lastEditor": string,
      "description": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "udmQuery": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` The unique resource name of the data access label.  
`displayName` |  `string` Output only. The short name displayed for the label as it appears on event data.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the data access label was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the data access label was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`author` |  `string` Output only. The user who created the data access label.  
`lastEditor` |  `string` Output only. The user who last updated the data access label.  
`description` |  `string` Optional. A description of the data access label for a human reader.  
Required. The definition of the data access label that determines which data gets tagged with this label. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`udmQuery` |  `string` A UDM query over event data.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessLabels/create)`

|  Creates a data access label.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessLabels/delete)`

|  Deletes a data access label.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessLabels/get)`

|  Gets a data access label.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessLabels/list)`

|  Lists all data access labels for the customer.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.dataAccessLabels/patch)`

|  Updates a data access label.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
