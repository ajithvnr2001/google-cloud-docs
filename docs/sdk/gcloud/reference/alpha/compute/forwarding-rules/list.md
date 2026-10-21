---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/list/
title: gcloud alpha compute forwarding-rules list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:45:20.679120+00:00
---

# gcloud alpha compute forwarding-rules list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute forwarding-rules list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute forwarding-rules list - list Google Compute Engine forwarding rules 
SYNOPSIS
    

`gcloud alpha compute forwarding-rules list` [`NAME` …] [`--regexp`=`REGEXP`, `-r` `REGEXP`] [`--global` | `--regions`=[`REGION`,…]] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha compute forwarding-rules list` displays all Google Compute Engine forwarding rules in a project. 

By default, global forwarding rules and forwarding rules from all regions are listed. The results can be narrowed down by providing the ``\--global`` or ``\--regions`` flag. 

EXAMPLES
     To list all forwarding rules in a project in table form, run: 
    
    
    gcloud alpha compute forwarding-rules list

To list the URIs of all forwarding rules in a project, run: 
    
    
    gcloud alpha compute forwarding-rules list --uri

To list all global forwarding rules in a project, run: 
    
    
    gcloud alpha compute forwarding-rules list --global

To list all forwarding rules in the ``us-central1`` and ``europe-west1`` regions, given they are regional resources, run: 
    
    
    gcloud alpha compute forwarding-rules list --filter="region:( europe-west1 us-central1 )"

POSITIONAL ARGUMENTS
    

[`NAME` …]
     (DEPRECATED) If provided, show details for the specified names and/or URIs of resources. 

Argument `NAME` is deprecated. Use `--filter="name=( 'NAME' … )"` instead. 

FLAGS
    

`--regexp`=`REGEXP`, `-r` `REGEXP`
     (DEPRECATED) Regular expression to filter the names of the results on. Any names that do not match the entire regular expression will be filtered out. 

Flag `--regexp` is deprecated. Use `--filter="name~'REGEXP'"` instead. 

At most one of these can be specified: 

`--global`
     If provided, only global resources are shown. 
`--regions`=[`REGION`,…]
     If provided, only regional resources are shown. If arguments are provided, only resources from the given regions are shown. 
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
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute forwarding-rules list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/list)
    
    
    [gcloud beta compute forwarding-rules list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/forwarding-rules/list)
    
    
    [gcloud preview compute forwarding-rules list](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/forwarding-rules/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
