---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/flex-template/run/
title: gcloud beta dataflow flex-template run \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:17.760129+00:00
---

# gcloud beta dataflow flex-template run  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/flex-template/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataflow flex-template run Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataflow flex-template run - runs a job from the specified path 
SYNOPSIS
    

`gcloud beta dataflow flex-template run` `JOB_NAME` `--template-file-gcs-location`=`TEMPLATE_FILE_GCS_LOCATION` [`--additional-experiments`=[`ADDITIONAL_EXPERIMENTS`,…]] [`--additional-pipeline-options`=[`ADDITIONAL_PIPELINE_OPTIONS`,…]] [`--additional-user-labels`=[`ADDITIONAL_USER_LABELS`,…]] [`--dataflow-kms-key`=`DATAFLOW_KMS_KEY`] [`--disable-public-ips`] [`--enable-streaming-engine`] [`--[no-]enable-turnkey-alerts`] [`--flexrs-goal`=`FLEXRS_GOAL`] [`--launcher-machine-type`=`LAUNCHER_MACHINE_TYPE`] [`--launcher-vm-timeout-secs`=`LAUNCHER_VM_TIMEOUT_SECS`] [`--max-workers`=`MAX_WORKERS`] [`--network`=`NETWORK`] [`--num-workers`=`NUM_WORKERS`] [`--parameters`=[`PARAMETERS`,…]] [`--region`=`REGION_ID`] [`--service-account-email`=`SERVICE_ACCOUNT_EMAIL`] [`--staging-location`=`STAGING_LOCATION`] [`--subnetwork`=`SUBNETWORK`] [`--temp-location`=`TEMP_LOCATION`] [`--worker-machine-type`=`WORKER_MACHINE_TYPE`] [[`--[no-]update` : `--transform-name-mappings`=[`TRANSFORM_NAME_MAPPINGS`,…]]] [`--worker-region`=`WORKER_REGION` | `--worker-zone`=`WORKER_ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Runs a job from the specified flex template gcs path. 
EXAMPLES
     To run a job from the flex template, run: 
    
    
    gcloud beta dataflow flex-template run my-job --template-file-gcs-location=gs://flex-template-path --region=europe-west1 --parameters=input="gs://input",output="gs://output-path" --max-workers=5

POSITIONAL ARGUMENTS
    

`JOB_NAME`
     Unique name to assign to the job. 
REQUIRED FLAGS
    

`--template-file-gcs-location`=`TEMPLATE_FILE_GCS_LOCATION`
     Google Cloud Storage location of the flex template to run. (Must be a URL beginning with 'gs://'.) 
OPTIONAL FLAGS
    

`--additional-experiments`=[`ADDITIONAL_EXPERIMENTS`,…]
     Additional experiments to pass to the job. Example: \--additional-experiments=experiment1,experiment2=value2 
`--additional-pipeline-options`=[`ADDITIONAL_PIPELINE_OPTIONS`,…]
     Additional pipeline options to pass to the job. Example: \--additional-pipeline-options=option1=value1,option2=value2 
`--additional-user-labels`=[`ADDITIONAL_USER_LABELS`,…]
     Additional user labels to pass to the job. Example: \--additional-user-labels='key1=value1,key2=value2' 
`--dataflow-kms-key`=`DATAFLOW_KMS_KEY`
     Cloud KMS key to protect the job resources. 
`--disable-public-ips`
     Cloud Dataflow workers must not use public IP addresses. Overrides the default `dataflow/disable_public_ips` property value for this command invocation. 
`--enable-streaming-engine`
     Enabling Streaming Engine for the streaming job. Overrides the default `dataflow/enable_streaming_engine` property value for this command invocation. 
`--[no-]enable-turnkey-alerts`
     Enable Turnkey Alerts for this job. Disabled by default. Use `--enable-turnkey-alerts` to enable and `--no-enable-turnkey-alerts` to disable. 
`--flexrs-goal`=`FLEXRS_GOAL`
     FlexRS goal for the flex template job. `FLEXRS_GOAL` must be one of: `COST_OPTIMIZED`, `SPEED_OPTIMIZED`. 
`--launcher-machine-type`=`LAUNCHER_MACHINE_TYPE`
     The machine type to use for launching the job. If not set, Dataflow will select a default machine type. 
`--launcher-vm-timeout-secs`=`LAUNCHER_VM_TIMEOUT_SECS`
     The timeout in seconds for the launcher VM. If not set, Dataflow uses a default timeout. 
`--max-workers`=`MAX_WORKERS`
     Maximum number of workers to run. 
`--network`=`NETWORK`
     Compute Engine network for launching instances to run your pipeline. 
`--num-workers`=`NUM_WORKERS`
     Initial number of workers to use. 
`--parameters`=[`PARAMETERS`,…]
     Parameters to pass to the job. For information about specifying an alternative delimiter, see `[gcloud topic escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping)`. 
`--region`=`REGION_ID`
     Region ID of the job's regional endpoint. Defaults to 'us-central1'. 
`--service-account-email`=`SERVICE_ACCOUNT_EMAIL`
     Service account to run the workers as. 
`--staging-location`=`STAGING_LOCATION`
     Default Google Cloud Storage location to stage local files.(Must be a URL beginning with 'gs://'.) 
`--subnetwork`=`SUBNETWORK`
     Compute Engine subnetwork for launching instances to run your pipeline. 
`--temp-location`=`TEMP_LOCATION`
     Default Google Cloud Storage location to stage temporary files. If not set, defaults to the value for --staging-location.(Must be a URL beginning with 'gs://'.) 
`--worker-machine-type`=`WORKER_MACHINE_TYPE`
     Type of machine to use for workers. Defaults to server-specified. 
`--[no-]update`
     Set this to true for streaming update jobs. Use `--update` to enable and `--no-update` to disable. 
`--transform-name-mappings`=[`TRANSFORM_NAME_MAPPINGS`,…]
     Transform name mappings for the streaming update job. 
At most one of these can be specified: 

`--worker-region`=`WORKER_REGION`
     Region to run the workers in. 
`--worker-zone`=`WORKER_ZONE`
     Zone to run the workers in. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud dataflow flex-template run](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/flex-template/run)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
