---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai/tuning-jobs/create/
title: gcloud ai tuning-jobs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:52.914422+00:00
---

# gcloud ai tuning-jobs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai/tuning-jobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai tuning-jobs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai tuning-jobs create - create a supervised fine-tuning job 
SYNOPSIS
    

`gcloud ai tuning-jobs create` `--source-model`=`SOURCE_MODEL` `--training-dataset-uri`=`TRAINING_DATASET_URI` [`--adapter-size`=`ADAPTER_SIZE`] [`--description`=`DESCRIPTION`] [`--epoch-count`=`EPOCH_COUNT`] [`--export-last-checkpoint-only`] [`--labels`=[`KEY`=`VALUE`,…]] [`--learning-rate-multiplier`=`LEARNING_RATE_MULTIPLIER`] [`--region`=`REGION`] [`--service-account`=`SERVICE_ACCOUNT`] [`--tuned-model-display-name`=`TUNED_MODEL_DISPLAY_NAME`] [`--validation-dataset-uri`=`VALIDATION_DATASET_URI`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command creates a new supervised fine-tuning (SFT) tuning job in Vertex AI. The job tunes a base foundation model using the provided training dataset to produce a customized tuned model. 
EXAMPLES
     To create a tuning job that fine-tunes ``gemini-1.0-pro-002`` in region ``us-central1``, run: 
    
    
    gcloud ai tuning-jobs create --region=us-central1 --source-model=gemini-1.0-pro-002 --training-dataset-uri=gs://my-bucket/training.jsonl --tuned-model-display-name=my-tuned-model

To create a tuning job with labels and hyperparameters: 
    
    
    gcloud ai tuning-jobs create --region=us-central1 --source-model=gemini-1.0-pro-002 --training-dataset-uri=gs://my-bucket/training.jsonl --validation-dataset-uri=gs://my-bucket/validation.jsonl --epoch-count=3 --learning-rate-multiplier=1.0 --labels=env=prod,team=ml

REQUIRED FLAGS
    

`--source-model`=`SOURCE_MODEL`
     The base model to tune, e.g. ``gemini-1.0-pro-002`` or ``meta/llama3_1@llama-3.1-8b``. To start tuning from a custom checkpoint or a previously tuned open model, also pass ``--custom-base-model``. 
`--training-dataset-uri`=`TRAINING_DATASET_URI`
     Cloud Storage URI of the training dataset. The dataset must be formatted as a JSONL file. 
OPTIONAL FLAGS
    

`--adapter-size`=`ADAPTER_SIZE`
     Adapter size for parameter-efficient fine-tuning. This is only applicable when using a PEFT-compatible model. `ADAPTER_SIZE` must be one of: `1`, `2`, `4`, `8`, `16`, `32`. 
`--description`=`DESCRIPTION`
     Description of the tuning job. 
`--epoch-count`=`EPOCH_COUNT`
     Number of training epochs. If not set, a default value will be calculated based on the training dataset size. 
`--export-last-checkpoint-only`
     If set, disable intermediate checkpoints for the tuning job and only export the last checkpoint. Default is to enable intermediate checkpoints. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--learning-rate-multiplier`=`LEARNING_RATE_MULTIPLIER`
     Multiplier for adjusting the default learning rate. Only applicable to Gemini models. Mutually exclusive with `--learning-rate`. If neither flag is set, a default value will be calculated based on the training dataset size. 
Region resource - Cloud region to create a tuning job. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--region` on the command line with a fully specified name; 
  * set the property `ai/region` with a fully specified name; 
  * choose one from the prompted list of available regions with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--region`=`REGION`
     ID of the region or fully qualified identifier for the region. 

To set the `region` attribute: 

  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


`--service-account`=`SERVICE_ACCOUNT`
     The service account that the tuning job runs as. If not specified, the Vertex AI Custom Code Service Agent is used. 
`--tuned-model-display-name`=`TUNED_MODEL_DISPLAY_NAME`
     Display name of the tuned model. 
`--validation-dataset-uri`=`VALIDATION_DATASET_URI`
     Cloud Storage URI of the optional validation dataset. The dataset must be formatted as a JSONL file. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the tuning job. The 'Vertex AI Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
`--kms-key`=`KMS_KEY`
     ID of the key or fully qualified identifier for the key. 

To set the `kms-key` attribute: 

  * provide the argument `--kms-key` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--kms-keyring`=`KMS_KEYRING`
     The KMS keyring of the key. 

To set the `kms-keyring` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-keyring` on the command line. 


`--kms-location`=`KMS_LOCATION`
     The Google Cloud location for the key. 

To set the `kms-location` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-location` on the command line. 


`--kms-project`=`KMS_PROJECT`
     The Google Cloud project for the key. 

To set the `kms-project` attribute: 

  * provide the argument `--kms-key` on the command line with a fully specified name; 
  * provide the argument `--kms-project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai tuning-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/tuning-jobs/create)
    
    
    [gcloud beta ai tuning-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/tuning-jobs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-16 UTC."],[],[]] 
