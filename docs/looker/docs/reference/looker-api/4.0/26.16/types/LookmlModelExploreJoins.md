---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreJoins/
title: LookmlModelExploreJoins \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:53.942307+00:00
---

# LookmlModelExploreJoins  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExploreJoins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  LookmlModelExploreJoins Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

name

_lock_

string 

Name of this join (and name of the view to join)

dependent_fields

string[] 

fields

string[] 

foreign_key

_lock_

string 

Name of the dimension in this explore whose value is in the primary key of the joined view

from

_lock_

string 

Name of view to join

outer_only

_lock_

boolean 

Specifies whether all queries must use an outer join

relationship

_lock_

string 

many_to_one, one_to_one, one_to_many, many_to_many

required_joins

string[] 

sql_foreign_key

_lock_

string 

SQL expression that produces a foreign key

sql_on

_lock_

string 

SQL ON expression describing the join condition

sql_table_name

_lock_

string 

SQL table name to join

type

_lock_

string 

The join type: left_outer, full_outer, inner, or cross

view_label

_lock_

string 

Label to display in UI selectors

## Related Types

  * [LookmlModelExplore](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/LookmlModelExplore "LookmlModelExplore")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
