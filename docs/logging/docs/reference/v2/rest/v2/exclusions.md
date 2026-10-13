---
url: https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/exclusions/
title: REST Resource: exclusions \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:37.314039+00:00
---

# REST Resource: exclusions  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/exclusions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  REST Resource: exclusions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: LogExclusion
    * JSON representation
  * Methods



## Resource: LogExclusion

Specifies a set of log entries that are filtered out by a sink. If your Google Cloud resource receives a large volume of log entries, you can use exclusions to reduce your chargeable logs. Note that exclusions on organization-level and folder-level sinks don't apply to child resources. Note also that you cannot modify the _Required sink or exclude logs from it.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "filter": string,
      "disabled": boolean,
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Optional. A client-assigned identifier, such as `"load-balancer-exclusion"`. Identifiers are limited to 100 characters and can include only letters, digits, underscores, hyphens, and periods. First character has to be alphanumeric.  
`description` |  `string` Optional. A description of this exclusion.  
`filter` |  `string` Required. An [advanced logs filter](https://docs.cloud.google.com/logging/docs/view/building-queries#queries-by-expression) that matches the log entries to be excluded. By using the [sample function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#sample), you can exclude less than 100% of the matching log entries.For example, the following query matches 99% of low-severity log entries from Google Cloud Storage buckets:`resource.type=gcs_bucket severity<ERROR sample(insertId, 0.99)`  
`disabled` |  `boolean` Optional. If set to True, then this exclusion is disabled and it does not exclude any log entries. You can `[update an exclusion](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/exclusions/patch#google.logging.v2.ConfigServiceV2.UpdateExclusion)` to change the value of this field.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of the exclusion.This field may not be present for older exclusions.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of the exclusion.This field may not be present for older exclusions.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/exclusions/create)`

|  Creates a new exclusion in the _Default sink in a specified parent resource.  
  
### `[delete](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/exclusions/delete)`

|  Deletes an exclusion in the _Default sink.  
  
### `[get](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/exclusions/get)`

|  Gets the description of an exclusion in the _Default sink.  
  
### `[list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/exclusions/list)`

|  Lists all the exclusions on the _Default sink in a parent resource.  
  
### `[patch](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/exclusions/patch)`

|  Changes one or more properties of an existing exclusion in the _Default sink.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-27 UTC."],[],[]] 
