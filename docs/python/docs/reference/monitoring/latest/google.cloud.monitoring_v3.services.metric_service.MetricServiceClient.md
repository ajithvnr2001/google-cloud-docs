---
url: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient
title: Class MetricServiceClient (2.32.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:27.870656+00:00
---

# Class MetricServiceClient (2.32.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MetricServiceClient (2.32.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.32.0 (latest)  2.31.0  2.30.0  2.29.1  2.28.0  2.27.2  2.26.0  2.25.0  2.24.0  2.23.1  2.22.2  2.21.0  2.20.0  2.19.4  2.18.0  2.17.0  2.16.0  2.15.1  2.14.2  2.13.0  2.12.0  2.11.3  2.10.1  2.9.2  2.8.0  2.7.0  2.6.0  2.5.2  2.4.2  2.3.0  2.2.1  2.1.0  2.0.1  1.1.2  1.0.0  0.36.2  0.35.0  0.34.0  0.33.0  0.32.0 
    
    
    MetricServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.monitoring_v3.services.metric_service.transports.base.MetricServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.monitoring_v3.services.metric_service.transports.base.MetricServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Manages metric descriptors, monitored resource descriptors, and time series data.

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
`MetricServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### MetricServiceClient
    
    
    MetricServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.monitoring_v3.services.metric_service.transports.base.MetricServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.monitoring_v3.services.metric_service.transports.base.MetricServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the metric service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,MetricServiceTransport,Callable[..., MetricServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the MetricServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_metric_descriptor
    
    
    create_metric_descriptor(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.CreateMetricDescriptorRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        metric_descriptor: typing.Optional[google.api.metric_pb2.MetricDescriptor] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api.metric_pb2.MetricDescriptor

Creates a new metric descriptor. The creation is executed asynchronously. User-created metric descriptors define `custom metrics <https://cloud.google.com/monitoring/custom-metrics>`__. The metric descriptor is updated if it already exists, except that metric labels are never removed.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_create_metric_descriptor():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[CreateMetricDescriptorRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.CreateMetricDescriptorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[create_metric_descriptor](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_metric_descriptor)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.CreateMetricDescriptorRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.CreateMetricDescriptorRequest), dict]`   
The request object. The `CreateMetricDescriptor` request.  
`name` |  `str`   
Required. The `project <https://cloud.google.com/monitoring/api/v3#project_name>`__ on which to execute the request. The format is: 4 projects/[PROJECT_ID_OR_NUMBER] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`metric_descriptor` |  `google.api.metric_pb2.MetricDescriptor`   
Required. The new `custom metric <https://cloud.google.com/monitoring/custom-metrics>`__ descriptor. This corresponds to the `metric_descriptor` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api.metric_pb2.MetricDescriptor` | Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.  
  
### create_service_time_series
    
    
    create_service_time_series(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.CreateTimeSeriesRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        time_series: typing.Optional[
            typing.MutableSequence[google.cloud.monitoring_v3.types.metric.TimeSeries]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Creates or adds data to one or more service time series. A service time series is a time series for a metric from a Google Cloud service. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. This endpoint rejects writes to user-defined metrics. This method is only for use by Google Cloud services. Use `projects.timeSeries.create][google.monitoring.v3.MetricService.CreateTimeSeries]` instead.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_create_service_time_series():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[CreateTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.CreateTimeSeriesRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[create_service_time_series](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_service_time_series)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.CreateTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.CreateTimeSeriesRequest), dict]`   
The request object. The `CreateTimeSeries` request.  
`name` |  `str`   
Required. The `project <https://cloud.google.com/monitoring/api/v3#project_name>`__ on which to execute the request. The format is: :: projects/[PROJECT_ID_OR_NUMBER] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`time_series` |  `MutableSequence[[google.cloud.monitoring_v3.types.TimeSeries](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeSeries)]`   
Required. The new data to be added to a list of time series. Adds at most one data point to each of several time series. The new data point must be more recent than any other point in its time series. Each `TimeSeries` value must fully specify a unique time series by supplying all label values for the metric and the monitored resource. The maximum number of `TimeSeries` objects per `Create` request is 200. This corresponds to the `time_series` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### create_time_series
    
    
    create_time_series(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.CreateTimeSeriesRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        time_series: typing.Optional[
            typing.MutableSequence[google.cloud.monitoring_v3.types.metric.TimeSeries]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Creates or adds data to one or more time series. The response is empty if all time series in the request were written. If any time series could not be written, a corresponding failure message is included in the error response. This method does not support `resource locations constraint of an organization policy <https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations#setting_the_organization_policy>`__.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_create_time_series():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[CreateTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.CreateTimeSeriesRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[create_time_series](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_create_time_series)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.CreateTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.CreateTimeSeriesRequest), dict]`   
The request object. The `CreateTimeSeries` request.  
`name` |  `str`   
Required. The `project <https://cloud.google.com/monitoring/api/v3#project_name>`__ on which to execute the request. The format is: :: projects/[PROJECT_ID_OR_NUMBER] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`time_series` |  `MutableSequence[[google.cloud.monitoring_v3.types.TimeSeries](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeSeries)]`   
Required. The new data to be added to a list of time series. Adds at most one data point to each of several time series. The new data point must be more recent than any other point in its time series. Each `TimeSeries` value must fully specify a unique time series by supplying all label values for the metric and the monitored resource. The maximum number of `TimeSeries` objects per `Create` request is 200. This corresponds to the `time_series` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_metric_descriptor
    
    
    delete_metric_descriptor(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.DeleteMetricDescriptorRequest,
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

Deletes a metric descriptor. Only user-created `custom metrics <https://cloud.google.com/monitoring/custom-metrics>`__ can be deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_delete_metric_descriptor():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[DeleteMetricDescriptorRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.DeleteMetricDescriptorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_metric_descriptor](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_delete_metric_descriptor)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.DeleteMetricDescriptorRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.DeleteMetricDescriptorRequest), dict]`   
The request object. The `DeleteMetricDescriptor` request.  
`name` |  `str`   
Required. The metric descriptor on which to execute the request. The format is: :: projects/[PROJECT_ID_OR_NUMBER]/metricDescriptors/[METRIC_ID] An example of `[METRIC_ID]` is: `"custom.googleapis.com/my_test_metric"`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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
`MetricServiceClient` | The constructed client.  
  
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
`MetricServiceClient` | The constructed client.  
  
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
`MetricServiceClient` | The constructed client.  
  
### get_metric_descriptor
    
    
    get_metric_descriptor(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.GetMetricDescriptorRequest,
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
    ) -> google.api.metric_pb2.MetricDescriptor

Gets a single metric descriptor.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_get_metric_descriptor():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GetMetricDescriptorRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.GetMetricDescriptorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_metric_descriptor](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_get_metric_descriptor)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.GetMetricDescriptorRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.GetMetricDescriptorRequest), dict]`   
The request object. The `GetMetricDescriptor` request.  
`name` |  `str`   
Required. The metric descriptor on which to execute the request. The format is: :: projects/[PROJECT_ID_OR_NUMBER]/metricDescriptors/[METRIC_ID] An example value of `[METRIC_ID]` is `"compute.googleapis.com/instance/disk/read_bytes_count"`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api.metric_pb2.MetricDescriptor` | Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.  
  
### get_monitored_resource_descriptor
    
    
    get_monitored_resource_descriptor(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.GetMonitoredResourceDescriptorRequest,
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
    ) -> google.api.monitored_resource_pb2.MonitoredResourceDescriptor

Gets a single monitored resource descriptor.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_get_monitored_resource_descriptor():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[GetMonitoredResourceDescriptorRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.GetMonitoredResourceDescriptorRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_monitored_resource_descriptor](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_get_monitored_resource_descriptor)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.GetMonitoredResourceDescriptorRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.GetMonitoredResourceDescriptorRequest), dict]`   
The request object. The `GetMonitoredResourceDescriptor` request.  
`name` |  `str`   
Required. The monitored resource descriptor to get. The format is: :: projects/[PROJECT_ID_OR_NUMBER]/monitoredResourceDescriptors/[RESOURCE_TYPE] The `[RESOURCE_TYPE]` is a predefined type, such as `cloudsql_database`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api.monitored_resource_pb2.MonitoredResourceDescriptor` | An object that describes the schema of a `MonitoredResource][google.api.MonitoredResource]` object using a type name and a set of labels. For example, the monitored resource descriptor for Google Compute Engine VM instances has a type of "gce_instance" and specifies the use of the labels "instance_id" and "zone" to identify particular VM instances. Different APIs can support different monitored resource types. APIs generally provide a list method that returns the monitored resource descriptors used by the API.  
  
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
  
### list_metric_descriptors
    
    
    list_metric_descriptors(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.ListMetricDescriptorsRequest,
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
    ) -> (
        google.cloud.monitoring_v3.services.metric_service.pagers.ListMetricDescriptorsPager
    )

Lists metric descriptors that match a filter.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_list_metric_descriptors():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ListMetricDescriptorsRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListMetricDescriptorsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_metric_descriptors](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_list_metric_descriptors)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.ListMetricDescriptorsRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListMetricDescriptorsRequest), dict]`   
The request object. The `ListMetricDescriptors` request.  
`name` |  `str`   
Required. The `project <https://cloud.google.com/monitoring/api/v3#project_name>`__ on which to execute the request. The format is: :: projects/[PROJECT_ID_OR_NUMBER] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.monitoring_v3.services.metric_service.pagers.ListMetricDescriptorsPager](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.pagers.ListMetricDescriptorsPager)` | The ListMetricDescriptors response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_monitored_resource_descriptors
    
    
    list_monitored_resource_descriptors(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.ListMonitoredResourceDescriptorsRequest,
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
    ) -> (
        google.cloud.monitoring_v3.services.metric_service.pagers.ListMonitoredResourceDescriptorsPager
    )

Lists monitored resource descriptors that match a filter.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_list_monitored_resource_descriptors():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListMonitoredResourceDescriptorsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[list_monitored_resource_descriptors](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_list_monitored_resource_descriptors)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.ListMonitoredResourceDescriptorsRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListMonitoredResourceDescriptorsRequest), dict]`   
The request object. The `ListMonitoredResourceDescriptors` request.  
`name` |  `str`   
Required. The `project <https://cloud.google.com/monitoring/api/v3#project_name>`__ on which to execute the request. The format is: :: projects/[PROJECT_ID_OR_NUMBER] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.monitoring_v3.services.metric_service.pagers.ListMonitoredResourceDescriptorsPager](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.pagers.ListMonitoredResourceDescriptorsPager)` | The ListMonitoredResourceDescriptors response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_time_series
    
    
    list_time_series(
        request: typing.Optional[
            typing.Union[
                google.cloud.monitoring_v3.types.metric_service.ListTimeSeriesRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        interval: typing.Optional[
            google.cloud.monitoring_v3.types.common.TimeInterval
        ] = None,
        view: typing.Optional[
            google.cloud.monitoring_v3.types.metric_service.ListTimeSeriesRequest.TimeSeriesView
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.monitoring_v3.services.metric_service.pagers.ListTimeSeriesPager

Lists time series that match a filter.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest)
    
    def sample_list_time_series():
        # Create a client
        client = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[MetricServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html)()
    
        # Initialize request argument(s)
        request = [monitoring_v3](https://docs.cloud.google.com/python/docs/reference/monitoring/latest).[ListTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest.html)(
            name="name_value",
            filter="filter_value",
            view="HEADERS",
        )
    
        # Make the request
        page_result = client.[list_time_series](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.MetricServiceClient.html#google_cloud_monitoring_v3_services_metric_service_MetricServiceClient_list_time_series)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.monitoring_v3.types.ListTimeSeriesRequest](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest), dict]`   
The request object. The `ListTimeSeries` request.  
`name` |  `str`   
Required. The `project <https://cloud.google.com/monitoring/api/v3#project_name>`__, organization or folder on which to execute the request. The format is: :: projects/[PROJECT_ID_OR_NUMBER] organizations/[ORGANIZATION_ID] folders/[FOLDER_ID] This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`filter` |  `str`   
Required. A `monitoring filter <https://cloud.google.com/monitoring/api/v3/filters>`__ that specifies which time series should be returned. The filter must specify a single metric type, and can additionally specify metric labels and other information. For example: :: metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND metric.labels.instance_name = "my-instance-name" This corresponds to the `filter` field on the `request` instance; if `request` is provided, this should not be set.  
`interval` |  `[google.cloud.monitoring_v3.types.TimeInterval](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.TimeInterval)`   
Required. The time interval for which results should be returned. Only time series that contain data points in the specified interval are included in the response. This corresponds to the `interval` field on the `request` instance; if `request` is provided, this should not be set.  
`view` |  `[google.cloud.monitoring_v3.types.ListTimeSeriesRequest.TimeSeriesView](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.types.ListTimeSeriesRequest.TimeSeriesView)`   
Required. Specifies which information is returned about the time series. This corresponds to the `view` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.monitoring_v3.services.metric_service.pagers.ListTimeSeriesPager](https://docs.cloud.google.com/python/docs/reference/monitoring/latest/google.cloud.monitoring_v3.services.metric_service.pagers.ListTimeSeriesPager)` | The ListTimeSeries response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### metric_descriptor_path
    
    
    metric_descriptor_path(project: str, metric_descriptor: str) -> str

Returns a fully-qualified metric_descriptor string.

### monitored_resource_descriptor_path
    
    
    monitored_resource_descriptor_path(
        project: str, monitored_resource_descriptor: str
    ) -> str

Returns a fully-qualified monitored_resource_descriptor string.

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

### parse_metric_descriptor_path
    
    
    parse_metric_descriptor_path(path: str) -> typing.Dict[str, str]

Parses a metric_descriptor path into its component segments.

### parse_monitored_resource_descriptor_path
    
    
    parse_monitored_resource_descriptor_path(path: str) -> typing.Dict[str, str]

Parses a monitored_resource_descriptor path into its component segments.

### parse_time_series_path
    
    
    parse_time_series_path(path: str) -> typing.Dict[str, str]

Parses a time_series path into its component segments.

### time_series_path
    
    
    time_series_path(project: str, time_series: str) -> str

Returns a fully-qualified time_series string.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
