---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/images/list-vulnerabilities/
title: gcloud beta artifacts docker images list-vulnerabilities \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:29:02.005551+00:00
---

# gcloud beta artifacts docker images list-vulnerabilities  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/artifacts/docker/images/list-vulnerabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta artifacts docker images list-vulnerabilities Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta artifacts docker images list-vulnerabilities - list On-Demand Scanning vulnerabilities 
SYNOPSIS
    

`gcloud beta artifacts docker images list-vulnerabilities` (`SCAN` : `--location`=`LOCATION`) [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` List On-Demand Scanning vulnerabilities from a completed scan. 
EXAMPLES
     The following command lists vulnerabilities from a completed On-Demand Scanning scan. 
    
    
    gcloud beta artifacts docker images list-vulnerabilities projects/my-project/locations/europe/scans/fff66882-0z55-4333-l619-z1z00df6040c

POSITIONAL ARGUMENTS
    

Scan resource - The scan resource to list vulnerabilites for. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `scan` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SCAN`
     ID of the scan or fully qualified identifier for the scan. 

To set the `scan` attribute: 

  * provide the argument `scan` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Cloud multi-region. 

To set the `location` attribute: 

  * provide the argument `scan` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


LIST COMMAND FLAGS
    

`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `ondemandscanning/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/container-analysis/docs/on-demand-scanning/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud artifacts docker images list-vulnerabilities](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/docker/images/list-vulnerabilities)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
