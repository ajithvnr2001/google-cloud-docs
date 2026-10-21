---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict/
title: gcloud alpha ai-platform local predict \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:00:11.237015+00:00
---

# gcloud alpha ai-platform local predict  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/local/predict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai-platform local predict Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai-platform local predict - run prediction locally 
SYNOPSIS
    

`gcloud alpha ai-platform local predict` `--model-dir`=`MODEL_DIR` (`--json-instances`=`JSON_INSTANCES` | `--json-request`=`JSON_REQUEST` | `--text-instances`=`TEXT_INSTANCES`) [`--framework`=`FRAMEWORK`] [`--signature-name`=`SIGNATURE_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha ai-platform local predict` performs prediction locally with the given instances. It requires the [TensorFlow SDK](https://www.tensorflow.org/install) be installed locally. The output format mirrors `[gcloud ai-platform predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/predict)` (online prediction). 

You cannot use this command with custom prediction routines. 

REQUIRED FLAGS
    

`--model-dir`=`MODEL_DIR`
     Path to the model. 
Exactly one of these must be specified: 

`--json-instances`=`JSON_INSTANCES`
     Path to a local file from which instances are read. Instances are in JSON format; newline delimited. 

An example of the JSON instances file: 
    
    
    {"images": [0.0, …, 0.1], "key": 3}
    {"images": [0.0, …, 0.1], "key": 2}
    …

This flag accepts "-" for stdin. 

`--json-request`=`JSON_REQUEST`
     Path to a local file containing the body of JSON request. 

An example of a JSON request: 
    
    
    {
      "instances": [
        {"x": [1, 2], "y": [3, 4]},
        {"x": [-1, -2], "y": [-3, -4]}
      ]
    }

This flag accepts "-" for stdin. 

`--text-instances`=`TEXT_INSTANCES`
     Path to a local file from which instances are read. Instances are in UTF-8 encoded text format; newline delimited. 

An example of the text instances file: 
    
    
    107,4.9,2.5,4.5,1.7
    100,5.7,2.8,4.1,1.3
    …

This flag accepts "-" for stdin. 

OPTIONAL FLAGS
    

`--framework`=`FRAMEWORK`
     ML framework used to train this version of the model. If not specified, defaults to 'tensorflow'. `FRAMEWORK` must be one of: `scikit-learn`, `tensorflow`, `xgboost`. 
`--signature-name`=`SIGNATURE_NAME`
     Name of the signature defined in the SavedModel to use for this job. Defaults to DEFAULT_SERVING_SIGNATURE_DEF_KEY in https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_constants, which is "serving_default". Only applies to TensorFlow models. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ai-platform local predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/local/predict)
    
    
    [gcloud beta ai-platform local predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/local/predict)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
