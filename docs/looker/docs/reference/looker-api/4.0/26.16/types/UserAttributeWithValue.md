---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/UserAttributeWithValue/
title: UserAttributeWithValue \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:53.043433+00:00
---

# UserAttributeWithValue  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/UserAttributeWithValue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  UserAttributeWithValue Stay organized with collections  Save and categorize content based on your preferences. 

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

name

_lock_

string 

Name of user attribute

label

_lock_

string 

Human-friendly label for user attribute

rank

_lock_

integer 

Precedence for setting value on user (lowest wins)

value

string 

Value of attribute for user

user_id

_lock_

string 

Id of User

user_can_edit

_lock_

boolean 

Can the user set this value

value_is_hidden

_lock_

boolean 

If true, the "value" field will be null, because the attribute settings block access to this value

user_attribute_id

_lock_

string 

Id of User Attribute

source

_lock_

string 

How user got this value for this attribute

hidden_value_domain_whitelist

_lock_

string 

If this user attribute is hidden, allowed list of destinations to which it may be sent.

## Related Methods

  * [User/set_user_attribute_user_value](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/User/set_user_attribute_user_value "User/set_user_attribute_user_value")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
