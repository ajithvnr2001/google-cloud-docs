---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Project/update_repository_credential/
title: Create Repository Credential \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:47:24.471845+00:00
---

# Create Repository Credential  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Project/update_repository_credential/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Create Repository Credential Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.16 

**Note:** These docs are for an older version of the API. The API reference is also available for [ the latest version, 4.0.26.18 ](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest). 

### Configure Repository Credential for a remote dependency

Admin required.

`root_project_id` is required. `credential_id` is required.

## Request

PUT /projects/{root_project_id}/credential/{credential_id} 

Datatype

Description

Request

HTTP Request 

path

HTTP Path 

Expand HTTP Path definition... 

root_project_id

string 

Root Project Id

credential_id

string 

Credential Id

body

HTTP Body 

Expand HTTP Body definition... 

body

[RepositoryCredential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/RepositoryCredential)

Remote Project Information

Expand RepositoryCredential definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

root_project_id

_lock_

string 

Root project Id

remote_url

_lock_

string 

Git remote repository url

git_username

string 

Git username for HTTPS authentication.

git_password

string 

(Write-Only) Git password for HTTPS authentication.

ssh_public_key

string 

Public deploy key for SSH authentication.

is_configured

_lock_

boolean 

Whether the credentials have been configured for the Git Repository.

## Response

### 200: Repository Credential

Datatype

Description

(object)

[RepositoryCredential](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/RepositoryCredential)

can

_lock_

object 

Operations the current user is able to perform on this object

id

_lock_

string 

Unique Id

root_project_id

_lock_

string 

Root project Id

remote_url

_lock_

string 

Git remote repository url

git_username

string 

Git username for HTTPS authentication.

git_password

string 

(Write-Only) Git password for HTTPS authentication.

ssh_public_key

string 

Public deploy key for SSH authentication.

is_configured

_lock_

boolean 

Whether the credentials have been configured for the Git Repository.

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

### 409: Resource Already Exists

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

### 422: Validation Error

Datatype

Description

(object)

[ValidationError](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ValidationError)

message

_lock_

string 

Error details

errors

[ValidationErrorDetail](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ValidationErrorDetail)[] 

Expand ValidationErrorDetail definition... 

field

_lock_

string 

Field with error

code

_lock_

string 

Error code

message

_lock_

string 

Error info message

documentation_url

_lock_

string 

Documentation link

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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
