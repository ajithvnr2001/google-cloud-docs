---
url: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface/
title: gcloud edge-cloud networking routers add-interface \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:18:50.123693+00:00
---

# gcloud edge-cloud networking routers add-interface  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/routers/add-interface/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud edge-cloud networking routers add-interface Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud edge-cloud networking routers add-interface - add an interface to a Distributed Cloud Edge Network router 
SYNOPSIS
    

`gcloud edge-cloud networking routers add-interface` (`ROUTER` : `--location`=`LOCATION` `--zone`=`ZONE`) `--interface-name`=`INTERFACE_NAME` (`--loopback-ip-addresses`=[`LOOPBACK_IP_ADDRESSES`,…] | `--subnetwork`=`SUBNETWORK` | `--interconnect-attachment`=`INTERCONNECT_ATTACHMENT` `--ip-address`=`IP_ADDRESS` `--ip-mask-length`=`IP_MASK_LENGTH`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create an interface to a Distributed Cloud Edge Network router. 
EXAMPLES
     To create and add a northbound interface for Distributed Cloud Edge Network router 'my-router' in edge zone 'us-central1-edge-den1' , run: 
    
    
    gcloud edge-cloud networking routers add-interface my-router --interface-name=my-int-r1 --interconnect-attachment=my-link-attachment --ip-address=208.117.254.233 --ip-mask-length=31 --location=us-central1 --zone=us-central1-edge-den1

To create and add a southbound interface for Distributed Cloud Edge Network router 'my-router' in edge zone 'us-central1-edge-den1', run: 
    
    
    gcloud edge-cloud networking routers add-interface my-router --interface-name=my-int-r2 --subnetwork=my-subnet --location=us-central1 --zone=us-central1-edge-den1

POSITIONAL ARGUMENTS
    

Router resource - The router to which we add an interface. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ROUTER`
     ID of the router or fully qualified identifier for the router. 

To set the `router` attribute: 

  * provide the argument `router` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The Cloud location for the router. 

To set the `location` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--zone`=`ZONE`
     The zone of the router. 

To set the `zone` attribute: 

  * provide the argument `router` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line. 


REQUIRED FLAGS
    

`--interface-name`=`INTERFACE_NAME`
     The name of the interface being added. 
The argument group for configuring the interface for the router. 

Exactly one of these must be specified: 

The argument group for adding loopback interfaces to edge router. 
`--loopback-ip-addresses`=[`LOOPBACK_IP_ADDRESSES`,…]
     The list of ip ranges for the loopback interface. 
The argument group for adding southbound interfaces to edge router. 
`--subnetwork`=`SUBNETWORK`
     Subnetwork of the interface being added. 
The argument group for adding northbound interfaces to edge router. 
`--interconnect-attachment`=`INTERCONNECT_ATTACHMENT`
     Interconnect attachment of the interface being added. 
`--ip-address`=`IP_ADDRESS`
     Link-local address of the router for this interface. 
`--ip-mask-length`=`IP_MASK_LENGTH`
     Subnet mask for the link-local IP range of the interface. The interface IP address and BGP peer IP address must be selected from the subnet defined by this link-local range. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha edge-cloud networking routers add-interface](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud/networking/routers/add-interface)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
