---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TensorboardRun
title: Class TensorboardRun (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:55.375417+00:00
---

# Class TensorboardRun (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.TensorboardRun

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TensorboardRun (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    TensorboardRun(
        tensorboard_run_name: str,
        tensorboard_id: typing.Optional[str] = None,
        tensorboard_experiment_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Managed tensorboard resource for Vertex AI.

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

### TensorboardRun
    
    
    TensorboardRun(
        tensorboard_run_name: str,
        tensorboard_id: typing.Optional[str] = None,
        tensorboard_experiment_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves an existing tensorboard run given a tensorboard run name or ID.
    
    
    Example Usage:
        tb_run = aiplatform.TensorboardRun(
            tensorboard_run_name= "projects/123/locations/us-central1/tensorboards/456/experiments/678/run/8910"
        )
    
        tb_run = aiplatform.TensorboardRun(
            tensorboard_run_name= "8910",
            tensorboard_id = "456",
            tensorboard_experiment_id = "678"
        )
    

**Parameters**  
---  
**Name** | **Description**  
`tensorboard_run_name` |  `str`   
Required. A fully-qualified tensorboard run resource name or resource ID. Example: "projects/123/locations/us-central1/tensorboards/456/experiments/678/runs/8910" or "8910" when tensorboard_id and tensorboard_experiment_id are passed and project and location are initialized or passed.  
`tensorboard_id` |  `str`   
Optional. A tensorboard resource ID.  
`tensorboard_experiment_id` |  `str`   
Optional. A tensorboard experiment resource ID.  
`project` |  `str`   
Optional. Project to retrieve tensorboard from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve tensorboard from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this Tensorboard. Overrides credentials set in aiplatform.init.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if only one of tensorboard_id or tensorboard_experiment_id is provided.  
  
### create
    
    
    create(
        tensorboard_run_id: str,
        tensorboard_experiment_name: str,
        tensorboard_id: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        request_metadata: typing.Sequence[typing.Tuple[str, str]] = (),
        create_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.tensorboard.tensorboard_resource.TensorboardRun

Creates a new tensorboard run.

Example Usage:
    
    
    tb_run = aiplatform.TensorboardRun.create(
        tensorboard_run_id='my-run'
        tensorboard_experiment_name='my-experiment'
        tensorboard_id='456'
        display_name='my display name',
        description='my description',
        labels={
            'key1': 'value1',
            'key2': 'value2'
        }
    )
    

**Parameters**  
---  
**Name** | **Description**  
`tensorboard_run_id` |  `str`   
Required. The ID to use for the Tensorboard run, which will become the final component of the Tensorboard run's resource name. This value should be 1-128 characters, and valid: characters are /`a-z][0-9]`-/.  
`tensorboard_experiment_name` |  `str`   
Required. The resource name or ID of the TensorboardExperiment to create the TensorboardRun in. Resource name format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}` If resource ID is provided then tensorboard_id must be provided.  
`tensorboard_id` |  `str`   
Optional. The resource ID of the Tensorboard to create the TensorboardRun in.  
`display_name` |  `str`   
Optional. The user-defined name of the Tensorboard Run. This value must be unique among all TensorboardRuns belonging to the same parent TensorboardExperiment. If not provided tensorboard_run_id will be used.  
`description` |  `str`   
Optional. Description of this Tensorboard Run.  
`labels` |  `Dict[str, str]`   
Optional. Labels with user-defined metadata to organize your Tensorboards. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded). See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.  
`project` |  `str`   
Optional. Project to upload this model to. Overrides project set in aiplatform.init.  
`location` |  `str`   
Optional. Location to upload this model to. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to upload this model. Overrides credentials set in aiplatform.init.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`TensorboardRun` | The TensorboardRun resource.  
  
### create_tensorboard_time_series
    
    
    create_tensorboard_time_series(
        display_name: str,
        value_type: typing.Union[
            google.cloud.aiplatform_v1.types.tensorboard_time_series.TensorboardTimeSeries.ValueType,
            str,
        ] = "SCALAR",
        plugin_name: str = "scalars",
        plugin_data: typing.Optional[bytes] = None,
        description: typing.Optional[str] = None,
    ) -> google.cloud.aiplatform.tensorboard.tensorboard_resource.TensorboardTimeSeries

Creates a new tensorboard time series.

Example Usage:
    
    
    tb_ts = tensorboard_run.create_tensorboard_time_series(
        display_name='my display name',
        tensorboard_run_name='my-run'
        tensorboard_id='456'
        tensorboard_experiment_id='my-experiment'
        description='my description',
        labels={
            'key1': 'value1',
            'key2': 'value2'
        }
    )
    

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. User provided name of this TensorboardTimeSeries. This value should be unique among all TensorboardTimeSeries resources belonging to the same TensorboardRun resource (parent resource).  
`value_type` |  `Union[gca_tensorboard_time_series.TensorboardTimeSeries.ValueType, str]`   
Optional. Type of TensorboardTimeSeries value. One of 'SCALAR', 'TENSOR', 'BLOB_SEQUENCE'.  
`plugin_name` |  `str`   
Optional. Name of the plugin this time series pertain to. Such as Scalar, Tensor, Blob.  
`plugin_data` |  `bytes`   
Optional. Data of the current plugin, with the size limited to 65KB.  
`description` |  `str`   
Optional. Description of this TensorboardTimeseries.  
**Returns**  
---  
**Type** | **Description**  
`TensorboardTimeSeries` | The TensorboardTimeSeries resource.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### list
    
    
    list(
        tensorboard_experiment_name: str,
        tensorboard_id: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[
        google.cloud.aiplatform.tensorboard.tensorboard_resource.TensorboardRun
    ]

List all instances of TensorboardRun in TensorboardExperiment.

Example Usage:
    
    
    aiplatform.TensorboardRun.list(
        tensorboard_experiment_name='projects/my-project/locations/us-central1/tensorboards/123/experiments/456'
    )
    

**Parameters**  
---  
**Name** | **Description**  
`tensorboard_experiment_name` |  `str`   
Required. The resource name or resource ID of the TensorboardExperiment to list TensorboardRun. Format, if resource name: 'projects/{project}/locations/{location}/tensorboards/{tensorboard}/experiments/{experiment}' If resource ID is provided then tensorboard_id must be provided.  
`tensorboard_id` |  `str`   
Optional. The resource ID of the Tensorboard that contains the TensorboardExperiment to list TensorboardRun.  
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
  
### read_time_series_data
    
    
    read_time_series_data() -> (
        typing.Dict[str, google.cloud.aiplatform_v1.types.tensorboard_data.TimeSeriesData]
    )

Read the time series data of this run.
    
    
    time_series_data = tensorboard_run.read_time_series_data()
    
    print(time_series_data['loss'].values[-1].scalar.value)
    

### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

### write_tensorboard_scalar_data
    
    
    write_tensorboard_scalar_data(
        time_series_data: typing.Dict[str, float],
        step: int,
        wall_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
    )

Writes tensorboard scalar data to this run.

**Parameters**  
---  
**Name** | **Description**  
`time_series_data` |  `Dict[str, float]`   
Required. Dictionary of where keys are TensorboardTimeSeries display name and values are the scalar value..  
`step` |  `int`   
Required. Step index of this data point within the run.  
`wall_time` |  `timestamp_pb2.Timestamp`   
Optional. Wall clock timestamp when this data point is generated by the end user. If not provided, this will be generated based on the value from time.time()  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
