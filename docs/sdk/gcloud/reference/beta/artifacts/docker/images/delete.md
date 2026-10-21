---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/images/delete/
title: gcloud beta artifacts docker images delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:06.628913+00:00
---

# gcloud beta artifacts docker images delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/images/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts docker images delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts docker images delete - delete an Artifact Registry container image 
SYNOPSIS
    

`gcloud beta artifacts docker images delete` `IMAGE` [`--async`] [`--delete-tags`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` A valid container image has the format of 
    
    
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE

A valid container image that can be referenced by tag or digest, has the format of 
    
    
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest

This command can fail for the following reasons: 

  * Trying to delete an image by digest when the image is still tagged. Add \--delete-tags to delete the digest and the tags. 
  * Trying to delete an image by tag when the image has other tags. Add \--delete-tags to delete all tags. 
  * A valid repository format was not provided. 
  * The specified image does not exist. 
  * The active account does not have permission to delete images. 


EXAMPLES
     To delete image `busy-box` in `us-west1` and all of its digests and tags: 
    
    
    gcloud beta artifacts docker images delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box

To delete image digest `abcxyz` under image `busy-box`: 
    
    
    gcloud beta artifacts docker images delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz

To delete image digest `abcxyz` under image `busy-box` while there're other tags associate with the digest: 
    
    
    gcloud beta artifacts docker images delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box@sha256:abcxyz --delete-tags

To delete an image digest and its only tag `my-tag` under image `busy-box`: 
    
    
    gcloud beta artifacts docker images delete us-west1-docker.pkg.dev/my-project/my-repository/busy-box:my-tag

POSITIONAL ARGUMENTS
    

`IMAGE`
     A container image. 

A valid container image has the format of LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE 

A valid container image that can be referenced by tag or digest, has the format of LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE:tag LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE@sha256:digest 

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--delete-tags`
     If specified, all tags associated with the image are deleted. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud artifacts docker images delete](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/delete)
    
    
    [gcloud alpha artifacts docker images delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/images/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
