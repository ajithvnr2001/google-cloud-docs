---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/mirroring-deployment-groups/create/
title: gcloud beta network-security mirroring-deployment-groups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:55:56.233422+00:00
---

# gcloud beta network-security mirroring-deployment-groups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/mirroring-deployment-groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-security mirroring-deployment-groups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-security mirroring-deployment-groups create - create a Mirroring Deployment Group 
SYNOPSIS
    

`gcloud beta network-security mirroring-deployment-groups create` (`MIRRORING_DEPLOYMENT_GROUP` : `--location`=`LOCATION`) `--network`=`NETWORK` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--max-wait`=`MAX_WAIT`; default="20m"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a mirroring deployment group. Successful creation of a deployment group results in a deployment group in ACTIVE state. Check the progress of deployment group creation by using `[gcloud network-security mirroring-deployment-groups list](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployment-groups/list)`. 

For more examples, refer to the EXAMPLES section below. 

EXAMPLES
     To create a mirroring deployment group called `my-deployment-group`, in project ID `my-project`, run:
    
    
    gcloud beta network-security mirroring-deployment-groups create my-deployment-group --project=my-project --location=global --network=my-network

OR 
    
    
    gcloud beta network-security mirroring-deployment-groups create my-deployment-group --project=my-project --location=global --network=projects/my-project/global/networks/my-network

OR 
    
    
    gcloud beta network-security mirroring-deployment-groups create projects/my-project/locations/global/mirroringDeploymentGroups/my-deployment-group --network=projects/my-project/global/networks/my-network

OR 
    
    
    gcloud beta network-security mirroring-deployment-groups create projects/my-project/locations/global/mirroringDeploymentGroups/my-deployment-group --network=projects/my-project/global/networks/my-network --description="my-description"

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


REQUIRED FLAGS
    

Network resource - Mirroring Deployment Group. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--network` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--network`=`NETWORK`
     ID of the network or fully qualified identifier for the network. 

To set the `network-name` attribute: 

  * provide the argument `--network` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--description`=`DESCRIPTION`
     Description of the mirroring deployment group 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--max-wait`=`MAX_WAIT`; default="20m"
     Time to synchronously wait for the operation to complete, after which the operation continues asynchronously. Ignored if --no-async isn't specified. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-security mirroring-deployment-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/mirroring-deployment-groups/create)
    
    
    [gcloud alpha network-security mirroring-deployment-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/mirroring-deployment-groups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
