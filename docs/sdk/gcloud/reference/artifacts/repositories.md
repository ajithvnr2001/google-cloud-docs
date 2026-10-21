---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/
title: gcloud artifacts repositories \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:12.417933+00:00
---

# gcloud artifacts repositories  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts repositories Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts repositories - manage Artifact Registry repositories 
SYNOPSIS
    

`gcloud artifacts repositories` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a repository with the name `my-repo`, run: 
    
    
    [gcloud artifacts repositories create](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create) my-repo

To delete a repository with the name `my-repo`, run: 
    
    
    [gcloud artifacts repositories delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/delete) my-repo

To describe a repository with the name `my-repo`, run: 
    
    
    [gcloud artifacts repositories describe](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/describe) my-repo

To list all Artifact Registry repositories, run: 
    
    
    [gcloud artifacts repositories list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/list)

To set an IAM policy for repository `my-repo`, run: 
    
    
    [gcloud artifacts repositories set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-iam-policy) my-repo policy.json

To get an IAM policy for repository `my-repo`, run: 
    
    
    [gcloud artifacts repositories get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/get-iam-policy) my-repo

To add an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' on repository `my-repo`, run: 
    
    
    [gcloud artifacts repositories add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/add-iam-policy-binding) my-repo --member='user:test-user@gmail.com' --role='roles/editor'

To remove an IAM policy binding for the role of 'roles/editor' for the user 'test-user@gmail.com' on repository `my-repo`, run: 
    
    
    [gcloud artifacts repositories remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/remove-iam-policy-binding) my-repo --member='user:test-user@gmail.com' --role='roles/editor'

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/add-iam-policy-binding)`
     Add an IAM policy binding to the IAM policy of an Artifact Registry repository. 
`[create](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create)`
     Create an Artifact Registry repository. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/delete)`
     Delete an Artifact Registry repository. 
`[delete-cleanup-policies](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/delete-cleanup-policies)`
     Delete cleanup policies from an Artifact Registry repository. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/describe)`
     Describe an Artifact Registry repository. 
`[get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/get-iam-policy)`
     Get IAM policy for an Artifact Registry repository. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/list)`
     List repositories in the specified project. 
`[list-cleanup-policies](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/list-cleanup-policies)`
     List cleanup policies of an Artifact Registry repository. 
`[remove-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/remove-iam-policy-binding)`
     Remove an IAM policy binding from the IAM policy of an Artifact Registry repository. 
`[set-cleanup-policies](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-cleanup-policies)`
     Set or update cleanup policies for an Artifact Registry repository. 
`[set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/set-iam-policy)`
     Set the IAM policy for an Artifact Registry repository. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/repositories/update)`
     Update an Artifact Registry repository. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts repositories](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/repositories)
    
    
    [gcloud beta artifacts repositories](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/repositories)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
