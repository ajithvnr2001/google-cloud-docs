---
url: https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/create/
title: gcloud active-directory domains create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:43:33.529350+00:00
---

# gcloud active-directory domains create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/active-directory/domains/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud active-directory domains create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud active-directory domains create - create a Managed Microsoft AD domain 
SYNOPSIS
    

`gcloud active-directory domains create` `DOMAIN` `--region`=[`REGION`,…] `--reserved-ip-range`=`RESERVED_IP_RANGE` [`--admin-name`=`ADMIN_NAME`] [`--async`] [`--authorized-networks`=[`AUTHORIZED_NETWORKS`,…]] [`--enable-audit-logs`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a new Managed Microsoft AD domain with the given name using Google Cloud's Managed Service for Microsoft Active Directory. 

This command can fail for the following reasons: 

  * An AD domain with the same name already exists. 
  * The active account does not have permission to create AD domains. 
  * There is an overlap between the provided CIDR range and authorized network's CIDR. 
  * A valid region was not provided. 


EXAMPLES
     The following command creates an AD domain with the name `my-domain.com` in region `us-central1`, a network peering to `my-network` and consuming the IP address range `10.172.0.0/24`. 
    
    
    gcloud active-directory domains create my-domain.com --region=us-central1 --reserved-ip-range="10.172.0.0/24" --authorized-networks=projects/my-project/global/networks/my-network

POSITIONAL ARGUMENTS
    

Domain resource - Name of the managed Managed Microsoft AD domain you want to create. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `domain` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DOMAIN`
     ID of the domain or fully qualified identifier for the domain. 

To set the `domain` attribute: 

  * provide the argument `domain` on the command line. 


REQUIRED FLAGS
    

`--region`=[`REGION`,…]
     Google Compute Engine region in which to provision domain controllers. 
`--reserved-ip-range`=`RESERVED_IP_RANGE`
     Classless Inter-Domain Routing range of internal addresses that are reserved for this domain. 
OPTIONAL FLAGS
    

`--admin-name`=`ADMIN_NAME`
     Name of the administrator that may be used to perform Active Directory operations. This is a delegated administrator account provisioned by our service. If left unspecified `MIAdmin` will be used. This is different from both the domain administrator and the Directory Services Restore Mode (DSRM) administrator. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--authorized-networks`=[`AUTHORIZED_NETWORKS`,…]
     Names of the Google Compute Engine networks to which the domain will be connected. 
`--enable-audit-logs`
     If specified, Active Directory data audit logs are enabled for the domain. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `managedidentities/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-microsoft-ad/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha active-directory domains create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/active-directory/domains/create)
    
    
    [gcloud beta active-directory domains create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/active-directory/domains/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
