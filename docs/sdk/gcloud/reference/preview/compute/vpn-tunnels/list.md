---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/vpn-tunnels/list/
title: gcloud preview compute vpn-tunnels list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:06.824227+00:00
---

# gcloud preview compute vpn-tunnels list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/vpn-tunnels/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute vpn-tunnels list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute vpn-tunnels list - list Google Compute Engine VPN tunnels 
SYNOPSIS
    

`gcloud preview compute vpn-tunnels list` [`NAME` …] [`--regexp`=`REGEXP`, `-r` `REGEXP`] [`--regions`=`REGION`,[`REGION`,…]] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute vpn-tunnels list` displays all Google Compute Engine VPN tunnels in a project. 

By default, VPN tunnels from all regions are listed. The results can be narrowed down using a filter: `--filter="region:( REGION … )"`. 

EXAMPLES
     To list all VPN tunnels in a project in table form, run: 
    
    
    gcloud preview compute vpn-tunnels list

To list the URIs of all VPN tunnels in a project, run: 
    
    
    gcloud preview compute vpn-tunnels list --uri

To list all VPN tunnels in the ``us-central1`` and ``europe-west1`` regions, run: 
    
    
    gcloud preview compute vpn-tunnels list --filter="region:( us-central1 europe-west1 )"

POSITIONAL ARGUMENTS
    

[`NAME` …]
     (DEPRECATED) If provided, show details for the specified names and/or URIs of resources. 

Argument `NAME` is deprecated. Use `--filter="name=( 'NAME' … )"` instead. 

FLAGS
    

`--regexp`=`REGEXP`, `-r` `REGEXP`
     (DEPRECATED) Regular expression to filter the names of the results on. Any names that do not match the entire regular expression will be filtered out. 

Flag `--regexp` is deprecated. Use `--filter="name~'REGEXP'"` instead. 

`--regions`=`REGION`,[`REGION`,…]
     If provided, only resources from the given regions are queried. 
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
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute vpn-tunnels list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/list)
    
    
    [gcloud alpha compute vpn-tunnels list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/vpn-tunnels/list)
    
    
    [gcloud beta compute vpn-tunnels list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/vpn-tunnels/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
