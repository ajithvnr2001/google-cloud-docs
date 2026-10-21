---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/create/
title: gcloud network-security org-address-groups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:35:31.594340+00:00
---

# gcloud network-security org-address-groups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-security/org-address-groups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-security org-address-groups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-security org-address-groups create - create an address group 
SYNOPSIS
    

`gcloud network-security org-address-groups create` (`ADDRESS_GROUP` : `--location`=`LOCATION` `--organization`=`ORGANIZATION`) `--capacity`=`CAPACITY` `--type`=`TYPE` [`--async`] [`--description`=`DESCRIPTION`] [`--items`=[`ITEMS`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`--purpose`=[`PURPOSE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new address group with the given name. 
EXAMPLES
     Create an address group with the name ``my-address-group``, type ``IPV4``, capacity ``100`` and the description ``optional description``. 
    
    
    gcloud network-security org-address-groups create my-address-group --type=IPV4 --capacity=100 --description="optional description" --organization=1234

POSITIONAL ARGUMENTS
    

Address group resource - Name of the address group to be created. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`ADDRESS_GROUP`
     ID of the address group or fully qualified identifier for the address group. 

To set the `address_group` attribute: 

  * provide the argument `address_group` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. To set the `location` attribute: 

  * provide the argument `address_group` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     Organization number. To set the `organization` attribute: 

  * provide the argument `address_group` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


REQUIRED FLAGS
    

`--capacity`=`CAPACITY`
     Capacity of the address group. 
`--type`=`TYPE`
     Type of the address group. `TYPE` must be one of: `ipv4`, `ipv6`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the address group. 
`--items`=[`ITEMS`,…]
     Items of the address group. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
`--purpose`=[`PURPOSE`,…]
     List of Address Group purposes. `PURPOSE` must be one of: `cloud-armor`, `default`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networksecurity/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-security org-address-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/org-address-groups/create)
    
    
    [gcloud beta network-security org-address-groups create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/org-address-groups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
