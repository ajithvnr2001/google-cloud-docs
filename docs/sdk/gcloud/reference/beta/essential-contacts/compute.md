---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/essential-contacts/compute/
title: gcloud beta essential-contacts compute \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:26:43.830802+00:00
---

# gcloud beta essential-contacts compute  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/essential-contacts/compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta essential-contacts compute Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta essential-contacts compute - compute the essential contacts that are subscribed to the specified notification categories for a resource 
SYNOPSIS
    

`gcloud beta essential-contacts compute` `--notification-categories`=[`NOTIFICATION_CATEGORIES`,…] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command will return the contacts subscribed to any of the notification categories that have been set on the requested resource or any of its ancestors. 
EXAMPLES
     To compute contacts subscribed to the technical category for the current project, run: 
    
    
    gcloud beta essential-contacts compute --notification-categories=technical

To compute contacts subscribed to the product-updates or billing categories for the folder with id ``123``, run: 
    
    
    gcloud beta essential-contacts compute --notification-categories=product-updates,billing --folder=123

To compute contacts subscribed to the legal category for the organization with id ``456``, run: 
    
    
    gcloud beta essential-contacts compute --notification-categories=legal --organization=456

REQUIRED FLAGS
    

`--notification-categories`=[`NOTIFICATION_CATEGORIES`,…]
     list of notification categories contact is subscribed to. `NOTIFICATION_CATEGORIES` must be one of: `all`, `billing`, `legal`, `notification-category-unspecified`, `product-updates`, `security`, `suspension`, `technical`, `technical-incidents`. 
FLAGS
    

At most one of these can be specified: 

`--folder`=`FOLDER`
     folder number where contacts are set. If neither --project, --folder, nor \--organization are provided then the config property [core/project] will be used as the resource. 
`--organization`=`ORGANIZATION`
     organization number where contacts are set. If neither --project, --folder, nor \--organization are provided then the config property [core/project] will be used as the resource. 
`--project`=`PROJECT`
     project number or id where contacts are set. If neither --project, --folder, nor \--organization are provided then the config property [core/project] will be used as the resource. 
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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud essential-contacts compute](https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts/compute)
    
    
    [gcloud alpha essential-contacts compute](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/essential-contacts/compute)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
