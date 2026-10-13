---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Project/all_projects/
title: Get All Projects \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:06.020510+00:00
---

# Get All Projects  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Project/all_projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Get All Projects Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.20 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Get All Projects

Returns all projects visible to the current user

## Request

GET /projects 

Datatype

Description

Request

HTTP Request 

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields

## Response

### 200: Project

Datatype

Description

(array)

[Project](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Project)[] 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Project Id

name

string 

Project display name

uses_git

_lock_

boolean 

If true the project is configured with a git repository

is_git_dev_locked

_lock_

boolean 

If true, the project git repository is locked.

git_remote_url

string 

Git remote repository url

git_username

string 

Git username for HTTPS authentication. (For production only, if using user attributes.)

git_password

string 

(Write-Only) Git password for HTTPS authentication. (For production only, if using user attributes.)

git_production_branch_name

string 

Git production branch name. Defaults to master. Supported only in Looker 21.0 and higher.

use_git_cookie_auth

boolean 

If true, the project uses a git cookie for authentication.

git_username_user_attribute

string 

User attribute name for username in per-user HTTPS authentication.

git_password_user_attribute

string 

User attribute name for password in per-user HTTPS authentication.

git_service_name

string 

Name of the git service provider

git_application_server_http_port

integer 

Port that HTTP(S) application server is running on (for PRs, file browsing, etc.)

git_application_server_http_scheme

string 

Scheme that is running on application server (for PRs, file browsing, etc.)

deploy_secret

string 

(Write-Only) Optional secret token with which to authenticate requests to the webhook deploy endpoint. If not set, endpoint is unauthenticated.

unset_deploy_secret

boolean 

(Write-Only) When true, unsets the deploy secret to allow unauthenticated access to the webhook deploy endpoint.

pull_request_mode

string 

The git pull request policy for this project. Valid values are: "off", "links", "recommended", "required".

validation_required

boolean 

Validation policy: If true, the project must pass validation checks before project changes can be committed to the git repository

git_release_mgmt_enabled

boolean 

If true, advanced git release management is enabled for this project

allow_warnings

boolean 

Validation policy: If true, the project can be committed with warnings when `validation_required` is true. (`allow_warnings` does nothing if `validation_required` is false).

is_example

_lock_

boolean 

If true the project is an example project and cannot be modified

has_production_counterpart

_lock_

boolean 

If true the project has been pushed to production.

dependency_status

string 

Status of dependencies in your manifest & lockfile

### 400: Bad Request

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

### 403: Permission Denied

Datatype

Description

(object)

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

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

[Error](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/Error)

message

_lock_

string 

Error details

documentation_url

_lock_

string 

Documentation link

## Examples

### Ruby

[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/all_git_branches.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/all_git_branches.rb#L10 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/all_git_branches.rb")  
---  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/list_files_per_project.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/list_files_per_project.rb#L11 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/list_files_per_project.rb")  
[https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/validate_projects.rb ](https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/validate_projects.rb#L14 "https://github.com/looker-open-source/sdk-codegen/blob/main/examples/ruby/validate_projects.rb")  
  
### Kotlin

[https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt ](https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt#L430 "https://github.com/looker-open-source/sdk-codegen/blob/main/kotlin/src/test/TestMethods.kt")  
---  
  
### Swift

[https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift ](https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift#L327 "https://github.com/looker-open-source/sdk-codegen/blob/main/swift/looker/Tests/lookerTests/smokeTests.swift")  
---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
