---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/providers/scim-tenants/tokens/create/
title: gcloud beta iam workforce-pools providers scim-tenants tokens create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:52.969477+00:00
---

# gcloud beta iam workforce-pools providers scim-tenants tokens create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/providers/scim-tenants/tokens/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta iam workforce-pools providers scim-tenants tokens create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta iam workforce-pools providers scim-tenants tokens create - create an IAM workforce identity pool provider SCIM tenant token 
SYNOPSIS
    

`gcloud beta iam workforce-pools providers scim-tenants tokens create` (`TOKEN` : `--location`=`LOCATION` `--provider`=`PROVIDER` `--scim-tenant`=`SCIM_TENANT` `--workforce-pool`=`WORKFORCE_POOL`) [`--display-name`=`DISPLAY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new SCIM token associated with a specific workforce identity pool provider SCIM tenant. 

Upon successful creation, the command returns the created SCIM token resource. 

EXAMPLES
     To create a SCIM token with ID `my-token` under tenant `my-tenant` provider `my-provider` in pool `my-pool` located in `global`: 
    
    
    [gcloud beta iam workforce-pools providers scim-tenants tokens](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/providers/scim-tenants/tokens) create my-token --location=global --workforce-pool=my-pool --provider=my-provider --scim-tenant=my-tenant

POSITIONAL ARGUMENTS
    

Workforce pool provider scim token resource - The ID of the SCIM token to create. Must be 4-32 characters, alphanumeric ([a-z0-9-]), and cannot start with gcp-. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`TOKEN`
     ID of the workforce pool provider scim token or fully qualified identifier for the workforce pool provider scim token. 

To set the `token` attribute: 

  * provide the argument `token` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the workforce pool. 

To set the `location` attribute: 

  * provide the argument `token` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--provider`=`PROVIDER`
     The ID to use for the workforce pool provider, which becomes the final component of the resource name. This value must be unique within the workforce pool, 4-32 characters in length, and may contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `provider` attribute: 

  * provide the argument `token` on the command line with a fully specified name; 
  * provide the argument `--provider` on the command line. 


`--scim-tenant`=`SCIM_TENANT`
     The ID for the SCIM tenant, which becomes the final component of the resource name. This value must be 4-32 characters, alphanumeric ([a-z0-9-]), and cannot start with gcp-. To set the `scim-tenant` attribute: 

  * provide the argument `token` on the command line with a fully specified name; 
  * provide the argument `--scim-tenant` on the command line. 


`--workforce-pool`=`WORKFORCE_POOL`
     The ID to use for the workforce pool, which becomes the final component of the resource name. This value must be a globally unique string of 6 to 63 lowercase letters, digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `workforce-pool` attribute: 

  * provide the argument `token` on the command line with a fully specified name; 
  * provide the argument `--workforce-pool` on the command line. 


FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Optional, user-specified display name for the SCIM token (max 32 characters). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud iam workforce-pools providers scim-tenants tokens create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/scim-tenants/tokens/create)
    
    
    [gcloud alpha iam workforce-pools providers scim-tenants tokens](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/providers/scim-tenants/tokens) create

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
