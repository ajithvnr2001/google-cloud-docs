---
url: https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/auth-tokens/describe/
title: gcloud memorystore instances token-auth-users auth-tokens describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:23.525563+00:00
---

# gcloud memorystore instances token-auth-users auth-tokens describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/auth-tokens/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud memorystore instances token-auth-users auth-tokens describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud memorystore instances token-auth-users auth-tokens describe - describe authTokens 
SYNOPSIS
    

`gcloud memorystore instances token-auth-users auth-tokens describe` (`AUTH_TOKEN` : `--instance`=`INSTANCE` `--location`=`LOCATION` `--token-auth-user`=`TOKEN_AUTH_USER`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Describe an authToken 
EXAMPLES
     To describe the authToken, run: 
    
    
    gcloud memorystore instances token-auth-users auth-tokens describe

POSITIONAL ARGUMENTS
    

AuthToken resource - The name of token auth user for a token auth enabled instance. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user}/authTokens/{auth_token} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `auth_token` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`AUTH_TOKEN`
     ID of the authToken or fully qualified identifier for the authToken. 

To set the `auth_token` attribute: 

  * provide the argument `auth_token` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The instance id of the authToken resource. 

To set the `instance` attribute: 

  * provide the argument `auth_token` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


`--location`=`LOCATION`
     The location id of the authToken resource. 

To set the `location` attribute: 

  * provide the argument `auth_token` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--token-auth-user`=`TOKEN_AUTH_USER`
     The tokenAuthUser id of the authToken resource. 

To set the `token-auth-user` attribute: 

  * provide the argument `auth_token` on the command line with a fully specified name; 
  * provide the argument `--token-auth-user` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `memorystore/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha memorystore instances token-auth-users auth-tokens](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memorystore/instances/token-auth-users/auth-tokens) describe
    
    
    [gcloud beta memorystore instances token-auth-users auth-tokens](https://docs.cloud.google.com/sdk/gcloud/reference/beta/memorystore/instances/token-auth-users/auth-tokens) describe

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
