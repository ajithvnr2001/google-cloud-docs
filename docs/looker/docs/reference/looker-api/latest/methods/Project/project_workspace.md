---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/project_workspace/
title: Get Project Workspace \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:00:20.498747+00:00
---

# Get Project Workspace  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Project/project_workspace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ API Reference ](https://docs.cloud.google.com/looker/docs/reference/available-apis)



Send feedback 

#  Get Project Workspace Stay organized with collections  Save and categorize content based on your preferences. 

Version 4.0.26.20 (latest) 

### Get Project Workspace

Returns information about the state of the project files in the currently selected workspace

## Request

GET /projects/{project_id}/current_workspace 

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

query

HTTP Query 

Expand HTTP Query definition... 

fields

string 

Requested fields

## Response

### 200: Project Workspace

Datatype

Description

(object)

[ProjectWorkspace](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/ProjectWorkspace)

can

_lock_

object 

Operations the current user is able to perform on this object

project_id

_lock_

string 

The id of the project

workspace_id

_lock_

string 

The id of the local workspace containing the project files

git_status

_lock_

string 

The status of the local git directory

git_head

_lock_

string 

Git head revision name

dependency_status

_lock_

string 

Status of the dependencies in your project. Valid values are: "lock_optional", "lock_required", "lock_error", "install_none".

git_branch

_lock_

[GitBranch](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/types/GitBranch)

GitBranch

Expand GitBranch definition... 

can

_lock_

object 

Operations the current user is able to perform on this object

name

string 

The short name on the local. Updating `name` results in `git checkout `

remote

_lock_

string 

The name of the remote

remote_name

_lock_

string 

The short name on the remote

error

_lock_

string 

Name of error

message

_lock_

string 

Message describing an error if present

owner_name

_lock_

string 

Name of the owner of a personal branch

readonly

_lock_

boolean 

Whether or not this branch is readonly

personal

_lock_

boolean 

Whether or not this branch is a personal branch - readonly for all developers except the owner

is_local

_lock_

boolean 

Whether or not a local ref exists for the branch

is_remote

_lock_

boolean 

Whether or not a remote ref exists for the branch

is_production

_lock_

boolean 

Whether or not this is the production branch

ahead_count

_lock_

integer 

Number of commits the local branch is ahead of the remote

behind_count

_lock_

integer 

Number of commits the local branch is behind the remote

commit_at

_lock_

integer 

UNIX timestamp at which this branch was last committed.

ref

string 

The resolved ref of this branch. Updating `ref` results in `git reset --hard ``.

remote_ref

_lock_

string 

The resolved ref of this branch remote.

lookml_type

_lock_

string 

The lookml syntax used by all files in this project

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
