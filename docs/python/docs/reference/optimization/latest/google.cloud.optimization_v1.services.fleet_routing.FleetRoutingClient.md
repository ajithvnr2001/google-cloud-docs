---
url: https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.services.fleet_routing.FleetRoutingClient
title: Class FleetRoutingClient (1.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:27.764928+00:00
---

# Class FleetRoutingClient (1.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.services.fleet_routing.FleetRoutingClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FleetRoutingClient (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.2  1.10.0  1.9.1  1.8.5  1.7.0  1.6.0  1.5.0  1.4.3  1.3.2  1.2.0  1.1.3  1.0.1  0.1.1 
    
    
    FleetRoutingClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.optimization_v1.services.fleet_routing.transports.base.FleetRoutingTransport,
                typing.Callable[
                    [...],
                    google.cloud.optimization_v1.services.fleet_routing.transports.base.FleetRoutingTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

A service for optimizing vehicle tours.

Validity of certain types of fields:

  * `google.protobuf.Timestamp`

    * Times are in Unix time: seconds since 1970-01-01T00:00:00+00:00.
    * seconds must be in [0, 253402300799], i.e. in [1970-01-01T00:00:00+00:00, 9999-12-31T23:59:59+00:00].
    * nanos must be unset or set to 0.
  * `google.protobuf.Duration`

    * seconds must be in [0, 253402300799], i.e. in [1970-01-01T00:00:00+00:00, 9999-12-31T23:59:59+00:00].
    * nanos must be unset or set to 0.
  * `google.type.LatLng`

    * latitude must be in [-90.0, 90.0].
    * longitude must be in [-180.0, 180.0].
    * at least one of latitude and longitude must be non-zero.



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
`FleetRoutingTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### FleetRoutingClient
    
    
    FleetRoutingClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.optimization_v1.services.fleet_routing.transports.base.FleetRoutingTransport,
                typing.Callable[
                    [...],
                    google.cloud.optimization_v1.services.fleet_routing.transports.base.FleetRoutingTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the fleet routing client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,FleetRoutingTransport,Callable[..., FleetRoutingTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the FleetRoutingTransport constructor. If set to None, a transport is chosen automatically.  
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

### batch_optimize_tours
    
    
    batch_optimize_tours(
        request: typing.Optional[
            typing.Union[
                google.cloud.optimization_v1.types.fleet_routing.BatchOptimizeToursRequest,
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

Optimizes vehicle tours for one or more `OptimizeToursRequest` messages as a batch.

This method is a Long Running Operation (LRO). The inputs for optimization (`OptimizeToursRequest` messages) and outputs (`OptimizeToursResponse` messages) are read/written from/to Cloud Storage in user-specified format. Like the `OptimizeTours` method, each `OptimizeToursRequest` contains a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`\ s, which are a set of routes to be performed by vehicles minimizing the overall cost.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [optimization_v1](https://docs.cloud.google.com/python/docs/reference/optimization/latest)
    
    def sample_batch_optimize_tours():
        # Create a client
        client = [optimization_v1](https://docs.cloud.google.com/python/docs/reference/optimization/latest).[FleetRoutingClient](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.services.fleet_routing.FleetRoutingClient.html)()
    
        # Initialize request argument(s)
        model_configs = [optimization_v1](https://docs.cloud.google.com/python/docs/reference/optimization/latest).[AsyncModelConfig](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.BatchOptimizeToursRequest.AsyncModelConfig.html)()
        model_configs.input_config.gcs_source.uri = "uri_value"
        model_configs.output_config.gcs_destination.uri = "uri_value"
    
        request = [optimization_v1](https://docs.cloud.google.com/python/docs/reference/optimization/latest).[BatchOptimizeToursRequest](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.BatchOptimizeToursRequest.html)(
            parent="parent_value",
            model_configs=model_configs,
        )
    
        # Make the request
        operation = client.[batch_optimize_tours](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.services.fleet_routing.FleetRoutingClient.html#google_cloud_optimization_v1_services_fleet_routing_FleetRoutingClient_batch_optimize_tours)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.optimization_v1.types.BatchOptimizeToursRequest](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.BatchOptimizeToursRequest), dict]`   
The request object. Request to batch optimize tours as an asynchronous operation. Each input file should contain one `OptimizeToursRequest`, and each output file will contain one `OptimizeToursResponse`. The request contains information to read/write and parse the files. All the input and output files should be under the same project.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [BatchOptimizeToursResponse](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.BatchOptimizeToursResponse) Response to a BatchOptimizeToursRequest. This is returned in the LRO Operation after the operation is complete.  
  
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
`FleetRoutingClient` | The constructed client.  
  
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
`FleetRoutingClient` | The constructed client.  
  
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
`FleetRoutingClient` | The constructed client.  
  
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
  
### optimize_tours
    
    
    optimize_tours(
        request: typing.Optional[
            typing.Union[
                google.cloud.optimization_v1.types.fleet_routing.OptimizeToursRequest, dict
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
    ) -> google.cloud.optimization_v1.types.fleet_routing.OptimizeToursResponse

Sends an `OptimizeToursRequest` containing a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`\ s, which are a set of routes to be performed by vehicles minimizing the overall cost.

A `ShipmentModel` model consists mainly of `Shipment`\ s that need to be carried out and `Vehicle`\ s that can be used to transport the `Shipment`\ s. The `ShipmentRoute`\ s assign `Shipment`\ s to `Vehicle`\ s. More specifically, they assign a series of `Visit`\ s to each vehicle, where a `Visit` corresponds to a `VisitRequest`, which is a pickup or delivery for a `Shipment`.

The goal is to provide an assignment of `ShipmentRoute`\ s to `Vehicle`\ s that minimizes the total cost where cost has many components defined in the `ShipmentModel`.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [optimization_v1](https://docs.cloud.google.com/python/docs/reference/optimization/latest)
    
    def sample_optimize_tours():
        # Create a client
        client = [optimization_v1](https://docs.cloud.google.com/python/docs/reference/optimization/latest).[FleetRoutingClient](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.services.fleet_routing.FleetRoutingClient.html)()
    
        # Initialize request argument(s)
        request = [optimization_v1](https://docs.cloud.google.com/python/docs/reference/optimization/latest).[OptimizeToursRequest](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.OptimizeToursRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[optimize_tours](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.services.fleet_routing.FleetRoutingClient.html#google_cloud_optimization_v1_services_fleet_routing_FleetRoutingClient_optimize_tours)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.optimization_v1.types.OptimizeToursRequest](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.OptimizeToursRequest), dict]`   
The request object. Request to be given to a tour optimization solver which defines the shipment model to solve as well as optimization parameters.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.optimization_v1.types.OptimizeToursResponse](https://docs.cloud.google.com/python/docs/reference/optimization/latest/google.cloud.optimization_v1.types.OptimizeToursResponse)` | Response after solving a tour optimization problem containing the routes followed by each vehicle, the shipments which have been skipped and the overall cost of the solution.  
  
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
