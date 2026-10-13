---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.DeploymentResourcePool
title: Class DeploymentResourcePool (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:36.060700+00:00
---

# Class DeploymentResourcePool (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.DeploymentResourcePool

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DeploymentResourcePool (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    DeploymentResourcePool(
        deployment_resource_pool_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves a DeploymentResourcePool.

## Parameters  
  
---  
**Name** | **Description**  
`deployment_resource_pool_name` |  `str`   
Required. The fully-qualified resource name or ID of the deployment resource pool. Example: "projects/123/locations/us-central1/deploymentResourcePools/456" or "456" when project and location are initialized or passed.  
`project` |  `str`   
Optional. Project containing the deployment resource pool to retrieve. If not set, the project given to `aiplatform.init` will be used.  
`location` |  `str`   
Optional. Location containing the deployment resource pool to retrieve. If not set, the location given to `aiplatform.init` will be used.  
  
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

### create
    
    
    create(
        deployment_resource_pool_id: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        metadata: typing.Sequence[typing.Tuple[str, str]] = (),
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        machine_type: typing.Optional[str] = None,
        min_replica_count: int = 1,
        max_replica_count: int = 1,
        accelerator_type: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
        autoscaling_target_cpu_utilization: typing.Optional[int] = None,
        autoscaling_target_accelerator_duty_cycle: typing.Optional[int] = None,
        sync=True,
        create_request_timeout: typing.Optional[float] = None,
        reservation_affinity_type: typing.Optional[str] = None,
        reservation_affinity_key: typing.Optional[str] = None,
        reservation_affinity_values: typing.Optional[typing.List[str]] = None,
        spot: bool = False,
        required_replica_count: typing.Optional[int] = 0,
    ) -> google.cloud.aiplatform.models.DeploymentResourcePool

Creates a new DeploymentResourcePool.

**Parameters**  
---  
**Name** | **Description**  
`create_request_timeout` |  `float`   
Optional. The create request timeout in seconds.  
`reservation_affinity_type` |  `str`   
Optional. The type of reservation affinity. One of NO_RESERVATION, ANY_RESERVATION, SPECIFIC_RESERVATION, SPECIFIC_THEN_ANY_RESERVATION, SPECIFIC_THEN_NO_RESERVATION  
`reservation_affinity_key` |  `str`   
Optional. Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, use `compute.googleapis.com/reservation-name` as the key and specify the name of your reservation as its value.  
`reservation_affinity_values` |  `List[str]`   
Optional. Corresponds to the label values of a reservation resource. This must be the full resource name of the reservation. Format: 'projects/{project_id_or_number}/zones/{zone}/reservations/{reservation_name}'  
`spot` |  `bool`   
Optional. Whether to schedule the deployment workload on spot VMs.  
`required_replica_count` |  `int`   
Optional. Number of required available replicas for the deployment to succeed. This field is only needed when partial model deployment/mutation is desired, with a value greater than or equal to 1 and fewer than or equal to min_replica_count. If set, the model deploy/mutate operation will succeed once available_replica_count reaches required_replica_count, and the rest of the replicas will be retried.  
`deployment_resource_pool_id` |  `str`   
Required. User-specified name for the new deployment resource pool.  
`project` |  `str`   
Optional. Project containing the deployment resource pool to retrieve. If not set, the project given to `aiplatform.init` will be used.  
`location` |  `str`   
Optional. Location containing the deployment resource pool to retrieve. If not set, the location given to `aiplatform.init` will be used.  
`metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`machine_type` |  `str`   
Optional. Machine type to use for the deployment resource pool. If not set, the default machine type of `n1-standard-2` is used.  
`min_replica_count` |  `int`   
Optional. The minimum replica count of the new deployment resource pool. Each replica serves a copy of each model deployed on the deployment resource pool. If this value is less than `max_replica_count`, then autoscaling is enabled, and the actual number of replicas will be adjusted to bring resource usage in line with the autoscaling targets.  
`max_replica_count` |  `int`   
Optional. The maximum replica count of the new deployment resource pool.  
`accelerator_type` |  `str`   
Optional. Hardware accelerator type. Must also set accelerator_ count if used. One of NVIDIA_TESLA_K80, NVIDIA_TESLA_P100, NVIDIA_TESLA_V100, NVIDIA_TESLA_P4, NVIDIA_TESLA_T4, or NVIDIA_TESLA_A100.  
`accelerator_count` |  `int`   
Optional. The number of accelerators attached to each replica.  
`autoscaling_target_cpu_utilization` |  `int`   
Optional. Target CPU utilization value for autoscaling. A default value of 60 will be used if not specified.  
`autoscaling_target_accelerator_duty_cycle` |  `int`   
Optional. Target accelerator duty cycle percentage to use for autoscaling. Must also set accelerator_type and accelerator count if specified. A default value of 60 will be used if accelerators are requested and this is not specified.  
`sync` |  `bool`   
Optional. Whether to execute this method synchronously. If False, this method will be executed in a concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.models.DeploymentResourcePool]

Lists the deployment resource pools.

filter (str): Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported. order_by (str): Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: `display_name`, `create_time`, `update_time` project (str): Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used. location (str): Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used. credentials (auth_credentials.Credentials): Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.

### query_deployed_models
    
    
    query_deployed_models(
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform_v1.types.deployed_model_ref.DeployedModelRef]

Lists the deployed models using this resource pool.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `str`   
Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.  
  
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
