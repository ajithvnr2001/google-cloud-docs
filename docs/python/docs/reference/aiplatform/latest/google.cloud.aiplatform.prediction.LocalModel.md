---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalModel
title: Class LocalModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:18.767894+00:00
---

# Class LocalModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.prediction.LocalModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LocalModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    LocalModel(
        serving_container_spec: typing.Optional[
            google.cloud.aiplatform_v1.types.model.ModelContainerSpec
        ] = None,
        serving_container_image_uri: typing.Optional[str] = None,
        serving_container_predict_route: typing.Optional[str] = None,
        serving_container_health_route: typing.Optional[str] = None,
        serving_container_command: typing.Optional[typing.Sequence[str]] = None,
        serving_container_args: typing.Optional[typing.Sequence[str]] = None,
        serving_container_environment_variables: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        serving_container_ports: typing.Optional[typing.Sequence[int]] = None,
        serving_container_grpc_ports: typing.Optional[typing.Sequence[int]] = None,
        serving_container_deployment_timeout: typing.Optional[int] = None,
        serving_container_shared_memory_size_mb: typing.Optional[int] = None,
        serving_container_startup_probe_exec: typing.Optional[typing.Sequence[str]] = None,
        serving_container_startup_probe_period_seconds: typing.Optional[int] = None,
        serving_container_startup_probe_timeout_seconds: typing.Optional[int] = None,
        serving_container_health_probe_exec: typing.Optional[typing.Sequence[str]] = None,
        serving_container_health_probe_period_seconds: typing.Optional[int] = None,
        serving_container_health_probe_timeout_seconds: typing.Optional[int] = None,
    )

Class that represents a local model.

## Methods 

### LocalModel
    
    
    LocalModel(
        serving_container_spec: typing.Optional[
            google.cloud.aiplatform_v1.types.model.ModelContainerSpec
        ] = None,
        serving_container_image_uri: typing.Optional[str] = None,
        serving_container_predict_route: typing.Optional[str] = None,
        serving_container_health_route: typing.Optional[str] = None,
        serving_container_command: typing.Optional[typing.Sequence[str]] = None,
        serving_container_args: typing.Optional[typing.Sequence[str]] = None,
        serving_container_environment_variables: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        serving_container_ports: typing.Optional[typing.Sequence[int]] = None,
        serving_container_grpc_ports: typing.Optional[typing.Sequence[int]] = None,
        serving_container_deployment_timeout: typing.Optional[int] = None,
        serving_container_shared_memory_size_mb: typing.Optional[int] = None,
        serving_container_startup_probe_exec: typing.Optional[typing.Sequence[str]] = None,
        serving_container_startup_probe_period_seconds: typing.Optional[int] = None,
        serving_container_startup_probe_timeout_seconds: typing.Optional[int] = None,
        serving_container_health_probe_exec: typing.Optional[typing.Sequence[str]] = None,
        serving_container_health_probe_period_seconds: typing.Optional[int] = None,
        serving_container_health_probe_timeout_seconds: typing.Optional[int] = None,
    )

Creates a local model instance.

**Parameters**  
---  
**Name** | **Description**  
`serving_container_spec` |  `aiplatform.gapic.ModelContainerSpec`   
Optional. The container spec of the LocalModel instance.  
`serving_container_image_uri` |  `str`   
Optional. The URI of the Model serving container.  
`serving_container_predict_route` |  `str`   
Optional. An HTTP path to send prediction requests to the container, and which must be supported by it. If not specified a default HTTP path will be used by Vertex AI.  
`serving_container_health_route` |  `str`   
Optional. An HTTP path to send health check requests to the container, and which must be supported by it. If not specified a standard HTTP path will be used by Vertex AI.  
`serving_container_command` |  `Sequence[str]`   
Optional. The command with which the container is run. Not executed within a shell. The Docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not.  
`serving_container_args` |  `typing.Optional[typing.Sequence[str]]`   
(Sequence[str]): Optional. The arguments to the command. The Docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not.  
`serving_container_environment_variables` |  `Dict[str, str]`   
Optional. The environment variables that are to be present in the container. Should be a dictionary where keys are environment variable names and values are environment variable values for those names.  
`serving_container_ports` |  `Sequence[int]`   
Optional. Declaration of ports that are exposed by the container. This field is primarily informational, it gives Vertex AI information about the network connections the container uses. Listing or not a port here has no impact on whether the port is actually exposed, any port listening on the default "0.0.0.0" address inside a container will be accessible from the network.  
`serving_container_grpc_ports` |  `typing.Optional[typing.Sequence[int]]`   
Optional[Sequence[int]]=None, Declaration of ports that are exposed by the container. Vertex AI sends gRPC prediction requests that it receives to the first port on this list. Vertex AI also sends liveness and health checks to this port. If you do not specify this field, gRPC requests to the container will be disabled. Vertex AI does not use ports other than the first one listed. This field corresponds to the `ports` field of the Kubernetes Containers v1 core API.  
`serving_container_deployment_timeout` |  `int`   
Optional. Deployment timeout in seconds.  
`serving_container_shared_memory_size_mb` |  `int`   
Optional. The amount of the VM memory to reserve as the shared memory for the model in megabytes.  
`serving_container_startup_probe_exec` |  `Sequence[str]`   
Optional. Exec specifies the action to take. Used by startup probe. An example of this argument would be ["cat", "/tmp/healthy"]  
`serving_container_startup_probe_period_seconds` |  `int`   
Optional. How often (in seconds) to perform the startup probe. Default to 10 seconds. Minimum value is 1.  
`serving_container_startup_probe_timeout_seconds` |  `int`   
Optional. Number of seconds after which the startup probe times out. Defaults to 1 second. Minimum value is 1.  
`serving_container_health_probe_exec` |  `Sequence[str]`   
Optional. Exec specifies the action to take. Used by health probe. An example of this argument would be ["cat", "/tmp/healthy"]  
`serving_container_health_probe_period_seconds` |  `int`   
Optional. How often (in seconds) to perform the health probe. Default to 10 seconds. Minimum value is 1.  
`serving_container_health_probe_timeout_seconds` |  `int`   
Optional. Number of seconds after which the health probe times out. Defaults to 1 second. Minimum value is 1.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `serving_container_spec` is specified but `serving_container_spec.image_uri` is `None`. Also if `serving_container_spec` is None but `serving_container_image_uri` is `None`.  
  
### build_cpr_model
    
    
    build_cpr_model(
        src_dir: str,
        output_image_uri: str,
        predictor: typing.Optional[
            typing.Type[google.cloud.aiplatform.prediction.predictor.Predictor]
        ] = None,
        handler: typing.Type[
            google.cloud.aiplatform.prediction.handler.Handler
        ] = google.cloud.aiplatform.prediction.handler.PredictionHandler,
        base_image: str = "python:3.10",
        requirements_path: typing.Optional[str] = None,
        extra_packages: typing.Optional[typing.List[str]] = None,
        no_cache: bool = False,
        platform: typing.Optional[str] = None,
    ) -> google.cloud.aiplatform.prediction.local_model.LocalModel

Builds a local model from a custom predictor.

This method builds a docker image to include user-provided predictor, and handler.

Sample `src_dir` contents (e.g. `./user_src_dir`):
    
    
    user_src_dir/
    |-- predictor.py
    |-- requirements.txt
    |-- user_code/
    |   |-- utils.py
    |   |-- custom_package.tar.gz
    |   |-- ...
    |-- ...
    

To build a custom container:
    
    
    local_model = LocalModel.build_cpr_model(
        "./user_src_dir",
        "us-docker.pkg.dev/$PROJECT/$REPOSITORY/$IMAGE_NAME$",
        predictor=$CUSTOM_PREDICTOR_CLASS,
        requirements_path="./user_src_dir/requirements.txt",
        extra_packages=["./user_src_dir/user_code/custom_package.tar.gz"],
        platform="linux/amd64", # i.e., if you're building on a non-x86 machine
    )
    

In the built image, user provided files will be copied as follows:
    
    
    container_workdir/
    |-- predictor.py
    |-- requirements.txt
    |-- user_code/
    |   |-- utils.py
    |   |-- custom_package.tar.gz
    |   |-- ...
    |-- ...
    

To exclude files and directories from being copied into the built container images, create a `.dockerignore` file in the `src_dir`. See <https://docs.docker.com/engine/reference/builder/#dockerignore-file> for more details about usage.

In order to save and restore class instances transparently with Pickle, the class definition must be importable and live in the same module as when the object was stored. If you want to use Pickle, you must save your objects right under the `src_dir` you provide.

The created CPR images default the number of model server workers to the number of cores. Depending on the characteristics of your model, you may need to adjust the number of workers. You can set the number of workers with the following environment variables:
    
    
    VERTEX_CPR_WEB_CONCURRENCY:
        The number of the workers. This will overwrite the number calculated by the other
        variables, min(VERTEX_CPR_WORKERS_PER_CORE * number_of_cores, VERTEX_CPR_MAX_WORKERS).
    VERTEX_CPR_WORKERS_PER_CORE:
        The number of the workers per core. The default is 1.
    VERTEX_CPR_MAX_WORKERS:
        The maximum number of workers can be used given the value of VERTEX_CPR_WORKERS_PER_CORE
        and the number of cores.
    

If you hit the error showing "model server container out of memory" when you deploy models to endpoints, you should decrease the number of workers.

**Parameters**  
---  
**Name** | **Description**  
`src_dir` |  `str`   
Required. The path to the local directory including all needed files such as predictor. The whole directory will be copied to the image.  
`output_image_uri` |  `str`   
Required. The image uri of the built image.  
`predictor` |  `Type[Predictor]`   
Optional. The custom predictor class consumed by handler to do prediction.  
`handler` |  `Type[Handler]`   
Required. The handler class to handle requests in the model server.  
`base_image` |  `str`   
Required. The base image used to build the custom images. The base image must have python and pip installed where the two commands `python` and `pip` must be available.  
`requirements_path` |  `str`   
Optional. The path to the local requirements.txt file. This file will be copied to the image and the needed packages listed in it will be installed.  
`extra_packages` |  `List[str]`   
Optional. The list of user custom dependency packages to install.  
`no_cache` |  `bool`   
Required. Do not use cache when building the image. Using build cache usually reduces the image building time. See <https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#leverage-build-cache> for more details.  
`platform` |  `str`   
Optional. The target platform for the Docker image build. See <https://docs.docker.com/build/building/multi-platform/#building-multi-platform-images> for more details.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If handler is `None` or if handler is `PredictionHandler` but predictor is `None`.  
**Returns**  
---  
**Type** | **Description**  
`local model` | Instantiated representation of the local model.  
  
### copy_image
    
    
    copy_image(
        dst_image_uri: str,
    ) -> google.cloud.aiplatform.prediction.local_model.LocalModel

Copies the image to another image uri.

**Parameter**  
---  
**Name** | **Description**  
`dst_image_uri` |  `str`   
The destination image uri to copy the image to.  
**Exceptions**  
---  
**Type** | **Description**  
`DockerError` | If the command fails.  
**Returns**  
---  
**Type** | **Description**  
`local model` | Instantiated representation of the local model with the copied image.  
  
### deploy_to_local_endpoint
    
    
    deploy_to_local_endpoint(
        artifact_uri: typing.Optional[str] = None,
        credential_path: typing.Optional[str] = None,
        host_port: typing.Optional[str] = None,
        gpu_count: typing.Optional[int] = None,
        gpu_device_ids: typing.Optional[typing.List[str]] = None,
        gpu_capabilities: typing.Optional[typing.List[typing.List[str]]] = None,
        container_ready_timeout: typing.Optional[int] = None,
        container_ready_check_interval: typing.Optional[int] = None,
    ) -> google.cloud.aiplatform.prediction.local_endpoint.LocalEndpoint

Deploys the local model instance to a local endpoint.

An environment variable, `GOOGLE_CLOUD_PROJECT`, will be set to the project in the global config. This is required if the credentials file does not have project specified and used to recognize the project by the Cloud Storage client.

Example 1:
    
    
    with local_model.deploy_to_local_endpoint(
        artifact_uri="gs://path/to/your/model",
        credential_path="local/path/to/your/credentials",
    ) as local_endpoint:
        health_check_response = local_endpoint.run_health_check()
        print(health_check_response, health_check_response.content)
    
        predict_response = local_endpoint.predict(
            request='{"instances": [[1, 2, 3, 4]]}',
            headers={"header-key": "header-value"},
        )
        print(predict_response, predict_response.content)
    
        local_endpoint.print_container_logs()
    

Example 2:
    
    
    local_endpoint = local_model.deploy_to_local_endpoint(
        artifact_uri="gs://path/to/your/model",
        credential_path="local/path/to/your/credentials",
    )
    local_endpoint.serve()
    
    health_check_response = local_endpoint.run_health_check()
    print(health_check_response, health_check_response.content)
    
    predict_response = local_endpoint.predict(
        request='{"instances": [[1, 2, 3, 4]]}',
        headers={"header-key": "header-value"},
    )
    print(predict_response, predict_response.content)
    
    local_endpoint.print_container_logs()
    local_endpoint.stop()
    

**Parameters**  
---  
**Name** | **Description**  
`artifact_uri` |  `str`   
Optional. The path to the directory containing the Model artifact and any of its supporting files. The path is either a GCS uri or the path to a local directory. If this parameter is set to a GCS uri: (1) `credential_path` must be specified for local prediction. (2) The GCS uri will be passed directly to `Predictor.load`. If this parameter is a local directory: (1) The directory will be mounted to a default temporary model path. (2) The mounted path will be passed to `Predictor.load`.  
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
  
### get_serving_container_spec
    
    
    get_serving_container_spec() -> (
        google.cloud.aiplatform_v1.types.model.ModelContainerSpec
    )

Returns the container spec for the image.

### pull_image_if_not_exists
    
    
    pull_image_if_not_exists()

Pulls the image if the image does not exist locally.

**Exceptions**  
---  
**Type** | **Description**  
`DockerError` | If the command fails.  
  
### push_image
    
    
    push_image() -> None

Pushes the image to a registry.

If you hit permission errors while calling this function, please refer to <https://cloud.google.com/artifact-registry/docs/docker/authentication> to set up the authentication.

For Artifact Registry, the repository must be created before you are able to push images to it. Otherwise, you will hit the error, "Repository {REPOSITORY} not found". To create Artifact Registry repositories, use UI or call the following gcloud command.
    
    
    gcloud artifacts repositories create {REPOSITORY}                 --project {PROJECT}                 --location {REGION}                 --repository-format docker
    

See <https://cloud.google.com/artifact-registry/docs/manage-repos#create> for more details.

If you hit a "Permission artifactregistry.repositories.uploadArtifacts denied" error, set up authentication for Docker.
    
    
    gcloud auth configure-docker {REPOSITORY}
    

See <https://cloud.google.com/artifact-registry/docs/docker/authentication> for mode details.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the image uri is not a container registry or artifact registry uri.  
`DockerError` | If the command fails.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
