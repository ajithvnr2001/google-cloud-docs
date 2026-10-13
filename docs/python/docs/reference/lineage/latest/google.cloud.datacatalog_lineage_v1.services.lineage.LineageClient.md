---
url: https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient
title: Class LineageClient (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:00.417560+00:00
---

# Class LineageClient (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class LineageClient (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.14  0.2.3 
    
    
    LineageClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.datacatalog_lineage_v1.services.lineage.transports.base.LineageTransport,
                typing.Callable[
                    [...],
                    google.cloud.datacatalog_lineage_v1.services.lineage.transports.base.LineageTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Lineage is used to track data flows between assets over time. You can create LineageEvents to record lineage between multiple sources and a single target, for example, when table data is based on data from multiple tables.

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
`LineageTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### LineageClient
    
    
    LineageClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.datacatalog_lineage_v1.services.lineage.transports.base.LineageTransport,
                typing.Callable[
                    [...],
                    google.cloud.datacatalog_lineage_v1.services.lineage.transports.base.LineageTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the lineage client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,LineageTransport,Callable[..., LineageTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the LineageTransport constructor. If set to None, a transport is chosen automatically.  
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

### batch_search_link_processes
    
    
    batch_search_link_processes(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.BatchSearchLinkProcessesRequest,
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
    ) -> (
        google.cloud.datacatalog_lineage_v1.services.lineage.pagers.BatchSearchLinkProcessesPager
    )

Retrieve information about LineageProcesses associated with specific links. LineageProcesses are transformation pipelines that result in data flowing from **source** to **target** assets. Links between assets represent this operation.

If you have specific link names, you can use this method to verify which LineageProcesses contribute to creating those links. See the xref_SearchLinks method for more information on how to retrieve link name.

You can retrieve the LineageProcess information in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_batch_search_link_processes():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesRequest.html)(
            parent="parent_value",
            links=['links_value1', 'links_value2'],
        )
    
        # Make the request
        page_result = client.[batch_search_link_processes](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_batch_search_link_processes)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.BatchSearchLinkProcessesRequest), dict]`   
The request object. Request message for BatchSearchLinkProcesses.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.services.lineage.pagers.BatchSearchLinkProcessesPager](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.pagers.BatchSearchLinkProcessesPager)` | Response message for BatchSearchLinkProcesses. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### create_lineage_event
    
    
    create_lineage_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.CreateLineageEventRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        lineage_event: typing.Optional[
            google.cloud.datacatalog_lineage_v1.types.lineage.LineageEvent
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datacatalog_lineage_v1.types.lineage.LineageEvent

Creates a new lineage event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_create_lineage_event():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[CreateLineageEventRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.CreateLineageEventRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_lineage_event](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_create_lineage_event)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.CreateLineageEventRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.CreateLineageEventRequest), dict]`   
The request object. Request message for CreateLineageEvent.  
`parent` |  `str`   
Required. The name of the run that should own the lineage event. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`lineage_event` |  `[google.cloud.datacatalog_lineage_v1.types.LineageEvent](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.LineageEvent)`   
Required. The lineage event to create. This corresponds to the `lineage_event` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.LineageEvent](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.LineageEvent)` | A lineage event represents an operation on assets. Within the operation, the data flows from the source to the target defined in the links field.  
  
### create_process
    
    
    create_process(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.CreateProcessRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        process: typing.Optional[
            google.cloud.datacatalog_lineage_v1.types.lineage.Process
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datacatalog_lineage_v1.types.lineage.Process

Creates a new process.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_create_process():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[CreateProcessRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.CreateProcessRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_create_process)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.CreateProcessRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.CreateProcessRequest), dict]`   
The request object. Request message for CreateProcess.  
`parent` |  `str`   
Required. The name of the project and its location that should own the process. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`process` |  `[google.cloud.datacatalog_lineage_v1.types.Process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Process)`   
Required. The process to create. This corresponds to the `process` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.Process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Process)` | A process is the definition of a data transformation operation.  
  
### create_run
    
    
    create_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.CreateRunRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        run: typing.Optional[google.cloud.datacatalog_lineage_v1.types.lineage.Run] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datacatalog_lineage_v1.types.lineage.Run

Creates a new run.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_create_run():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        run = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[Run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Run.html)()
        run.state = "ABORTED"
    
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[CreateRunRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.CreateRunRequest.html)(
            parent="parent_value",
            run=run,
        )
    
        # Make the request
        response = client.[create_run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_create_run)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.CreateRunRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.CreateRunRequest), dict]`   
The request object. Request message for CreateRun.  
`parent` |  `str`   
Required. The name of the process that should own the run. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`run` |  `[google.cloud.datacatalog_lineage_v1.types.Run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Run)`   
Required. The run to create. This corresponds to the `run` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.Run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Run)` | A lineage run represents an execution of a process that creates lineage events.  
  
### delete_lineage_event
    
    
    delete_lineage_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.DeleteLineageEventRequest,
                dict,
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
    ) -> None

Deletes the lineage event with the specified name.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_delete_lineage_event():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[DeleteLineageEventRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.DeleteLineageEventRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_lineage_event](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_delete_lineage_event)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.DeleteLineageEventRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.DeleteLineageEventRequest), dict]`   
The request object. Request message for DeleteLineageEvent.  
`name` |  `str`   
Required. The name of the lineage event to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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
  
### delete_process
    
    
    delete_process(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.DeleteProcessRequest, dict
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

Deletes the process with the specified name.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_delete_process():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[DeleteProcessRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.DeleteProcessRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_delete_process)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.DeleteProcessRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.DeleteProcessRequest), dict]`   
The request object. Request message for DeleteProcess.  
`name` |  `str`   
Required. The name of the process to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_run
    
    
    delete_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.DeleteRunRequest, dict
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

Deletes the run with the specified name.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_delete_run():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[DeleteRunRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.DeleteRunRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_delete_run)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.DeleteRunRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.DeleteRunRequest), dict]`   
The request object. Request message for DeleteRun.  
`name` |  `str`   
Required. The name of the run to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`LineageClient` | The constructed client.  
  
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
`LineageClient` | The constructed client.  
  
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
`LineageClient` | The constructed client.  
  
### get_lineage_event
    
    
    get_lineage_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.GetLineageEventRequest,
                dict,
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
    ) -> google.cloud.datacatalog_lineage_v1.types.lineage.LineageEvent

Gets details of a specified lineage event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_get_lineage_event():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[GetLineageEventRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.GetLineageEventRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_lineage_event](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_get_lineage_event)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.GetLineageEventRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.GetLineageEventRequest), dict]`   
The request object. Request message for GetLineageEvent.  
`name` |  `str`   
Required. The name of the lineage event to get. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.LineageEvent](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.LineageEvent)` | A lineage event represents an operation on assets. Within the operation, the data flows from the source to the target defined in the links field.  
  
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
  
### get_process
    
    
    get_process(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.GetProcessRequest, dict
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
    ) -> google.cloud.datacatalog_lineage_v1.types.lineage.Process

Gets the details of the specified process.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_get_process():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[GetProcessRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.GetProcessRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_get_process)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.GetProcessRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.GetProcessRequest), dict]`   
The request object. Request message for GetProcess.  
`name` |  `str`   
Required. The name of the process to get. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.Process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Process)` | A process is the definition of a data transformation operation.  
  
### get_run
    
    
    get_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.GetRunRequest, dict
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
    ) -> google.cloud.datacatalog_lineage_v1.types.lineage.Run

Gets the details of the specified run.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_get_run():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[GetRunRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.GetRunRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_get_run)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.GetRunRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.GetRunRequest), dict]`   
The request object. Request message for GetRun.  
`name` |  `str`   
Required. The name of the run to get. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.Run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Run)` | A lineage run represents an execution of a process that creates lineage events.  
  
### lineage_event_path
    
    
    lineage_event_path(
        project: str, location: str, process: str, run: str, lineage_event: str
    ) -> str

Returns a fully-qualified lineage_event string.

### list_lineage_events
    
    
    list_lineage_events(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.ListLineageEventsRequest,
                dict,
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
    ) -> google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListLineageEventsPager

Lists lineage events in the given project and location. The list order is not defined.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_list_lineage_events():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[ListLineageEventsRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ListLineageEventsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_lineage_events](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_list_lineage_events)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.ListLineageEventsRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ListLineageEventsRequest), dict]`   
The request object. Request message for ListLineageEvents.  
`parent` |  `str`   
Required. The name of the run that owns the collection of lineage events to get. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListLineageEventsPager](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListLineageEventsPager)` | Response message for ListLineageEvents. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_processes
    
    
    list_processes(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.ListProcessesRequest, dict
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
    ) -> google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListProcessesPager

List processes in the given project and location. List order is descending by insertion time.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_list_processes():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[ListProcessesRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ListProcessesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_processes](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_list_processes)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.ListProcessesRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ListProcessesRequest), dict]`   
The request object. Request message for ListProcesses.  
`parent` |  `str`   
Required. The name of the project and its location that owns this collection of processes. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListProcessesPager](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListProcessesPager)` | Response message for ListProcesses. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_runs
    
    
    list_runs(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.ListRunsRequest, dict
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
    ) -> google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListRunsPager

Lists runs in the given project and location. List order is descending by `start_time`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_list_runs():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[ListRunsRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ListRunsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_runs](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_list_runs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.ListRunsRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ListRunsRequest), dict]`   
The request object. Request message for ListRuns.  
`parent` |  `str`   
Required. The name of process that owns this collection of runs. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListRunsPager](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.pagers.ListRunsPager)` | Response message for ListRuns. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_lineage_event_path
    
    
    parse_lineage_event_path(path: str) -> typing.Dict[str, str]

Parses a lineage_event path into its component segments.

### parse_process_path
    
    
    parse_process_path(path: str) -> typing.Dict[str, str]

Parses a process path into its component segments.

### parse_run_path
    
    
    parse_run_path(path: str) -> typing.Dict[str, str]

Parses a run path into its component segments.

### process_open_lineage_run_event
    
    
    process_open_lineage_run_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.ProcessOpenLineageRunEventRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        open_lineage: typing.Optional[google.protobuf.struct_pb2.Struct] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.datacatalog_lineage_v1.types.lineage.ProcessOpenLineageRunEventResponse
    )

Creates new lineage events together with their parents: process and run. Updates the process and run if they already exist. Mapped from Open Lineage specification:

<https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json>.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_process_open_lineage_run_event():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[ProcessOpenLineageRunEventRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ProcessOpenLineageRunEventRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[process_open_lineage_run_event](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_process_open_lineage_run_event)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.ProcessOpenLineageRunEventRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ProcessOpenLineageRunEventRequest), dict]`   
The request object. Request message for ProcessOpenLineageRunEvent.  
`parent` |  `str`   
Required. The name of the project and its location that should own the process, run, and lineage event. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`open_lineage` |  `google.protobuf.struct_pb2.Struct`   
Required. OpenLineage message following OpenLineage format: <https://github.com/OpenLineage/OpenLineage/blob/main/spec/OpenLineage.json> This corresponds to the `open_lineage` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.ProcessOpenLineageRunEventResponse](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.ProcessOpenLineageRunEventResponse)` | Response message for ProcessOpenLineageRunEvent.  
  
### process_path
    
    
    process_path(project: str, location: str, process: str) -> str

Returns a fully-qualified process string.

### run_path
    
    
    run_path(project: str, location: str, process: str, run: str) -> str

Returns a fully-qualified run string.

### search_lineage_streaming
    
    
    search_lineage_streaming(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.SearchLineageStreamingRequest,
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
    ) -> typing.Iterable[
        google.cloud.datacatalog_lineage_v1.types.lineage.SearchLineageStreamingResponse
    ]

Retrieves a streaming response of lineage links connected to the requested assets by performing a breadth-first search in the given direction. Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them. This method retrieves links from all valid locations provided in the request. This method supports Column-Level Lineage (CLL) along with wildcard support to retrieve all CLL for an Entity FQN.

Following permissions are required to retrieve links:

  * `datalineage.events.get` permission for the project where the link is stored for entity-level lineage.
  * `datalineage.events.getFields` permission for the project where the link is stored for column-level lineage.



This method also returns processes that created the links if explicitly requested by setting `max_process_per_link <google.cloud.datacatalog.lineage.v1.SearchLineageStreamingRequest.limits.max_process_per_link>`**is non-zero and full process details are requested via`links.processes.process` in the `FieldMask <https://developers.google.com/workspace/docs/api/how-tos/field-masks#read_with_a_field_mask>`**.

Permission required to retrieve processes:

  * `datalineage.processes.get` permission for the project where the process is stored.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_search_lineage_streaming():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[SearchLineageStreamingRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest.html)(
            parent="parent_value",
            locations=['locations_value1', 'locations_value2'],
            direction="UPSTREAM",
        )
    
        # Make the request
        stream = client.[search_lineage_streaming](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_search_lineage_streaming)(request=request)
    
        # Handle the response
        for response in stream:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingRequest), dict]`   
The request object. Request message for SearchLineageStreaming.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`Iterable[[google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingResponse](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.SearchLineageStreamingResponse)]` | Response message for SearchLineageStreaming.  
  
### search_links
    
    
    search_links(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.SearchLinksRequest, dict
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
    ) -> google.cloud.datacatalog_lineage_v1.services.lineage.pagers.SearchLinksPager

Retrieve a list of links connected to a specific asset. Links represent the data flow between **source** (upstream) and **target** (downstream) assets in transformation pipelines. Links are stored in the same project as the Lineage Events that create them.

You can retrieve links in every project where you have the `datalineage.events.get` permission. The project provided in the URL is used for Billing and Quota.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_search_links():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        source = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[EntityReference](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.EntityReference.html)()
        source.fully_qualified_name = "fully_qualified_name_value"
    
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[SearchLinksRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.SearchLinksRequest.html)(
            source=source,
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[search_links](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_search_links)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.SearchLinksRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.SearchLinksRequest), dict]`   
The request object. Request message for SearchLinks.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.services.lineage.pagers.SearchLinksPager](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.pagers.SearchLinksPager)` | Response message for SearchLinks. Iterating over this object will yield results and resolve additional pages automatically.  
  
### update_process
    
    
    update_process(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.UpdateProcessRequest, dict
            ]
        ] = None,
        *,
        process: typing.Optional[
            google.cloud.datacatalog_lineage_v1.types.lineage.Process
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datacatalog_lineage_v1.types.lineage.Process

Updates a process.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_update_process():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[UpdateProcessRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.UpdateProcessRequest.html)(
        )
    
        # Make the request
        response = client.[update_process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_update_process)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.UpdateProcessRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.UpdateProcessRequest), dict]`   
The request object. Request message for UpdateProcess.  
`process` |  `[google.cloud.datacatalog_lineage_v1.types.Process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Process)`   
Required. The lineage process to update. The process's `name` field is used to identify the process to update. This corresponds to the `process` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. The list of fields to update. Currently not used. The whole message is updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.Process](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Process)` | A process is the definition of a data transformation operation.  
  
### update_run
    
    
    update_run(
        request: typing.Optional[
            typing.Union[
                google.cloud.datacatalog_lineage_v1.types.lineage.UpdateRunRequest, dict
            ]
        ] = None,
        *,
        run: typing.Optional[google.cloud.datacatalog_lineage_v1.types.lineage.Run] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datacatalog_lineage_v1.types.lineage.Run

Updates a run.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest)
    
    def sample_update_run():
        # Create a client
        client = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[LineageClient](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html)()
    
        # Initialize request argument(s)
        run = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[Run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Run.html)()
        run.state = "ABORTED"
    
        request = [datacatalog_lineage_v1](https://docs.cloud.google.com/python/docs/reference/lineage/latest).[UpdateRunRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.UpdateRunRequest.html)(
            run=run,
        )
    
        # Make the request
        response = client.[update_run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.services.lineage.LineageClient.html#google_cloud_datacatalog_lineage_v1_services_lineage_LineageClient_update_run)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.datacatalog_lineage_v1.types.UpdateRunRequest](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.UpdateRunRequest), dict]`   
The request object. Request message for UpdateRun.  
`run` |  `[google.cloud.datacatalog_lineage_v1.types.Run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Run)`   
Required. The lineage run to update. The run's `name` field is used to identify the run to update. Format: `projects/{project}/locations/{location}/processes/{process}/runs/{run}`. This corresponds to the `run` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. The list of fields to update. Currently not used. The whole message is updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datacatalog_lineage_v1.types.Run](https://docs.cloud.google.com/python/docs/reference/lineage/latest/google.cloud.datacatalog_lineage_v1.types.Run)` | A lineage run represents an execution of a process that creates lineage events.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
