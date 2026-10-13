---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DataSourceSchema/
title: DataSourceSchema \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:22:33.538236+00:00
---

# DataSourceSchema  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DataSourceSchema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  DataSourceSchema Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

fields

[Field](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Field)[] 

Expand Field definition... 

name

_lock_

string 

The name of the field.

type

_lock_

string 

The type of the field.

description

_lock_

string 

A brief description of the field.

mode

_lock_

string 

The mode of the field (e.g., NULLABLE, REPEATED).

synonyms

string[] 

tags

string[] 

displayName

_lock_

string 

Field displayName.

subfields

any[] 

category

_lock_

string 

Field category.

valueFormat

_lock_

string 

Looker only. Value format of the field.

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

[DataFilter](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DataFilter)[] 

Expand DataFilter definition... 

field

_lock_

string 

The field to filter on.

value

_lock_

string 

The default value used for this filter.

type

_lock_

string 

The type of filter present on a datasource.

## Related Types

  * [DataResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DataResult "DataResult")
  * [BigQueryJob](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/BigQueryJob "BigQueryJob")
  * [BigQueryTableReference](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/BigQueryTableReference "BigQueryTableReference")
  * [LookerExploreReference](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookerExploreReference "LookerExploreReference")
  * [Datasource](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Datasource "Datasource")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
