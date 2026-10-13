---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalEndpoint
title: Class LocalEndpoint (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:17.878287+00:00
---

# Class LocalEndpoint (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalEndpoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LocalEndpoint (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    LocalEndpoint(
        serving_container_image_uri: str,
        artifact_uri: typing.Optional[str] = None,
        serving_container_predict_route: typing.Optional[str] = None,
        serving_container_health_route: typing.Optional[str] = None,
        serving_container_command: typing.Optional[typing.Sequence[str]] = None,
        serving_container_args: typing.Optional[typing.Sequence[str]] = None,
        serving_container_environment_variables: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        serving_container_ports: typing.Optional[typing.Sequence[int]] = None,
        credential_path: typing.Optional[str] = None,
        host_port: typing.Optional[str] = None,
        gpu_count: typing.Optional[int] = None,
        gpu_device_ids: typing.Optional[typing.List[str]] = None,
        gpu_capabilities: typing.Optional[typing.List[typing.List[str]]] = None,
        container_ready_timeout: typing.Optional[int] = None,
        container_ready_check_interval: typing.Optional[int] = None,
    )

Class that represents a local endpoint.

## Methods 

### LocalEndpoint
    
    
    LocalEndpoint(
        serving_container_image_uri: str,
        artifact_uri: typing.Optional[str] = None,
        serving_container_predict_route: typing.Optional[str] = None,
        serving_container_health_route: typing.Optional[str] = None,
        serving_container_command: typing.Optional[typing.Sequence[str]] = None,
        serving_container_args: typing.Optional[typing.Sequence[str]] = None,
        serving_container_environment_variables: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        serving_container_ports: typing.Optional[typing.Sequence[int]] = None,
        credential_path: typing.Optional[str] = None,
        host_port: typing.Optional[str] = None,
        gpu_count: typing.Optional[int] = None,
        gpu_device_ids: typing.Optional[typing.List[str]] = None,
        gpu_capabilities: typing.Optional[typing.List[typing.List[str]]] = None,
        container_ready_timeout: typing.Optional[int] = None,
        container_ready_check_interval: typing.Optional[int] = None,
    )

Creates a local endpoint instance.

**Parameters**  
---  
**Name** | **Description**  
`serving_container_image_uri` |  `str`   
Required. The URI of the Model serving container.  
`artifact_uri` |  `str`   
Optional. The path to the directory containing the Model artifact and any of its supporting files. The path is either a GCS uri or the path to a local directory. If this parameter is set to a GCS uri: (1) `credential_path` must be specified for local prediction. (2) The GCS uri will be passed directly to `Predictor.load`. If this parameter is a local directory: (1) The directory will be mounted to a default temporary model path. (2) The mounted path will be passed to `Predictor.load`.  
`serving_container_predict_route` |  `str`   
Optional. An HTTP path to send prediction requests to the container, and which must be supported by it. If not specified a default HTTP path will be used by Vertex AI.  
`serving_container_health_route` |  `str`   
Optional. An HTTP path to send health check requests to the container, and which must be supported by it. If not specified a standard HTTP path will be used by Vertex AI.  
`serving_container_command` |  `Sequence[str]`   
Optional. The command with which the container is run. Not executed within a shell. The Docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not.  
`serving_container_environment_variables` |  `Dict[str, str]`   
Optional. The environment variables that are to be present in the container. Should be a dictionary where keys are environment variable names and values are environment variable values for those names.  
`serving_container_ports` |  `Sequence[int]`   
Optional. Declaration of ports that are exposed by the container. This field is primarily informational, it gives Vertex AI information about the network connections the container uses. Listing or not a port here has no impact on whether the port is actually exposed, any port listening on the default "0.0.0.0" address inside a container will be accessible from the network.  
`credential_path` |  `str`   
Optional. The path to the credential key that will be mounted to the container. If it's unset, the environment variable, `GOOGLE_APPLICATION_CREDENTIALS`, will be used if set.  
`host_port` |  `str`   
Optional. The port on the host that the port, `AIP_HTTP_PORT`, inside the container will be exposed as. If it's unset, a random host port will be assigned.  
`gpu_count` |  `int`   
Optional. Number of devices to request. Set to -1 to request all available devices. To use GPU, set either `gpu_count` or `gpu_device_ids`. The default value is -1 if `gpu_capabilities` is set but both `gpu_count` and `gpu_device_ids` are not set.  
`gpu_device_ids` |  `List[str]`   
Optional. This parameter corresponds to `NVIDIA_VISIBLE_DEVICES` in the NVIDIA Runtime. To use GPU, set either `gpu_count` or `gpu_device_ids`.  
`gpu_capabilities` |  `List[List[str]]`   
Optional. This parameter corresponds to `NVIDIA_DRIVER_CAPABILITIES` in the NVIDIA Runtime. The outer list acts like an OR, and each sub-list acts like an AND. The driver will try to satisfy one of the sub-lists. Available capabilities for the NVIDIA driver can be found in <https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/user-guide.html#driver-capabilities>. The default value is `[["utility", "compute"]]` if `gpu_count` or `gpu_device_ids` is set.  
`container_ready_timeout` |  `int`   
Optional. The timeout in second used for starting the container or succeeding the first health check.  
`container_ready_check_interval` |  `int`   
Optional. The time interval in second to check if the container is ready or the first health check succeeds.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If both `gpu_count` and `gpu_device_ids` are set.  
  
### __del__
    
    
    __del__()

Stops the container when the instance is about to be destroyed.

### __enter__
    
    
    __enter__()

Enters the runtime context related to this object.

### __exit__
    
    
    __exit__(exc_type, exc_value, exc_traceback)

Exits the runtime context related to this object.

### get_container_status
    
    
    get_container_status() -> str

Gets the container status.

### predict
    
    
    predict(
        request: typing.Optional[typing.Any] = None,
        request_file: typing.Optional[str] = None,
        headers: typing.Optional[typing.Dict] = None,
        verbose: bool = True,
    ) -> requests.models.Response

Executes a prediction.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Any`   
Optional. The request sent to the container.  
`request_file` |  `str`   
Optional. The path to a request file sent to the container.  
`headers` |  `Dict`   
Optional. The headers in the prediction request.  
`verbose` |  `bool`   
Required. Whether or not print logs if any.  
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If the local endpoint has been stopped.  
`ValueError` | If both `request` and `request_file` are specified, both `request` and `request_file` are not provided, or `request_file` is specified but does not exist.  
`requests.exception.RequestException` | If the request fails with an exception.  
  
### print_container_logs
    
    
    print_container_logs(
        show_all: bool = False, message: typing.Optional[str] = None
    ) -> None

Prints container logs.

**Parameters**  
---  
**Name** | **Description**  
`show_all` |  `bool`   
Required. If True, prints all logs since the container starts.  
`message` |  `str`   
Optional. The message to be printed before printing the logs.  
  
### print_container_logs_if_container_is_not_running
    
    
    print_container_logs_if_container_is_not_running(
        show_all: bool = False, message: typing.Optional[str] = None
    ) -> None

Prints container logs if the container is not in "running" status.

**Parameters**  
---  
**Name** | **Description**  
`show_all` |  `bool`   
Required. If True, prints all logs since the container starts.  
`message` |  `str`   
Optional. The message to be printed before printing the logs.  
  
### run_health_check
    
    
    run_health_check(verbose: bool = True) -> requests.models.Response

Runs a health check.

**Parameter**  
---  
**Name** | **Description**  
`verbose` |  `bool`   
Required. Whether or not print logs if any.  
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If the local endpoint has been stopped.  
`requests.exception.RequestException` | If the request fails with an exception.  
  
### serve
    
    
    serve()

Starts running the container and serves the traffic locally.

An environment variable, `GOOGLE_CLOUD_PROJECT`, will be set to the project in the global config. This is required if the credentials file does not have project specified and used to recognize the project by the Cloud Storage client.

**Exceptions**  
---  
**Type** | **Description**  
`DockerError` | If the container is not ready or health checks do not succeed after the timeout.  
  
### stop
    
    
    stop() -> None

Explicitly stops the container.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
