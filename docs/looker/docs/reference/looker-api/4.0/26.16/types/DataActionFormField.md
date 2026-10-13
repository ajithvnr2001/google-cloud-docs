---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DataActionFormField/
title: DataActionFormField \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:36.877865+00:00
---

# DataActionFormField  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DataActionFormField/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  DataActionFormField Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

name

_lock_

string 

Name

label

_lock_

string 

Human-readable label

description

_lock_

string 

Description of field

type

_lock_

string 

Type of field.

default

_lock_

string 

Default value of the field.

oauth_url

_lock_

string 

The URL for an oauth link, if type is 'oauth_link'.

interactive

_lock_

boolean 

Whether or not a field supports interactive forms.

required

_lock_

boolean 

Whether or not the field is required. This is a user-interface hint. A user interface displaying this form should not submit it without a value for this field. The action server must also perform this validation.

options

[DataActionFormSelectOption](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DataActionFormSelectOption)[] 

Expand DataActionFormSelectOption definition... 

name

_lock_

string 

Name

label

_lock_

string 

Human-readable label

## Related Types

  * [DataActionForm](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/DataActionForm "DataActionForm")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
