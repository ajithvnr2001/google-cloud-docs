---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/
title: gcloud artifacts docker images \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:08.317434+00:00
---

# gcloud artifacts docker images  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts docker images Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts docker images - manage Artifact Registry container images 
SYNOPSIS
    

`gcloud artifacts docker images` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     To list images under the current project, repository, and location: 
    
    
    [gcloud artifacts docker images list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list)

To list images under repository `my-repo`, project `my-project`, in `us-central1`: 
    
    
    [gcloud artifacts docker images list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list) us-central1-docker.pkg.dev/my-project/my-repo

To list images with tags, under repository `my-repo`, project `my-project` across all locations: 
    
    
    [gcloud artifacts docker images list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list) docker.pkg.dev/my-project/my-repo --include-tags

To list all images under image `busy-box`, in repository `my-repo`, project `my-project` across all locations: 
    
    
    [gcloud artifacts docker images list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list) docker.pkg.dev/my-project/my-repo/busy-box

To delete image `busy-box` in `us-west1` and all of its digests and tags: 
    
    
    [gcloud artifacts docker images delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete)
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box

To delete image digest `abcxyz` under image `busy-box`: 
    
    
    [gcloud artifacts docker images delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete)
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz

To delete image digest `abcxyz` under image `busy-box` while there're some other tags associate with the digest: 
    
    
    [gcloud artifacts docker images delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete)
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz
    --delete-tags

To delete an image digest and its only tag `my-tag` under image `busy-box`: 
    
    
    [gcloud artifacts docker images delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete)
    us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete)`
     Delete an Artifact Registry container image. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/describe)`
     Describe an Artifact Registry container image. 
`[get-operation](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/get-operation)`
     Get an On-Demand Scanning operation. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list)`
     List Artifact Registry container images. 
`[list-vulnerabilities](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities)`
     List On-Demand Scanning vulnerabilities. 
`[scan](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/scan)`
     Perform a vulnerability scan on a container image. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts docker images](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images)
    
    
    [gcloud beta artifacts docker images](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/images)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
