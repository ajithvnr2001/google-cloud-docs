---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DataQuery/
title: DataQuery \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:17.533334+00:00
---

# DataQuery  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DataQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  DataQuery Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Datatype

Description

(object)

object 

question

_lock_

string 

A natural language question to answer.

name

_lock_

string 

A snake-case name for the query.

datasources

[Datasource](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Datasource)[] 

Expand Datasource definition... 

lookerExploreReference

_lock_

[LookerExploreReference](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/LookerExploreReference)

A reference to a Looker explore.

Expand LookerExploreReference definition... 

lookerInstanceUri

_lock_

string 

The base url of the Looker instance.

privateLookerInstanceInfo

_lock_

[PrivateLookerInstanceInfo](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/PrivateLookerInstanceInfo)

Private Looker instance info.

lookmlModel

_lock_

string 

Name of the LookML model.

explore

_lock_

string 

Name of the LookML Explore.

schema

_lock_

[DataSourceSchema](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DataSourceSchema)

The schema of the datasource.

schema

_lock_

[DataSourceSchema](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DataSourceSchema)

The schema of the datasource.

Expand DataSourceSchema definition... 

fields

[Field](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Field)[] 

description

_lock_

string 

A textual description of the table's content and purpose.

synonyms

string[] 

tags

string[] 

displayName

_lock_

string 

Table displayName.

filters

[DataFilter](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DataFilter)[] 

structSchema

_lock_

object 

A struct representation of the schema.

looker

_lock_

[Query](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/Query)

A query for retrieving data from a Looker explore.

Expand Query definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

model

string 

Model

view

string 

Explore Name

fields

string[] 

pivots

string[] 

fill_fields

string[] 

filters

object 

Filters will contain data pertaining to complex filters that do not contain "or" conditions. When "or" conditions are present, filter data will be found on the `filter_expression` property.

filter_expression

string 

Filter Expression

sorts

string[] 

limit

string 

Row limit. To download unlimited results, set the limit to -1 (negative one).

column_limit

string 

Column Limit

total

boolean 

Total

row_total

string 

Raw Total

subtotals

string[] 

vis_config

object 

Visualization configuration properties. These properties are typically opaque and differ based on the type of visualization used. There is no specified set of allowed keys. The values can be any type supported by JSON. A "type" key with a string value is often present, and is used by Looker to determine which visualization to present. Visualizations ignore unknown vis_config properties.

filter_config

object 

The filter_config represents the state of the filter UI on the explore page for a given query. When running a query via the Looker UI, this parameter takes precedence over "filters". When creating a query or modifying an existing query, "filter_config" should be set to null. Setting it to any other value could cause unexpected filtering behavior. The format should be considered opaque.

visible_ui_sections

string 

Visible UI Sections

slug

_lock_

string 

Slug

dynamic_fields

string 

Dynamic Fields

client_id

string 

Client Id: used to generate shortened explore URLs. If set by client, must be a unique 22 character alphanumeric string. Otherwise one will be generated.

share_url

_lock_

string 

Share Url

expanded_share_url

_lock_

string 

Expanded Share Url

url

_lock_

string 

Expanded Url

query_timezone

string 

Query Timezone

has_table_calculations

_lock_

boolean 

Has Table Calculations

## Related Types

  * [DataMessage](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/DataMessage "DataMessage")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
