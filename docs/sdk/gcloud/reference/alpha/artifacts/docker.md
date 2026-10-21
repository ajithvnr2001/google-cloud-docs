---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/
title: gcloud alpha artifacts docker \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:56:32.411999+00:00
---

# gcloud alpha artifacts docker  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha artifacts docker Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha artifacts docker - manage Artifact Registry container images and tags 
SYNOPSIS
    

`gcloud alpha artifacts docker` `GROUP` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` To list images under repository `my-repo`, project `my-project`, in `us-central1`: 
    
    
    [gcloud alpha artifacts docker images list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/list) us-central1-docker.pkg.dev/my-project/my-repo

To delete image `busy-box` in `us-west1` and all of its digests and tags: 
    
    
    [gcloud alpha artifacts docker images delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/delete)
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box

To add tag `my-tag` to image `busy-box` referenced by digest `abcxyz` in `us-west1`: 
    
    
    [gcloud alpha artifacts docker tags add](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/add)
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag

To delete tag `my-tag` from image `busy-box` in `us-west1`: 
    
    
    [gcloud alpha artifacts docker tags delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/delete)
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag

To list tags for image `busy-box` in `us-west1`: 
    
    
    [gcloud alpha artifacts docker tags list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/list)
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[images](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images)`
     `(ALPHA)` Manage Artifact Registry container images. 
`[tags](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags)`
     `(ALPHA)` Manage Artifact Registry container image tags. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud artifacts docker](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker)
    
    
    [gcloud beta artifacts docker](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
