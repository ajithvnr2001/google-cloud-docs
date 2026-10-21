---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports/
title: gcloud compute instance-groups managed set-named-ports \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:40:40.575281+00:00
---

# gcloud compute instance-groups managed set-named-ports  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-named-ports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instance-groups managed set-named-ports Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instance-groups managed set-named-ports - sets the list of named ports for an instance group 
SYNOPSIS
    

`gcloud compute instance-groups managed set-named-ports` `NAME` `--named-ports`=[`NAME`:`PORT`,…] [`--region`=`REGION` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Named ports are key:value pairs metadata representing the service name and the port that it's running on. Named ports can be assigned to an instance group, which indicates that the service is available on all instances in the group. This information is used by Application Load Balancers and proxy Network Load Balancers. 

`gcloud compute instance-groups managed set-named-ports` sets the list of named ports for all instances in an instance group. 

Note: Running this command will clear all existing named ports. 

EXAMPLES
     For example, to apply the named ports to an entire instance group: 
    
    
    gcloud compute instance-groups managed set-named-ports example-instance-group --named-ports=example-service:1111 --zone=us-central1-a

The above example will assign a name 'example-service' for port 1111 to the instance group called 'example-instance-group' in the ``us-central1-a`` zone. The command removes any named ports that are already set for this instance group. 

To clear named ports from instance group provide empty named ports list as parameter: 
    
    
    gcloud compute instance-groups managed set-named-ports example-instance-group --named-ports="" --zone=us-central1-a

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the instance group to operate on. 
REQUIRED FLAGS
    

`--named-ports`=[`NAME`:`PORT`,…]
     The comma-separated list of key:value pairs representing the service name and the port that it is running on. 

To clear the list of named ports pass empty list as flag value. For example: 
    
    
    gcloud compute instance-groups managed set-named-ports example-instance-group --named-ports ""

OPTIONAL FLAGS
    

At most one of these can be specified: 

`--region`=`REGION`
     Region of the instance group to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

Overrides the default `compute/region` property value for this command invocation. 

`--zone`=`ZONE`
     Zone of the instance group to operate on. If not specified, you might be prompted to select a zone (interactive mode only). 

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

Overrides the default `compute/zone` property value for this command invocation. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute instance-groups managed set-named-ports](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instance-groups/managed/set-named-ports)
    
    
    [gcloud beta compute instance-groups managed set-named-ports](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/set-named-ports)
    
    
    [gcloud preview compute instance-groups managed set-named-ports](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instance-groups/managed/set-named-ports)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
