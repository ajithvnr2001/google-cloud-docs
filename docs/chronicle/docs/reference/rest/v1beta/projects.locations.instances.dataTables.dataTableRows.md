---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows
title: REST Resource: projects.locations.instances.dataTables.dataTableRows \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:06.169384+00:00
---

# REST Resource: projects.locations.instances.dataTables.dataTableRows  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.dataTables.dataTableRows Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DataTableRow
    * JSON representation
  * Methods



## Resource: DataTableRow

DataTableRow represents a single row in a data table.

JSON representation  
---  
      
    
    {
      "name": string,
      "values": [
        string
      ],
      "createTime": string,
      "updateTime": string,
      "rowTimeToLive": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the data table Format: projects/{project}/locations/{location}/instances/{instance}/dataTables/{dataTable}/dataTableRows/{dataTableRow}  
`values[]` |  `string` Required. All column values for a single row. The values should be in the same order as the columns of the data tables.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. DataTableRow create timeUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. DataTableRow update timeUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rowTimeToLive` |  `string` Optional. User-provided TTL of the data table row.  
  
## Methods  
  
---  
  
### `[bulkCreate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkCreate)`

|  Create data table rows in bulk.  
  
### `[bulkCreateAsync](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkCreateAsync)`

|  Create data table rows in bulk asynchronously.  
  
### `[bulkDelete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkDelete)`

|  Delete data table rows in bulk.  
  
### `[bulkDeleteAsync](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkDeleteAsync)`

|  Delete data table rows in bulk asynchronously.  
  
### `[bulkGet](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkGet)`

|  Get data table rows in bulk.  
  
### `[bulkReplace](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkReplace)`

|  Replace all existing data table rows with new data table rows.  
  
### `[bulkReplaceAsync](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkReplaceAsync)`

|  Replace all existing data table rows with new data table rows asynchronously.  
  
### `[bulkUpdate](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkUpdate)`

|  Update data table rows in bulk.  
  
### `[bulkUpdateAsync](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/bulkUpdateAsync)`

|  Update data table rows in bulk asynchronously.  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/create)`

|  Create a new data table row.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/delete)`

|  Delete data table row.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/get)`

|  Get data table row  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/list)`

|  List data table rows.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.dataTables.dataTableRows/patch)`

|  Update data table row  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
