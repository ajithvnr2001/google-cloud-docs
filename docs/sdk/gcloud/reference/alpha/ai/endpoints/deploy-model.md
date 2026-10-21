---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model/
title: gcloud alpha ai endpoints deploy-model \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:47:34.393595+00:00
---

# gcloud alpha ai endpoints deploy-model  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha ai endpoints deploy-model Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha ai endpoints deploy-model - deploy a model to an existing Vertex AI endpoint 
SYNOPSIS
    

`gcloud alpha ai endpoints deploy-model` (`ENDPOINT` : `--region`=`REGION`) `--display-name`=`DISPLAY_NAME` `--model`=`MODEL` [`--accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]] [`--autoscaling-metric-specs`=[`METRIC-NAME`=`TARGET`,…]] [`--deployed-model-id`=`DEPLOYED_MODEL_ID`] [`--enable-access-logging`] [`--enable-container-logging`] [`--gpu-partition-size`=`GPU_PARTITION_SIZE`] [`--idle-scaledown-period`=`IDLE_SCALEDOWN_PERIOD`] [`--initial-replica-count`=`INITIAL_REPLICA_COUNT`] [`--machine-type`=`MACHINE_TYPE`] [`--max-replica-count`=`MAX_REPLICA_COUNT`] [`--min-replica-count`=`MIN_REPLICA_COUNT`] [`--min-scaleup-period`=`MIN_SCALEUP_PERIOD`] [`--multihost-gpu-node-count`=`MULTIHOST_GPU_NODE_COUNT`] [`--required-replica-count`=`REQUIRED_REPLICA_COUNT`] [`--reservation-affinity`=[`key`=`KEY`],[`reservation-affinity-type`=`RESERVATION-AFFINITY-TYPE`],[`values`=`VALUES`]] [`--service-account`=`SERVICE_ACCOUNT`] [`--spot`] [`--tpu-topology`=`TPU_TOPOLOGY`] [`--traffic-split`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]] [`--shared-resources`=`SHARED_RESOURCES` : `--shared-resources-region`=`SHARED_RESOURCES_REGION`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To deploy a model ``456`` to an endpoint ``123`` under project ``example`` in region ``us-central1``, run: 
    
    
    gcloud alpha ai endpoints deploy-model 123 --project=example --region=us-central1 --model=456 --display-name=my_deployed_model

POSITIONAL ARGUMENTS
    

Endpoint resource - The endpoint to deploy a model to. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENDPOINT`
     ID of the endpoint or fully qualified identifier for the endpoint. 

To set the `name` attribute: 

  * provide the argument `endpoint` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the endpoint. 

To set the `region` attribute: 

  * provide the argument `endpoint` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Display name of the deployed model. 
`--model`=`MODEL`
     ID of the uploaded model. The alpha and beta tracks also support GDC connected models. 
OPTIONAL FLAGS
    

`--accelerator`=[`count`=`COUNT`],[`type`=`TYPE`]
     Manage the accelerator config for GPU serving. When deploying a model with Compute Engine Machine Types, a GPU accelerator may also be selected. 

`type`
     The type of the accelerator. Choices are 'nvidia-a100-80gb', 'nvidia-b200', 'nvidia-gb200', 'nvidia-h100-80gb', 'nvidia-h100-mega-80gb', 'nvidia-h200-141gb', 'nvidia-l4', 'nvidia-rtx-pro-6000', 'nvidia-tesla-a100', 'nvidia-tesla-k80', 'nvidia-tesla-p100', 'nvidia-tesla-p4', 'nvidia-tesla-t4', 'nvidia-tesla-v100'. 
`count`
     The number of accelerators to attach to each machine running the job. This is usually 1. If not specified, the default value is 1. 

For example: `--accelerator=type=nvidia-tesla-k80,count=1`

`--autoscaling-metric-specs`=[`METRIC-NAME`=`TARGET`,…]
     Metric specifications that control autoscaling behavior. At most one entry is allowed per metric. 

`METRIC-NAME`
     Resource metric name. Choices are 'cpu-usage', 'dcgm-fi-dev-gpu-util', 'gpu-duty-cycle', 'request-counts-per-minute', 'vllm-gpu-cache-usage-perc', 'vllm-num-requests-waiting'. 
`TARGET`
     Target value for the given metric. For `cpu-usage`, `gpu-duty-cycle`, `dcgm-fi-dev-gpu-util`, and `vllm-gpu-cache-usage-perc`, the target is the target resource utilization in percentage (1% - 100%). For `request-counts-per-minute`, the target is the number of requests per minute per replica. For `vllm-num-requests-waiting`, the target is the number of pending requests allowed on the replica. 

For example, to set target CPU usage to 70% and target requests to 600 per minute per replica: `--autoscaling-metric-specs=cpu-usage=70,request-counts-per-minute=600`

`--deployed-model-id`=`DEPLOYED_MODEL_ID`
     User-specified ID of the deployed-model. 
`--enable-access-logging`
     If true, online prediction access logs are sent to Cloud Logging. 

These logs are standard server access logs, containing information like timestamp and latency for each prediction request. 

`--enable-container-logging`
     If true, the container of the deployed model instances will send `stderr` and `stdout` streams to Cloud Logging. 

Currently, only supported for custom-trained Models and AutoML Tabular Models. 

`--gpu-partition-size`=`GPU_PARTITION_SIZE`
     The partition size of the GPU accelerator. This can be used to partition a single GPU into multiple smaller GPU instances. See <https://cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi#multi-instance_gpu_partitions> for more details. 
`--idle-scaledown-period`=`IDLE_SCALEDOWN_PERIOD`
     Duration (in seconds) without traffic before a deployment is scaled down to zero replicas. Defaults to 1 hour if min replica count is 0. 
`--initial-replica-count`=`INITIAL_REPLICA_COUNT`
     Initial number of replicas for the deployment resources the model will be scaled up to. Cannot be smaller than min replica count or larger than max replica count. 
`--machine-type`=`MACHINE_TYPE`
     The machine resources to be used for each node of this deployment. For available machine types, see <https://cloud.google.com/ai-platform-unified/docs/predictions/machine-types>. 
`--max-replica-count`=`MAX_REPLICA_COUNT`
     Maximum number of machine replicas for the deployment resources the model will be deployed on. 
`--min-replica-count`=`MIN_REPLICA_COUNT`
     Minimum number of machine replicas for the deployment resources the model will be deployed on. For normal deployments, the value must be equal to or larger than 1. If the value is 0, the deployment will be enrolled in the scale-to-zero feature. If not specified and the uploaded models use dedicated resources, the default value is 1. 

NOTE: DeploymentResourcePools (model-cohosting) is currently not supported for scale-to-zero deployments. 

`--min-scaleup-period`=`MIN_SCALEUP_PERIOD`
     Minimum duration (in seconds) that a deployment will be scaled up before traffic is evaluated for potential scale-down. Defaults to 1 hour if min replica count is 0. 
`--multihost-gpu-node-count`=`MULTIHOST_GPU_NODE_COUNT`
     The number of nodes per replica for multihost GPU deployments. Required for multihost GPU deployments. 
`--required-replica-count`=`REQUIRED_REPLICA_COUNT`
     Required number of machine replicas for the deployment resources the model will be considered successfully deployed. This value must be greater than or equal to 1 and less than or equal to min-replica-count. 
`--reservation-affinity`=[`key`=`KEY`],[`reservation-affinity-type`=`RESERVATION-AFFINITY-TYPE`],[`values`=`VALUES`]
     A ReservationAffinity can be used to configure a Vertex AI resource (e.g., a DeployedModel) to draw its Compute Engine resources from a Shared Reservation, or exclusively from on-demand capacity. 
`--service-account`=`SERVICE_ACCOUNT`
     Service account that the deployed model's container runs as. Specify the email address of the service account. If this service account is not specified, the container runs as a service account that doesn't have access to the resource project. 
`--spot`
     If true, schedule the deployment workload on Spot VMs. 
`--tpu-topology`=`TPU_TOPOLOGY`
     CloudTPU topology to use for this deployment. Required for multihost CloudTPU deployments: <https://cloud.google.com/kubernetes-engine/docs/concepts/tpus#topology>. 
`--traffic-split`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]
     List of pairs of deployed model id and value to set as traffic split. 
Deployment resource pool resource - The deployment resource pool to co-host a model on. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--shared-resources` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--shared-resources`=`SHARED_RESOURCES`
     ID of the deployment_resource_pool or fully qualified identifier for the deployment_resource_pool. 

To set the `name` attribute: 

  * provide the argument `--shared-resources` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--shared-resources-region`=`SHARED_RESOURCES_REGION`
     Cloud region for the deployment_resource_pool. 

To set the `region` attribute: 

  * provide the argument `--shared-resources` on the command line with a fully specified name; 
  * provide the argument `--shared-resources-region` on the command line; 
  * provide the argument `--region` on the command line; 
  * set the property `ai/region`; 
  * choose one from the prompted list of available regions. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud ai endpoints deploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/deploy-model)
    
    
    [gcloud beta ai endpoints deploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/deploy-model)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
