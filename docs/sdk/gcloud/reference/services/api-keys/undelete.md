---
url: https://docs.cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete/
title: gcloud services api-keys undelete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:43.929542+00:00
---

# gcloud services api-keys undelete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/services/api-keys/undelete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud services api-keys undelete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud services api-keys undelete - undelete an API key 
SYNOPSIS
    

`gcloud services api-keys undelete` ([`KEY` : `--location`=`LOCATION`] `--key-string`=`KEY_STRING`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     API Keys that are deleted will be retained in the system for 30 days. If a key is still within this retention window, it can be undeleted with this command. 
EXAMPLES
     UnDelete an API Key (Key or key-string should be specified): 

To undelete with key `1234`, run: 
    
    
    gcloud services api-keys undelete 1234

To undelete with `1234` in project `myproject` using the fully qualified API key name, run: 
    
    
    gcloud services api-keys undelete projects/myproject/locations/global/keys/1234

To undelete using a Key-string, run: 
    
    
    gcloud services api-keys undelete --key-string='my-key-string'

POSITIONAL ARGUMENTS
    

Exactly one of these must be specified: 

Key resource - The name of the key to undelete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `key` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



`KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `key` attribute: 

* provide the argument `key` on the command line. 

This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the key. 

To set the `location` attribute: 

* provide the argument `key` on the command line with a fully specified name; 
* provide the argument `--location` on the command line; 
* location will default to global. 
`--key-string`=`KEY_STRING`
     Key String of the key. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha services api-keys undelete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/services/api-keys/undelete)
    
    
    [gcloud beta services api-keys undelete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/api-keys/undelete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
