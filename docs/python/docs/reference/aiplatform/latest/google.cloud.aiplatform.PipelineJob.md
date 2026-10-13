---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJob
title: Class PipelineJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:47.730784+00:00
---

# Class PipelineJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PipelineJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    PipelineJob(
        display_name: str,
        template_path: str,
        job_id: typing.Optional[str] = None,
        pipeline_root: typing.Optional[str] = None,
        parameter_values: typing.Optional[typing.Dict[str, typing.Any]] = None,
        input_artifacts: typing.Optional[typing.Dict[str, str]] = None,
        enable_caching: typing.Optional[bool] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        failure_policy: typing.Optional[str] = None,
    )

Retrieves a PipelineJob resource and instantiates its representation.

## Parameters  
  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The user-defined name of this Pipeline.  
`template_path` |  `str`   
Required. The path of PipelineJob or PipelineSpec JSON or YAML file. It can be a local path, a Google Cloud Storage URI (e.g. "gs://project.name"), an Artifact Registry URI (e.g. "<https://us-central1-kfp.pkg.dev/proj/repo/pack/latest>"), or an HTTPS URI.  
`job_id` |  `str`   
Optional. The unique ID of the job run. If not specified, pipeline name + timestamp will be used.  
`pipeline_root` |  `str`   
Optional. The root of the pipeline outputs. If not set, the staging bucket set in aiplatform.init will be used. If that's not set a pipeline-specific artifacts bucket will be used.  
`parameter_values` |  `Dict[str, Any]`   
Optional. The mapping from runtime parameter names to its values that control the pipeline run.  
`input_artifacts` |  `Dict[str, str]`   
Optional. The mapping from the runtime parameter name for this artifact to its resource id. For example: "vertex_model":"456". Note: full resource name ("projects/123/locations/us-central1/metadataStores/default/artifacts/456") cannot be used.  
`enable_caching` |  `bool`   
Optional. Whether to turn on caching for the run. If this is not set, defaults to the compile time settings, which are True for all tasks by default, while users may specify different caching options for individual tasks. If this is set, the setting applies to all tasks in the pipeline. Overrides the compile time settings.  
`encryption_spec_key_name` |  `str`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the job. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If this is set, then all resources created by the PipelineJob will be encrypted with the provided encryption key. Overrides encryption_spec_key_name set in aiplatform.init.  
`labels` |  `Dict[str, str]`   
Optional. The user defined metadata to organize PipelineJob.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create this PipelineJob. Overrides credentials set in aiplatform.init.  
`project` |  `str`   
Optional. The project that you want to run this PipelineJob in. If not set, the project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to create PipelineJob. If not set, location set in aiplatform.init will be used.  
`failure_policy` |  `str`   
Optional. The failure policy - "slow" or "fast". Currently, the default of a pipeline is that the pipeline will continue to run until no more tasks can be executed, also known as PIPELINE_FAILURE_POLICY_FAIL_SLOW (corresponds to "slow"). However, if a pipeline is set to PIPELINE_FAILURE_POLICY_FAIL_FAST (corresponds to "fast"), it will stop scheduling any new tasks when a task has failed. Any scheduled tasks will continue to completion.  
  
## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### gca_resource

The underlying resource proto representation.

### has_failed

Returns True if pipeline has failed.

False otherwise.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### resource_name

Full qualified resource name.

### state

Current pipeline state.

### update_time

Time this resource was last updated.

## Methods 

### __init_subclass__
    
    
    __init_subclass__(
        *,
        experiment_loggable_schemas: typing.Tuple[
            google.cloud.aiplatform.metadata.experiment_resources._ExperimentLoggableSchema
        ],
        **kwargs
    )

Register the metadata_schema for the subclass so Experiment can use it to retrieve the associated types.

usage:

class PipelineJob(..., experiment_loggable_schemas= (_ExperimentLoggableSchema(title='system.PipelineRun'), )

### batch_cancel
    
    
    batch_cancel(
        project: str, location: str, names: typing.List[str]
    ) -> google.api_core.operation.Operation

Example Usage: pipeline_job = aiplatform.PipelineJob( display_name='job_display_name', template_path='your_pipeline.yaml', ) pipeline_job.batch_cancel( project='your_project_id', location='your_location', names=['pipeline_job_name', 'pipeline_job_name2'] )

**Returns**  
---  
**Type** | **Description**  
`operation (Operation)` | An object representing a long-running operation.  
  
### batch_delete
    
    
    batch_delete(
        project: str, location: str, names: typing.List[str]
    ) -> google.cloud.aiplatform_v1.types.pipeline_service.BatchDeletePipelineJobsResponse

Example Usage: pipeline_job = aiplatform.PipelineJob( display_name='job_display_name', template_path='your_pipeline.yaml', ) pipeline_job.batch_delete( project='your_project_id', location='your_location', names=['pipeline_job_name', 'pipeline_job_name2'] )

### cancel
    
    
    cancel() -> None

Starts asynchronous cancellation on the PipelineJob. The server makes a best effort to cancel the job, but success is not guaranteed. On successful cancellation, the PipelineJob is not deleted; instead it becomes a job with state set to `CANCELLED`.

### clone
    
    
    clone(
        display_name: typing.Optional[str] = None,
        job_id: typing.Optional[str] = None,
        pipeline_root: typing.Optional[str] = None,
        parameter_values: typing.Optional[typing.Dict[str, typing.Any]] = None,
        input_artifacts: typing.Optional[typing.Dict[str, str]] = None,
        enable_caching: typing.Optional[bool] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
    ) -> google.cloud.aiplatform.pipeline_jobs.PipelineJob

Returns a new PipelineJob object with the same settings as the original one.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of this cloned Pipeline. If not specified, original pipeline display name will be used.  
`job_id` |  `str`   
Optional. The unique ID of the job run. If not specified, "cloned" + pipeline name + timestamp will be used.  
`pipeline_root` |  `str`   
Optional. The root of the pipeline outputs. Default to be the same staging bucket as original pipeline.  
`parameter_values` |  `Dict[str, Any]`   
Optional. The mapping from runtime parameter names to its values that control the pipeline run. Defaults to be the same values as original PipelineJob.  
`input_artifacts` |  `Dict[str, str]`   
Optional. The mapping from the runtime parameter name for this artifact to its resource id. Defaults to be the same values as original PipelineJob. For example: "vertex_model":"456". Note: full resource name ("projects/123/locations/us-central1/metadataStores/default/artifacts/456") cannot be used.  
`enable_caching` |  `bool`   
Optional. Whether to turn on caching for the run. If this is not set, defaults to be the same as original pipeline. If this is set, the setting applies to all tasks in the pipeline.  
`encryption_spec_key_name` |  `str`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the job. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If this is set, then all resources created by the PipelineJob will be encrypted with the provided encryption key. If not specified, encryption_spec of original PipelineJob will be used.  
`labels` |  `Dict[str, str]`   
Optional. The user defined metadata to organize PipelineJob.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create this PipelineJob. Overrides credentials set in aiplatform.init.  
`project` |  `str`   
Optional. The project that you want to run this PipelineJob in. If not set, the project set in original PipelineJob will be used.  
`location` |  `str`   
Optional. Location to create PipelineJob. If not set, location set in original PipelineJob will be used.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If job_id or labels have incorrect format.  
  
### create_schedule
    
    
    create_schedule(
        cron: str,
        display_name: str,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        allow_queueing: bool = False,
        max_run_count: typing.Optional[int] = None,
        max_concurrent_run_count: int = 1,
        max_concurrent_active_run_count: typing.Optional[int] = None,
        service_account: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.pipeline_job_schedules.PipelineJobSchedule

Creates a PipelineJobSchedule directly from a PipelineJob.

Example Usage:

pipeline_job = aiplatform.PipelineJob( display_name='job_display_name', template_path='your_pipeline.yaml', ) pipeline_job.run() pipeline_job_schedule = pipeline_job.create_schedule( cron='* * * * *', display_name='schedule_display_name', )

**Parameters**  
---  
**Name** | **Description**  
`cron` |  `str`   
Required. Time specification (cron schedule expression) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, "CRON_TZ=America/New_York 1 * * * *", or "TZ=America/New_York 1 * * * *".  
`display_name` |  `str`   
Required. The user-defined name of this PipelineJobSchedule.  
`start_time` |  `str`   
Optional. Timestamp after which the first run can be scheduled. If unspecified, it defaults to the schedule creation timestamp.  
`end_time` |  `str`   
Optional. Timestamp after which no more runs will be scheduled. If unspecified, then runs will be scheduled indefinitely.  
`allow_queueing` |  `bool`   
Optional. Whether new scheduled runs can be queued when max_concurrent_runs limit is reached.  
`max_run_count` |  `int`   
Optional. Maximum run count of the schedule. If specified, The schedule will be completed when either started_run_count >= max_run_count or when end_time is reached. Must be positive and <= 2^63-1.  
`max_concurrent_run_count` |  `int`   
Optional. Maximum number of runs that can be started concurrently for this PipelineJobSchedule.  
`max_concurrent_active_run_count` |  `int`   
Optional. Maximum number of active runs that can be executed concurrently for this PipelineJobSchedule. Active runs are those in a non-terminal state (e.g., RUNNING, PENDING, or QUEUED).  
`service_account` |  `str`   
Optional. Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account.  
`network` |  `str`   
Optional. The full name of the Compute Engine network to which the job should be peered. For example, projects/12345/global/networks/myVPC. Private services access must already be configured for the network. If left unspecified, the network set in aiplatform.init will be used. Otherwise, the job is not peered with any network.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### done
    
    
    done() -> bool

Helper method that return True is PipelineJob is done. False otherwise.

### from_pipeline_func
    
    
    from_pipeline_func(
        pipeline_func: typing.Callable,
        parameter_values: typing.Optional[typing.Dict[str, typing.Any]] = None,
        input_artifacts: typing.Optional[typing.Dict[str, str]] = None,
        output_artifacts_gcs_dir: typing.Optional[str] = None,
        enable_caching: typing.Optional[bool] = None,
        context_name: typing.Optional[str] = "pipeline",
        display_name: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        job_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
    ) -> google.cloud.aiplatform.pipeline_jobs.PipelineJob

Creates PipelineJob by compiling a pipeline function.

**Parameters**  
---  
**Name** | **Description**  
`pipeline_func` |  `Callable`   
Required. A pipeline function to compile. A pipeline function creates instances of components and connects component inputs to outputs.  
`parameter_values` |  `Dict[str, Any]`   
Optional. The mapping from runtime parameter names to its values that control the pipeline run.  
`input_artifacts` |  `Dict[str, str]`   
Optional. The mapping from the runtime parameter name for this artifact to its resource id. For example: "vertex_model":"456". Note: full resource name ("projects/123/locations/us-central1/metadataStores/default/artifacts/456") cannot be used.  
`output_artifacts_gcs_dir` |  `str`   
Optional. The GCS location of the pipeline outputs. A GCS bucket for artifacts will be created if not specified.  
`enable_caching` |  `bool`   
Optional. Whether to turn on caching for the run. If this is not set, defaults to the compile time settings, which are True for all tasks by default, while users may specify different caching options for individual tasks. If this is set, the setting applies to all tasks in the pipeline. Overrides the compile time settings.  
`context_name` |  `str`   
Optional. The name of metadata context. Used for cached execution reuse.  
`display_name` |  `str`   
Optional. The user-defined name of this Pipeline.  
`labels` |  `Dict[str, str]`   
Optional. The user defined metadata to organize PipelineJob.  
`job_id` |  `str`   
Optional. The unique ID of the job run. If not specified, pipeline name + timestamp will be used.  
`project` |  `str`   
Optional. The project that you want to run this PipelineJob in. If not set, the project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to create PipelineJob. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create this PipelineJob. Overrides credentials set in aiplatform.init.  
`encryption_spec_key_name` |  `str`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the job. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If this is set, then all resources created by the PipelineJob will be encrypted with the provided encryption key. Overrides encryption_spec_key_name set in aiplatform.init.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If job_id or labels have incorrect format.  
  
### get
    
    
    get(
        resource_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> google.cloud.aiplatform.pipeline_jobs.PipelineJob

Get a Vertex AI Pipeline Job for the given resource_name.

**Parameters**  
---  
**Name** | **Description**  
`resource_name` |  `str`   
Required. A fully-qualified resource name or ID.  
`project` |  `str`   
Optional. Project to retrieve dataset from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve dataset from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to upload this model. Overrides credentials set in aiplatform.init.  
  
### get_associated_experiment
    
    
    get_associated_experiment() -> (
        typing.Optional[google.cloud.aiplatform.metadata.experiment_resources.Experiment]
    )

Gets the aiplatform.Experiment associated with this PipelineJob, or None if this PipelineJob is not associated with an experiment.

### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        enable_simple_view: bool = False,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.pipeline_jobs.PipelineJob]

List all instances of this PipelineJob resource.

Example Usage:

aiplatform.PipelineJob.list( filter='display_name="experiment_a27"', order_by='create_time desc' )

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: `display_name`, `create_time`, `update_time`  
`enable_simple_view` |  `bool`   
Optional. Whether to pass the `read_mask` parameter to the list call. Defaults to `False` if not provided. This improves the performance of calling the `list()` method. It's recommended to set this parameter to `True` if your region has multiple pipeline runs, which can result in high latency and errors. However, the returned pipeline job list doesn't include all fields for each `PipelineJob`. Setting this to `True` excludes the following fields from your response: `runtime_config`, `service_account`, `network`, and some subfields of `pipeline_spec` and `job_detail`. The following fields are included in each `PipelineJob` resource in your response: `state`, `display_name`, `pipeline_spec.pipeline_info`, `create_time`, `start_time`, `end_time`, `update_time`, `labels`, `template_uri`, `template_metadata.version`, `job_detail.pipeline_run_context`, and `job_detail.pipeline_context`.  
`project` |  `str`   
Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.  
  
### run
    
    
    run(
        service_account: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        reserved_ip_ranges: typing.Optional[typing.List[str]] = None,
        sync: typing.Optional[bool] = True,
        create_request_timeout: typing.Optional[float] = None,
        enable_preflight_validations: typing.Optional[bool] = False,
    ) -> None

Run this configured PipelineJob and monitor the job until completion.

**Parameters**  
---  
**Name** | **Description**  
`service_account` |  `str`   
Optional. Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account.  
`network` |  `str`   
Optional. The full name of the Compute Engine network to which the job should be peered. For example, projects/12345/global/networks/myVPC. Private services access must already be configured for the network. If left unspecified, the network set in aiplatform.init will be used. Otherwise, the job is not peered with any network.  
`reserved_ip_ranges` |  `List[str]`   
Optional. A list of names for the reserved IP ranges under the VPC network that can be used for this PipelineJob's workload. For example: ['vertex-ai-ip-range'].  
`sync` |  `bool`   
Optional. Whether to execute this method synchronously. If False, this method will unblock and it will be executed in a concurrent Future.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`enable_preflight_validations` |  `bool`   
Optional. Whether to enable preflight validations for the PipelineJob.  
  
### submit
    
    
    submit(
        service_account: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        reserved_ip_ranges: typing.Optional[typing.List[str]] = None,
        create_request_timeout: typing.Optional[float] = None,
        *,
        experiment: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.metadata.experiment_resources.Experiment, str
            ]
        ] = None,
        enable_preflight_validations: typing.Optional[bool] = False
    ) -> None

Run this configured PipelineJob.

**Parameters**  
---  
**Name** | **Description**  
`service_account` |  `str`   
Optional. Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account.  
`network` |  `str`   
Optional. The full name of the Compute Engine network to which the job should be peered. For example, projects/12345/global/networks/myVPC. Private services access must already be configured for the network. If left unspecified, the network set in aiplatform.init will be used. Otherwise, the job is not peered with any network.  
`reserved_ip_ranges` |  `List[str]`   
Optional. A list of names for the reserved IP ranges under the VPC network that can be used for this PipelineJob's workload. For example: ['vertex-ai-ip-range']. If left unspecified, the job will be deployed to any IP ranges under the provided VPC network.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`experiment` |  `Union[str, experiments_resource.Experiment]`   
Optional. The Vertex AI experiment name or instance to associate to this PipelineJob. Metrics produced by the PipelineJob as system.Metric Artifacts will be associated as metrics to the current Experiment Run. Pipeline parameters will be associated as parameters to the current Experiment Run.  
`enable_preflight_validations` |  `bool`   
Optional. Whether to enable preflight validations for the PipelineJob.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### wait
    
    
    wait()

Wait for this PipelineJob to complete.

### wait_for_resource_creation
    
    
    wait_for_resource_creation() -> None

Waits until resource has been created.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
