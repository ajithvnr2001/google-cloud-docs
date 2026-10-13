---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJobSchedule
title: Class PipelineJobSchedule (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:48.470343+00:00
---

# Class PipelineJobSchedule (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJobSchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PipelineJobSchedule (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    PipelineJobSchedule(
        pipeline_job: google.cloud.aiplatform.pipeline_jobs.PipelineJob,
        display_name: str,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
    )

Retrieves a PipelineJobSchedule resource and instantiates its representation.

## Parameters  
  
---  
**Name** | **Description**  
`pipeline_job` |  `PipelineJob`   
Required. PipelineJob used to init the schedule.  
`display_name` |  `str`   
Required. The user-defined name of this PipelineJobSchedule.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to create this PipelineJobSchedule. Overrides credentials set in aiplatform.init.  
`project` |  `str`   
Optional. The project that you want to run this PipelineJobSchedule in. If not set, the project used for the PipelineJob will be used.  
`location` |  `str`   
Optional. Location to create PipelineJobSchedule. If not set, location used for the PipelineJob will be used.  
  
## Properties 

### allow_queueing

Whether current Schedule allows queueing.

### create_time

Time this resource was created.

### cron

Current Schedule cron.

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

### max_concurrent_active_run_count

Current Schedule max_concurrent_active_run_count.

### max_concurrent_run_count

Current Schedule max_concurrent_run_count.

### max_run_count

Current Schedule max_run_count.

### name

Name of this resource.

### resource_name

Full qualified resource name.

### state

Current Schedule state.

### update_time

Time this resource was last updated.

## Methods 

### create
    
    
    create(
        cron: str,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        allow_queueing: bool = False,
        max_run_count: typing.Optional[int] = None,
        max_concurrent_run_count: int = 1,
        max_concurrent_active_run_count: typing.Optional[int] = None,
        service_account: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        create_request_timeout: typing.Optional[float] = None,
    ) -> None

Create a PipelineJobSchedule.

**Parameters**  
---  
**Name** | **Description**  
`cron` |  `str`   
Required. Time specification (cron schedule expression) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, "CRON_TZ=America/New_York 1 * * * *", or "TZ=America/New_York 1 * * * *".  
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

Helper method that return True is Schedule is done. False otherwise.

### get
    
    
    get(
        schedule_id: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.Any

Get a Vertex AI Schedule for the given resource_name.

**Parameters**  
---  
**Name** | **Description**  
`schedule_id` |  `str`   
Required. Schedule ID used to identify or locate the schedule.  
`project` |  `str`   
Optional. Project to retrieve dataset from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve dataset from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to upload this model. Overrides credentials set in aiplatform.init.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.pipeline_job_schedules.PipelineJobSchedule]

List all instances of this PipelineJobSchedule resource.

Example Usage:

aiplatform.PipelineJobSchedule.list( filter='display_name="experiment_a27"', order_by='create_time desc' )

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
  
### list_jobs
    
    
    list_jobs(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        enable_simple_view: bool = True,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.pipeline_jobs.PipelineJob]

List all PipelineJob 's created by this PipelineJobSchedule.

Example usage:

pipeline_job_schedule.list_jobs(order_by='create_time_desc')

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: `display_name`, `create_time`, `update_time`  
`enable_simple_view` |  `bool`   
Optional. Whether to pass the `read_mask` parameter to the list call. Defaults to True if not provided. This will improve the performance of calling list(). However, the returned PipelineJob list will not include all fields for each PipelineJob. Setting this to True will exclude the following fields in your response: `runtime_config`, `service_account`, `network`, and some subfields of `pipeline_spec` and `job_detail`. The following fields will be included in each PipelineJob resource in your response: `state`, `display_name`, `pipeline_spec.pipeline_info`, `create_time`, `start_time`, `end_time`, `update_time`, `labels`, `template_uri`, `template_metadata.version`, `job_detail.pipeline_run_context`, `job_detail.pipeline_context`.  
`project` |  `str`   
Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.  
  
### pause
    
    
    pause() -> None

Starts asynchronous pause on the Schedule.

Changes Schedule state from State.ACTIVE to State.PAUSED.

### resume
    
    
    resume(catch_up: bool = True) -> None

Starts asynchronous resume on the Schedule.

Changes Schedule state from State.PAUSED to State.ACTIVE.

**Parameter**  
---  
**Name** | **Description**  
`catch_up` |  `bool`   
Optional. Whether to backfill missed runs when the Schedule is resumed from State.PAUSED.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        display_name: typing.Optional[str] = None,
        cron: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        allow_queueing: typing.Optional[bool] = None,
        max_run_count: typing.Optional[int] = None,
        max_concurrent_run_count: typing.Optional[int] = None,
        max_concurrent_active_run_count: typing.Optional[int] = None,
    ) -> None

Update an existing PipelineJobSchedule.

Example usage:

pipeline_job_schedule.update( display_name='updated-display-name', cron='* * * * *', )

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of this PipelineJobSchedule.  
`cron` |  `str`   
Optional. Time specification (cron schedule expression) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, "CRON_TZ=America/New_York 1 * * * *", or "TZ=America/New_York 1 * * * *".  
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
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | User tried to call update() before create().  
  
### wait
    
    
    wait() -> None

Wait for all runs scheduled by this Schedule to complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
