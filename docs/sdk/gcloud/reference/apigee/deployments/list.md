---
url: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/list/
title: gcloud apigee deployments list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:10:43.001643+00:00
---

# gcloud apigee deployments list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/apigee/deployments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud apigee deployments list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud apigee deployments list - list Apigee API proxy deployments 
SYNOPSIS
    

`gcloud apigee deployments list` [`--api`=`API` `--environment`=`ENVIRONMENT` `--organization`=`ORGANIZATION` `--revision`=`REVISION`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     List Apigee API proxy deployments. 

`gcloud apigee deployments list` lists deployments of API proxies, optionally filtered by environment, proxy name, proxy revision, or a combination of these. 

EXAMPLES
     To list all deployments for the active Cloud Platform project, run: 
    
    
    gcloud apigee deployments list

To list all deployments in an Apigee organization called ``my-org``, run: 
    
    
    gcloud apigee deployments list --organization=my-org

To list all deployments of an API proxy called ``my-proxy`` in the active Cloud Platform project, run: 
    
    
    gcloud apigee deployments list --api=my-proxy

To list all deployments to the ``test`` environment of the active Cloud Platform project, formatted as a JSON array, run: 
    
    
    gcloud apigee deployments list --environment=test --format=json

To list all deployments of ``my-proxy`` to the ``test`` environment in an Apigee organization called ``my-org``, run: 
    
    
    gcloud apigee deployments list --organization=my-org --api=my-proxy --environment=test

FLAGS
    

Revision resource - API proxy revision and environment whose deployments should be listed. Providing a REVISION is only valid if API is also specified. If no REVISION is provided, all deployed revisions that match the other arguments will be included. The arguments in this group can be used to specify the attributes of this resource. 
`--api`=`API`
     The API proxy whose deployments should be listed. If not provided, all proxies will be listed. To get a list of existing API proxies, run `[gcloud apigee apis list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/apis/list)`. 

To set the `api` attribute: 

  * provide the argument `--revision` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--api` on the command line; 
  * leave the argument unspecified for it to be chosen automatically. 


`--environment`=`ENVIRONMENT`
     The environment whose deployments should be listed. If not provided, all environments will be listed. To get a list of available environments, run `[gcloud apigee environments list](https://docs.cloud.google.com/sdk/gcloud/reference/apigee/environments/list)`. 

To set the `environment` attribute: 

  * provide the argument `--revision` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--environment` on the command line; 
  * leave the argument unspecified for it to be chosen automatically. 


`--organization`=`ORGANIZATION`
     The organization whose deployments should be listed.If unspecified, the Cloud Platform project's associated organization will be used. 

To set the `organization` attribute: 

  * provide the argument `--revision` on the command line with a fully specified name; 
  * leave the argument unspecified for it to be chosen automatically with a fully specified name; 
  * provide the argument `--organization` on the command line; 
  * set the property [project] or provide the argument [--project] on the command line, using a Cloud Platform project with an associated Apigee organization. 


`--revision`=`REVISION`
     ID of the revision or fully qualified identifier for the revision. 

To set the `revision` attribute: 

  * provide the argument `--revision` on the command line; 
  * leave the argument unspecified for it to be chosen automatically. 


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
     These variants are also available: 
    
    
    [gcloud alpha apigee deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apigee/deployments/list)
    
    
    [gcloud beta apigee deployments list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/apigee/deployments/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
