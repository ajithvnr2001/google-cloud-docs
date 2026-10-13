---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient
title: Class NotebookServiceClient (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:37.529005+00:00
---

# Class NotebookServiceClient (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class NotebookServiceClient (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 
    
    
    NotebookServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

API v1 service for Cloud AI Platform Notebooks.

## Properties 

### api_endpoint

Return the API endpoint used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The API endpoint used by the client instance.  
  
### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`NotebookServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### NotebookServiceClient
    
    
    NotebookServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the notebook service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,NotebookServiceTransport,Callable[..., NotebookServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the NotebookServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that the `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If mutual TLS transport creation failed for any reason.  
  
### __exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

**Warning:** ONLY use as a context manager if the transport is NOT shared with other clients! Exiting the with block will CLOSE the transport and may cause errors in other clients! 

### cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Starts asynchronous cancellation on a long-running operation.

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.CancelOperationRequest``   
The request object. Request message for `CancelOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

### common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

### common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

### common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

### common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

### create_environment
    
    
    create_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateEnvironmentRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        environment: typing.Optional[
            google.cloud.notebooks_v1.types.environment.Environment
        ] = None,
        environment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Environment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_create_environment():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        environment = notebooks_v1.[Environment](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Environment.html)()
        environment.vm_image.image_name = "image_name_value"
        environment.vm_image.project = "project_value"
    
        request = notebooks_v1.[CreateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateEnvironmentRequest.html)(
            parent="parent_value",
            environment_id="environment_id_value",
            environment=environment,
        )
    
        # Make the request
        operation = client.[create_environment](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_create_environment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.CreateEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateEnvironmentRequest), dict]`   
The request object. Request for creating a notebook environment.  
`parent` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`environment` |  `[google.cloud.notebooks_v1.types.Environment](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Environment)`   
Required. The environment to be created. This corresponds to the `environment` field on the `request` instance; if `request` is provided, this should not be set.  
`environment_id` |  `str`   
Required. User-defined unique ID of this environment. The `environment_id` must be 1 to 63 characters long and contain only lowercase letters, numeric characters, and dashes. The first character must be a lowercase letter and the last character cannot be a dash. This corresponds to the `environment_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Environment](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Environment) Definition of a software environment that is used to start a notebook instance.  
  
### create_execution
    
    
    create_execution(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateExecutionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        execution: typing.Optional[
            google.cloud.notebooks_v1.types.execution.Execution
        ] = None,
        execution_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Execution in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_create_execution():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[CreateExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateExecutionRequest.html)(
            parent="parent_value",
            execution_id="execution_id_value",
        )
    
        # Make the request
        operation = client.[create_execution](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_create_execution)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.CreateExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateExecutionRequest), dict]`   
The request object. Request to create notebook execution  
`parent` |  `str`   
Required. Format: `parent=projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`execution` |  `[google.cloud.notebooks_v1.types.Execution](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Execution)`   
Required. The execution to be created. This corresponds to the `execution` field on the `request` instance; if `request` is provided, this should not be set.  
`execution_id` |  `str`   
Required. User-defined unique ID of this execution. This corresponds to the `execution_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Execution](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Execution) The definition of a single executed notebook.  
  
### create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateInstanceRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance: typing.Optional[google.cloud.notebooks_v1.types.instance.Instance] = None,
        instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Instance in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_create_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        instance = notebooks_v1.Instance()
        instance.vm_image.image_name = "image_name_value"
        instance.vm_image.project = "project_value"
        instance.machine_type = "machine_type_value"
    
        request = notebooks_v1.CreateInstanceRequest(
            parent="parent_value",
            instance_id="instance_id_value",
            instance=instance,
        )
    
        # Make the request
        operation = client.[create_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_create_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.CreateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateInstanceRequest), dict]`   
The request object. Request for creating a notebook instance.  
`parent` |  `str`   
Required. Format: `parent=projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `[google.cloud.notebooks_v1.types.Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance)`   
Required. The instance to be created. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_id` |  `str`   
Required. User-defined unique ID of this instance. This corresponds to the `instance_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### create_schedule
    
    
    create_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateScheduleRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        schedule: typing.Optional[google.cloud.notebooks_v1.types.schedule.Schedule] = None,
        schedule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Scheduled Notebook in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_create_schedule():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[CreateScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateScheduleRequest.html)(
            parent="parent_value",
            schedule_id="schedule_id_value",
        )
    
        # Make the request
        operation = client.[create_schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_create_schedule)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.CreateScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateScheduleRequest), dict]`   
The request object. Request for created scheduled notebooks  
`parent` |  `str`   
Required. Format: `parent=projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`schedule` |  `[google.cloud.notebooks_v1.types.Schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Schedule)`   
Required. The schedule to be created. This corresponds to the `schedule` field on the `request` instance; if `request` is provided, this should not be set.  
`schedule_id` |  `str`   
Required. User-defined unique ID of this schedule. This corresponds to the `schedule_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Schedule) The definition of a schedule.  
  
### delete_environment
    
    
    delete_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteEnvironmentRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Deletes a single Environment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_delete_environment():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[DeleteEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteEnvironmentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_environment](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_environment)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.DeleteEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteEnvironmentRequest), dict]`   
The request object. Request for deleting a notebook environment.  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/environments/{environment_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_execution
    
    
    delete_execution(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteExecutionRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Deletes execution
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_delete_execution():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[DeleteExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteExecutionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_execution](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_execution)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.DeleteExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteExecutionRequest), dict]`   
The request object. Request for deleting a scheduled notebook execution  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/executions/{execution_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Deletes a single Instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_delete_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.DeleteInstanceRequest(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteInstanceRequest), dict]`   
The request object. Request for deleting a notebook instance.  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a long-running operation.

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.DeleteOperationRequest``   
The request object. Request message for `DeleteOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_schedule
    
    
    delete_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteScheduleRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Deletes schedule and all underlying jobs
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_delete_schedule():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[DeleteScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteScheduleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_schedule)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.DeleteScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteScheduleRequest), dict]`   
The request object. Request for deleting an Schedule  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### diagnose_instance
    
    
    diagnose_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DiagnoseInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        diagnostic_config: typing.Optional[
            google.cloud.notebooks_v1.types.diagnostic_config.DiagnosticConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a Diagnostic File and runs Diagnostic Tool given an Instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_diagnose_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        diagnostic_config = notebooks_v1.DiagnosticConfig()
        diagnostic_config.gcs_bucket = "gcs_bucket_value"
    
        request = notebooks_v1.DiagnoseInstanceRequest(
            name="name_value",
            diagnostic_config=diagnostic_config,
        )
    
        # Make the request
        operation = client.[diagnose_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_diagnose_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.DiagnoseInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnoseInstanceRequest), dict]`   
The request object. Request for creating a notebook instance diagnostic file.  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`diagnostic_config` |  `[google.cloud.notebooks_v1.types.DiagnosticConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnosticConfig)`   
Required. Defines flags that are used to run the diagnostic tool This corresponds to the `diagnostic_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### environment_path
    
    
    environment_path(project: str, environment: str) -> str

Returns a fully-qualified environment string.

### execution_path
    
    
    execution_path(project: str, location: str, execution: str) -> str

Returns a fully-qualified execution string.

### from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`NotebookServiceClient` | The constructed client.  
  
### from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

**Parameter**  
---  
**Name** | **Description**  
`info` |  `dict`   
The service account private key info.  
**Returns**  
---  
**Type** | **Description**  
`NotebookServiceClient` | The constructed client.  
  
### from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`NotebookServiceClient` | The constructed client.  
  
### get_environment
    
    
    get_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.GetEnvironmentRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.types.environment.Environment

Gets details of a single Environment.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_get_environment():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[GetEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetEnvironmentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_environment](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_environment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.GetEnvironmentRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetEnvironmentRequest), dict]`   
The request object. Request for getting a notebook environment.  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/environments/{environment_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.Environment](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Environment)` | Definition of a software environment that is used to start a notebook instance.  
  
### get_execution
    
    
    get_execution(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetExecutionRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.types.execution.Execution

Gets details of executions
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_get_execution():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[GetExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetExecutionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_execution](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_execution)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.GetExecutionRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetExecutionRequest), dict]`   
The request object. Request for getting scheduled notebook execution  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/executions/{execution_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.Execution](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Execution)` | The definition of a single executed notebook.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

Returns an empty policy if the function exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.GetIamPolicyRequest``   
The request object. Request message for `GetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetInstanceRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.types.instance.Instance

Gets details of a single Instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_get_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.GetInstanceRequest(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_instance)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetInstanceRequest), dict]`   
The request object. Request for getting a notebook instance.  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance)` | The definition of a notebook instance.  
  
### get_instance_health
    
    
    get_instance_health(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.GetInstanceHealthRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.types.service.GetInstanceHealthResponse

Check if a notebook instance is healthy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_get_instance_health():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[GetInstanceHealthRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetInstanceHealthRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_instance_health](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_instance_health)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.GetInstanceHealthRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetInstanceHealthRequest), dict]`   
The request object. Request for checking if a notebook instance is healthy.  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.GetInstanceHealthResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetInstanceHealthResponse)` | Response for checking if a notebook instance is healthy.  
  
### get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.Location`` | Location object.  
  
### get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated. Return the API endpoint and client cert source for mutual TLS.

The client cert source is determined in the following order: (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the client cert source is None. (2) if `client_options.client_cert_source` is provided, use the provided one; if the default client cert source exists, use the default one; otherwise the client cert source is None.

The API endpoint is determined in the following order: (1) if `client_options.api_endpoint` if provided, use the provided one. (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the default mTLS endpoint; if the environment variable is "never", use the default API endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise use the default API endpoint.

More details can be found at <https://google.aip.dev/auth/4114>.

**Parameter**  
---  
**Name** | **Description**  
`client_options` |  `google.api_core.client_options.ClientOptions`   
Custom options for the client. Only the `api_endpoint` and `client_cert_source` properties may be used in this method.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If any errors happen.  
**Returns**  
---  
**Type** | **Description**  
`Tuple[str, Callable[[], Tuple[bytes, bytes]]]` | returns the API endpoint and the client cert source to use.  
  
### get_operation
    
    
    get_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.GetOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.longrunning.operations_pb2.Operation

Gets the latest state of a long-running operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.GetOperationRequest``   
The request object. Request message for `GetOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### get_schedule
    
    
    get_schedule(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetScheduleRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.types.schedule.Schedule

Gets details of schedule
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_get_schedule():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[GetScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetScheduleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_schedule)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.GetScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetScheduleRequest), dict]`   
The request object. Request for getting scheduled notebook.  
`name` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.Schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Schedule)` | The definition of a schedule.  
  
### instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

### is_instance_upgradeable
    
    
    is_instance_upgradeable(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.IsInstanceUpgradeableRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.types.service.IsInstanceUpgradeableResponse

Check if a notebook instance is upgradable.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_is_instance_upgradeable():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[IsInstanceUpgradeableRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.IsInstanceUpgradeableRequest.html)(
            notebook_instance="notebook_instance_value",
        )
    
        # Make the request
        response = client.[is_instance_upgradeable](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_is_instance_upgradeable)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.IsInstanceUpgradeableRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.IsInstanceUpgradeableRequest), dict]`   
The request object. Request for checking if a notebook instance is upgradeable.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.IsInstanceUpgradeableResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.IsInstanceUpgradeableResponse)` | Response for checking if a notebook instance is upgradeable.  
  
### list_environments
    
    
    list_environments(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ListEnvironmentsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsPager

Lists environments in a project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_list_environments():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[ListEnvironmentsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListEnvironmentsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_environments](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_environments)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.ListEnvironmentsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListEnvironmentsRequest), dict]`   
The request object. Request for listing environments.  
`parent` |  `str`   
Required. Format: `projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsPager](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsPager)` | Response for listing environments. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_executions
    
    
    list_executions(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ListExecutionsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsPager

Lists executions in a given project and location
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_list_executions():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[ListExecutionsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListExecutionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_executions](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_executions)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.ListExecutionsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListExecutionsRequest), dict]`   
The request object. Request for listing scheduled notebook executions.  
`parent` |  `str`   
Required. Format: `parent=projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsPager](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsPager)` | Response for listing scheduled notebook executions Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ListInstancesRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesPager

Lists instances in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_list_instances():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.ListInstancesRequest(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_instances](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_instances)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListInstancesRequest), dict]`   
The request object. Request for listing notebook instances.  
`parent` |  `str`   
Required. Format: `parent=projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesPager](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesPager)` | Response for listing notebook instances. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.ListLocationsResponse`` | Response message for `ListLocations` method.  
  
### list_operations
    
    
    list_operations(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.ListOperationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.longrunning.operations_pb2.ListOperationsResponse

Lists operations that match the specified filter in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.ListOperationsRequest``   
The request object. Request message for `ListOperations` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
### list_schedules
    
    
    list_schedules(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ListSchedulesRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesPager

Lists schedules in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_list_schedules():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[ListSchedulesRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListSchedulesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_schedules](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_schedules)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.ListSchedulesRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListSchedulesRequest), dict]`   
The request object. Request for listing scheduled notebook job.  
`parent` |  `str`   
Required. Format: `parent=projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesPager](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesPager)` | Response for listing scheduled notebook job. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

### parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

### parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

### parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

### parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

### parse_environment_path
    
    
    parse_environment_path(path: str) -> typing.Dict[str, str]

Parses a environment path into its component segments.

### parse_execution_path
    
    
    parse_execution_path(path: str) -> typing.Dict[str, str]

Parses a execution path into its component segments.

### parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

### parse_schedule_path
    
    
    parse_schedule_path(path: str) -> typing.Dict[str, str]

Parses a schedule path into its component segments.

### parse_tensorboard_path
    
    
    parse_tensorboard_path(path: str) -> typing.Dict[str, str]

Parses a tensorboard path into its component segments.

### register_instance
    
    
    register_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.RegisterInstanceRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Registers an existing legacy notebook instance to the Notebooks API server. Legacy instances are instances created with the legacy Compute Engine calls. They are not manageable by the Notebooks API out of the box. This call makes these instances manageable by the Notebooks API.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_register_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[RegisterInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RegisterInstanceRequest.html)(
            parent="parent_value",
            instance_id="instance_id_value",
        )
    
        # Make the request
        operation = client.[register_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_register_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.RegisterInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RegisterInstanceRequest), dict]`   
The request object. Request for registering a notebook instance.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### report_instance_info
    
    
    report_instance_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ReportInstanceInfoRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Allows notebook instances to report their latest instance information to the Notebooks API server. The server will merge the reported information to the instance metadata store. Do not use this method directly.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_report_instance_info():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[ReportInstanceInfoRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ReportInstanceInfoRequest.html)(
            name="name_value",
            vm_id="vm_id_value",
        )
    
        # Make the request
        operation = client.[report_instance_info](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_report_instance_info)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.ReportInstanceInfoRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ReportInstanceInfoRequest), dict]`   
The request object. Request for notebook instances to report information to Notebooks API.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### reset_instance
    
    
    reset_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ResetInstanceRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Resets a notebook instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_reset_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.ResetInstanceRequest(
            name="name_value",
        )
    
        # Make the request
        operation = client.[reset_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_reset_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.ResetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ResetInstanceRequest), dict]`   
The request object. Request for resetting a notebook instance  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### rollback_instance
    
    
    rollback_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.RollbackInstanceRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Rollbacks a notebook instance to the previous version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_rollback_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.RollbackInstanceRequest(
            name="name_value",
            target_snapshot="target_snapshot_value",
        )
    
        # Make the request
        operation = client.[rollback_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_rollback_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.RollbackInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RollbackInstanceRequest), dict]`   
The request object. Request for rollbacking a notebook instance  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### schedule_path
    
    
    schedule_path(project: str, location: str, schedule: str) -> str

Returns a fully-qualified schedule string.

### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.SetIamPolicyRequest``   
The request object. Request message for `SetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### set_instance_accelerator
    
    
    set_instance_accelerator(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceAcceleratorRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates the guest accelerators of a single Instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_set_instance_accelerator():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[SetInstanceAcceleratorRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceAcceleratorRequest.html)(
            name="name_value",
            type_="TPU_V3",
            core_count=1073,
        )
    
        # Make the request
        operation = client.[set_instance_accelerator](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_set_instance_accelerator)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.SetInstanceAcceleratorRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceAcceleratorRequest), dict]`   
The request object. Request for setting instance accelerator.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### set_instance_labels
    
    
    set_instance_labels(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceLabelsRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Replaces all the labels of an Instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_set_instance_labels():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[SetInstanceLabelsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceLabelsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[set_instance_labels](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_set_instance_labels)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.SetInstanceLabelsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceLabelsRequest), dict]`   
The request object. Request for setting instance labels.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### set_instance_machine_type
    
    
    set_instance_machine_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceMachineTypeRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates the machine type of a single Instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_set_instance_machine_type():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[SetInstanceMachineTypeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceMachineTypeRequest.html)(
            name="name_value",
            machine_type="machine_type_value",
        )
    
        # Make the request
        operation = client.[set_instance_machine_type](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_set_instance_machine_type)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.SetInstanceMachineTypeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SetInstanceMachineTypeRequest), dict]`   
The request object. Request for setting instance machine type.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### start_instance
    
    
    start_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.StartInstanceRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Starts a notebook instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_start_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.StartInstanceRequest(
            name="name_value",
        )
    
        # Make the request
        operation = client.[start_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_start_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.StartInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StartInstanceRequest), dict]`   
The request object. Request for starting a notebook instance  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### stop_instance
    
    
    stop_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.StopInstanceRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Stops a notebook instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_stop_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.StopInstanceRequest(
            name="name_value",
        )
    
        # Make the request
        operation = client.[stop_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_stop_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.StopInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StopInstanceRequest), dict]`   
The request object. Request for stopping a notebook instance  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### tensorboard_path
    
    
    tensorboard_path(project: str, location: str, tensorboard: str) -> str

Returns a fully-qualified tensorboard string.

### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.TestIamPermissionsRequest``   
The request object. Request message for `TestIamPermissions` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.iam_policy_pb2.TestIamPermissionsResponse`` | Response message for `TestIamPermissions` method.  
  
### trigger_schedule
    
    
    trigger_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.TriggerScheduleRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Triggers execution of an existing schedule.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_trigger_schedule():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[TriggerScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.TriggerScheduleRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[trigger_schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_trigger_schedule)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.TriggerScheduleRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.TriggerScheduleRequest), dict]`   
The request object. Request for created scheduled notebooks  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Schedule](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Schedule) The definition of a schedule.  
  
### update_instance_config
    
    
    update_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateInstanceConfigRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Update Notebook Instance configurations.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_update_instance_config():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[UpdateInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateInstanceConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[update_instance_config](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_update_instance_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.UpdateInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateInstanceConfigRequest), dict]`   
The request object. Request for updating instance configurations.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### update_instance_metadata_items
    
    
    update_instance_metadata_items(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateInstanceMetadataItemsRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.types.service.UpdateInstanceMetadataItemsResponse

Add/update metadata items for an instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_update_instance_metadata_items():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[UpdateInstanceMetadataItemsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateInstanceMetadataItemsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[update_instance_metadata_items](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_update_instance_metadata_items)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.UpdateInstanceMetadataItemsRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateInstanceMetadataItemsRequest), dict]`   
The request object. Request for adding/changing metadata items for an instance.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.UpdateInstanceMetadataItemsResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateInstanceMetadataItemsResponse)` | Response for adding/changing metadata items for an instance.  
  
### update_shielded_instance_config
    
    
    update_shielded_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateShieldedInstanceConfigRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates the Shielded instance configuration of a single Instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_update_shielded_instance_config():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[UpdateShieldedInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateShieldedInstanceConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[update_shielded_instance_config](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_update_shielded_instance_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.UpdateShieldedInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateShieldedInstanceConfigRequest), dict]`   
The request object. Request for updating the Shielded Instance config for a notebook instance. You can only use this method on a stopped instance  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### upgrade_instance
    
    
    upgrade_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpgradeInstanceRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Upgrades a notebook instance to the latest version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_upgrade_instance():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.UpgradeInstanceRequest(
            name="name_value",
        )
    
        # Make the request
        operation = client.[upgrade_instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_upgrade_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.UpgradeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeInstanceRequest), dict]`   
The request object. Request for upgrading a notebook instance  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
### upgrade_instance_internal
    
    
    upgrade_instance_internal(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpgradeInstanceInternalRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Allows notebook instances to call this endpoint to upgrade themselves. Do not use this method directly.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    def sample_upgrade_instance_internal():
        # Create a client
        client = notebooks_v1.NotebookServiceClient()
    
        # Initialize request argument(s)
        request = notebooks_v1.[UpgradeInstanceInternalRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeInstanceInternalRequest.html)(
            name="name_value",
            vm_id="vm_id_value",
        )
    
        # Make the request
        operation = client.[upgrade_instance_internal](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.html#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_upgrade_instance_internal)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.notebooks_v1.types.UpgradeInstanceInternalRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeInstanceInternalRequest), dict]`   
The request object. Request for upgrading a notebook instance from within the VM  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Instance) The definition of a notebook instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
