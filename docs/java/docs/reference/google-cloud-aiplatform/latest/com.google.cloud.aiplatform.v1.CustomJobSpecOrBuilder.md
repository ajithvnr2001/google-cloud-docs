---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpecOrBuilder
title: Interface CustomJobSpecOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:53.787521+00:00
---

# Interface CustomJobSpecOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CustomJobSpecOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface CustomJobSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBaseOutputDirectory()
    
    
    public abstract GcsDestination getBaseOutputDirectory()

The Cloud Storage location to store the output of this CustomJob or HyperparameterTuningJob. For HyperparameterTuningJob, the baseOutputDirectory of each child CustomJob backing a Trial is set to a subdirectory of name id under its parent HyperparameterTuningJob's baseOutputDirectory.

The following Vertex AI environment variables will be passed to containers or python modules when this field is set:

For CustomJob:

  * AIP_MODEL_DIR = `<base_output_directory>/model/`
  * AIP_CHECKPOINT_DIR = `<base_output_directory>/checkpoints/`
  * AIP_TENSORBOARD_LOG_DIR = `<base_output_directory>/logs/`

For CustomJob backing a Trial of HyperparameterTuningJob:

  * AIP_MODEL_DIR = `<base_output_directory>/<trial_id>/model/`

  * AIP_CHECKPOINT_DIR = `<base_output_directory>/<trial_id>/checkpoints/`
  * AIP_TENSORBOARD_LOG_DIR = `<base_output_directory>/<trial_id>/logs/`



`.google.cloud.aiplatform.v1.GcsDestination base_output_directory = 6;`

**Returns**  
---  
**Type** | **Description**  
`[GcsDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestination)` | The baseOutputDirectory.  
  
### getBaseOutputDirectoryOrBuilder()
    
    
    public abstract GcsDestinationOrBuilder getBaseOutputDirectoryOrBuilder()

The Cloud Storage location to store the output of this CustomJob or HyperparameterTuningJob. For HyperparameterTuningJob, the baseOutputDirectory of each child CustomJob backing a Trial is set to a subdirectory of name id under its parent HyperparameterTuningJob's baseOutputDirectory.

The following Vertex AI environment variables will be passed to containers or python modules when this field is set:

For CustomJob:

  * AIP_MODEL_DIR = `<base_output_directory>/model/`
  * AIP_CHECKPOINT_DIR = `<base_output_directory>/checkpoints/`
  * AIP_TENSORBOARD_LOG_DIR = `<base_output_directory>/logs/`

For CustomJob backing a Trial of HyperparameterTuningJob:

  * AIP_MODEL_DIR = `<base_output_directory>/<trial_id>/model/`

  * AIP_CHECKPOINT_DIR = `<base_output_directory>/<trial_id>/checkpoints/`
  * AIP_TENSORBOARD_LOG_DIR = `<base_output_directory>/<trial_id>/logs/`



`.google.cloud.aiplatform.v1.GcsDestination base_output_directory = 6;`

**Returns**  
---  
**Type** | **Description**  
`[GcsDestinationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GcsDestinationOrBuilder)` |   
  
### getEnableDashboardAccess()
    
    
    public abstract boolean getEnableDashboardAccess()

Optional. Whether you want Vertex AI to enable access to the customized dashboard in training chief container.

If set to `true`, you can access the dashboard at the URIs given by CustomJob.web_access_uris or Trial.web_access_uris (within HyperparameterTuningJob.trials).

`bool enable_dashboard_access = 16 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableDashboardAccess.  
  
### getEnableWebAccess()
    
    
    public abstract boolean getEnableWebAccess()

Optional. Whether you want Vertex AI to enable [interactive shell access](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell) to training containers.

If set to `true`, you can access interactive shells at the URIs given by CustomJob.web_access_uris or Trial.web_access_uris (within HyperparameterTuningJob.trials).

`bool enable_web_access = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableWebAccess.  
  
### getExperiment()
    
    
    public abstract String getExperiment()

Optional. The Experiment associated with this job. Format: `projects/{project}/locations/{location}/metadataStores/{metadataStores}/contexts/{experiment-name}`

` string experiment = 17 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The experiment.  
  
### getExperimentBytes()
    
    
    public abstract ByteString getExperimentBytes()

Optional. The Experiment associated with this job. Format: `projects/{project}/locations/{location}/metadataStores/{metadataStores}/contexts/{experiment-name}`

` string experiment = 17 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for experiment.  
  
### getExperimentRun()
    
    
    public abstract String getExperimentRun()

Optional. The Experiment Run associated with this job. Format: `projects/{project}/locations/{location}/metadataStores/{metadataStores}/contexts/{experiment-name}-{experiment-run-name}`

` string experiment_run = 18 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The experimentRun.  
  
### getExperimentRunBytes()
    
    
    public abstract ByteString getExperimentRunBytes()

Optional. The Experiment Run associated with this job. Format: `projects/{project}/locations/{location}/metadataStores/{metadataStores}/contexts/{experiment-name}-{experiment-run-name}`

` string experiment_run = 18 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for experimentRun.  
  
### getModels(int index)
    
    
    public abstract String getModels(int index)

Optional. The name of the Model resources for which to generate a mapping to artifact URIs. Applicable only to some of the Google-provided custom jobs. Format: `projects/{project}/locations/{location}/models/{model}`

In order to retrieve a specific version of the model, also provide the version ID or version alias. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version ID or alias is specified, the "default" version will be returned. The "default" version alias is created for the first version of the model, and can be moved to other versions later on. There will be exactly one default version.

` repeated string models = 20 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The models at the given index.  
  
### getModelsBytes(int index)
    
    
    public abstract ByteString getModelsBytes(int index)

Optional. The name of the Model resources for which to generate a mapping to artifact URIs. Applicable only to some of the Google-provided custom jobs. Format: `projects/{project}/locations/{location}/models/{model}`

In order to retrieve a specific version of the model, also provide the version ID or version alias. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version ID or alias is specified, the "default" version will be returned. The "default" version alias is created for the first version of the model, and can be moved to other versions later on. There will be exactly one default version.

` repeated string models = 20 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the models at the given index.  
  
### getModelsCount()
    
    
    public abstract int getModelsCount()

Optional. The name of the Model resources for which to generate a mapping to artifact URIs. Applicable only to some of the Google-provided custom jobs. Format: `projects/{project}/locations/{location}/models/{model}`

In order to retrieve a specific version of the model, also provide the version ID or version alias. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version ID or alias is specified, the "default" version will be returned. The "default" version alias is created for the first version of the model, and can be moved to other versions later on. There will be exactly one default version.

` repeated string models = 20 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of models.  
  
### getModelsList()
    
    
    public abstract List<String> getModelsList()

Optional. The name of the Model resources for which to generate a mapping to artifact URIs. Applicable only to some of the Google-provided custom jobs. Format: `projects/{project}/locations/{location}/models/{model}`

In order to retrieve a specific version of the model, also provide the version ID or version alias. Example: `projects/{project}/locations/{location}/models/{model}@2` or `projects/{project}/locations/{location}/models/{model}@golden` If no version ID or alias is specified, the "default" version will be returned. The "default" version alias is created for the first version of the model, and can be moved to other versions later on. There will be exactly one default version.

` repeated string models = 20 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the models.  
  
### getNetwork()
    
    
    public abstract String getNetwork()

Optional. The full name of the Compute Engine [network](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the Job should be peered. For example, `projects/12345/global/networks/myVPC`. [Format](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert) is of the form `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in `12345`, and {network} is a network name.

To specify this field, you must have already [configured VPC Network Peering for Vertex AI](https://cloud.google.com/vertex-ai/docs/general/vpc-peering).

If this field is left unspecified, the job is not peered with any network.

` string network = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public abstract ByteString getNetworkBytes()

Optional. The full name of the Compute Engine [network](https://docs.cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the Job should be peered. For example, `projects/12345/global/networks/myVPC`. [Format](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert) is of the form `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in `12345`, and {network} is a network name.

To specify this field, you must have already [configured VPC Network Peering for Vertex AI](https://cloud.google.com/vertex-ai/docs/general/vpc-peering).

If this field is left unspecified, the job is not peered with any network.

` string network = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getPersistentResourceId()
    
    
    public abstract String getPersistentResourceId()

Optional. The ID of the PersistentResource in the same Project and Location which to run

If this is specified, the job will be run on existing machines held by the PersistentResource instead of on-demand short-live machines. The network and CMEK configs on the job should be consistent with those on the PersistentResource, otherwise, the job will be rejected.

` string persistent_resource_id = 14 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The persistentResourceId.  
  
### getPersistentResourceIdBytes()
    
    
    public abstract ByteString getPersistentResourceIdBytes()

Optional. The ID of the PersistentResource in the same Project and Location which to run

If this is specified, the job will be run on existing machines held by the PersistentResource instead of on-demand short-live machines. The network and CMEK configs on the job should be consistent with those on the PersistentResource, otherwise, the job will be rejected.

` string persistent_resource_id = 14 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for persistentResourceId.  
  
### getProtectedArtifactLocationId()
    
    
    public abstract String getProtectedArtifactLocationId()

The ID of the location to store protected artifacts. e.g. us-central1. Populate only when the location is different than CustomJob location. List of supported locations: <https://cloud.google.com/vertex-ai/docs/general/locations>

`string protected_artifact_location_id = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The protectedArtifactLocationId.  
  
### getProtectedArtifactLocationIdBytes()
    
    
    public abstract ByteString getProtectedArtifactLocationIdBytes()

The ID of the location to store protected artifacts. e.g. us-central1. Populate only when the location is different than CustomJob location. List of supported locations: <https://cloud.google.com/vertex-ai/docs/general/locations>

`string protected_artifact_location_id = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for protectedArtifactLocationId.  
  
### getPscInterfaceConfig()
    
    
    public abstract PscInterfaceConfig getPscInterfaceConfig()

Optional. Configuration for PSC-I for CustomJob.

` .google.cloud.aiplatform.v1.PscInterfaceConfig psc_interface_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PscInterfaceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PscInterfaceConfig)` | The pscInterfaceConfig.  
  
### getPscInterfaceConfigOrBuilder()
    
    
    public abstract PscInterfaceConfigOrBuilder getPscInterfaceConfigOrBuilder()

Optional. Configuration for PSC-I for CustomJob.

` .google.cloud.aiplatform.v1.PscInterfaceConfig psc_interface_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PscInterfaceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.PscInterfaceConfigOrBuilder)` |   
  
### getReservedIpRanges(int index)
    
    
    public abstract String getReservedIpRanges(int index)

Optional. A list of names for the reserved ip ranges under the VPC network that can be used for this job.

If set, we will deploy the job within the provided ip ranges. Otherwise, the job will be deployed to any ip ranges under the provided VPC network.

Example: ['vertex-ai-ip-range'].

`repeated string reserved_ip_ranges = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The reservedIpRanges at the given index.  
  
### getReservedIpRangesBytes(int index)
    
    
    public abstract ByteString getReservedIpRangesBytes(int index)

Optional. A list of names for the reserved ip ranges under the VPC network that can be used for this job.

If set, we will deploy the job within the provided ip ranges. Otherwise, the job will be deployed to any ip ranges under the provided VPC network.

Example: ['vertex-ai-ip-range'].

`repeated string reserved_ip_ranges = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the reservedIpRanges at the given index.  
  
### getReservedIpRangesCount()
    
    
    public abstract int getReservedIpRangesCount()

Optional. A list of names for the reserved ip ranges under the VPC network that can be used for this job.

If set, we will deploy the job within the provided ip ranges. Otherwise, the job will be deployed to any ip ranges under the provided VPC network.

Example: ['vertex-ai-ip-range'].

`repeated string reserved_ip_ranges = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of reservedIpRanges.  
  
### getReservedIpRangesList()
    
    
    public abstract List<String> getReservedIpRangesList()

Optional. A list of names for the reserved ip ranges under the VPC network that can be used for this job.

If set, we will deploy the job within the provided ip ranges. Otherwise, the job will be deployed to any ip ranges under the provided VPC network.

Example: ['vertex-ai-ip-range'].

`repeated string reserved_ip_ranges = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the reservedIpRanges.  
  
### getScheduling()
    
    
    public abstract Scheduling getScheduling()

Scheduling options for a CustomJob.

`.google.cloud.aiplatform.v1.Scheduling scheduling = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Scheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Scheduling)` | The scheduling.  
  
### getSchedulingOrBuilder()
    
    
    public abstract SchedulingOrBuilder getSchedulingOrBuilder()

Scheduling options for a CustomJob.

`.google.cloud.aiplatform.v1.Scheduling scheduling = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SchedulingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SchedulingOrBuilder)` |   
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account. If unspecified, the [Vertex AI Custom Code Service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) for the CustomJob's project is used.

`string service_account = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account. If unspecified, the [Vertex AI Custom Code Service Agent](https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) for the CustomJob's project is used.

`string service_account = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getTensorboard()
    
    
    public abstract String getTensorboard()

Optional. The name of a Vertex AI Tensorboard resource to which this CustomJob will upload Tensorboard logs. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`

` string tensorboard = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tensorboard.  
  
### getTensorboardBytes()
    
    
    public abstract ByteString getTensorboardBytes()

Optional. The name of a Vertex AI Tensorboard resource to which this CustomJob will upload Tensorboard logs. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`

` string tensorboard = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for tensorboard.  
  
### getWorkerPoolSpecs(int index)
    
    
    public abstract WorkerPoolSpec getWorkerPoolSpecs(int index)

Required. The spec of the worker pools including machine type and Docker image. All worker pools except the first one are optional and can be skipped by providing an empty value.

` repeated .google.cloud.aiplatform.v1.WorkerPoolSpec worker_pool_specs = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPoolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec)` |   
  
### getWorkerPoolSpecsCount()
    
    
    public abstract int getWorkerPoolSpecsCount()

Required. The spec of the worker pools including machine type and Docker image. All worker pools except the first one are optional and can be skipped by providing an empty value.

` repeated .google.cloud.aiplatform.v1.WorkerPoolSpec worker_pool_specs = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getWorkerPoolSpecsList()
    
    
    public abstract List<WorkerPoolSpec> getWorkerPoolSpecsList()

Required. The spec of the worker pools including machine type and Docker image. All worker pools except the first one are optional and can be skipped by providing an empty value.

` repeated .google.cloud.aiplatform.v1.WorkerPoolSpec worker_pool_specs = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[WorkerPoolSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpec)>` |   
  
### getWorkerPoolSpecsOrBuilder(int index)
    
    
    public abstract WorkerPoolSpecOrBuilder getWorkerPoolSpecsOrBuilder(int index)

Required. The spec of the worker pools including machine type and Docker image. All worker pools except the first one are optional and can be skipped by providing an empty value.

` repeated .google.cloud.aiplatform.v1.WorkerPoolSpec worker_pool_specs = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPoolSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.WorkerPoolSpecOrBuilder)` |   
  
### getWorkerPoolSpecsOrBuilderList()
    
    
    public abstract List<? extends WorkerPoolSpecOrBuilder> getWorkerPoolSpecsOrBuilderList()

Required. The spec of the worker pools including machine type and Docker image. All worker pools except the first one are optional and can be skipped by providing an empty value.

` repeated .google.cloud.aiplatform.v1.WorkerPoolSpec worker_pool_specs = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1.WorkerPoolSpecOrBuilder>` |   
  
### hasBaseOutputDirectory()
    
    
    public abstract boolean hasBaseOutputDirectory()

The Cloud Storage location to store the output of this CustomJob or HyperparameterTuningJob. For HyperparameterTuningJob, the baseOutputDirectory of each child CustomJob backing a Trial is set to a subdirectory of name id under its parent HyperparameterTuningJob's baseOutputDirectory.

The following Vertex AI environment variables will be passed to containers or python modules when this field is set:

For CustomJob:

  * AIP_MODEL_DIR = `<base_output_directory>/model/`
  * AIP_CHECKPOINT_DIR = `<base_output_directory>/checkpoints/`
  * AIP_TENSORBOARD_LOG_DIR = `<base_output_directory>/logs/`

For CustomJob backing a Trial of HyperparameterTuningJob:

  * AIP_MODEL_DIR = `<base_output_directory>/<trial_id>/model/`

  * AIP_CHECKPOINT_DIR = `<base_output_directory>/<trial_id>/checkpoints/`
  * AIP_TENSORBOARD_LOG_DIR = `<base_output_directory>/<trial_id>/logs/`



`.google.cloud.aiplatform.v1.GcsDestination base_output_directory = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the baseOutputDirectory field is set.  
  
### hasPscInterfaceConfig()
    
    
    public abstract boolean hasPscInterfaceConfig()

Optional. Configuration for PSC-I for CustomJob.

` .google.cloud.aiplatform.v1.PscInterfaceConfig psc_interface_config = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pscInterfaceConfig field is set.  
  
### hasScheduling()
    
    
    public abstract boolean hasScheduling()

Scheduling options for a CustomJob.

`.google.cloud.aiplatform.v1.Scheduling scheduling = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the scheduling field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
