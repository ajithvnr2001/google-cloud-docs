---
url: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list/
title: gcloud artifacts sbom list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:15.279216+00:00
---

# gcloud artifacts sbom list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/sbom/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud artifacts sbom list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud artifacts sbom list - list SBOM file references 
SYNOPSIS
    

`gcloud artifacts sbom list` [`--location`=`LOCATION`] [`--dependency`=`DEPENDENCY` | `--resource`=`RESOURCE` | `--resource-prefix`=`RESOURCE_PREFIX`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]; default=`"occ.create_time"`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     List SBOM file references. 
EXAMPLES
     To list SBOM file references: 
    
    
    gcloud artifacts sbom list

To list SBOM file references related to the image with the tag "us-east1-docker.pkg.dev/project/repo/my-image:1.0": 
    
    
    gcloud artifacts sbom list --resource="us-east1-docker.pkg.dev/project/repo/my-image:1.0"

To list SBOM file references related to the image with the digest "us-east1-docker.pkg.dev/project/repo/my-image@sha256:88b205d7995332e10e836514fbfd59ecaf8976fc15060cd66e85cdcebe7fb356": 
    
    
    gcloud artifacts sbom list --resource="us-east1-docker.pkg.dev/project/repo/my-image@sha256:88b205d7995332e10e836514fbfd59ecaf8976fc15060cd66e85cdcebe7fb356"

To list SBOM file references related to the images with the resource path prefix "us-east1-docker.pkg.dev/project/repo": 
    
    
    gcloud artifacts sbom list --resource-prefix="us-east1-docker.pkg.dev/project/repo"

To list SBOM file references generated when the images were pushed to Artifact Registry and related to the installed package dependency "perl": 
    
    
    gcloud artifacts sbom list --dependency="perl"

FLAGS
    

`--location`=`LOCATION`
     If specified, all requests to Artifact Analysis for occurrences will go to location specified 
At most one of these can be specified: 

`--dependency`=`DEPENDENCY`
     List SBOM file references generated when the images were pushed to Artifact Registry and related to the installed package dependency. See <https://cloud.google.com/container-analysis/docs/scanning-types> for supported packages. 
`--resource`=`RESOURCE`
     List SBOM file references related to the image resource uri. 
`--resource-prefix`=`RESOURCE_PREFIX`
     List SBOM file references related to the resource uri with the resource path prefix. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]; default=`"occ.create_time"`
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. The default is `occ.create_time`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
