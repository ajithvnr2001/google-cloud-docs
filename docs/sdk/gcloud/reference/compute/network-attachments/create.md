---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create/
title: gcloud compute network-attachments create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:29:19.575721+00:00
---

# gcloud compute network-attachments create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute network-attachments create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute network-attachments create - create a Google Compute Engine network attachment 
SYNOPSIS
    

`gcloud compute network-attachments create` `NAME` `--subnets`=`SUBNETS`,[`SUBNETS`,…] [`--connection-preference`=`CONNECTION_PREFERENCE`; default=`"ACCEPT_AUTOMATIC"`] [`--description`=`DESCRIPTION`] [`--producer-accept-list`=[`ACCEPT_LIST`,…]] [`--producer-reject-list`=[`REJECT_LIST`,…]] [`--region`=`REGION`] [`--subnets-region`=`SUBNETS_REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute network-attachments create` is used to create network attachments. A service consumer creates network attachments and makes it available to producers. Service producers then use a multi-NIC VM to form a bi-directional, non-NAT'd communication channel. 
EXAMPLES
    
    
    
    gcloud compute network-attachments create NETWORK_ATTACHMENT_NAME --region=us-central1 --subnets=MY_SUBNET --connection-preference=ACCEPT_MANUAL --producer-accept-list=PROJECT1,PROJECT2 --producer-reject-list=PROJECT3,PROJECT4

To create a network attachment with a textual description, run: 
    
    
    gcloud compute network-attachments create NETWORK_ATTACHMENT_NAME --region=us-central1 --subnets=MY_SUBNET --connection-preference=ACCEPT_MANUAL --producer-accept-list=PROJECT1,PROJECT2 --producer-reject-list=PROJECT3,PROJECT4 --description='default network attachment'

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the network attachment to create. 
REQUIRED FLAGS
    

`--subnets`=`SUBNETS`,[`SUBNETS`,…]
     The subnetworks provided by the consumer for the producers 
OPTIONAL FLAGS
    

`--connection-preference`=`CONNECTION_PREFERENCE`; default=`"ACCEPT_AUTOMATIC"`
     The connection preference of network attachment. The value can be set to ACCEPT_AUTOMATIC or ACCEPT_MANUAL. An ACCEPT_AUTOMATIC network attachment is one that always accepts the connection from producer NIC. An ACCEPT_MANUAL network attachment is one that requires an explicit addition of the producer project id or project number to the producer accept list. `CONNECTION_PREFERENCE` must be one of: `ACCEPT_AUTOMATIC`, `ACCEPT_MANUAL`. 
`--description`=`DESCRIPTION`
     An optional, textual description for the network attachment. 
`--producer-accept-list`=[`ACCEPT_LIST`,…]
     Projects that are allowed to connect to this network attachment. 
`--producer-reject-list`=[`REJECT_LIST`,…]
     Projects that are not allowed to connect to this network attachment. 
`--region`=`REGION`
     Region of the network attachment to create. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

`--subnets-region`=`SUBNETS_REGION`
     Region of the subnetworks to operate on. Overrides the default `compute/region` property value for this command invocation. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute network-attachments create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/network-attachments/create)
    
    
    [gcloud beta compute network-attachments create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/network-attachments/create)
    
    
    [gcloud preview compute network-attachments create](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/network-attachments/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
