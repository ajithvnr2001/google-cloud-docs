---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ModelDeploymentMonitoringJob
title: Class ModelDeploymentMonitoringJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:28.285292+00:00
---

# Class ModelDeploymentMonitoringJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ModelDeploymentMonitoringJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModelDeploymentMonitoringJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    ModelDeploymentMonitoringJob(
        model_deployment_monitoring_job_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Vertex AI Model Deployment Monitoring Job.

This class should be used in conjunction with the Endpoint class in order to configure model monitoring for deployed models.

## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### end_time

Time when the Job resource entered the `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, or `JOB_STATE_CANCELLED` state.

### error

Detailed error info for this Job resource. Only populated when the Job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.

### gca_resource

The underlying resource proto representation.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### resource_name

Full qualified resource name.

### start_time

Time when the Job resource entered the `JOB_STATE_RUNNING` for the first time.

### state

Fetch Job again and return the current JobState.

**Returns**  
---  
**Type** | **Description**  
`state (job_state.JobState)` | Enum that describes the state of a Vertex AI job.  
  
### update_time

Time this resource was last updated.

## Methods 

### ModelDeploymentMonitoringJob
    
    
    ModelDeploymentMonitoringJob(
        model_deployment_monitoring_job_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Initializer for ModelDeploymentMonitoringJob.

**Parameter**  
---  
**Name** | **Description**  
`model_deployment_monitoring_job_name` |  `str`   
Required. A fully-qualified ModelDeploymentMonitoringJob resource name or ID. Example: "projects/.../locations/.../modelDeploymentMonitoringJobs/456" or "456" when project and location are initialized or passed.  
  
### cancel
    
    
    cancel()

Cancels this Job.

Success of cancellation is not guaranteed. Use `Job.state` property to verify if cancellation was successful.

### create
    
    
    create(
        endpoint: typing.Union[str, google.cloud.aiplatform.models.Endpoint],
        objective_configs: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.model_monitoring.objective.ObjectiveConfig,
                typing.Dict[
                    str, google.cloud.aiplatform.model_monitoring.objective.ObjectiveConfig
                ],
            ]
        ] = None,
        logging_sampling_strategy: typing.Optional[
            google.cloud.aiplatform.model_monitoring.sampling.RandomSampleConfig
        ] = None,
        schedule_config: typing.Optional[
            google.cloud.aiplatform.model_monitoring.schedule.ScheduleConfig
        ] = None,
        display_name: typing.Optional[str] = None,
        deployed_model_ids: typing.Optional[typing.List[str]] = None,
        alert_config: typing.Optional[
            google.cloud.aiplatform.model_monitoring.alert.EmailAlertConfig
        ] = None,
        predict_instance_schema_uri: typing.Optional[str] = None,
        sample_predict_instance: typing.Optional[str] = None,
        analysis_instance_schema_uri: typing.Optional[str] = None,
        bigquery_tables_log_ttl: typing.Optional[int] = None,
        stats_anomalies_base_directory: typing.Optional[str] = None,
        enable_monitoring_pipeline_logs: typing.Optional[bool] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.jobs.ModelDeploymentMonitoringJob

Creates and launches a model monitoring job.

**Parameters**  
---  
**Name** | **Description**  
`endpoint` |  `Union[str, "aiplatform.Endpoint"]`   
Required. Endpoint resource name or an instance of `aiplatform.Endpoint`. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`  
`logging_sampling_strategy` |  `model_monitoring.sampling.RandomSampleConfig`   
Optional. Sample Strategy for logging.  
`schedule_config` |  `model_monitoring.schedule.ScheduleConfig`   
Optional. Configures model monitoring job scheduling interval in hours. This defines how often the monitoring jobs are triggered.  
`display_name` |  `str`   
Optional. The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can be consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob.  
`deployed_model_ids` |  `List[str]`   
Optional. Use this argument to specify which deployed models to apply the objective config to. If left unspecified, the same config will be applied to all deployed models.  
`alert_config` |  `model_monitoring.alert.EmailAlertConfig`   
Optional. Configures how alerts are sent to the user. Right now only email alert is supported.  
`predict_instance_schema_uri` |  `str`   
Optional. YAML schema file uri describing the format of a single instance, which are given to format the Endpoint's prediction (and explanation). If not set, the schema will be generated from collected predict requests.  
`sample_predict_instance` |  `str`   
Optional. Sample Predict instance, same format as PredictionRequest.instances, this can be set as a replacement of predict_instance_schema_uri If not set, the schema will be generated from collected predict requests.  
`analysis_instance_schema_uri` |  `str`   
Optional. YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string.  
`bigquery_tables_log_ttl` |  `int`   
Optional. The TTL(time to live) of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl = 1 day.  
`stats_anomalies_base_directory` |  `str`   
Optional. Stats anomalies base folder path.  
`enable_monitoring_pipeline_logs` |  `bool`   
Optional. If true, the scheduled monitoring pipeline logs are sent to Google Cloud Logging, including pipeline status and anomalies detected. Please note the logs incur cost, which are subject to `Cloud Logging pricing <https://cloud.google.com/logging#pricing>`__.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize the ModelDeploymentMonitoringJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`encryption_spec_key_name` |  `str`   
Optional. Customer-managed encryption key spec for a ModelDeploymentMonitoringJob. If set, this ModelDeploymentMonitoringJob and all sub-resources of this ModelDeploymentMonitoringJob will be secured by this key.  
`create_request_timeout` |  `int`   
Optional. Timeout in seconds for the model monitoring job creation request.  
  
### delete
    
    
    delete() -> None

Deletes an MDM job.

### done
    
    
    done() -> bool

Method indicating whether a job has completed.

### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Job Resource.

Example Usage:

aiplatform.BatchPredictionJobs.list( filter='state="JOB_STATE_SUCCEEDED" AND display_name="my_job"', )

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: `display_name`, `create_time`, `update_time`  
`project` |  `str`   
Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.  
  
### pause
    
    
    pause() -> google.cloud.aiplatform.jobs.ModelDeploymentMonitoringJob

Pause a running MDM job.

### resume
    
    
    resume() -> google.cloud.aiplatform.jobs.ModelDeploymentMonitoringJob

Resumes a paused MDM job.

### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        *,
        display_name: typing.Optional[str] = None,
        schedule_config: typing.Optional[
            google.cloud.aiplatform.model_monitoring.schedule.ScheduleConfig
        ] = None,
        alert_config: typing.Optional[
            google.cloud.aiplatform.model_monitoring.alert.EmailAlertConfig
        ] = None,
        logging_sampling_strategy: typing.Optional[
            google.cloud.aiplatform.model_monitoring.sampling.RandomSampleConfig
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        bigquery_tables_log_ttl: typing.Optional[int] = None,
        enable_monitoring_pipeline_logs: typing.Optional[bool] = None,
        objective_configs: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.model_monitoring.objective.ObjectiveConfig,
                typing.Dict[
                    str, google.cloud.aiplatform.model_monitoring.objective.ObjectiveConfig
                ],
            ]
        ] = None,
        deployed_model_ids: typing.Optional[typing.List[str]] = None,
        update_request_timeout: typing.Optional[float] = None
    ) -> google.cloud.aiplatform.jobs.ModelDeploymentMonitoringJob

Updates an existing ModelDeploymentMonitoringJob.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of the ModelDeploymentMonitoringJob. The name can be up to 128 characters long and can be consist of any UTF-8 characters. Display name of a ModelDeploymentMonitoringJob.  
`schedule_config` |  `model_monitoring.schedule.ScheduleConfig`   
Required. Configures model monitoring job scheduling interval in hours. This defines how often the monitoring jobs are triggered.  
`alert_config` |  `model_monitoring.alert.EmailAlertConfig`   
Optional. Configures how alerts are sent to the user. Right now only email alert is supported.  
`logging_sampling_strategy` |  `model_monitoring.sampling.RandomSampleConfig`   
Required. Sample Strategy for logging.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize the ModelDeploymentMonitoringJob. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`bigquery_tables_log_ttl` |  `int`   
Optional. The number of days for which the logs are stored. The TTL(time to live) of BigQuery tables in user projects which stores logs. A day is the basic unit of the TTL and we take the ceil of TTL/86400(a day). e.g. { second: 3600} indicates ttl = 1 day.  
`enable_monitoring_pipeline_logs` |  `bool`   
Optional. If true, the scheduled monitoring pipeline logs are sent to Google Cloud Logging, including pipeline status and anomalies detected. Please note the logs incur cost, which are subject to `Cloud Logging pricing <https://cloud.google.com/logging#pricing>`__.  
`deployed_model_ids` |  `List[str]`   
Optional. Use this argument to specify which deployed models to apply the updated objective config to. If left unspecified, the same config will be applied to all deployed models.  
`upate_request_timeout` |  `float`   
Optional. Timeout in seconds for the model monitoring job update request.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

### wait_for_completion
    
    
    wait_for_completion() -> None

Waits for job to complete.

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If job failed or cancelled.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
