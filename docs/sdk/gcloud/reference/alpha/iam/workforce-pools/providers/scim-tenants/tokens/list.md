---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/providers/scim-tenants/tokens/list/
title: gcloud alpha iam workforce-pools providers scim-tenants tokens list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:08.229274+00:00
---

# gcloud alpha iam workforce-pools providers scim-tenants tokens list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/providers/scim-tenants/tokens/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iam workforce-pools providers scim-tenants tokens list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iam workforce-pools providers scim-tenants tokens list - list IAM workforce identity pool provider SCIM tenant tokens 
SYNOPSIS
    

`gcloud alpha iam workforce-pools providers scim-tenants tokens list` (`--scim-tenant`=`SCIM_TENANT` : `--location`=`LOCATION` `--provider`=`PROVIDER` `--workforce-pool`=`WORKFORCE_POOL`) [`--show-deleted`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List all SCIM tokens associated with a specific workforce identity pool provider SCIM tenant. 
EXAMPLES
     To list all SCIM tokens under tenant `my-tenant` provider `my-provider` in pool `my-pool` located in `global`: 
    
    
    [gcloud alpha iam workforce-pools providers scim-tenants tokens](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/providers/scim-tenants/tokens) list --location=global --workforce-pool=my-pool --provider=my-provider --scim-tenant=my-tenant

To list deleted SCIM tokens as well: 
    
    
    [gcloud alpha iam workforce-pools providers scim-tenants tokens](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/providers/scim-tenants/tokens) list --location=global --workforce-pool=my-pool --provider=my-provider --scim-tenant=my-tenant --show-deleted

REQUIRED FLAGS
    

Workforce pool provider scim tenant resource - The SCIM tenant to list tokens for. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`--scim-tenant`=`SCIM_TENANT`
     ID of the workforce pool provider scim tenant or fully qualified identifier for the workforce pool provider scim tenant. 

To set the `scim-tenant` attribute: 

  * provide the argument `--scim-tenant` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the workforce pool. 

To set the `location` attribute: 

  * provide the argument `--scim-tenant` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--provider`=`PROVIDER`
     The ID to use for the workforce pool provider, which becomes the final component of the resource name. This value must be unique within the workforce pool, 4-32 characters in length, and may contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `provider` attribute: 

  * provide the argument `--scim-tenant` on the command line with a fully specified name; 
  * provide the argument `--provider` on the command line. 


`--workforce-pool`=`WORKFORCE_POOL`
     The ID to use for the workforce pool, which becomes the final component of the resource name. This value must be a globally unique string of 6 to 63 lowercase letters, digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `workforce-pool` attribute: 

  * provide the argument `--scim-tenant` on the command line with a fully specified name; 
  * provide the argument `--workforce-pool` on the command line. 


FLAGS
    

`--show-deleted`
     Include soft-deleted tokens in the results. 
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
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud iam workforce-pools providers scim-tenants tokens list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/scim-tenants/tokens/list)
    
    
    [gcloud beta iam workforce-pools providers scim-tenants tokens list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/providers/scim-tenants/tokens/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
