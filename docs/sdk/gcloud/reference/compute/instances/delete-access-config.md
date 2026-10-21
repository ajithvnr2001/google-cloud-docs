---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete-access-config/
title: gcloud compute instances delete-access-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:51:07.341075+00:00
---

# gcloud compute instances delete-access-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete-access-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute instances delete-access-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute instances delete-access-config - delete an access configuration from a virtual machine network interface 
SYNOPSIS
    

`gcloud compute instances delete-access-config` `INSTANCE_NAME` [`--access-config-name`=`ACCESS_CONFIG_NAME`; default="external-nat"] [`--network-interface`=`NETWORK_INTERFACE`; default="nic0"] [`--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `gcloud compute instances delete-access-config` is used to delete access configurations from network interfaces of Compute Engine virtual machines. Access configurations let you assign a public, external IP to a virtual machine. The delete-access-config operation removes external IP from the instance interface. If there is traffic routed to the external IP, after deleting the access config operation, traffic to the external IP will not reach the VM anymore. 
EXAMPLES
     To remove the externally accessible IP from a virtual machine named ``example-instance`` in zone ``us-central1-a``, run: 
    
    
    gcloud compute instances delete-access-config example-instance --zone=us-central1-a

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--access-config-name`=`ACCESS_CONFIG_NAME`; default="external-nat"
     Specifies the name of the access configuration to delete. ``external-nat`` is used as the default if this flag is not provided. 
`--network-interface`=`NETWORK_INTERFACE`; default="nic0"
     Specifies the name of the network interface from which to delete the access configuration. If this is not provided, then ``nic0`` is used as the default. 
`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha compute instances delete-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/delete-access-config)
    
    
    [gcloud beta compute instances delete-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/delete-access-config)
    
    
    [gcloud preview compute instances delete-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/delete-access-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
