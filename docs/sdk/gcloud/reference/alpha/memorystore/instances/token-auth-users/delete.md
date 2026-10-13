---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memorystore/instances/token-auth-users/delete/
title: gcloud alpha memorystore instances token-auth-users delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:18.707620+00:00
---

# gcloud alpha memorystore instances token-auth-users delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memorystore/instances/token-auth-users/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha memorystore instances token-auth-users delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha memorystore instances token-auth-users delete - delete tokenAuthUsers 
SYNOPSIS
    

`gcloud alpha memorystore instances token-auth-users delete` (`TOKEN_AUTH_USER` : `--instance`=`INSTANCE` `--location`=`LOCATION`) [`--async`] [`--no-force`] [`--request-id`=`REQUEST_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Delete a tokenAuthUser 
EXAMPLES
     To delete the tokenAuthUser, run: 
    
    
    gcloud alpha memorystore instances token-auth-users delete

POSITIONAL ARGUMENTS
    

TokenAuthUser resource - The name of the token auth user to delete. Format: projects/{project}/locations/{location}/instances/{instance}/tokenAuthUsers/{token_auth_user} The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `token_auth_user` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`TOKEN_AUTH_USER`
     ID of the tokenAuthUser or fully qualified identifier for the tokenAuthUser. 

To set the `token_auth_user` attribute: 

  * provide the argument `token_auth_user` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The instance id of the tokenAuthUser resource. 

To set the `instance` attribute: 

  * provide the argument `token_auth_user` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


`--location`=`LOCATION`
     The location id of the tokenAuthUser resource. 

To set the `location` attribute: 

  * provide the argument `token_auth_user` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--force`
     If set to true, any auth tokens from this user will also be deleted. Otherwise, the request will only work if the user has no auth tokens. Enabled by default, use `--no-force` to disable. 
`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `memorystore/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud memorystore instances token-auth-users delete](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/token-auth-users/delete)
    
    
    [gcloud beta memorystore instances token-auth-users delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/memorystore/instances/token-auth-users/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
