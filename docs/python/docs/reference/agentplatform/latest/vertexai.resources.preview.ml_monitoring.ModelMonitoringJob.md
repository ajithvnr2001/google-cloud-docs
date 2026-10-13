---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob
title: Class ModelMonitoringJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:43.221101+00:00
---

# Class ModelMonitoringJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModelMonitoringJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ModelMonitoringJob(
        model_monitoring_job_name: str,
        model_monitor_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Initializer for ModelMonitoringJob.

Example Usage:
    
    
     my_monitoring_job = aiplatform.ModelMonitoringJob(
         model_monitoring_job_name='projects/123/locations/us-central1/modelMonitors/\
         my_model_monitor_id/modelMonitoringJobs/my_monitoring_job_id'
     )
     or
     my_monitoring_job = aiplatform.aiplatform.ModelMonitoringJob(
         model_monitoring_job_name='my_monitoring_job_id',
         model_monitor_id='my_model_monitor_id',
     )
    

## Parameters  
  
---  
**Name** | **Description**  
`model_monitoring_job_name` |  `str`   
Required. The resource name for the Model Monitoring Job if provided alone, or the model monitoring job id if provided with model_monitor_id.  
`model_monitor_id` |  `str`   
Optional. The model monitor id depends on the way of initializing ModelMonitoringJob.  
`project` |  `str`   
Required. Project to retrieve endpoint from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Required. Location to retrieve endpoint from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to init model monitoring job. Overrides credentials set in aiplatform.init.  
  
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

### state

Fetch Job again and return the current JobState.

**Returns**  
---  
**Type** | **Description**  
`state (job_state.JobState)` | Enum that describes the state of a Model Monitoring Job.  
  
### update_time

Time this resource was last updated.

## Methods 

### ModelMonitoringJob
    
    
    ModelMonitoringJob(
        model_monitoring_job_name: str,
        model_monitor_id: typing.Optional[str] = None,
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
        model_monitor_name: typing.Optional[str] = None,
        target_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        display_name: typing.Optional[str] = None,
        model_monitoring_job_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        baseline_dataset: typing.Optional[
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
        sync: bool = False,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitoringJob

Creates a new ModelMonitoringJob.

**Parameters**  
---  
**Name** | **Description**  
`model_monitor_name` |  `str`   
Required. The parent model monitor resource name. Format: `projects/{project}/locations/{location}/modelMonitors/{model_monitor}`  
`target_dataset` |  `objective.MonitoringInput`   
Required. The target dataset for analysis.  
`display_name` |  `str`   
Optional. The user-defined name of the ModelMonitoringJob. The name can be up to 128 characters long and can comprise any UTF-8 character.  
`model_monitoring_job_id` |  `str`   
Optional. The unique ID of the model monitoring job run, which will become the final component of the model monitoring job resource name. The maximum length is 63 characters, and valid characters are /^[a-z](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$/. If not specified, it will be generated by Vertex AI.  
`project` |  `str`   
Optional. Project to retrieve endpoint from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve endpoint from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create model monitoring job. Overrides credentials set in aiplatform.init.  
`baseline_dataset` |  `objective.MonitoringInput`   
Optional. The baseline dataset for monitoring job. If not set, the training dataset in ModelMonitor will be used as baseline dataset.  
`output_spec` |  `output.OutputSpec`   
Optional. The monitoring metrics/logs export spec. If not set, will use the default output_spec defined in ModelMonitor.  
`notification_spec` |  `notification.NotificationSpec`   
Optional. The notification spec for monitoring result. If not set, will use the default notification_spec defined in ModelMonitor.  
`explanation_spec` |  `explanation.ExplanationSpec`   
Optional. The explanation spec for feature attribution monitoring. If not set, will use the default explanation_spec defined in ModelMonitor.  
`sync` |  `bool`   
Required. Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed. Default is False.  
**Returns**  
---  
**Type** | **Description**  
`ModelMonitoringJob` | The model monitoring job that was created.  
  
### delete
    
    
    delete() -> None

Deletes an Model Monitoring Job.

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
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
