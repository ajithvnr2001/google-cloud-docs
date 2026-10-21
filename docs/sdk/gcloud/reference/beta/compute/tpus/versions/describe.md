---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/tpus/versions/describe/
title: gcloud beta compute tpus versions describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:18:38.613286+00:00
---

# gcloud beta compute tpus versions describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/tpus/versions/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta compute tpus versions describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta compute tpus versions describe - describe a Tensorflow version available for Cloud TPUs 
SYNOPSIS
    

`gcloud beta compute tpus versions describe` (`VERSION` : `--zone`=`ZONE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Get details on a Tensorflow version. 

To get a list of available Tesnorflow versions for your location run: 
    
    
    [gcloud beta compute tpus versions list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/tpus/versions/list)

EXAMPLES
     The following command describes the TensorFlow `1.15` version running in zone `us-central1-b`: 
    
    
    gcloud beta compute tpus versions describe 1.15 --zone=us-central1-b

POSITIONAL ARGUMENTS
    

Tensorflow version resource - The Tensorflow version you want to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `version` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`VERSION`
     ID of the tensorflow_version or fully qualified identifier for the tensorflow_version. 

To set the `version` attribute: 

  * provide the argument `version` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--zone`=`ZONE`
     The compute/zone of the Cloud TPU. 

If not specified, will use `default` compute/zone. To set the `zone` attribute: 

  * provide the argument `version` on the command line with a fully specified name; 
  * provide the argument `--zone` on the command line; 
  * set the property `compute/zone`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `tpu/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/tpu/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud compute tpus versions describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/versions/describe)
    
    
    [gcloud alpha compute tpus versions describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/versions/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
