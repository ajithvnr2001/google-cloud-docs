---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/revert/
title: gcloud beta filestore instances revert \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:33:37.793294+00:00
---

# gcloud beta filestore instances revert  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/filestore/instances/revert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta filestore instances revert Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta filestore instances revert - revert a Filestore instance 
SYNOPSIS
    

`gcloud beta filestore instances revert` (`INSTANCE` : `--location`=`LOCATION`) `--target-snapshot`=`TARGET_SNAPSHOT` [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Revert a Filestore instance to the target snapshot. 

This command can fail for the following reasons: 

  * The target snapshot does not exist. 
  * The active account does not have permission to revert the instance. 
  * The service tier of the instance does not support the operation. 


EXAMPLES
     To revert an instance with the name ``my-instance`` that's located in ``us-central1`` to the target snapshot named ``my-snapshot`` , run: 
    
    
    gcloud beta filestore instances revert my-instance --target-snapshot=my-snapshot --location=us-central1

POSITIONAL ARGUMENTS
    

Instance resource - Arguments and flags that specify the Filestore instance to revert. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

`--location`=`LOCATION`
     The location of the Filestore instance. To set the `location` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `filestore/location`. 


REQUIRED FLAGS
    

`--target-snapshot`=`TARGET_SNAPSHOT`
     Name of the Filestore snapshot to revert to. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `file/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/filestore/>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud filestore instances revert](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/revert)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
