---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run/
title: gcloud dataflow jobs run \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:27:09.777838+00:00
---

# gcloud dataflow jobs run  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataflow jobs run Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataflow jobs run - runs a job from the specified path 
SYNOPSIS
    

`gcloud dataflow jobs run` `JOB_NAME` `--gcs-location`=`GCS_LOCATION` [`--additional-experiments`=[`ADDITIONAL_EXPERIMENTS`,…]] [`--additional-pipeline-options`=[`ADDITIONAL_PIPELINE_OPTIONS`,…]] [`--additional-user-labels`=[`ADDITIONAL_USER_LABELS`,…]] [`--dataflow-kms-key`=`DATAFLOW_KMS_KEY`] [`--disable-public-ips`] [`--enable-streaming-engine`] [`--[no-]enable-turnkey-alerts`] [`--max-workers`=`MAX_WORKERS`] [`--network`=`NETWORK`] [`--num-workers`=`NUM_WORKERS`] [`--parameters`=[`PARAMETERS`,…]] [`--region`=`REGION_ID`] [`--service-account-email`=`SERVICE_ACCOUNT_EMAIL`] [`--staging-location`=`STAGING_LOCATION`] [`--subnetwork`=`SUBNETWORK`] [`--worker-machine-type`=`WORKER_MACHINE_TYPE`] [[`--[no-]update` : `--transform-name-mappings`=[`TRANSFORM_NAME_MAPPINGS`,…]]] [`--worker-region`=`WORKER_REGION` | `--worker-zone`=`WORKER_ZONE` | `--zone`=`ZONE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Runs a job from the specified path. 
POSITIONAL ARGUMENTS
    

`JOB_NAME`
     The unique name to assign to the job. 
REQUIRED FLAGS
    

`--gcs-location`=`GCS_LOCATION`
     The Google Cloud Storage location of the job template to run. (Must be a URL beginning with 'gs://'.) 
OPTIONAL FLAGS
    

`--additional-experiments`=[`ADDITIONAL_EXPERIMENTS`,…]
     Additional experiments to pass to the job. These experiments are appended to any experiments already set by the template. 
`--additional-pipeline-options`=[`ADDITIONAL_PIPELINE_OPTIONS`,…]
     Additional pipeline options to pass to the job for launching a Dataflow template. Example: --additional-pipeline-options=option1=value1,option2=value2 
`--additional-user-labels`=[`ADDITIONAL_USER_LABELS`,…]
     Additional user labels to pass to the job. Example: \--additional-user-labels='key1=value1,key2=value2' 
`--dataflow-kms-key`=`DATAFLOW_KMS_KEY`
     The Cloud KMS key to protect the job resources. 
`--disable-public-ips`
     The Cloud Dataflow workers must not use public IP addresses. Overrides the default `dataflow/disable_public_ips` property value for this command invocation. 
`--enable-streaming-engine`
     Enabling Streaming Engine for the streaming job. Overrides the default `dataflow/enable_streaming_engine` property value for this command invocation. 
`--[no-]enable-turnkey-alerts`
     Enable Turnkey Alerts for this job. Disabled by default. Use `--enable-turnkey-alerts` to enable and `--no-enable-turnkey-alerts` to disable. 
`--max-workers`=`MAX_WORKERS`
     The maximum number of workers to run. 
`--network`=`NETWORK`
     The Compute Engine network for launching instances to run your pipeline. 
`--num-workers`=`NUM_WORKERS`
     The initial number of workers to use. 
`--parameters`=[`PARAMETERS`,…]
     The parameters to pass to the job. 
`--region`=`REGION_ID`
     Region ID of the job's regional endpoint. Defaults to 'us-central1'. 
`--service-account-email`=`SERVICE_ACCOUNT_EMAIL`
     The service account to run the workers as. 
`--staging-location`=`STAGING_LOCATION`
     The Google Cloud Storage location to stage temporary files. (Must be a URL beginning with 'gs://'.) 
`--subnetwork`=`SUBNETWORK`
     The Compute Engine subnetwork for launching instances to run your pipeline. 
`--worker-machine-type`=`WORKER_MACHINE_TYPE`
     The type of machine to use for workers. Defaults to server-specified. 
`--[no-]update`
     Set this to true for streaming update jobs. Use `--update` to enable and `--no-update` to disable. 
`--transform-name-mappings`=[`TRANSFORM_NAME_MAPPINGS`,…]
     Transform name mappings for the streaming update job. 
Worker location options. 

At most one of these can be specified: 

`--worker-region`=`WORKER_REGION`
     The region to run the workers in. 
`--worker-zone`=`WORKER_ZONE`
     The zone to run the workers in. 
`--zone`=`ZONE`
     (DEPRECATED) The zone to run the workers in. 

The --zone option is deprecated; use --worker-region or --worker-zone instead. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta dataflow jobs run](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/jobs/run)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
