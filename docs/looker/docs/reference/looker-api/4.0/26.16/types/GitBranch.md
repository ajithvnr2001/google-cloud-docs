---
url: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/GitBranch/
title: GitBranch \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:15.061282+00:00
---

# GitBranch  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/GitBranch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  GitBranch Stay organized with collections  Save and categorize content based on your preferences. 

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

## Related Methods

  * [Project/git_branch](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Project/git_branch "Project/git_branch")
  * [Project/create_git_branch](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Project/create_git_branch "Project/create_git_branch")
  * [Project/update_git_branch](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Project/update_git_branch "Project/update_git_branch")
  * [Project/find_git_branch](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/methods/Project/find_git_branch "Project/find_git_branch")



## Related Types

  * [ProjectWorkspace](https://docs.cloud.google.com/looker/docs/reference/looker-api/4.0/26.16/types/ProjectWorkspace "ProjectWorkspace")



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
