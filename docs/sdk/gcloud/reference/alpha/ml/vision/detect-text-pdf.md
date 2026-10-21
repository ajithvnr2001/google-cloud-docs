---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/detect-text-pdf/
title: gcloud alpha ml vision detect-text-pdf \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:47:56.644308+00:00
---

# gcloud alpha ml vision detect-text-pdf  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/detect-text-pdf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ml vision detect-text-pdf Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ml vision detect-text-pdf - detect and transcribe text from PDF files stored in Google Cloud Storage 
SYNOPSIS
    

`gcloud alpha ml vision detect-text-pdf` `INPUT_FILE` `OUTPUT_PATH` [`--batch-size`=`BATCH_SIZE`] [`--model-version`=`MODEL_VERSION`; default="builtin/stable"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Detect and transcribe text from PDF files stored in Google Cloud Storage. 

The Vision API accepts PDF files up to 2000 pages. Larger files will return an error. 

EXAMPLES
     To detect text for input PDF file 'gs://my_bucket/input_file' and store output in 'gs://my_bucket/out_put_prefix': 
    
    
    gcloud alpha ml vision detect-text-pdf gs://my_bucket/input_file gs://my_bucket/out_put_prefix

POSITIONAL ARGUMENTS
    

`INPUT_FILE`
     Google Cloud Storage location to read the input from. It must be in Google Cloud Storage format (gs://bucket/object) 
`OUTPUT_PATH`
     Google Cloud Storage location to store the output file. It must be in Google Cloud Storage format (gs://bucket/object) 
FLAGS
    

`--batch-size`=`BATCH_SIZE`
     Maximum number of response protos to put into each output JSON file on Google Cloud Storage. The valid range is [1, 100]. If not specified, the default value is 20. 
`--model-version`=`MODEL_VERSION`; default="builtin/stable"
     Model version to use for the feature. `MODEL_VERSION` must be one of: `builtin/latest`, `builtin/stable`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vision/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/vision/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ml vision detect-text-pdf](https://docs.cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text-pdf)
    
    
    [gcloud beta ml vision detect-text-pdf](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/vision/detect-text-pdf)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
