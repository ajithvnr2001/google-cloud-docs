---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes
title: REST Resource: projects.locations.instances.dataAccessScopes \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:08.497892+00:00
---

# REST Resource: projects.locations.instances.dataAccessScopes  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.dataAccessScopes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DataAccessScope
    * JSON representation
  * DataAccessLabelReference
    * JSON representation
  * IngestionLabel
    * JSON representation
  * Methods



## Resource: DataAccessScope

A DataAccessScope is a boolean expression of data access labels used to restrict access to data for users.

JSON representation  
---  
      
    
    {
      "name": string,
      "allowedDataAccessLabels": [
        {
          object ([DataAccessLabelReference](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes#DataAccessLabelReference))
        }
      ],
      "deniedDataAccessLabels": [
        {
          object ([DataAccessLabelReference](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes#DataAccessLabelReference))
        }
      ],
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "author": string,
      "lastEditor": string,
      "description": string,
      "allowAll": boolean
    }  
  
Fields  
---  
`name` |  `string` The unique full name of the data access scope. The name should comply with <https://google.aip.dev/122> standards.  
`allowedDataAccessLabels[]` |  `object (`[DataAccessLabelReference](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes#DataAccessLabelReference)`)` Optional. The allowed labels for the scope. Either allowAll or allowedDataAccessLabels needs to be provided. When provided, there has to be at least one label allowed for the scope to be valid. The logical operator for evaluation of the allowed labels is OR. E.g.: A customer with scope with allowed labels A and B will be able to see data with labeled with A or B or (A and B).  
`deniedDataAccessLabels[]` |  `object (`[DataAccessLabelReference](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes#DataAccessLabelReference)`)` Optional. The denied labels for the scope. The logical operator for evaluation of the denied labels is AND. E.g.: A customer with scope with denied labels A and B won't be able to see data labeled with A and data labeled with B and data with labels A and B.  
`displayName` |  `string` Output only. The name to be used for display to customers of the data access scope.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the data access scope was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the data access scope was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`author` |  `string` Output only. The user who created the data access scope.  
`lastEditor` |  `string` Output only. The user who last updated the data access scope.  
`description` |  `string` Optional. A description of the data access scope for a human reader.  
`allowAll` |  `boolean` Optional. Whether or not the scope allows all labels, allowAll and allowedDataAccessLabels are mutually exclusive and one of them must be present. deniedDataAccessLabels can still be used along with allowAll. When combined with deniedDataAccessLabels, access will be granted to all data that doesn't have labels mentioned in deniedDataAccessLabels. E.g.: A customer with scope with denied labels A and B and allowAll will be able to see all data except data labeled with A and data labeled with B and data with labels A and B.  
  
## DataAccessLabelReference

Reference object to a data access label.

JSON representation  
---  
      
    
    {
      "displayName": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dataAccessLabel": string,
      "logType": string,
      "assetNamespace": string,
      "ingestionLabel": {
        object ([IngestionLabel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes#IngestionLabel))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The display name of the label. Data access label and log types's name will match the display name of the resource. The asset namespace will match the namespace itself. The ingestion key value pair will match the key of the tuple.  
The unique identifier for the label. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dataAccessLabel` |  `string` The name of the data access label.  
`logType` |  `string` The name of the log type.  
`assetNamespace` |  `string` The asset namespace configured in the forwarder of the customer's events.  
`ingestionLabel` |  `object (`[IngestionLabel](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes#IngestionLabel)`)` The ingestion label configured in the forwarder of the customer's events.  
End of mutually exclusive fields.  
  
## IngestionLabel

Representation of an ingestion label type.

JSON representation  
---  
      
    
    {
      "ingestionLabelKey": string,
      "ingestionLabelValue": string
    }  
  
Fields  
---  
`ingestionLabelKey` |  `string` Required. The key of the ingestion label. Always required.  
`ingestionLabelValue` |  `string` Optional. The value of the ingestion label. Optional. An object with no provided value and some key provided would match against the given key and ANY value.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes/create)`

|  Creates a data access scope.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes/delete)`

|  Deletes a data access scope.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes/get)`

|  Retrieves an existing data access scope.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes/list)`

|  Lists all existing data access scopes for the customer.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.dataAccessScopes/patch)`

|  Updates a data access scope.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
