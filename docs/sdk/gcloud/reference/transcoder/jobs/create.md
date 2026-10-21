---
url: https://docs.cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create/
title: gcloud transcoder jobs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:21:18.879123+00:00
---

# gcloud transcoder jobs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud transcoder jobs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud transcoder jobs create - create Transcoder jobs 
SYNOPSIS
    

`gcloud transcoder jobs create` [`--batch-mode-priority`=`BATCH_MODE_PRIORITY`] [`--input-uri`=`INPUT_URI`] [`--labels`=[`KEY`=`VALUE`,…]] [`--location`=`LOCATION`] [`--mode`=`MODE`] [`--optimization`=`OPTIMIZATION`] [`--output-uri`=`OUTPUT_URI`] [`--file`=`FILE` | `--json`=`JSON` | `--template-id`=`TEMPLATE_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Create Transcoder jobs. 
EXAMPLES
     To create a transcoder job with default template, input URI, and output URI: 
    
    
    gcloud transcoder jobs create --location=us-central1 --input-uri="gs://bucket/input.mp4" --output-uri="gs://bucket/output/"

To create a transcoder job with template id, input URI, and output URI: 
    
    
    gcloud transcoder jobs create --location=us-central1 --input-uri="gs://bucket/input.mp4" --output-uri="gs://bucket/output/" --template-id=my-template

To create a transcoder job with json format configuration: 
    
    
    gcloud transcoder jobs create --location=us-central1 --json="config: json-format"

To create a transcoder job with json format configuration file: 
    
    
    gcloud transcoder jobs create --location=us-central1 --file="config.json"

To create a transcoder job with labels: 
    
    
    gcloud transcoder jobs create --location=us-central1 --file="config.json" --labels=key=value

To create a transcoder job in batch mode: 
    
    
    gcloud transcoder jobs create --location=us-central1 --file="config.json" --mode=PROCESSING_MODE_BATCH

To create a transcoder job in batch mode with priority: 
    
    
    gcloud transcoder jobs create --location=us-central1 --file="config.json" --mode=PROCESSING_MODE_BATCH --batch-mode-priority=3

To create a transcoder job with optimizations disabled: 
    
    
    gcloud transcoder jobs create --location=us-central1 --file="config.json" --optimization=DISABLED

FLAGS
    

`--batch-mode-priority`=`BATCH_MODE_PRIORITY`
     Processing priority of a batch mode transcoder job. This value will override batch mode priority in job config. 
`--input-uri`=`INPUT_URI`
     Google Cloud Storage URI. This value will override input URI in job config. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

Location resource - Transcoder location This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * set the property `transcoder/location` with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line; 
  * set the property `transcoder/location`. 


`--mode`=`MODE`
     Processing mode of transcode job. This value will override mode in job config. `MODE` must be one of: `PROCESSING_MODE_INTERACTIVE`, `PROCESSING_MODE_BATCH`. 
`--optimization`=`OPTIMIZATION`
     Optimization strategy of transcode job. This value will override optimization in job config. `OPTIMIZATION` must be one of: `AUTODETECT`, `DISABLED`. 
`--output-uri`=`OUTPUT_URI`
     Google Cloud Storage directory URI (followed by a trailing forward slash). This value will override output URI in job config. 
At most one of these can be specified: 

`--file`=`FILE`
     Path to job config. 
`--json`=`JSON`
     Job config in json format. 
`--template-id`=`TEMPLATE_ID`
     Job template id. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
