---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/GoldenQuery/
title: GoldenQuery \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:17.465407+00:00
---

# GoldenQuery  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/GoldenQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  GoldenQuery Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

integer 

Unique identifier for the golden question

query_id

_lock_

integer 

ID of the associated Looker Query resolved from the answer

questions

string[] 

answer

string 

The Explore URL representing the answer to the question

is_active

_lock_

boolean 

Whether this golden question should be utilized by the agent

created_by_user_id

_lock_

integer 

ID of the user who created the question

last_updated_by_user_id

_lock_

integer 

ID of the user who last updated the question

created_at

_lock_

string 

Time when the question was created

last_updated_at

_lock_

string 

Time when the question was last updated

explore

_lock_

string 

The explore name of the golden query

model

_lock_

string 

The LookML model name of the golden query

fields

string[] 

filters

_lock_

object 

Filters of the associated Looker Query

sorts

string[] 

limit

_lock_

string 

Limit of the associated Looker Query

client_id

_lock_

string 

Client ID of the associated Looker Query

pivots

string[] 

dynamic_fields

_lock_

string 

Dynamic fields of the associated Looker Query

## Related Methods

  * [ConversationalAnalytics/create_golden_query](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/ConversationalAnalytics/create_golden_query "ConversationalAnalytics/create_golden_query")
  * [ConversationalAnalytics/update_golden_query](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/ConversationalAnalytics/update_golden_query "ConversationalAnalytics/update_golden_query")



## Related Types

  * [Agent](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Agent "Agent")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
