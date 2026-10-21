---
url: https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domains/create/
title: gcloud network-services multicast-domains create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:07:44.868144+00:00
---

# gcloud network-services multicast-domains create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/network-services/multicast-domains/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud network-services multicast-domains create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud network-services multicast-domains create - create a multicast domain 
SYNOPSIS
    

`gcloud network-services multicast-domains create` (`MULTICAST_DOMAIN` : `--location`=`LOCATION`) `--admin-network`=`ADMIN_NETWORK` (`--connection-type`=`CONNECTION_TYPE`; default=`"CONNECTION_TYPE_UNSPECIFIED"` `--ncc-hub`=`NCC_HUB`) [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--multicast-domain-group`=`MULTICAST_DOMAIN_GROUP`] [`--ull-multicast-domain`=`ULL_MULTICAST_DOMAIN`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a multicast domain in the specified location of the current project. 
EXAMPLES
     Create a multicast domain with the name 'my-multicast-domain', admin-network 'path_to_admin_network', connection-type 'SAME_VPC', and location 'global'. 
    
    
    gcloud network-services multicast-domains create my-multicast-domain --admin-network=path_to_admin_network --connection-type=SAME_VPC --location=global

Create a multicast domain with the name 'my-multicast-domain', admin-network 'path_to_admin_network', connection-type 'NCC', ncc-hub 'path_to_ncc_hub', and location 'global'. 
    
    
    gcloud network-services multicast-domains create my-multicast-domain --admin-network=path_to_admin_network --connection-type=NCC --ncc-hub=path_to_ncc_hub --location=global

POSITIONAL ARGUMENTS
    

Multicast domain resource - Name of the multicast domain to be created. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `multicast_domain` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`MULTICAST_DOMAIN`
     ID of the multicast domain or fully qualified identifier for the multicast domain. 

To set the `multicast_domain` attribute: 

  * provide the argument `multicast_domain` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location Id. 

To set the `location` attribute: 

  * provide the argument `multicast_domain` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--admin-network`=`ADMIN_NETWORK`
     The URI of the admin network to be used. 
At least one of these must be specified: 

`--connection-type`=`CONNECTION_TYPE`; default=`"CONNECTION_TYPE_UNSPECIFIED"`
     The connection type for authorizing multicast traffic. `CONNECTION_TYPE` must be one of: `connection-type-unspecified`, `ncc`, `same-vpc`. 
`--ncc-hub`=`NCC_HUB`
     The URI of the NCC hub to be used. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description for the multicast domain. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--multicast-domain-group`=`MULTICAST_DOMAIN_GROUP`
     The URI of the multicast domain group to be used. 
`--ull-multicast-domain`=`ULL_MULTICAST_DOMAIN`
     The name of the ULL multicast feed to be used. This is for ULL multicast service only. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha network-services multicast-domains create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/multicast-domains/create)
    
    
    [gcloud beta network-services multicast-domains create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/multicast-domains/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
