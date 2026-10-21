---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/describe/
title: gcloud network-security mirroring-endpoint-group-associations describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:29.359475+00:00
---

# gcloud network-security mirroring-endpoint-group-associations describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-security mirroring-endpoint-group-associations describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-security mirroring-endpoint-group-associations describe - describe a Mirroring Endpoint Group Association 
SYNOPSIS
    

`gcloud network-security mirroring-endpoint-group-associations describe` (`MIRRORING_ENDPOINT_GROUP_ASSOCIATION` : `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe a mirroring endpoint group association. 

For more examples, refer to the EXAMPLES section below. 

EXAMPLES
     To get a description of a mirroring endpoint group association called `my-association` in project `my-project` and location `global`, run: 

$ [gcloud network-security mirroring-endpoint-group-associations](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations) \
    
    
    describe my-association --project=my-project --location=global

OR 

$ [gcloud network-security mirroring-endpoint-group-associations](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-endpoint-group-associations) \
    
    
    describe \
    projects/my-project/locations/global/\
    mirroringEndpointGroupAssociations/my-association

POSITIONAL ARGUMENTS
    

Mirroring endpoint group association resource - Mirroring Endpoint Group Association. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `MIRRORING_ENDPOINT_GROUP_ASSOCIATION` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MIRRORING_ENDPOINT_GROUP_ASSOCIATION`
     ID of the mirroring endpoint group association or fully qualified identifier for the mirroring endpoint group association. 

To set the `endpoint-group-association-id` attribute: 

  * provide the argument `MIRRORING_ENDPOINT_GROUP_ASSOCIATION` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the mirroring endpoint group association. 

To set the `location` attribute: 

  * provide the argument `MIRRORING_ENDPOINT_GROUP_ASSOCIATION` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-security](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security) mirroring-endpoint-group-associations describe
    
    
    [gcloud beta network-security](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security) mirroring-endpoint-group-associations describe

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
