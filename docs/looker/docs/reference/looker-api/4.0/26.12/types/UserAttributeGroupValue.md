---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/UserAttributeGroupValue/
title: UserAttributeGroupValue \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:21.586900+00:00
---

# UserAttributeGroupValue  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/UserAttributeGroupValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  UserAttributeGroupValue Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

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

string 

Unique Id of this group-attribute relation

group_id

_lock_

string 

Id of group

user_attribute_id

_lock_

string 

Id of user attribute

value_is_hidden

_lock_

boolean 

If true, the "value" field will be null, because the attribute settings block access to this value

rank

_lock_

integer 

Precedence for resolving value for user

value

_lock_

string 

Value of user attribute for group

## Related Methods

  * [Group/update_user_attribute_group_value](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/methods/Group/update_user_attribute_group_value "Group/update_user_attribute_group_value")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
