---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployment-groups/describe/
title: gcloud network-security mirroring-deployment-groups describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:26.328212+00:00
---

# gcloud network-security mirroring-deployment-groups describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployment-groups/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-security mirroring-deployment-groups describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-security mirroring-deployment-groups describe - describe a Mirroring Deployment Group 
SYNOPSIS
    

`gcloud network-security mirroring-deployment-groups describe` (`MIRRORING_DEPLOYMENT_GROUP` : `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe a mirroring deployment group. 

For more examples, refer to the EXAMPLES section below. 

EXAMPLES
     To get a description of a mirroring deployment group called `my-deployment-group` in project ID `my-project`, run: 
    
    
    gcloud network-security mirroring-deployment-groups describe my-deployment-group --project=my-project --location=global

OR 
    
    
    gcloud network-security mirroring-deployment-groups describe projects/my-project/locations/global/mirroringDeploymentGroups/my-deployment-group

POSITIONAL ARGUMENTS
    

Mirroring deployment group resource - Mirroring Deployment Group. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `MIRRORING_DEPLOYMENT_GROUP` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MIRRORING_DEPLOYMENT_GROUP`
     ID of the mirroring deployment group or fully qualified identifier for the mirroring deployment group. 

To set the `deployment-group-id` attribute: 

  * provide the argument `MIRRORING_DEPLOYMENT_GROUP` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the mirroring deployment group. 

To set the `location` attribute: 

  * provide the argument `MIRRORING_DEPLOYMENT_GROUP` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-security mirroring-deployment-groups describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/mirroring-deployment-groups/describe)
    
    
    [gcloud beta network-security mirroring-deployment-groups describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/mirroring-deployment-groups/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
