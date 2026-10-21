---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/images/packages/diff/
title: gcloud alpha compute images packages diff \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:09:53.392241+00:00
---

# gcloud alpha compute images packages diff  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/images/packages/diff/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute images packages diff Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute images packages diff - displays the version differences of packages between two images 
SYNOPSIS
    

`gcloud alpha compute images packages diff` (`--base-image`=`BASE_IMAGE` : `--base-project`=`BASE_PROJECT`) (`--diff-image`=`DIFF_IMAGE` : `--diff-project`=`DIFF_PROJECT`) [`--show-added-packages`] [`--show-removed-packages`] [`--show-updated-packages`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Displays the version differences of packages between two images. 
REQUIRED FLAGS
    

Image resource - Name of the disk image as the diff base. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--base-image`=`BASE_IMAGE`
     ID of the image or fully qualified identifier for the image. 

To set the `name` attribute: 

  * provide the argument `--base-image` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--base-project`=`BASE_PROJECT`
     Project ID of the Google Cloud project for the image. 

To set the `project` attribute: 

  * provide the argument `--base-image` on the command line with a fully specified name; 
  * provide the argument `--base-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


Image resource - Name of the disk image to diff with base image. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--diff-image`=`DIFF_IMAGE`
     ID of the image or fully qualified identifier for the image. 

To set the `name` attribute: 

  * provide the argument `--diff-image` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--diff-project`=`DIFF_PROJECT`
     Project ID of the Google Cloud project for the image. 

To set the `project` attribute: 

  * provide the argument `--diff-image` on the command line with a fully specified name; 
  * provide the argument `--diff-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


FLAGS
    

`--show-added-packages`
     Show only the packages added to the diff image. 
`--show-removed-packages`
     Show only the packages removed from the base image. 
`--show-updated-packages`
     Show only the packages updated between two images. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
