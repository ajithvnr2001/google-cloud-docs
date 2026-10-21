---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ml/vision/detect-labels/
title: gcloud ml vision detect-labels \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:27.448532+00:00
---

# gcloud ml vision detect-labels  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ml/vision/detect-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ml vision detect-labels Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ml vision detect-labels - detect broad sets of categories within an image 
SYNOPSIS
    

`gcloud ml vision detect-labels` `IMAGE_PATH` [`--max-results`=`MAX_RESULTS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Label Detection detects categories in an image, ranging from modes of transportation to animals. 
EXAMPLES
     To detect categories in an image 'gs://my_bucket/input_file': 
    
    
    gcloud ml vision detect-labels gs://my_bucket/input_file

POSITIONAL ARGUMENTS
    

`IMAGE_PATH`
     Path to the image to be analyzed. This can be either a local path or a URL. If you provide a local file, the contents will be sent directly to Google Cloud Vision. If you provide a URL, it must be in Google Cloud Storage format (gs://bucket/object) or an HTTP URL (<http://..>. or https://…) 
FLAGS
    

`--max-results`=`MAX_RESULTS`
     Maximum number of results to be provided. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vision/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/vision/>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha ml vision detect-labels](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/detect-labels)
    
    
    [gcloud beta ml vision detect-labels](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/vision/detect-labels)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
