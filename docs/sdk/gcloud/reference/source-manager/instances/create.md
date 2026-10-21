---
url: https://docs.cloud.google.com/sdk/gcloud/reference/source-manager/instances/create/
title: gcloud source-manager instances create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:07.907748+00:00
---

# gcloud source-manager instances create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/source-manager/instances/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud source-manager instances create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud source-manager instances create - create a Secure Source Manager instance 
SYNOPSIS
    

`gcloud source-manager instances create` (`INSTANCE` : `--region`=`REGION`) [`--async`] [`--enable-workforce-identity-federation`] [`--endpoint-mode`=`ENDPOINT_MODE`] [`--kms-key`=`KMS_KEY`] [`--max-wait`=`MAX_WAIT`; default="60m"] [`--is-private` : `--ca-pool`=`CA_POOL` `--psc-allowed-projects`=[`PROJECTS`,…] `--custom-hostname-api`=`CUSTOM_HOSTNAME_API` `--custom-hostname-git-http`=`CUSTOM_HOSTNAME_GIT_HTTP` `--custom-hostname-git-ssh`=`CUSTOM_HOSTNAME_GIT_SSH` `--custom-hostname-html`=`CUSTOM_HOSTNAME_HTML`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create a Secure Source Manager instance. 
EXAMPLES
     To create a Secure Source Manager instance named 'my-instance' in location 'us-central1' asynchronously, run: 
    
    
    gcloud source-manager instances create my-instance --region=us-central1

To create a Secure Source Manager instance named 'my-instance' in location 'us-central1' synchronously, and wait a maximum of 30 minutes for it to finish being created, run: 
    
    
    gcloud source-manager instances create my-instance --region=us-central1 --no-async --max-wait=30m

POSITIONAL ARGUMENTS
    

Instance resource - The Secure Source Manager instance to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Secure Source Manager location. 

To set the `region` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--enable-workforce-identity-federation`
     Bool indicator for workforce identity federation instance. 
`--endpoint-mode`=`ENDPOINT_MODE`
     Specifies endpoint mode for a given command. Regional endpoints provide enhanced data residency and reliability by ensuring your request is handled entirely within the specified Google Cloud region. This differs from global endpoints, which may process parts of the request outside the target region. Overrides the default `regional/endpoint_mode` property value for this command invocation. `ENDPOINT_MODE` must be one of: 

`global`
     (Default) Use global rather than regional endpoints. 
`regional`
     Only use regional endpoints. An error will be raised if a regional endpoint is not available for a given command. 
`regional-preferred`
     Use regional endpoints when available, otherwise use global endpoints. Recommended for most users. 
`--kms-key`=`KMS_KEY`
     KMS key used to encrypt instance optionally. 
`--max-wait`=`MAX_WAIT`; default="60m"
     Time to synchronously wait for the operation to complete, after which the operation continues asynchronously. Ignored if `--no-async` isn't specified. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
Private instance configuration. 
`--is-private`
     Bool indicator for private instance. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--ca-pool`=`CA_POOL`
     CA Pool path for private instance. 
`--psc-allowed-projects`=[`PROJECTS`,…]
     List of additional projects allowed to connect to the instance via private service connect. 
Custom hostname configuration. 
`--custom-hostname-api`=`CUSTOM_HOSTNAME_API`
     Custom hostname for api. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-hostname-git-http`=`CUSTOM_HOSTNAME_GIT_HTTP`
     Custom hostname for git http. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-hostname-git-ssh`=`CUSTOM_HOSTNAME_GIT_SSH`
     Custom hostname for git ssh. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--custom-hostname-html`=`CUSTOM_HOSTNAME_HTML`
     Custom hostname for html. 

This flag argument must be specified if any of the other arguments in this group are specified. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha source-manager instances create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/source-manager/instances/create)
    
    
    [gcloud beta source-manager instances create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/source-manager/instances/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
