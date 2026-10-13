---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/get_continuous_integration_run/
title: Get a Continuous Integration run \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:16.198761+00:00
---

# Get a Continuous Integration run  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/get_continuous_integration_run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get a Continuous Integration run Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Gets a Continuous Integration run.

## Request

GET /projects/{project_id}/continuous_integration/runs/{run_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

project_id

string 

Project Id

run_id

string 

Run Id

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields

## Response

### 200: Continuous Integration run info

Datatype

Description

(object)

[CIRun](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIRun)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Public ID of the CI run

ci_suite_id

_lock_

string 

ID of the CI suite

project_id

_lock_

string 

ID of the project

status

string 

Status of the CI run

title

_lock_

string 

Title of the CI run

trigger_type

_lock_

string 

Trigger type of the CI run

user_id

_lock_

integer 

ID of the user that triggered the CI run

triggered_by_name

_lock_

string 

Name of user that triggered the CI run

execution_id

_lock_

string 

Execution ID of the CI run

result

[CIRunResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIRunResult)

Results of the CI run

Expand CIRunResult definition... 

sql_result

[CISqlValidatorResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CISqlValidatorResult)

Results of the SQL validation

Expand CISqlValidatorResult definition... 

name

string 

Name of the validator (sql)

incremental

boolean 

Whether the validation was incremental

status

string 

Status of the validation (unknown, failed, passed, skipped, errored, cancelled, queued, running)

tested

[CISqlValidatorTestedExplore](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CISqlValidatorTestedExplore)[] 

sql_error

[CIGenericError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIGenericError)

Errors that occurred when attempting SQL validation

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

assert_result

[CIAssertValidatorResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIAssertValidatorResult)

Results of the assert validation

Expand CIAssertValidatorResult definition... 

name

string 

Name of the validator (assert)

status

string 

Status of the validation (unknown, failed, passed, skipped, errored, cancelled, queued, running)

tested

[CIAssertValidatorTestedExplore](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIAssertValidatorTestedExplore)[] 

assert_error

[CIGenericError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIGenericError)

Errors that occurred when attempting assert validation

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

content_result

[CIContentValidatorResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIContentValidatorResult)

Results of the content validation

Expand CIContentValidatorResult definition... 

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

[CIContentValidatorTestedExplore](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIContentValidatorTestedExplore)[] 

content_error

[CIGenericError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIGenericError)

Errors that occurred when attempting content validation

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

lookml_result

[CILookMLValidatorResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CILookMLValidatorResult)

Results of the LookML validation

Expand CILookMLValidatorResult definition... 

name

string 

Name of the validator (lookml)

status

string 

Status of the validation (unknown, failed, passed, skipped, errored, cancelled, queued, running)

error_count

integer 

Total number of failed LookML validations

errors

[CILookMLValidatorErrorItem](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CILookMLValidatorErrorItem)[] 

lookml_error

[CIGenericError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIGenericError)

Errors that occurred when attempting LookML validation

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

style_result

[CIStyleValidatorResult](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIStyleValidatorResult)

Results of the style validation

Expand CIStyleValidatorResult definition... 

name

string 

Name of the validator (style)

incremental

boolean 

Whether the validation was incremental

status

string 

Status of the validation (unknown, failed, passed, skipped, errored, cancelled, queued, running)

error_count

integer 

Total number of failed style validations

errors

[CIStyleValidatorErrorItem](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIStyleValidatorErrorItem)[] 

style_error

[CIGenericError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIGenericError)

Errors that occurred when attempting style validation

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

generic_error

[CIGenericError](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIGenericError)

Errors that occurred when attempting validation

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

change_request_number

integer 

Change request number of the CI run

change_request_url

string 

Change request URL of the CI run

change_request_name

string 

Change request name of the CI run

change_request_commits_url

string 

Change request commits URL of the CI run

git_service_name

_lock_

string 

Git service name of the CI run

git_commit_ref

string 

Git commit ref of the CI run

git_branch_name

string 

Git branch name of the CI run

git_repository_name

string 

Git repository name of the CI run

git_target_branch_name

string 

Git target branch name of the CI run

git_status_url

string 

Git status URL of the CI run

git_target_url

string 

Git target URL of the CI run

dbt_cloud_git_branch_name

string 

Git branch name in dbt Cloud

dbt_cloud_git_commit_ref

string 

Git commit ref in dbt Cloud

dbt_cloud_git_repository_name

string 

Git repository name in dbt Cloud

created_at

_lock_

string 

Time and date that the CI run was created

started_at

_lock_

string 

Time and date that the CI run was started

finished_at

_lock_

string 

Time and date that the CI run was finished

retries

_lock_

integer 

Number of retries of the CI run

assigned_ci_user_id

_lock_

integer 

ID of the CI user assigned to the CI run

assigned_ci_user_at

_lock_

string 

Time and date that the CI user was assigned to the CI run

crashed_check_count

_lock_

integer 

Number of crashed checks of the CI run

run_url

_lock_

string 

URL of the CI run

user_attributes

[CIRunUserAttribute](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/CIRunUserAttribute)[] 

Expand CIRunUserAttribute definition... 

id

integer 

ID of the user attribute

name

string 

Name of the user attribute

value

string 

Value of the user attribute

project_imports

_lock_

object 

Map of upstream project names to the commit ref pinned for the CI run

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
