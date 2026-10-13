---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/search_lookml_dashboards/
title: Search LookML Dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:25:48.477931+00:00
---

# Search LookML Dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/search_lookml_dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Search LookML Dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Search LookML Dashboards

Returns an array of **LookML Dashboard** objects that match the specified search criteria. Note, this only returns LookML Dashboards in production.

If multiple search params are given and `filter_or` is FALSE or not specified, search params are combined in a logical AND operation. Only rows that match _all_ search param criteria will be returned.

If `filter_or` is TRUE, multiple search params are combined in a logical OR operation. Results will include rows that match **any** of the search criteria.

String search params use case-insensitive matching. String search params can contain `%` and '_' as SQL LIKE pattern match wildcard expressions. example="dan%" will match "danger" and "Danzig" but not "David" example="D_m%" will match "Damage" and "dump"

Integer search params can accept a single value or a comma separated list of values. The multiple values will be combined under a logical OR operation - results will match at least one of the given values.

Most search params can accept "IS NULL" and "NOT NULL" as special expressions to match or exclude (respectively) rows where the column is null.

Boolean search params accept only "true" and "false" as values.

**Note:** When searching and sorting by `title`, the search uses the `dashboard_name` defined in the LookML code, rather than the user-facing display title.

The parameters `limit`, and `offset` are recommended for fetching results in page-size chunks.

Get a **single LookML dashboard** by id with [dashboard_lookml()](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/dashboard_lookml)

## Request

GET /dashboards/lookml/search 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

folder_id

string 

Filter on a particular folder.

title

string 

Match LookML Dashboard title. Note: This matches on the dashboard_name defined in the LookML code, not the display title.

content_favorite_id

string 

Filter on a content favorite id.

fields

string 

Requested fields.

limit

integer 

Number of results to return. (used with offset and takes priority over page and per_page)

offset

integer 

Number of results to skip before returning any. (used with limit and takes priority over page and per_page)

sorts

string 

One or more fields to sort by. Sortable fields: [:title, :id, :folder_id, :content_favorite_id, :content_metadata_id, :certification_status]. Note: Sorting by title sorts by the dashboard_name defined in the LookML code, not the display title.

## Response

### 200: dashboards

Datatype

Description

(object)

[DashboardLookml](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DashboardLookml)

dashboard_id

_lock_

string 

Id of Dashboard

folder_id

string 

(Write-Only) Id of the folder

lookml

string 

lookml of UDD

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 404: Not Found

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 429: Too Many Requests

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
