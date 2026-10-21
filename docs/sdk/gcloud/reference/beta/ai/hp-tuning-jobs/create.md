---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create/
title: gcloud beta ai hp-tuning-jobs create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:15.916802+00:00
---

# gcloud beta ai hp-tuning-jobs create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/hp-tuning-jobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai hp-tuning-jobs create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai hp-tuning-jobs create - create a hyperparameter tuning job 
SYNOPSIS
    

`gcloud beta ai hp-tuning-jobs create` `--config`=`CONFIG` `--display-name`=`DISPLAY_NAME` [`--algorithm`=`ALGORITHM`] [`--enable-dashboard-access`] [`--enable-web-access`] [`--labels`=[`KEY`=`VALUE`,…]] [`--max-trial-count`=`MAX_TRIAL_COUNT`] [`--network`=`NETWORK`] [`--parallel-trial-count`=`PARALLEL_TRIAL_COUNT`] [`--region`=`REGION`] [`--service-account`=`SERVICE_ACCOUNT`] [`--kms-key`=`KMS_KEY` : `--kms-keyring`=`KMS_KEYRING` `--kms-location`=`KMS_LOCATION` `--kms-project`=`KMS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a hyperparameter tuning job. 
EXAMPLES
     To create a job named ``test`` under project ``example`` in region ``us-central1``, run: 
    
    
    gcloud beta ai hp-tuning-jobs create --region=us-central1 --project=example --config=config.yaml --display-name=test

REQUIRED FLAGS
    

`--config`=`CONFIG`
     Path to the job configuration file. This file should be a YAML document containing a HyperparameterTuningSpec. If an option is specified both in the configuration file **and** via command line arguments, the command line arguments override the configuration file. 

Example(YAML): 
    
    
    displayName: TestHpTuningJob
    maxTrialCount: 1
    parallelTrialCount: 1
    studySpec:
      metrics:
      - metricId: x
        goal: MINIMIZE
      parameters:
      - parameterId: z
        integerValueSpec:
          minValue: 1
          maxValue: 100
      algorithm: RANDOM_SEARCH
    trialJobSpec:
      workerPoolSpecs:
      - machineSpec:
          machineType: n1-standard-4
        replicaCount: 1
        containerSpec:
          imageUri: gcr.io/ucaip-test/ucaip-training-test

`--display-name`=`DISPLAY_NAME`
     Display name of the hyperparameter tuning job to create. 
OPTIONAL FLAGS
    

`--algorithm`=`ALGORITHM`
     Search algorithm specified for the given study. `ALGORITHM` must be one of: `algorithm-unspecified`, `grid-search`, `random-search`. 
`--enable-dashboard-access`
     Whether you want Vertex AI to enable dashboard built on the training containers. If set to ``true``, you can access the dashboard at the URIs given by CustomJob.web_access_uris or Trial.web_access_uris (within HyperparameterTuningJob.trials). 
`--enable-web-access`
     Whether you want Vertex AI to enable [interactive shell access](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell) to training containers. If set to ``true``, you can access interactive shells at the URIs given by CustomJob.web_access_uris or Trial.web_access_uris (within HyperparameterTuningJob.trials). 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--max-trial-count`=`MAX_TRIAL_COUNT`
     Desired total number of trials. The default value is 1. 
`--network`=`NETWORK`
     Full name of the Google Compute Engine network to which the Job is peered with. Private services access must already have been configured. If unspecified, the Job is not peered with any network. 
`--parallel-trial-count`=`PARALLEL_TRIAL_COUNT`
     Desired number of Trials to run in parallel. The default value is 1. 
Region resource - Cloud region to create a hyperparameter tuning job. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
     The email address of a service account to use when running the training appplication. You must have the `iam.serviceAccounts.actAs` permission for the specified service account. 
Key resource - The Cloud KMS (Key Management Service) cryptokey that will be used to protect the hyperparameter tuning job. The 'Vertex AI Service Agent' service account must hold permission 'Cloud KMS CryptoKey Encrypter/Decrypter'. The arguments in this group can be used to specify the attributes of this resource. 
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
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai hp-tuning-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/ai/hp-tuning-jobs/create)
    
    
    [gcloud alpha ai hp-tuning-jobs create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/hp-tuning-jobs/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
