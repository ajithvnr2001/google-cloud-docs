---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/providers/keys/create/
title: gcloud alpha iam workforce-pools providers keys create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:22.981730+00:00
---

# gcloud alpha iam workforce-pools providers keys create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iam/workforce-pools/providers/keys/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha iam workforce-pools providers keys create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha iam workforce-pools providers keys create - create a new workforce pool provider key 
SYNOPSIS
    

`gcloud alpha iam workforce-pools providers keys create` (`KEY` : `--location`=`LOCATION` `--provider`=`PROVIDER` `--workforce-pool`=`WORKFORCE_POOL`) `--spec`=`SPEC` `--use`=`USE` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a new workforce pool provider key. 
EXAMPLES
     The following command creates a workforce pool provider key with the ID ``my-key``. Explicit values for all required and optional parameters are provided. 
    
    
    gcloud alpha iam workforce-pools providers keys create my-key --location="global" --workforce-pool="my-workforce-pool" --provider="my-provider" --use="ENCRYPTION" --spec="RSA_4096"

POSITIONAL ARGUMENTS
    

Workforce pool provider key resource - The workforce pool provider key to create. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`KEY`
     ID of the workforce pool provider key or fully qualified identifier for the workforce pool provider key. 

To set the `key` attribute: 

  * provide the argument `key` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the workforce pool. 

To set the `location` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--provider`=`PROVIDER`
     The ID to use for the workforce pool provider, which becomes the final component of the resource name. This value must be unique within the workforce pool, 4-32 characters in length, and may contain the characters [a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `provider` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--provider` on the command line. 


`--workforce-pool`=`WORKFORCE_POOL`
     The ID to use for the workforce pool, which becomes the final component of the resource name. This value must be a globally unique string of 6 to 63 lowercase letters, digits, or hyphens. It must start with a letter, and cannot have a trailing hyphen. The prefix `gcp-` is reserved for use by Google, and may not be specified. To set the `workforce-pool` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--workforce-pool` on the command line. 


REQUIRED FLAGS
    

`--spec`=`SPEC`
     The specifications for the key. `SPEC` must be one of: `key-spec-unspecified`, `rsa-2048`, `rsa-3072`, `rsa-4096`. 
`--use`=`USE`
     The purpose of the key. `USE` must be one of: `encryption`, `key-use-unspecified`, `signing`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `iam/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/iam/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud iam workforce-pools providers keys create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/keys/create)
    
    
    [gcloud beta iam workforce-pools providers keys create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/workforce-pools/providers/keys/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
