---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/deploy/
title: gcloud ai model-garden models deploy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:09:12.143234+00:00
---

# gcloud ai model-garden models deploy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/deploy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai model-garden models deploy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai model-garden models deploy - deploy a model in Model Garden to a Vertex AI endpoint 
SYNOPSIS
    

`gcloud ai model-garden models deploy` `--model`=`MODEL` [`--accelerator-count`=`ACCELERATOR_COUNT`] [`--accelerator-type`=`ACCELERATOR_TYPE`] [`--accept-eula`] [`--asynchronous`] [`--container-args`=[`ARG`,…]] [`--container-command`=[`COMMAND`,…]] [`--container-deployment-timeout-seconds`=`CONTAINER_DEPLOYMENT_TIMEOUT_SECONDS`] [`--container-env-vars`=[`KEY`=`VALUE`,…]] [`--container-grpc-ports`=[`PORT`,…]] [`--container-health-probe-exec`=[`HEALTH_PROBE_EXEC`,…]] [`--container-health-probe-period-seconds`=`CONTAINER_HEALTH_PROBE_PERIOD_SECONDS`] [`--container-health-probe-timeout-seconds`=`CONTAINER_HEALTH_PROBE_TIMEOUT_SECONDS`] [`--container-health-route`=`CONTAINER_HEALTH_ROUTE`] [`--container-image-uri`=`CONTAINER_IMAGE_URI`] [`--container-ports`=[`PORT`,…]] [`--container-predict-route`=`CONTAINER_PREDICT_ROUTE`] [`--container-shared-memory-size-mb`=`CONTAINER_SHARED_MEMORY_SIZE_MB`] [`--container-startup-probe-exec`=[`STARTUP_PROBE_EXEC`,…]] [`--container-startup-probe-period-seconds`=`CONTAINER_STARTUP_PROBE_PERIOD_SECONDS`] [`--container-startup-probe-timeout-seconds`=`CONTAINER_STARTUP_PROBE_TIMEOUT_SECONDS`] [`--disable-dedicated-endpoint`] [`--enable-fast-tryout`] [`--endpoint-display-name`=`ENDPOINT_DISPLAY_NAME`] [`--hugging-face-access-token`=`HUGGING_FACE_ACCESS_TOKEN`] [`--machine-type`=`MACHINE_TYPE`] [`--region`=`REGION`] [`--reservation-affinity`=[`key`=`KEY`],[`reservation-affinity-type`=`RESERVATION-AFFINITY-TYPE`],[`values`=`VALUES`]] [`--spot`] [`--system-labels`=[`KEY`=`VALUE`,…]] [`--use-dedicated-endpoint`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To deploy a Model Garden model `google/gemma2/gemma2-9b` under project `example` in region `us-central1`, run: 
    
    
    gcloud ai model-garden models deploy --model=google/gemma2@gemma-2-9b --project=example --region=us-central1

To deploy a Hugging Face model `meta-llama/Meta-Llama-3-8B` under project `example` in region `us-central1`, run: 
    
    
    gcloud ai model-garden models deploy --model=meta-llama/Meta-Llama-3-8B --hugging-face-access-token={hf_token} --project=example --region=us-central1

REQUIRED FLAGS
    

`--model`=`MODEL`
     The model to be deployed. If it is a Model Garden model, it should be in the format of `{publisher_name}/{model_name}@{model_version_name}, e.g. `google/gemma2@gemma-2-2b`. If it is a Hugging Face model, it should be in the convention of Hugging Face models, e.g. `meta-llama/Meta-Llama-3-8B`. If it is a Custom Weights model, it should be in the format of `gs://{gcs_bucket_uri}`, e.g. `gs://-model-garden-public-us/llama3.1/Meta-Llama-3.1-8B-Instruct`. `
OPTIONAL FLAGS
    

`--accelerator-count`=`ACCELERATOR_COUNT`
     The accelerator count to serve the model. Accelerator count should be non-negative. 
`--accelerator-type`=`ACCELERATOR_TYPE`
     The accelerator type to serve the model. It should be a supported accelerator type from the verified deployment configurations of the model. Use `[gcloud ai model-garden models list-deployment-config](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list-deployment-config)` to check the supported accelerator types. 
`--accept-eula`
     When set, the user accepts the End User License Agreement (EULA) of the model. 
`--asynchronous`
     If set to true, the command will terminate immediately and not keep polling the operation status. 
`--container-args`=[`ARG`,…]
     Comma-separated arguments passed to the command run by the container image. If not specified and no `--command` is provided, the container image's default command is used. 
`--container-command`=[`COMMAND`,…]
     Entrypoint for the container image. If not specified, the container image's default entrypoint is run. 
`--container-deployment-timeout-seconds`=`CONTAINER_DEPLOYMENT_TIMEOUT_SECONDS`
     Deployment timeout in seconds. 
`--container-env-vars`=[`KEY`=`VALUE`,…]
     List of key-value pairs to set as environment variables. 
`--container-grpc-ports`=[`PORT`,…]
     Container ports to receive grpc requests at. Must be a number between 1 and 65535, inclusive. 
`--container-health-probe-exec`=[`HEALTH_PROBE_EXEC`,…]
     Exec specifies the action to take. Used by health probe. An example of this argument would be ["cat", "/tmp/healthy"]. 
`--container-health-probe-period-seconds`=`CONTAINER_HEALTH_PROBE_PERIOD_SECONDS`
     How often (in seconds) to perform the health probe. Default to 10 seconds. Minimum value is 1. 
`--container-health-probe-timeout-seconds`=`CONTAINER_HEALTH_PROBE_TIMEOUT_SECONDS`
     Number of seconds after which the health probe times out. Defaults to 1 second. Minimum value is 1. 
`--container-health-route`=`CONTAINER_HEALTH_ROUTE`
     HTTP path to send health checks to inside the container. 
`--container-image-uri`=`CONTAINER_IMAGE_URI`
     URI of the Model serving container file in the Container Registry (e.g. gcr.io/myproject/server:latest). 
`--container-ports`=[`PORT`,…]
     Container ports to receive http requests at. Must be a number between 1 and 65535, inclusive. 
`--container-predict-route`=`CONTAINER_PREDICT_ROUTE`
     HTTP path to send prediction requests to inside the container. 
`--container-shared-memory-size-mb`=`CONTAINER_SHARED_MEMORY_SIZE_MB`
     The amount of the VM memory to reserve as the shared memory for the model in megabytes. 
`--container-startup-probe-exec`=[`STARTUP_PROBE_EXEC`,…]
     Exec specifies the action to take. Used by startup probe. An example of this argument would be ["cat", "/tmp/healthy"]. 
`--container-startup-probe-period-seconds`=`CONTAINER_STARTUP_PROBE_PERIOD_SECONDS`
     How often (in seconds) to perform the startup probe. Default to 10 seconds. Minimum value is 1. 
`--container-startup-probe-timeout-seconds`=`CONTAINER_STARTUP_PROBE_TIMEOUT_SECONDS`
     Number of seconds after which the startup probe times out. Defaults to 1 second. Minimum value is 1. 
`--disable-dedicated-endpoint`
     If true, the dedicated endpoint will be disabled and the deployed model will be exposed through the shared DNS. 
`--enable-fast-tryout`
     If True, model will be deployed using faster deployment path. Useful for quick experiments. Not for production workloads. Only available for most popular models with certain machine types. 
`--endpoint-display-name`=`ENDPOINT_DISPLAY_NAME`
     Display name of the endpoint with the deployed model. 
`--hugging-face-access-token`=`HUGGING_FACE_ACCESS_TOKEN`
     The access token from Hugging Face needed to read the model artifacts of gated models. It is only needed when the Hugging Face model to deploy is gated. 
`--machine-type`=`MACHINE_TYPE`
     The machine type to deploy the model to. It should be a supported machine type from the deployment configurations of the model. Use `[gcloud ai model-garden models list-deployment-config](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list-deployment-config)` to check the supported machine types. 
Region resource - Cloud region to deploy the model. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


`--reservation-affinity`=[`key`=`KEY`],[`reservation-affinity-type`=`RESERVATION-AFFINITY-TYPE`],[`values`=`VALUES`]
     A ReservationAffinity can be used to configure a Vertex AI resource (e.g., a DeployedModel) to draw its Compute Engine resources from a Shared Reservation, or exclusively from on-demand capacity. 
`--spot`
     If true, schedule the deployment workload on Spot VM. 
`--system-labels`=[`KEY`=`VALUE`,…]
     System labels for Model Garden deployments. 
`--use-dedicated-endpoint`
     If true, the endpoint will be exposed through a dedicated DNS. Your request to the dedicated DNS will be isolated from other users' traffic and will have better performance and reliability. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai model-garden models deploy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/deploy)
    
    
    [gcloud beta ai model-garden models deploy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/deploy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
