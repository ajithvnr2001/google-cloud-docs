---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/lustre/instances/directory-policies/create/
title: gcloud alpha lustre instances directory-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:34:41.881398+00:00
---

# gcloud alpha lustre instances directory-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/lustre/instances/directory-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha lustre instances directory-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha lustre instances directory-policies create - create directoryPolicies 
SYNOPSIS
    

`gcloud alpha lustre instances directory-policies create` (`DIRECTORY_POLICY` : `--instance`=`INSTANCE` `--location`=`LOCATION`) `--directory-path`=`DIRECTORY_PATH` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a directoryPolicy 
EXAMPLES
     To create the directoryPolicy, run: 
    
    
    gcloud alpha lustre instances directory-policies create

POSITIONAL ARGUMENTS
    

DirectoryPolicy resource - Identifier. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`. {id} is user provided. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `directory_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DIRECTORY_POLICY`
     ID of the directoryPolicy or fully qualified identifier for the directoryPolicy. 

To set the `directory_policy` attribute: 

  * provide the argument `directory_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--instance`=`INSTANCE`
     The instance id of the directoryPolicy resource. 

To set the `instance` attribute: 

  * provide the argument `directory_policy` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line. 


`--location`=`LOCATION`
     The location id of the directoryPolicy resource. 

To set the `location` attribute: 

  * provide the argument `directory_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--directory-path`=`DIRECTORY_PATH`
     The lustre instance filesystem full path of the directory. It must start with a slash. e.g. /lustre/testFolder 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `lustre/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/managed-lustre/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud lustre instances directory-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/directory-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
