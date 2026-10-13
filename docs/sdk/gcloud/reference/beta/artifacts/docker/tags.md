---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/
title: gcloud beta artifacts docker tags \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:34.924489+00:00
---

# gcloud beta artifacts docker tags  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts docker tags Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts docker tags - manage Artifact Registry container image tags 
SYNOPSIS
    

`gcloud beta artifacts docker tags` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` To add tag `my-tag` to image `busy-box` referenced by digest `abcxyz` in `us-west1`: 
    
    
    [gcloud beta artifacts docker tags add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/add) us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag

To add tag `my-tag` to image `busy-box` referenced by tag `latest` in `us-west1`: 
    
    
    [gcloud beta artifacts docker tags add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/add) us-west1-docker.pkg.dev/my-project/my-repository/busy-box:latest us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag

To delete tag `my-tag` from image `busy-box` in `us-west1`: 
    
    
    [gcloud beta artifacts docker tags delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/delete) us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag

To list all tags in repository `my-repository` in `us-west1`: 
    
    
    [gcloud beta artifacts docker tags list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/list) us-west1-docker.pkg.dev/my-project/my-repository

To list tags for image `busy-box` in `us-west1`: 
    
    
    [gcloud beta artifacts docker tags list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/list) us-west1-docker.pkg.dev/my-project/my-repository/busy-box

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/add)`
     `(BETA)` Add a tag to a container image in Artifact Registry. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/delete)`
     `(BETA)` Delete a tag from a container image in Artifact Registry. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/list)`
     `(BETA)` List all tags associated with a container image in Artifact Registry. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud artifacts docker tags](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags)
    
    
    [gcloud alpha artifacts docker tags](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
