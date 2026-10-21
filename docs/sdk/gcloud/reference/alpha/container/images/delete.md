---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/images/delete/
title: gcloud alpha container images delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:57:51.853222+00:00
---

# gcloud alpha container images delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/images/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container images delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container images delete - delete existing images 
SYNOPSIS
    

`gcloud alpha container images delete` `IMAGE_NAME` [`IMAGE_NAME` …] [`--force-delete-tags`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The container images delete command deletes the specified image from the registry. All associated tags are also deleted. 
EXAMPLES
     Deletes the image as long as there aren't additional, unspecified tags referencing it: 
    
    
    gcloud alpha container images delete <IMAGE_NAME>

Deletes the image (and tags) from the input IMAGE_NAME: 
    
    
    gcloud alpha container images delete <IMAGE_NAME> --force-delete-tags

Deletes the image (and tags) from the input IMAGE_NAME, without additional prompting: 
    
    
    gcloud alpha container images delete <IMAGE_NAME> --force-delete-tags --quiet

To easily identify and delete untagged images in a project, first filter digests that lack tags: 
    
    
    [gcloud container images list-tags](https://docs.cloud.google.com/sdk/gcloud/reference/container/images/list-tags) [HOSTNAME]/[PROJECT-ID]/[IMAGE] --filter='-tags:*' --format="get(digest)" --limit=$BIG_NUMBER

Then, delete these tagless images without prompting by running: 
    
    
    gcloud alpha container images delete [HOSTNAME]/[PROJECT-ID]/[IMAGE]@DIGEST --quiet

POSITIONAL ARGUMENTS
    

`IMAGE_NAME` [`IMAGE_NAME` …]
     The fully qualified name(s) of image(s) to delete. The name(s) should be formatted as *.gcr.io/PROJECT_ID/IMAGE_PATH@sha256:DIGEST or *.gcr.io/PROJECT_ID/IMAGE_PATH:TAG. 
FLAGS
    

`--force-delete-tags`
     If there are tags pointing to an image to be deleted then they must all be specified explicitly, or this flag must be specified, for the command to succeed. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container images delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/images/delete)
    
    
    [gcloud beta container images delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/images/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
