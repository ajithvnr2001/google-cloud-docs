---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/backend-services/remove-backend/
title: gcloud beta compute backend-services remove-backend \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:35.068552+00:00
---

# gcloud beta compute backend-services remove-backend  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/backend-services/remove-backend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute backend-services remove-backend Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute backend-services remove-backend - remove a backend from a backend service 
SYNOPSIS
    

`gcloud beta compute backend-services remove-backend` `BACKEND_SERVICE_NAME` (`--service`=`SERVICE` | [`--instance-group`=`INSTANCE_GROUP` : `--instance-group-region`=`INSTANCE_GROUP_REGION` | `--instance-group-zone`=`INSTANCE_GROUP_ZONE`] | [`--network-endpoint-group`=`NETWORK_ENDPOINT_GROUP` : `--global-network-endpoint-group` | `--network-endpoint-group-region`=`NETWORK_ENDPOINT_GROUP_REGION` | `--network-endpoint-group-zone`=`NETWORK_ENDPOINT_GROUP_ZONE`]) [`--global` | `--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` `gcloud beta compute backend-services remove-backend` is used to remove a backend from a backend service. 

Before removing a backend, it is a good idea to "drain" the backend first. A backend can be drained by setting its capacity scaler to zero through 'gcloud compute backend-services edit'. 

POSITIONAL ARGUMENTS
    

`BACKEND_SERVICE_NAME`
     Name of the backend service to operate on. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

Service Group 
`--service`=`SERVICE`
     The name or URI of a Google Cloud service to use as a backend. 
Instance Group 
`--instance-group`=`INSTANCE_GROUP`
     Name of the instance group to remove from the backend service. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>

This flag argument must be specified if any of the other arguments in this group are specified. 

At most one of these can be specified: 

`--instance-group-region`=`INSTANCE_GROUP_REGION`
     Region of the instance group to remove from the backend service. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--instance-group-zone`=`INSTANCE_GROUP_ZONE`
     Zone of the instance group to remove from the backend service. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

Network Endpoint Group 
`--network-endpoint-group`=`NETWORK_ENDPOINT_GROUP`
     Name of the network endpoint group to remove from the backend service. 

This flag argument must be specified if any of the other arguments in this group are specified. 

At most one of these can be specified: 

`--global-network-endpoint-group`
     If set, the network endpoint group is global. 
`--network-endpoint-group-region`=`NETWORK_ENDPOINT_GROUP_REGION`
     Region of the network endpoint group to remove from the backend service. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--network-endpoint-group-zone`=`NETWORK_ENDPOINT_GROUP_ZONE`
     Zone of the network endpoint group to remove from the backend service. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

OPTIONAL FLAGS
    

At most one of these can be specified: 

`--global`
     If set, the backend service is global. 
`--region`=`REGION`
     Region of the backend service to operate on. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute backend-services remove-backend](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend)
    
    
    [gcloud alpha compute backend-services remove-backend](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/remove-backend)
    
    
    [gcloud preview compute backend-services remove-backend](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/backend-services/remove-backend)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
