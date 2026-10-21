---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/notifications/list/
title: gcloud scc notifications list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:05.926049+00:00
---

# gcloud scc notifications list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/notifications/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc notifications list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc notifications list - list Security Command Center notification configs 
SYNOPSIS
    

`gcloud scc notifications list` [`PARENT`] [`--location`=`LOCATION`; default="global"] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     List Security Command Center notification configs. 
    
    
    Notification Configs that are created with Security Command Center API V2
    and later include a `location` attribute. Include the `--location` flag to
    list Notification Configs with `location` attribute other than `global`.

EXAMPLES
     List notification configs from organization `123`
    
    
    gcloud scc notifications list 123
    gcloud scc notifications list organizations/123

List notification configs from folder `456`
    
    
    gcloud scc notifications list folders/456

List notification configs from project `789`
    
    
    gcloud scc notifications list projects/789

List notification configs from organization `123` and `location=eu`
    
    
    gcloud scc notifications list 123 --location=eu
    gcloud scc notifications list organizations/123 --location=locations/eu

POSITIONAL ARGUMENTS
    

Parent resource - parent organization, folder, or project in the Google Cloud resource hierarchy to be used for the `[gcloud scc](https://docs.cloud.google.com/sdk/gcloud/reference/scc)` command. Specify the argument as either [RESOURCE_TYPE/RESOURCE_ID] or [RESOURCE_ID], as shown in the preceding examples. This represents a Cloud resource. 
[`PARENT`]
     ID of the parent or fully qualified identifier for the parent. 

To set the `parent` attribute: 

  * provide the argument `parent` on the command line; 
  * Set the parent property in configuration using `gcloud config set scc/parent` if it is not specified in command line. 


FLAGS
    

`--location`=`LOCATION`; default="global"
     Required if either data residency is enabled or the `notificationConfig` resources were created by using the API v2. 

If data residency is enabled, specify the Security Command Center location in which the notifications are stored. 

If data residency is not enabled, including `/locations/```LOCATION´´ in the name or the `--location` flag in the command lists only the `notificationConfig` resources that were created by using the Security Command Center API v2 and the only valid location is `global`. 

At most one of these can be specified: 

`--folder`=`FOLDER`
     Folder where the notification config resides. Formatted as ``folders/456`` or just ``456``. 
`--organization`=`ORGANIZATION`
     Organization where the notification config resides. Formatted as ``organizations/123`` or just ``123``. 
`--project`=`PROJECT`
     Project (ID or number) where the notification config resides. Formatted as ``projects/789`` or just ``789``. 
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

API REFERENCE
     This command uses the Security Command Center API. For more information, see [Security Command Center API.](https://cloud.google.com/security-command-center/docs/reference/rest)
NOTES
     These variants are also available: 
    
    
    [gcloud alpha scc notifications list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/notifications/list)
    
    
    [gcloud beta scc notifications list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/scc/notifications/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
