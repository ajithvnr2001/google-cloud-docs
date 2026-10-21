---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/
title: gcloud beta artifacts repositories \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:04.975853+00:00
---

# gcloud beta artifacts repositories  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts repositories Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts repositories - manage Artifact Registry repositories 
SYNOPSIS
    

`gcloud beta artifacts repositories` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a repository with the name `my-repo`, run: 
    
    
    [gcloud beta artifacts repositories create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/create) my-repo

To delete a repository with the name `my-repo`, run: 
    
    
    [gcloud beta artifacts repositories delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/delete) my-repo

To describe a repository with the name `my-repo`, run: 
    
    
    [gcloud beta artifacts repositories describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/describe) my-repo

To list all Artifact Registry repositories, run: 
    
    
    [gcloud beta artifacts repositories list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/list)

To set an IAM policy for repository `my-repo`, run: 
    
    
    [gcloud beta artifacts repositories set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/set-iam-policy) my-repo policy.json

To get an IAM policy for repository `my-repo`, run: 
    
    
    [gcloud beta artifacts repositories get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/get-iam-policy) my-repo

To add an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' on repository `my-repo`, run: 
    
    
    [gcloud beta artifacts repositories add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/add-iam-policy-binding) my-repo --member='user:test-user@gmail.com' --role='roles/editor'

To remove an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' on repository `my-repo`, run: 
    
    
    [gcloud beta artifacts repositories remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/remove-iam-policy-binding) my-repo --member='user:test-user@gmail.com' --role='roles/editor'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/add-iam-policy-binding)`
     `(BETA)` Add an IAM policy binding to the IAM policy of an Artifact Registry repository. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/create)`
     `(BETA)` Create an Artifact Registry repository. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/delete)`
     `(BETA)` Delete an Artifact Registry repository. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/describe)`
     `(BETA)` Describe an Artifact Registry repository. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/get-iam-policy)`
     `(BETA)` Get IAM policy for an Artifact Registry repository. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/list)`
     `(BETA)` List repositories in the specified project. 
`[remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/remove-iam-policy-binding)`
     `(BETA)` Remove an IAM policy binding from the IAM policy of an Artifact Registry repository. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/set-iam-policy)`
     `(BETA)` Set the IAM policy for an Artifact Registry repository. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories/update)`
     `(BETA)` Update an Artifact Registry repository. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud artifacts repositories](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories)
    
    
    [gcloud alpha artifacts repositories](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
