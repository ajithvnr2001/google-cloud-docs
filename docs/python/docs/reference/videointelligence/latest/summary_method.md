---
url: https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/summary_method/
title: Package Methods (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:55.180981+00:00
---

# Package Methods (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.2  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.1  2.6.1  2.5.1  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.16.3  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0 

Summary of entries of Methods for videointelligence.

## 

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient
    
    
    VideoIntelligenceServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service async client.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_VideoIntelligenceServiceAsyncClient)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1.types.video_intelligence.Feature
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_annotate_video)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_billing_account_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_folder_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_location_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_organization_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_project_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_file)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_info)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_json)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.videointelligence_v1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_transport_class)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_folder_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_location_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_organization_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_project_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient
    
    
    VideoIntelligenceServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service client.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_VideoIntelligenceServiceClient)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.**exit**](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient___exit__)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1.types.video_intelligence.Feature
            ]
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

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_billing_account_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_folder_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_location_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_organization_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_project_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_file)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_info)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_json)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_folder_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_location_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_organization_path)

### google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_project_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient
    
    
    VideoIntelligenceServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1beta2.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1beta2.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service async client.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_VideoIntelligenceServiceAsyncClient)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1beta2.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1beta2.types.video_intelligence.Feature
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_annotate_video)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_billing_account_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_folder_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_location_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_organization_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_project_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_file)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_info)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_json)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.videointelligence_v1beta2.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_transport_class)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_folder_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_location_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_organization_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_project_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient
    
    
    VideoIntelligenceServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1beta2.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1beta2.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service client.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_VideoIntelligenceServiceClient)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.**exit**](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient___exit__)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1beta2.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1beta2.types.video_intelligence.Feature
            ]
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

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_common_billing_account_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_common_folder_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_common_location_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_common_organization_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_common_project_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_file)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_info)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_json)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_folder_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_location_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_organization_path)

### google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1beta2.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1beta2_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_project_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient
    
    
    VideoIntelligenceServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service async client.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_VideoIntelligenceServiceAsyncClient)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1p1beta1.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1p1beta1.types.video_intelligence.Feature
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_annotate_video)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_billing_account_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_folder_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_location_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_organization_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_project_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_file)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_info)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_json)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_transport_class)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_folder_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_location_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_organization_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_project_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient
    
    
    VideoIntelligenceServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service client.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_VideoIntelligenceServiceClient)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.**exit**](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient___exit__)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1p1beta1.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1p1beta1.types.video_intelligence.Feature
            ]
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

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_billing_account_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_folder_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_location_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_organization_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_project_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_file)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_info)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_json)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_folder_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_location_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_organization_path)

### google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p1beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_project_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient
    
    
    VideoIntelligenceServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service async client.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_VideoIntelligenceServiceAsyncClient)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1p2beta1.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1p2beta1.types.video_intelligence.Feature
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_annotate_video)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_billing_account_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_folder_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_location_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_organization_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_project_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_file)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_info)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_json)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_transport_class)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_folder_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_location_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_organization_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_project_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient
    
    
    VideoIntelligenceServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service client.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_VideoIntelligenceServiceClient)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.**exit**](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient___exit__)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1p2beta1.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1p2beta1.types.video_intelligence.Feature
            ]
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

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_billing_account_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_folder_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_location_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_organization_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_project_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_file)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_info)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_json)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_folder_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_location_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_organization_path)

### google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p2beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p2beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_project_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient
    
    
    StreamingVideoIntelligenceServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.transports.base.StreamingVideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.transports.base.StreamingVideoIntelligenceServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the streaming video intelligence service async client.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_StreamingVideoIntelligenceServiceAsyncClient)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_common_billing_account_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_common_folder_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_common_location_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_common_organization_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_common_project_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_from_service_account_file)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_from_service_account_info)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_from_service_account_json)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.transports.base.StreamingVideoIntelligenceServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_get_transport_class)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_parse_common_folder_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_parse_common_location_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_parse_common_organization_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_parse_common_project_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.streaming_annotate_video
    
    
    streaming_annotate_video(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.videointelligence_v1p3beta1.types.video_intelligence.StreamingAnnotateVideoRequest
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> typing.Awaitable[
        typing.AsyncIterable[
            google.cloud.videointelligence_v1p3beta1.types.video_intelligence.StreamingAnnotateVideoResponse
        ]
    ]

Performs video annotation with bidirectional streaming: emitting results while sending video/audio bytes.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient.streaming_annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceAsyncClient_streaming_annotate_video)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient
    
    
    StreamingVideoIntelligenceServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.transports.base.StreamingVideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.transports.base.StreamingVideoIntelligenceServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the streaming video intelligence service client.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_StreamingVideoIntelligenceServiceClient)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.**exit**](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient___exit__)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_common_billing_account_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_common_folder_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_common_location_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_common_organization_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_common_project_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_from_service_account_file)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_from_service_account_info)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_from_service_account_json)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_parse_common_folder_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_parse_common_location_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_parse_common_organization_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_parse_common_project_path)

### google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.streaming_annotate_video
    
    
    streaming_annotate_video(
        requests: typing.Optional[
            typing.Iterator[
                google.cloud.videointelligence_v1p3beta1.types.video_intelligence.StreamingAnnotateVideoRequest
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
        google.cloud.videointelligence_v1p3beta1.types.video_intelligence.StreamingAnnotateVideoResponse
    ]

Performs video annotation with bidirectional streaming: emitting results while sending video/audio bytes.

See more: [google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient.streaming_annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.streaming_video_intelligence_service.StreamingVideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_streaming_video_intelligence_service_StreamingVideoIntelligenceServiceClient_streaming_annotate_video)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient
    
    
    VideoIntelligenceServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service async client.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_VideoIntelligenceServiceAsyncClient)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1p3beta1.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1p3beta1.types.video_intelligence.Feature
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_annotate_video)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_billing_account_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_folder_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_location_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_organization_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_common_project_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_file)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_info)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_from_service_account_json)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_get_transport_class)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_folder_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_location_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_organization_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceAsyncClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceAsyncClient_parse_common_project_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient
    
    
    VideoIntelligenceServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.transports.base.VideoIntelligenceServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the video intelligence service client.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_VideoIntelligenceServiceClient)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.**exit**](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient___exit__)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video
    
    
    annotate_video(
        request: typing.Optional[
            typing.Union[
                google.cloud.videointelligence_v1p3beta1.types.video_intelligence.AnnotateVideoRequest,
                dict,
            ]
        ] = None,
        *,
        input_uri: typing.Optional[str] = None,
        features: typing.Optional[
            typing.MutableSequence[
                google.cloud.videointelligence_v1p3beta1.types.video_intelligence.Feature
            ]
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

Performs asynchronous video annotation.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.annotate_video](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_billing_account_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_folder_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_location_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_organization_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_common_project_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_file)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_info)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_from_service_account_json)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_billing_account_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_folder_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_location_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_organization_path)

### google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p3beta1.services.video_intelligence_service.VideoIntelligenceServiceClient#google_cloud_videointelligence_v1p3beta1_services_video_intelligence_service_VideoIntelligenceServiceClient_parse_common_project_path)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
