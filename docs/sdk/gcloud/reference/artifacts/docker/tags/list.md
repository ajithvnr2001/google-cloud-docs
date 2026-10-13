---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list/
title: gcloud artifacts docker tags list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:09.050811+00:00
---

# gcloud artifacts docker tags list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/tags/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts docker tags list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts docker tags list - list all tags associated with a container image in Artifact Registry 
SYNOPSIS
    

`gcloud artifacts docker tags list` [`IMAGE_PATH`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     A valid Docker top layer image has the format of 
    
    
    [<location>-]docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH

A valid container image can be referenced by tag or digest, has the format of 
    
    
    [<location>-]docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH:tag
    [<location>-]docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH@sha256:digest

To specify the maximum number of repositories to list, use the --limit flag. 

EXAMPLES
     To list all tags under the current project, repository, and location: 
    
    
    gcloud artifacts docker tags list

To list all tags under the `my-project`, `my-repository`, across all locations: 
    
    
    gcloud artifacts docker tags list docker.pkg.dev/my-project/my-repository

To list all tags in repository `my-repository` in `us-west1`: 
    
    
    gcloud artifacts docker tags list us-west1-docker.pkg.dev/my-project/my-repository

To list tags for image `busy-box` in `us-west1`: 
    
    
    gcloud artifacts docker tags list us-west1-docker.pkg.dev/my-project/my-repository/busy-box

POSITIONAL ARGUMENTS
    

[`IMAGE_PATH`]
     An Artifact Registry repository or a container image. If not specified, default config values are used. 

A valid docker repository has the format of LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID 

A valid image has the format of LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY-ID/IMAGE_PATH 

LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha artifacts docker tags list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/artifacts/docker/tags/list)
    
    
    [gcloud beta artifacts docker tags list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/tags/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
