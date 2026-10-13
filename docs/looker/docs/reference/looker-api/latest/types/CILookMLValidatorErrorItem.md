---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CILookMLValidatorErrorItem/
title: CILookMLValidatorErrorItem \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:28.250924+00:00
---

# CILookMLValidatorErrorItem  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CILookMLValidatorErrorItem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  CILookMLValidatorErrorItem Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

Datatype

Description

(object)

object 

lookml_error

[CILookMLValidatorError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CILookMLValidatorError)

Details of the LookML that failed validation

Expand CILookMLValidatorError definition... 

type

string 

A URI reference that identifies the problem type

title

string 

Overview of the error

detail

string 

Detail of the error

status

string 

The HTTP status code for the problem

instance

string 

URI reference that identifies the specific occurrence of the problem

model

string 

LookML model that contains the error

explore

string 

LookML Explore that contains the error

field_name

string 

LookML field that caused the error

message

string 

Message returned by the LookML validator

severity

string 

Severity of the error (warning, error, fatal, info, success)

line_number

string 

Line number of the error in the LookML file

lookml_url

string 

URL to the LookML that caused the error

file_path

string 

IDE folder path to the LookML file that caused the error

generic_error

[CIGenericError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIGenericError)

Error that occurred when attempting to run validation

Expand CIGenericError definition... 

type

string 

A URI reference that identifies the problem type

title

string 

Overview of the error

detail

string 

Detail of the error

status

string 

The HTTP status code for the problem

instance

string 

URI reference that identifies the specific occurrence of the problem

## Related Types

  * [CILookMLValidatorResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CILookMLValidatorResult "CILookMLValidatorResult")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
