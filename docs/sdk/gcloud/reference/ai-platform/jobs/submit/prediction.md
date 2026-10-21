---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction/
title: gcloud ai-platform jobs submit prediction \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:24:45.317914+00:00
---

# gcloud ai-platform jobs submit prediction  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/jobs/submit/prediction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai-platform jobs submit prediction Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai-platform jobs submit prediction - start an AI Platform batch prediction job 
SYNOPSIS
    

`gcloud ai-platform jobs submit prediction` `JOB` `--data-format`=`DATA_FORMAT` `--input-paths`=`INPUT_PATH`,[`INPUT_PATH`,…] `--output-path`=`OUTPUT_PATH` `--region`=`REGION` (`--model`=`MODEL` | `--model-dir`=`MODEL_DIR`) [`--batch-size`=`BATCH_SIZE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--max-worker-count`=`MAX_WORKER_COUNT`] [`--runtime-version`=`RUNTIME_VERSION`] [`--signature-name`=`SIGNATURE_NAME`] [`--version`=`VERSION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Start an AI Platform batch prediction job. 
POSITIONAL ARGUMENTS
    

`JOB`
     Name of the batch prediction job. 
REQUIRED FLAGS
    

`--data-format`=`DATA_FORMAT`
     Data format of the input files. `DATA_FORMAT` must be one of: 

`text`
     Text and JSON files; for text files, see https://www.tensorflow.org/guide/datasets#consuming_text_data, for JSON files, see <https://cloud.google.com/ai-platform/prediction/docs/overview#batch_prediction_input_data>
`tf-record`
     TFRecord files; see <https://www.tensorflow.org/guide/datasets#consuming_tfrecord_data>
`tf-record-gzip`
     GZIP-compressed TFRecord files. 
`--input-paths`=`INPUT_PATH`,[`INPUT_PATH`,…]
     Cloud Storage paths to the instances to run prediction on. 

Wildcards (`*`) accepted at the `end` of a path. More than one path can be specified if multiple file patterns are needed. For example, 
    
    
    gs://my-bucket/instances*,gs://my-bucket/other-instances1

will match any objects whose names start with `instances` in `my-bucket` as well as the `other-instances1` bucket, while 
    
    
    gs://my-bucket/instance-dir/*

will match any objects in the `instance-dir` "directory" (since directories aren't a first-class Cloud Storage concept) of `my-bucket`. 

`--output-path`=`OUTPUT_PATH`
     Cloud Storage path to which to save the output. Example: gs://my-bucket/output. 
`--region`=`REGION`
     The Compute Engine region to run the job in. 
Exactly one of these must be specified: 

`--model`=`MODEL`
     Name of the model to use for prediction. 
`--model-dir`=`MODEL_DIR`
     Cloud Storage location where the model files are located. 
OPTIONAL FLAGS
    

`--batch-size`=`BATCH_SIZE`
     The number of records per batch. The service will buffer batch_size number of records in memory before invoking TensorFlow. Defaults to 64 if not specified. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--max-worker-count`=`MAX_WORKER_COUNT`
     The maximum number of workers to be used for parallel processing. Defaults to 10 if not specified. 
`--runtime-version`=`RUNTIME_VERSION`
     AI Platform runtime version for this job. Must be specified unless \--master-image-uri is specified instead. It is defined in documentation along with the list of supported versions: <https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list>
`--signature-name`=`SIGNATURE_NAME`
     Name of the signature defined in the SavedModel to use for this job. Defaults to DEFAULT_SERVING_SIGNATURE_DEF_KEY in https://www.tensorflow.org/api_docs/python/tf/compat/v1/saved_model/signature_constants, which is "serving_default". Only applies to TensorFlow models. 
`--version`=`VERSION`
     Model version to be used. 

This flag may only be given if --model is specified. If unspecified, the default version of the model will be used. To list versions for a model, run 
    
    
    [gcloud ai-platform versions list](https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/versions/list)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai-platform jobs submit prediction](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/jobs/submit/prediction)
    
    
    [gcloud beta ai-platform jobs submit prediction](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/jobs/submit/prediction)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
