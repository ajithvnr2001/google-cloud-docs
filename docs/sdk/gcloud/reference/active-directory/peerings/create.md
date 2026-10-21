---
url: https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/peerings/create/
title: gcloud active-directory peerings create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:35.064791+00:00
---

# gcloud active-directory peerings create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/peerings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud active-directory peerings create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud active-directory peerings create - create a Managed Microsoft Active Directory domain peering 
SYNOPSIS
    

`gcloud active-directory peerings create` `PEERING` `--authorized-network`=`AUTHORIZED_NETWORK` `--domain`=`DOMAIN` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new Managed Microsoft AD domain peering with the given name using Google Cloud's Managed Service for Microsoft Active Directory. 

This command can fail for the following reasons: 

  * A domain peering with the same name already exists. 
  * The active account does not have permission to create AD domains peerings. 
  * There is an overlap between the provided CIDR range and authorized network's CIDR. 


EXAMPLES
     The following command creates an AD domain peering with the name ``my-peering``, network ``my-network`` and domain ``projects/domain-project/locations/global/domains/domain.com``
    
    
    gcloud active-directory peerings create my-peering --domain=projects/domain-project/locations/global/domains/domain.com --authorized-network=projects/network-project/global/networks/my-network

POSITIONAL ARGUMENTS
    

Peering resource - Name of the managed Managed Microsoft AD domain peering you want to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `peering` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`PEERING`
     ID of the peering or fully qualified identifier for the peering. 

To set the `peering` attribute: 

  * provide the argument `peering` on the command line. 


REQUIRED FLAGS
    

`--authorized-network`=`AUTHORIZED_NETWORK`
     Name of the Network that is authorized to communicate with Managed Microsoft AD domain. This is usually the full path name of the network in the peer project. 
`--domain`=`DOMAIN`
     Name of the managed Managed Microsoft AD domain you want to peer to. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedidentities/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-microsoft-ad/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha active-directory peerings create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/peerings/create)
    
    
    [gcloud beta active-directory peerings create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/peerings/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
