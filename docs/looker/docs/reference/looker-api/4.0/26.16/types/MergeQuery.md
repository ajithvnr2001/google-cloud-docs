---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/MergeQuery/
title: MergeQuery \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:35:13.983632+00:00
---

# MergeQuery  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/MergeQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  MergeQuery Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

can

_lock_

object 

Operations the current user is able to perform on this object

column_limit

string 

Column Limit

dynamic_fields

string 

Dynamic Fields

id

_lock_

string 

Unique Id

pivots

string[] 

result_maker_id

_lock_

string 

Unique to get results

sorts

string[] 

source_queries

[MergeQuerySourceQuery](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/MergeQuerySourceQuery)[] 

Expand MergeQuerySourceQuery definition... 

merge_fields

[MergeFields](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/MergeFields)[] 

Expand MergeFields definition... 

field_name

string 

Field name to map onto in the merged results

source_field_name

string 

Field name from the source query

name

string 

Display name

query_id

string 

Id of the query to merge

query_slug

string 

Slug of the query to merge

total

boolean 

Total

limit

string 

Limit

vis_config

object 

Visualization Config

## Related Methods

  * [Query/merge_query](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Query/merge_query "Query/merge_query")
  * [Query/create_merge_query](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Query/create_merge_query "Query/create_merge_query")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
