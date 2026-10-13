---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CIContentValidatorResult/
title: CIContentValidatorResult \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:43.682962+00:00
---

# CIContentValidatorResult  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CIContentValidatorResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  CIContentValidatorResult Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.12 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

Datatype

Description

(object)

object 

name

string 

Name of the validator (content)

incremental

boolean 

Whether the validation was incremental

status

string 

Status of the validation (unknown, failed, passed, skipped, errored, cancelled, queued, running)

tested

[CIContentValidatorTestedExplore](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CIContentValidatorTestedExplore)[] 

Expand CIContentValidatorTestedExplore definition... 

model

string 

LookML model that was tested

explore

string 

LookML Explore that was tested

status

string 

Status of the validation (unknown, failed, passed, skipped, errored, cancelled, queued, running)

skip_reason

string 

Reason the validation was skipped

error_count

integer 

Total number of failed content validations

errors

[CIContentValidatorErrorItem](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CIContentValidatorErrorItem)[] 

Expand CIContentValidatorErrorItem definition... 

content_error

[CIContentValidatorContentError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CIContentValidatorContentError)

Details of the content that failed validation

generic_error

[CIGenericError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CIGenericError)

Error that occurred when attempting to run validation

## Related Types

  * [CIRunResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.12/types/CIRunResult "CIRunResult")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
