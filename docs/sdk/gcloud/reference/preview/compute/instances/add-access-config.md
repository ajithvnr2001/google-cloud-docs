---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/add-access-config/
title: gcloud preview compute instances add-access-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:19:28.871841+00:00
---

# gcloud preview compute instances add-access-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/instances/add-access-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute instances add-access-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute instances add-access-config - create a Compute Engine virtual machine access configuration 
SYNOPSIS
    

`gcloud preview compute instances add-access-config` `INSTANCE_NAME` [`--access-config-name`=`ACCESS_CONFIG_NAME`; default="external-nat"] [`--address`=`ADDRESS`] [`--network-interface`=`NETWORK_INTERFACE`; default="nic0"] [`--network-tier`=`NETWORK_TIER`] [`--zone`=`ZONE`] [`--public-ptr` | `--no-public-ptr`] [`--public-ptr-domain`=`PUBLIC_PTR_DOMAIN` | `--no-public-ptr-domain`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute instances add-access-config` is used to create access configurations for network interfaces of Compute Engine virtual machines. This allows you to assign a public, external IP to a virtual machine. 
EXAMPLES
     To assign an public, externally accessible IP to a virtual machine named ``example-instance`` in zone ``us-central1-a``, run: 
    
    
    gcloud preview compute instances add-access-config example-instance --zone=us-central1-a

To assign the specific, reserved public IP address ``123.456.789.123`` to the virtual machine, run: 
    
    
    gcloud preview compute instances add-access-config example-instance --zone=us-central1-a --address=123.456.789.123

POSITIONAL ARGUMENTS
    

`INSTANCE_NAME`
     Name of the instance to operate on. For details on valid instance names, refer to the criteria documented under the field 'name' at: <https://cloud.google.com/compute/docs/reference/rest/v1/instances>
FLAGS
    

`--access-config-name`=`ACCESS_CONFIG_NAME`; default="external-nat"
     Specifies the name of the new access configuration. ``external-nat`` is used as the default if this flag is not provided. Since ONE_TO_ONE_NAT is currently the only access-config type, it is not recommended that you change this value. 
`--address`=`ADDRESS`
     Specifies the external IP address of the new access configuration. If this is not specified, then the service will choose an available ephemeral IP address. If an explicit IP address is given, then that IP address must be reserved by the project and not be in use by another resource. 
`--network-interface`=`NETWORK_INTERFACE`; default="nic0"
     Specifies the name of the network interface which contains the access configuration. If this is not provided, then "nic0" is used as the default. 
`--network-tier`=`NETWORK_TIER`
     Specifies the network tier of the access configuration. ``NETWORK_TIER`` must be one of: `PREMIUM`, `STANDARD`. The default value is `PREMIUM`. 
`--zone`=`ZONE`
     Zone of the instance to operate on. If not specified, you might be prompted to select a zone (interactive mode only). `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` attempts to identify the appropriate zone by searching for resources in your currently active project. If the zone cannot be determined, `[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference)` prompts you for a selection with all available Google Cloud Platform zones. 

To avoid prompting when this flag is omitted, the user can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

At most one of these can be specified: 

`--public-ptr`
     Creates a DNS PTR record for the external IP in the access configuration. This option can only be specified for the default network-interface, "nic0". 
`--no-public-ptr`
     If provided, no DNS PTR record is created for the external IP in the access configuration. Mutually exclusive with public-ptr-domain. 
At most one of these can be specified: 

`--public-ptr-domain`=`PUBLIC_PTR_DOMAIN`
     Assigns a custom PTR domain for the external IP in the access configuration. Mutually exclusive with no-public-ptr. This option can only be specified for the default network-interface, "nic0". 
`--no-public-ptr-domain`
     If both this flag and --public-ptr are specified, creates a DNS PTR record for the external IP in the access configuration with the PTR domain name being the DNS name of the instance. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute instances add-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/add-access-config)
    
    
    [gcloud alpha compute instances add-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/add-access-config)
    
    
    [gcloud beta compute instances add-access-config](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instances/add-access-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
