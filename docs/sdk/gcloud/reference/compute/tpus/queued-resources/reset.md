---
url: https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/reset/
title: gcloud compute tpus queued-resources reset \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:53:43.332530+00:00
---

# gcloud compute tpus queued-resources reset  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/reset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud compute tpus queued-resources reset Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud compute tpus queued-resources reset - reset a Queued Resource 
SYNOPSIS
    

`gcloud compute tpus queued-resources reset` (`QUEUED_RESOURCE` : `--zone`=`ZONE`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Reset an existing Queued Resource. 

To get a list of Queued Resources for resetting, run: 
    
    
    [gcloud compute tpus queued-resources list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/queued-resources/list)

EXAMPLES
     To reset a Queued Resource in zone `us-central1-b` and project `my-project`, run: 
    
    
    gcloud compute tpus queued-resources reset --zone=us-central1-b --project=my-project

POSITIONAL ARGUMENTS
    

Queued resource resource - The Queued Resource you want to reset. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `queued_resource` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`QUEUED_RESOURCE`
     ID of the queued_resource or fully qualified identifier for the queued_resource. 

To set the `queued_resource` attribute: 

  * provide the argument `queued_resource` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     The compute/zone of the Cloud TPU. 

If not specified, will use `default` compute/zone. To set the `zone` attribute: 

  * provide the argument `queued_resource` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * set the property `compute/zone`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `tpu/v2` API. The full documentation for this API can be found at: <https://cloud.google.com/tpu/>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha compute tpus queued-resources reset](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/reset)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
