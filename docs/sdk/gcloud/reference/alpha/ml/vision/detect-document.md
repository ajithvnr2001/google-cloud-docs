---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/detect-document/
title: gcloud alpha ml vision detect-document \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:47:56.102008+00:00
---

# gcloud alpha ml vision detect-document  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/vision/detect-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ml vision detect-document Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ml vision detect-document - detect dense text in an image 
SYNOPSIS
    

`gcloud alpha ml vision detect-document` `IMAGE_PATH` [`--language-hints`=[`LANGUAGE_HINTS`,…]] [`--model-version`=`MODEL_VERSION`; default="builtin/stable"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Detect dense text in an image, such as books and research reports. 

Google Cloud Vision uses OCR (Optical Character Recognition) to analyze text. This is a premium feature for dense text such as books, research reports, and PDFs. To detect small amounts of text such as on signs, use `detect-text` instead. For more information on this feature, see the Google Cloud Vision documentation at <https://cloud.google.com/vision/docs/>. 

Language hints can be provided to Google Cloud Vision API. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting `language_hints` is not needed. Text detection returns an error if one or more of the specified languages is not one of the supported languages. (See https://cloud.google.com/vision/docs/languages.) To provide language hints run: 
    
    
    gcloud alpha ml vision detect-document --language-hints ja,ko

EXAMPLES
     To detect dense text in image 'gs://my_bucket/input_file': 
    
    
    gcloud alpha ml vision detect-document gs://my_bucket/input_file

POSITIONAL ARGUMENTS
    

`IMAGE_PATH`
     Path to the image to be analyzed. This can be either a local path or a URL. If you provide a local file, the contents will be sent directly to Google Cloud Vision. If you provide a URL, it must be in Google Cloud Storage format (gs://bucket/object) or an HTTP URL (<http://..>. or https://…) 
FLAGS
    

`--language-hints`=[`LANGUAGE_HINTS`,…]
     List of languages to use for text detection. 
`--model-version`=`MODEL_VERSION`; default="builtin/stable"
     Model version to use for the feature. `MODEL_VERSION` must be one of: `builtin/latest`, `builtin/stable`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `vision/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/vision/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ml vision detect-document](https://docs.cloud.google.com/sdk/gcloud/reference/ml/vision/detect-document)
    
    
    [gcloud beta ml vision detect-document](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/vision/detect-document)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
