---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update/
title: gcloud network-connectivity internal-ranges update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:52:26.060159+00:00
---

# gcloud network-connectivity internal-ranges update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-connectivity internal-ranges update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-connectivity internal-ranges update - update an internal range 
SYNOPSIS
    

`gcloud network-connectivity internal-ranges update` (`INTERNAL_RANGE` : `--region`=`REGION`) [`--async`] [`--description`=`DESCRIPTION`] [`--clear-labels` | `--labels`=[`KEY`=`VALUE`,…]] [`--clear-overlaps` | `--overlaps`=[`OVERLAPS`,…]] [`--ip-cidr-range`=`IP_CIDR_RANGE` | `--prefix-length`=`PREFIX_LENGTH`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update the details of an internal range. 
EXAMPLES
     Update ip-cidr-range of an internal range named ``my-range``: 
    
    
    gcloud network-connectivity internal-ranges update my-range --ip-cidr-range="192.168.0.0/24"

Extend an internal range named ``my-range`` to an address block of /24: 
    
    
    gcloud network-connectivity internal-ranges update my-range --prefix-length=24

POSITIONAL ARGUMENTS
    

Internal range resource - Name of the internal range to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `internal_range` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INTERNAL_RANGE`
     ID of the internal range or fully qualified identifier for the internal range. 

To set the `internal_range` attribute: 

  * provide the argument `internal_range` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     The location ID. To set the `region` attribute: 

  * provide the argument `internal_range` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * use default global location . 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the Internal Range 
At most one of these can be specified: 

`--clear-labels`
     Clear existing labels for the range. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs for the range being updated. 
At most one of these can be specified: 

`--clear-overlaps`
     Clear existing overlap fields for the range. 
`--overlaps`=[`OVERLAPS`,…]
     Overlap specifications for the range being updated. `OVERLAPS` must be one of: 

`overlap-existing-subnet-range`
     Allows for creation of internal ranges that overlap with existing subnets. 
`overlap-route-range`
     Allows for creation or existence of routes that have a more specific destination than the created range. 
At most one of these can be specified: 

`--ip-cidr-range`=`IP_CIDR_RANGE`
     IP range that this internal range defines. 
`--prefix-length`=`PREFIX_LENGTH`
     An alternative to ip-cidr-range. Can be set when trying to create a reservation that automatically finds a free range of the given size. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha network-connectivity internal-ranges update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-connectivity/internal-ranges/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
