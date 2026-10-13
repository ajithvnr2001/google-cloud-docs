---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor
title: Class ModelMonitor (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:42.162192+00:00
---

# Class ModelMonitor (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModelMonitor (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ModelMonitor(
        model_monitor_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Initializer for ModelMonitor.

## Parameters  
  
---  
**Name** | **Description**  
`model_monitor_name` |  `str`   
Required. A fully-qualified model monitor resource name or model monitor ID. Example: "projects/123/locations/us-central1/modelMonitors/456" or "456" when project and location are initialized or passed.  
`project` |  `str`   
Required. Project to retrieve model monitor from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Required. Location to retrieve model monitor from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this model monitor. Overrides credentials set in aiplatform.init.  
  
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

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### resource_name

Full qualified resource name.

### update_time

Time this resource was last updated.

## Methods 

### ModelMonitor
    
    
    ModelMonitor(
        model_monitor_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Initializes class with project, location, and api_client.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `str`   
Optional. Project of the resource noun.  
`location` |  `str`   
Optional. The location of the resource noun.  
`credentials` |  `google.auth.credentials.Credentials`   
Optional. custom credentials to use when accessing interacting with resource noun.  
`resource_name` |  `str`   
A fully-qualified resource name or ID.  
  
### create
    
    
    create(
        model_name: str,
        model_version_id: str,
        training_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        display_name: typing.Optional[str] = None,
        model_monitoring_schema: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.schema.ModelMonitoringSchema
        ] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        model_monitor_id: typing.Optional[str] = None,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitor

Creates a new ModelMonitor.

**Parameters**  
---  
**Name** | **Description**  
`model_name` |  `str`   
Required. A model resource name as model monitoring target. Format: `projects/{project}/locations/{location}/models/{model}`  
`model_version_id` |  `str`   
Required. Model version id.  
`training_dataset` |  `objective.MonitoringInput`   
Optional. Training dataset used to train the model. It can serve as a baseline dataset to identify changes in production.  
`display_name` |  `str`   
Optional. The user-defined name of the ModelMonitor. The name can be up to 128 characters long and can comprise any UTF-8 character. Display name of the ModelMonitor.  
`model_monitoring_schema` |  `schema.ModelMonitoringSchema`   
Required for most models, but optional for Vertex AI AutoML Tables unless the schema information is not available. The Monitoring Schema specifies the model's features, prediction outputs and ground truth properties. It is used to extract pertinent data from the dataset and to process features based on their properties. Make sure that the schema aligns with your dataset, if it does not, Vertex AI will be unable to extract data form the dataset.  
`tabular_objective_spec` |  `objective.TabularObjective`   
Optional. The default tabular monitoring objective spec for the model monitor. It can be overriden in the ModelMonitoringJob objective spec.  
`output_spec` |  `output.OutputSpec`   
Optional. The default monitoring metrics/logs export spec, it can be overriden in the ModelMonitoringJob output spec. If not specified, a default Google Cloud Storage bucket will be created under your project.  
`notification_spec` |  `notification.NotificationSpec`   
Optional. The default notification spec for monitoring result. It can be overriden in the ModelMonitoringJob notification spec.  
`explanation_spec` |  `explanation.ExplanationSpec`   
Optional. The default explanation spec for feature attribution monitoring. It can be overriden in the ModelMonitoringJob explanation spec.  
`project` |  `str`   
Optional. Project to retrieve model monitor from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve model monitor from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create this model monitor. Overrides credentials set in aiplatform.init.  
`model_monitor_id` |  `str`   
Optional. The unique ID of the model monitor, which will become the final component of the model monitor resource name. If not specified, it will be generated by Vertex AI.  
**Returns**  
---  
**Type** | **Description**  
`ModelMonitor` | The model monitor that was created.  
  
### create_schedule
    
    
    create_schedule(
        cron: str,
        target_dataset: vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput,
        display_name: typing.Optional[str] = None,
        model_monitoring_job_display_name: typing.Optional[str] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        baseline_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
    ) -> google.cloud.aiplatform_v1beta1.types.schedule.Schedule

Creates a new Scheduled run for model monitoring job.

**Parameters**  
---  
**Name** | **Description**  
`cron` |  `str`   
Required. Cron schedule (<https://en.wikipedia.org/wiki/Cron>) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, "CRON_TZ=America/New_York 1 * * * *", or "TZ=America/New_York 1 * * * *".  
`target_dataset` |  `objective.MonitoringInput`   
Required. The target dataset for analysis.  
`display_name` |  `str`   
Optional. The user-defined name of the Schedule. The name can be up to 128 characters long and can be consist of any UTF-8 characters. Display name of the Schedule.  
`model_monitoring_job_display_name` |  `str`   
Optional. The user-defined name of the ModelMonitoringJob. The name can be up to 128 characters long and can be consist of any UTF-8 characters. Display name of the ModelMonitoringJob.  
`start_time` |  `timestamp_pb2.Timestamp`   
Optional. Timestamp after which the first run can be scheduled. Default to Schedule create time if not specified.  
`end_time` |  `timestamp_pb2.Timestamp`   
Optional. Timestamp after which no new runs can be scheduled. If specified, The schedule will be completed when the end_time is reached. If not specified, new runs will keep getting scheduled until this Schedule is paused or deleted. Already scheduled runs will be allowed to complete. Unset if not specified.  
`tabular_objective_spec` |  `objective.TabularObjective`   
Optional. The tabular monitoring objective spec. If not set, the default tabular objective spec in ModelMonitor will be used. You must either set here or set the default one in the ModelMonitor.  
`baseline_dataset` |  `objective.MonitoringInput`   
Optional. The baseline dataset for monitoring job. If not set, the training dataset in ModelMonitor will be used as baseline dataset.  
`output_spec` |  `output.OutputSpec`   
Optional. The monitoring metrics/logs export spec. If not set, will use the default output_spec defined in ModelMonitor.  
`notification_spec` |  `notification.NotificationSpec`   
Optional. The notification spec for monitoring result. If not set, will use the default notification_spec defined in ModelMonitor.  
`explanation_spec` |  `explanation.ExplanationSpec`   
Optional. The explanation spec for feature attribution monitoring. If not set, will use the default explanation_spec defined in ModelMonitor.  
**Returns**  
---  
**Type** | **Description**  
`Schedule` | The created schedule.  
  
### delete
    
    
    delete(force: bool = False, sync: bool = True) -> None

Force delete the model monitor.

### delete_model_monitoring_job
    
    
    delete_model_monitoring_job(model_monitoring_job_name: str) -> None

Delete a model monitoring job.

**Parameter**  
---  
**Name** | **Description**  
`model_monitoring_job_name` |  `str`   
Required. The resource name of the model monitoring job that needs to be deleted. Format: `projects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}` or `{model_monitoring_job}`  
  
### delete_schedule
    
    
    delete_schedule(schedule_name: str) -> None

Deletes an existing Schedule.

**Parameter**  
---  
**Name** | **Description**  
`schedule_name` |  `str`   
Required. The resource name of schedule that needs to be deleted. Format: `projects/{project}/locations/{location}/schedules/{schedule}` or `{schedule}`  
  
### get_model_monitoring_job
    
    
    get_model_monitoring_job(
        model_monitoring_job_name: str,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitoringJob

Get the specified ModelMonitoringJob.

**Parameter**  
---  
**Name** | **Description**  
`model_monitoring_job_name` |  `str`   
Required. The resource name of the ModelMonitoringJob that is needed. Format: `projects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}` or `{model_monitoring_job}`  
**Returns**  
---  
**Type** | **Description**  
`ModelMonitoringJob` | The model monitoring job get.  
  
### get_schedule
    
    
    get_schedule(
        schedule_name: str,
    ) -> google.cloud.aiplatform_v1beta1.types.schedule.Schedule

Gets an existing Schedule.

**Parameter**  
---  
**Name** | **Description**  
`schedule_name` |  `str`   
Required. The resource name of schedule that needs to be fetched. Format: `projects/{project}/locations/{location}/schedules/{schedule}` or `{schedule}`  
**Returns**  
---  
**Type** | **Description**  
`Schedule` | The schedule requested.  
  
### get_schema
    
    
    get_schema() -> (
        google.cloud.aiplatform_v1beta1.types.model_monitor.ModelMonitoringSchema
    )

Get the schema of the model monitor.

### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        parent: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Vertex AI Resource.

Example Usage:

aiplatform.BatchPredictionJobs.list( filter='state="JOB_STATE_SUCCEEDED" AND display_name="my_job"', )

aiplatform.Model.list(order_by="create_time desc, display_name")

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
`parent` |  `str`   
Optional. The parent resource name if any to retrieve list from.  
  
### list_jobs
    
    
    list_jobs(
        page_size: typing.Optional[int] = None, page_token: typing.Optional[str] = None
    ) -> ListJobsResponse.list_jobs

List ModelMonitoringJobs.

**Parameters**  
---  
**Name** | **Description**  
`page_size` |  `int`   
Optional. The standard page list size.  
`page_token` |  `str`   
Optional. A page token received from a previous call.  
**Returns**  
---  
**Type** | **Description**  
`ListJobsResponse.list_jobs` | The list model monitoring jobs responses.  
  
### list_schedules
    
    
    list_schedules(
        filter: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> ListSchedulesResponse.list_schedules

List Schedules.

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. Lists the Schedules that match the filter expression. The following fields are supported: - `display_name`: Supports `=`, `!=` comparisons, and `:` wildcard. - `state`: Supports `=` and `!=` comparisons. - `request`: Supports existence of the <request_type> check. (e.g. `create_pipeline_job_request:__`\--> Schedule has create_pipeline_job_request). - `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. - `start_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. - `end_time`: Supports `=`, `!=`, `<`, `>`, `<=`, `>=` comparisons and `:` existence check. Values must be in RFC 3339 format. - `next_run_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format. Filter expressions can be combined together using logical operators (`NOT`, `AND` & `OR`). The syntax to define filter expression is based on <https://google.aip.dev/160>.  
`page_size` |  `int`   
Optional. The standard page list size.  
`page_token` |  `str`   
Optional. A page token received from a previous call.  
**Returns**  
---  
**Type** | **Description**  
`MetricsSearchResponse` | The model monitoring stats results.  
  
### pause_schedule
    
    
    pause_schedule(schedule_name: str) -> None

Pauses an existing Schedule.

**Parameter**  
---  
**Name** | **Description**  
`schedule_name` |  `str`   
Required. The resource name of schedule that needs to be paused. Format: `projects/{project}/locations/{location}/schedules/{schedule}` or `{schedule}`  
  
### resume_schedule
    
    
    resume_schedule(schedule_name: str) -> None

Resumes an existing Schedule.

**Parameter**  
---  
**Name** | **Description**  
`schedule_name` |  `str`   
Required. The resource name of schedule that needs to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}` or `{schedule}`  
  
### run
    
    
    run(
        target_dataset: vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput,
        display_name: typing.Optional[str] = None,
        model_monitoring_job_id: typing.Optional[str] = None,
        sync: typing.Optional[bool] = False,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        baseline_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitoringJob

Creates a new ModelMonitoringJob.

**Parameters**  
---  
**Name** | **Description**  
`target_dataset` |  `objective.MonitoringInput`   
Required. The target dataset for analysis.  
`display_name` |  `str`   
Optional. The user-defined name of the ModelMonitoringJob. The name can be up to 128 characters long and can comprise any UTF-8 character. Display name of the ModelMonitoringJob.  
`model_monitoring_job_id` |  `str`   
Optional. The unique ID of the model monitoring job run, which will become the final component of the model monitoring job resource name. The maximum length is 63 characters, and valid characters are /^[a-z](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$/. If not specified, it will be generated by Vertex AI.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed. Default is False.  
`tabular_objective_spec` |  `objective.TabularObjective`   
Optional. The tabular monitoring objective spec for the model monitoring job.  
`baseline_dataset` |  `objective.MonitoringInput`   
Optional. The baseline dataset for monitoring job. If not set, the training dataset in ModelMonitor will be used as baseline dataset.  
`output_spec` |  `output.OutputSpec`   
Optional. The monitoring metrics/logs export spec. If not set, will use the default output_spec defined in ModelMonitor.  
`notification_spec` |  `notification.NotificationSpec`   
Optional. The notification spec for monitoring result. If not set, will use the default notification_spec defined in ModelMonitor.  
`explanation_config` |  `explanation.ExplanationSpec`   
Optional. The explanation spec for feature attribution monitoring. If not set, will use the default explanation_spec defined in ModelMonitor.  
**Returns**  
---  
**Type** | **Description**  
`ModelMonitoringJob` | The model monitoring job that was created.  
  
### search_alerts
    
    
    search_alerts(
        stats_name: typing.Optional[str] = None,
        objective_type: typing.Optional[str] = None,
        model_monitoring_job_name: typing.Optional[str] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> typing.Dict[str, typing.Any]

Search ModelMonitoringAlerts.

**Parameters**  
---  
**Name** | **Description**  
`stats_name` |  `str`   
Optional. The stats name filter for the search, if not set, all stats will be returned. For tabular models, provide the name of the feature to return alerts from.  
`objective_type` |  `str`   
Optional. Return alerts from one of the supported monitoring objectives: `raw-feature-drift` `prediction-output-drift` `feature-attribution`  
`model_monitoring_job_name` |  `str`   
Optional. The resource name of a particular model monitoring job that the user wants to search metrics result from. Format: `projects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}`  
`start_time` |  `timestamp_pb2.Timestamp`   
Optional. Inclusive start of the time interval for which alerts should be returned.  
`end_time` |  `timestamp_pb2.Timestamp`   
Optional. Exclusive end of the time interval for which alerts should be returned.  
`page_size` |  `int`   
Optional. The standard page list size.  
`page_token` |  `str`   
Optional. A page token received from a previous call.  
**Returns**  
---  
**Type** | **Description**  
`AlertsSearchResponse` | The model monitoring alerts results.  
  
### search_metrics
    
    
    search_metrics(
        stats_name: typing.Optional[str] = None,
        objective_type: typing.Optional[str] = None,
        model_monitoring_job_name: typing.Optional[str] = None,
        schedule_name: typing.Optional[str] = None,
        algorithm: typing.Optional[str] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> MetricsSearchResponse.monitoring_stats

Search ModelMonitoringStats.

**Parameters**  
---  
**Name** | **Description**  
`stats_name` |  `str`   
Optional. The stats name filter for the search, if not set, all stats will be returned. For tabular model it's the feature name.  
`objective_type` |  `str`   
Optional. One of the supported monitoring objectives: `raw-feature-drift` `prediction-output-drift` `feature-attribution`  
`model_monitoring_job_name` |  `str`   
Optional. The resource name of a particular model monitoring job that the user wants to search metrics result from. Format: `projects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}`  
`schedule_name` |  `str`   
Optional. The resource name of a particular model monitoring schedule that the user wants to search metrics result from. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`algorithm` |  `str`   
Optional. The algorithm type filter for the search, eg: jensen_shannon_divergence, l_infinity.  
`start_time` |  `timestamp_pb2.Timestamp`   
Optional. Inclusive start of the time interval for which results should be returned.  
`end_time` |  `timestamp_pb2.Timestamp`   
Optional. Exclusive end of the time interval for which results should be returned.  
`page_size` |  `int`   
Optional. The standard page list size.  
`page_token` |  `str`   
Optional. A page token received from a previous call.  
**Returns**  
---  
**Type** | **Description**  
`MetricsSearchResponse` | The model monitoring stats results.  
  
### show_feature_attribution_drift_stats
    
    
    show_feature_attribution_drift_stats(model_monitoring_job_name: str) -> None

The method to visualize the feature attribution drift result from a model monitoring job as a histogram chart and a table.

**Parameter**  
---  
**Name** | **Description**  
`model_monitoring_job_name` |  `str`   
Required. The resource name of model monitoring job to show the feature attribution drift stats from. Format: `projects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}` or `{model_monitoring_job}`  
  
### show_feature_drift_stats
    
    
    show_feature_drift_stats(model_monitoring_job_name: str) -> None

The method to visualize the feature drift result from a model monitoring job as a histogram chart and a table.

**Parameter**  
---  
**Name** | **Description**  
`model_monitoring_job_name` |  `str`   
Required. The resource name of model monitoring job to show the drift stats from. Format: `projects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}` or `{model_monitoring_job}`  
  
### show_output_drift_stats
    
    
    show_output_drift_stats(model_monitoring_job_name: str) -> None

The method to visualize the prediction output drift result from a model monitoring job as a histogram chart and a table.

**Parameter**  
---  
**Name** | **Description**  
`model_monitoring_job_name` |  `str`   
Required. The resource name of model monitoring job to show the drift stats from. Format: `projects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}` or `{model_monitoring_job}`  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        display_name: typing.Optional[str] = None,
        training_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        model_monitoring_schema: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.schema.ModelMonitoringSchema
        ] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitor

Updates an existing ModelMonitor.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of the ModelMonitor. The name can be up to 128 characters long and can comprise any UTF-8 character. Display name of the ModelMonitor.  
`training_dataset` |  `objective.MonitoringInput`   
Optional. Training dataset used to train the model. It can serve as a baseline dataset to identify changes in production.  
`model_monitoring_schema` |  `schema.ModelMonitoringSchema`   
Optional. The Monitoring Schema specifies the model's features, prediction outputs and ground truth properties. It is used to extract pertinent data from the dataset and to process features based on their properties. Make sure that the schema aligns with your dataset, if it does not, Vertex AI will be unable to extract data form the dataset.  
`tabular_objective_spec` |  `objective.TabularObjective`   
Optional. The default tabular monitoring objective spec for the model monitor. It can be overriden in the ModelMonitoringJob objective spec.  
`output_spec` |  `output.OutputSpec`   
Optional. The default monitoring metrics/logs export spec, it can be overriden in the ModelMonitoringJob output spec.  
`notification_spec` |  `notification.NotificationSpec`   
Optional. The default notification spec for monitoring result. It can be overriden in the ModelMonitoringJob notification spec.  
`explanation_spec` |  `explanation.ExplanationSpec`   
Optional. The default explanation spec for feature attribution monitoring. It can be overriden in the ModelMonitoringJob explanation spec.  
**Returns**  
---  
**Type** | **Description**  
`ModelMonitor` | The updated model monitor.  
  
### update_schedule
    
    
    update_schedule(
        schedule_name: str,
        display_name: typing.Optional[str] = None,
        model_monitoring_job_display_name: typing.Optional[str] = None,
        cron: typing.Optional[str] = None,
        baseline_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        target_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
    ) -> google.cloud.aiplatform_v1beta1.types.schedule.Schedule

Updates an existing Schedule.

**Parameters**  
---  
**Name** | **Description**  
`schedule_name` |  `str`   
Required. The resource name of schedule that needs to be updated. Format: `projects/{project}/locations/{location}/schedules/{schedule}` or `{schedule}`  
`display_name` |  `str`   
Optional. The user-defined name of the Schedule. The name can be up to 128 characters long and can be consist of any UTF-8 characters. Display name of the Schedule.  
`model_monitoring_job_display_name` |  `str`   
Optional. The user-defined display name of the ModelMonitoringJob that needs to be updated.  
`cron` |  `str`   
Optional. Cron schedule (<https://en.wikipedia.org/wiki/Cron>) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, "CRON_TZ=America/New_York 1 * * * *", or "TZ=America/New_York 1 * * * *".  
`baseline_dataset` |  `objective.MonitoringInput`   
Optional. The baseline dataset for monitoring job.  
`target_dataset` |  `objective.MonitoringInput`   
Optional. The target dataset for analysis.  
`tabular_objective_spec` |  `objective.TabularObjective`   
Optional. The tabular monitoring objective spec.  
`output_spec` |  `output.OutputSpec`   
Optional. The monitoring metrics/logs export spec.  
`notification_spec` |  `notification.NotificationSpec`   
Optional. The notification spec for monitoring result.  
`explanation_spec` |  `explanation.ExplanationSpec`   
Optional. The explanation spec for feature attribution monitoring.  
`end_time` |  `timestamp_pb2.Timestamp`   
Optional. Timestamp after which no new runs can be scheduled.  
**Returns**  
---  
**Type** | **Description**  
`Schedule` | The updated schedule.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
