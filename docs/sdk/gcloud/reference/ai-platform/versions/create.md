---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/versions/create/
title: gcloud ai-platform versions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:52.957762+00:00
---

# gcloud ai-platform versions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai-platform/versions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai-platform versions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai-platform versions create - create a new AI Platform version 
SYNOPSIS
    

`gcloud ai-platform versions create` `VERSION` `--model`=`MODEL` [`--accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]] [`--async`] [`--config`=`CONFIG`] [`--description`=`DESCRIPTION`] [`--framework`=`FRAMEWORK`] [`--labels`=[`KEY`=`VALUE`,…]] [`--machine-type`=`MACHINE_TYPE`] [`--origin`=`ORIGIN`] [`--python-version`=`PYTHON_VERSION`] [`--region`=`REGION`] [`--runtime-version`=`RUNTIME_VERSION`] [`--staging-bucket`=`STAGING_BUCKET`] [`--max-nodes`=`MAX_NODES` `--metric-targets`=[`METRIC-NAME`=`TARGET`,…] `--min-nodes`=`MIN_NODES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Creates a new version of an AI Platform model. 

For more details on managing AI Platform models and versions see <https://cloud.google.com/ai-platform/prediction/docs/managing-models-jobs>

EXAMPLES
     To create an AI Platform version model with the version ID 'versionId' and with the name 'model-name', run: 
    
    
    gcloud ai-platform versions create versionId --model=model-name

POSITIONAL ARGUMENTS
    

`VERSION`
     Name of the model version. 
REQUIRED FLAGS
    

`--model`=`MODEL`
     Name of the model. 
OPTIONAL FLAGS
    

`--accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]
     Manage the accelerator config for GPU serving. When deploying a model with Compute Engine Machine Types, a GPU accelerator may also be selected. 

`type`
     The type of the accelerator. Choices are 'nvidia-tesla-a100', 'nvidia-tesla-k80', 'nvidia-tesla-p100', 'nvidia-tesla-p4', 'nvidia-tesla-t4', 'nvidia-tesla-v100'. 
`count`
     The number of accelerators to attach to each machine running the job. If not specified, the default value is 1. Your model must be specially designed to accommodate more than 1 accelerator per machine. To configure how many replicas your model has, set the `manualScaling` or `autoScaling` parameters. 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--config`=`CONFIG`
     Path to a YAML configuration file containing configuration parameters for the [Version](https://cloud.google.com/ai-platform/prediction/docs/reference/rest/v1/projects.models.versions) to create. 

The file is in YAML format. Note that not all attributes of a version are configurable; available attributes (with example values) are: 
    
    
    description: A free-form description of the version.
    deploymentUri: gs://path/to/source
    runtimeVersion: '2.1'
    #  Set only one of either manualScaling or autoScaling.
    manualScaling:
      nodes: 10  # The number of nodes to allocate for this model.
    autoScaling:
      minNodes: 0  # The minimum number of nodes to allocate for this model.
    labels:
      user-defined-key: user-defined-value

The name of the version must always be specified via the required VERSION argument. 

Only one of manualScaling or autoScaling can be specified. If both are specified in same yaml file an error will be returned. 

If an option is specified both in the configuration file and via command-line arguments, the command-line arguments override the configuration file. 

`--description`=`DESCRIPTION`
     Description of the version. 
`--framework`=`FRAMEWORK`
     ML framework used to train this version of the model. If not specified, defaults to 'tensorflow'. `FRAMEWORK` must be one of: `scikit-learn`, `tensorflow`, `xgboost`. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--machine-type`=`MACHINE_TYPE`
     Type of machine on which to serve the model. Currently only applies to online prediction. For available machine types, see <https://cloud.google.com/ai-platform/prediction/docs/machine-types-online-prediction#available_machine_types>. 
`--origin`=`ORIGIN`
     Location of `model/` "directory" (see https://cloud.google.com/ai-platform/prediction/docs/deploying-models#upload-model). 

This overrides `deploymentUri` in the `--config` file. If this flag is not passed, `deploymentUri` `must` be specified in the file from `--config`. 

Can be a Cloud Storage (`gs://`) path or local file path (no prefix). In the latter case the files will be uploaded to Cloud Storage and a `--staging-bucket` argument is required. 

`--python-version`=`PYTHON_VERSION`
     Version of Python used when creating the version. Choices are 3.7, 3.5, and 2.7. However, this value must be compatible with the chosen runtime version for the job. 

Must be used with a compatible runtime version: 

  * 3.7 is compatible with runtime versions 1.15 and later. 
  * 3.5 is compatible with runtime versions 1.4 through 1.14. 
  * 2.7 is compatible with runtime versions 1.15 and earlier. 


`--region`=`REGION`
     Google Cloud region of the regional endpoint to use for this command. For the global endpoint, the region needs to be specified as `global`. 

Learn more about regional endpoints and see a list of available regions: <https://cloud.google.com/ai-platform/prediction/docs/regional-endpoints>

`REGION` must be one of: `global`, `asia-east1`, `asia-northeast1`, `asia-southeast1`, `australia-southeast1`, `europe-west1`, `europe-west2`, `europe-west3`, `europe-west4`, `northamerica-northeast1`, `us-central1`, `us-east1`, `us-east4`, `us-west1`. 

`--runtime-version`=`RUNTIME_VERSION`
     AI Platform runtime version for this job. Must be specified unless \--master-image-uri is specified instead. It is defined in documentation along with the list of supported versions: <https://cloud.google.com/ai-platform/prediction/docs/runtime-version-list>
`--staging-bucket`=`STAGING_BUCKET`
     Bucket in which to stage training archives. 

Required only if a file upload is necessary (that is, other flags include local paths) and no other flags implicitly specify an upload path. 

Configure the autoscaling settings to be deployed. 
`--max-nodes`=`MAX_NODES`
     The maximum number of nodes to scale this model under load. 
`--metric-targets`=[`METRIC-NAME`=`TARGET`,…]
     List of key-value pairs to set as metrics' target for autoscaling. Autoscaling could be based on CPU usage or GPU duty cycle, valid key could be cpu-usage or gpu-duty-cycle. 
`--min-nodes`=`MIN_NODES`
     The minimum number of nodes to scale this model under load. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai-platform versions create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai-platform/versions/create)
    
    
    [gcloud beta ai-platform versions create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai-platform/versions/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
