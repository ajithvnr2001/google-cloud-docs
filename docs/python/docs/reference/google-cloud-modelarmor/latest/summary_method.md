---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/summary_method/
title: Package Methods (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:53.497183+00:00
---

# Package Methods (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 

Summary of entries of Methods for google-cloud-modelarmor.

## 

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient
    
    
    ModelArmorAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.modelarmor_v1.services.model_armor.transports.base.ModelArmorTransport,
                typing.Callable[
                    [...],
                    google.cloud.modelarmor_v1.services.model_armor.transports.base.ModelArmorTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the model armor async client.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_ModelArmorAsyncClient)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_common_billing_account_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_common_folder_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_common_location_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_common_organization_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_common_project_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.create_template
    
    
    create_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.CreateTemplateRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        template: typing.Optional[google.cloud.modelarmor_v1.types.service.Template] = None,
        template_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1.types.service.Template

Creates a new Template in a given project and location.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.create_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_create_template)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.delete_template
    
    
    delete_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.DeleteTemplateRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a single Template.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.delete_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_delete_template)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.floor_setting_path
    
    
    floor_setting_path(project: str, location: str) -> str

Returns a fully-qualified floor_setting string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.floor_setting_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_floor_setting_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_from_service_account_file)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_from_service_account_info)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_from_service_account_json)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_floor_setting
    
    
    get_floor_setting(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.GetFloorSettingRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1.types.service.FloorSetting

Gets details of a single floor setting of a project.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_floor_setting](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_get_floor_setting)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_get_location)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_template
    
    
    get_template(
        request: typing.Optional[
            typing.Union[google.cloud.modelarmor_v1.types.service.GetTemplateRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1.types.service.Template

Gets details of a single Template.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_get_template)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.modelarmor_v1.services.model_armor.transports.base.ModelArmorTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_get_transport_class)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_list_locations)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.list_templates
    
    
    list_templates(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.ListTemplatesRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesAsyncPager

Lists Templates in a given project and location.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.list_templates](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_list_templates)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_parse_common_billing_account_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_parse_common_folder_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_parse_common_location_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_parse_common_organization_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_parse_common_project_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_floor_setting_path
    
    
    parse_floor_setting_path(path: str) -> typing.Dict[str, str]

Parses a floor_setting path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_floor_setting_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_parse_floor_setting_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_template_path
    
    
    parse_template_path(path: str) -> typing.Dict[str, str]

Parses a template path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.parse_template_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_parse_template_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.sanitize_model_response
    
    
    sanitize_model_response(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.SanitizeModelResponseRequest, dict
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
    ) -> google.cloud.modelarmor_v1.types.service.SanitizeModelResponseResponse

Sanitizes Model Response.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.sanitize_model_response](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_sanitize_model_response)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.sanitize_user_prompt
    
    
    sanitize_user_prompt(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.SanitizeUserPromptRequest, dict
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
    ) -> google.cloud.modelarmor_v1.types.service.SanitizeUserPromptResponse

Sanitizes User Prompt.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.sanitize_user_prompt](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_sanitize_user_prompt)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.stream_sanitize_model_response
    
    
    stream_sanitize_model_response(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.modelarmor_v1.types.service.SanitizeModelResponseRequest
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
            google.cloud.modelarmor_v1.types.service.SanitizeModelResponseResponse
        ]
    ]

Streaming version of Sanitizes Model Response.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.stream_sanitize_model_response](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_stream_sanitize_model_response)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.stream_sanitize_user_prompt
    
    
    stream_sanitize_user_prompt(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.modelarmor_v1.types.service.SanitizeUserPromptRequest
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
            google.cloud.modelarmor_v1.types.service.SanitizeUserPromptResponse
        ]
    ]

Streaming version of Sanitize User Prompt.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.stream_sanitize_user_prompt](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_stream_sanitize_user_prompt)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.template_path
    
    
    template_path(project: str, location: str, template: str) -> str

Returns a fully-qualified template string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.template_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_template_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.update_floor_setting
    
    
    update_floor_setting(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.UpdateFloorSettingRequest, dict
            ]
        ] = None,
        *,
        floor_setting: typing.Optional[
            google.cloud.modelarmor_v1.types.service.FloorSetting
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1.types.service.FloorSetting

Updates the parameters of a single floor setting of a project.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.update_floor_setting](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_update_floor_setting)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.update_template
    
    
    update_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.UpdateTemplateRequest, dict
            ]
        ] = None,
        *,
        template: typing.Optional[google.cloud.modelarmor_v1.types.service.Template] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1.types.service.Template

Updates the parameters of a single Template.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient.update_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorAsyncClient_update_template)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient
    
    
    ModelArmorClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.modelarmor_v1.services.model_armor.transports.base.ModelArmorTransport,
                typing.Callable[
                    [...],
                    google.cloud.modelarmor_v1.services.model_armor.transports.base.ModelArmorTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the model armor client.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_ModelArmorClient)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient___exit__)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_common_billing_account_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_common_folder_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_common_location_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_common_organization_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_common_project_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.create_template
    
    
    create_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.CreateTemplateRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        template: typing.Optional[google.cloud.modelarmor_v1.types.service.Template] = None,
        template_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1.types.service.Template

Creates a new Template in a given project and location.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.create_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_create_template)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.delete_template
    
    
    delete_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.DeleteTemplateRequest, dict
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

Deletes a single Template.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.delete_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_delete_template)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.floor_setting_path
    
    
    floor_setting_path(project: str, location: str) -> str

Returns a fully-qualified floor_setting string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.floor_setting_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_floor_setting_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_from_service_account_file)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_from_service_account_info)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_from_service_account_json)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.get_floor_setting
    
    
    get_floor_setting(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.GetFloorSettingRequest, dict
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
    ) -> google.cloud.modelarmor_v1.types.service.FloorSetting

Gets details of a single floor setting of a project.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.get_floor_setting](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_floor_setting)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.get_location
    
    
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

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_location)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_mtls_endpoint_and_cert_source)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.get_template
    
    
    get_template(
        request: typing.Optional[
            typing.Union[google.cloud.modelarmor_v1.types.service.GetTemplateRequest, dict]
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
    ) -> google.cloud.modelarmor_v1.types.service.Template

Gets details of a single Template.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.get_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_template)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.list_locations
    
    
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

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_list_locations)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.list_templates
    
    
    list_templates(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.ListTemplatesRequest, dict
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
    ) -> google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesPager

Lists Templates in a given project and location.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.list_templates](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_list_templates)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_parse_common_billing_account_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_parse_common_folder_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_parse_common_location_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_parse_common_organization_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_parse_common_project_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_floor_setting_path
    
    
    parse_floor_setting_path(path: str) -> typing.Dict[str, str]

Parses a floor_setting path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_floor_setting_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_parse_floor_setting_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_template_path
    
    
    parse_template_path(path: str) -> typing.Dict[str, str]

Parses a template path into its component segments.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.parse_template_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_parse_template_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.sanitize_model_response
    
    
    sanitize_model_response(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.SanitizeModelResponseRequest, dict
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
    ) -> google.cloud.modelarmor_v1.types.service.SanitizeModelResponseResponse

Sanitizes Model Response.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.sanitize_model_response](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_sanitize_model_response)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.sanitize_user_prompt
    
    
    sanitize_user_prompt(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.SanitizeUserPromptRequest, dict
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
    ) -> google.cloud.modelarmor_v1.types.service.SanitizeUserPromptResponse

Sanitizes User Prompt.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.sanitize_user_prompt](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_sanitize_user_prompt)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.stream_sanitize_model_response
    
    
    stream_sanitize_model_response(
        requests: typing.Optional[
            typing.Iterator[
                google.cloud.modelarmor_v1.types.service.SanitizeModelResponseRequest
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
        google.cloud.modelarmor_v1.types.service.SanitizeModelResponseResponse
    ]

Streaming version of Sanitizes Model Response.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.stream_sanitize_model_response](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_stream_sanitize_model_response)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.stream_sanitize_user_prompt
    
    
    stream_sanitize_user_prompt(
        requests: typing.Optional[
            typing.Iterator[
                google.cloud.modelarmor_v1.types.service.SanitizeUserPromptRequest
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
        google.cloud.modelarmor_v1.types.service.SanitizeUserPromptResponse
    ]

Streaming version of Sanitize User Prompt.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.stream_sanitize_user_prompt](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_stream_sanitize_user_prompt)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.template_path
    
    
    template_path(project: str, location: str, template: str) -> str

Returns a fully-qualified template string.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.template_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_template_path)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.update_floor_setting
    
    
    update_floor_setting(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.UpdateFloorSettingRequest, dict
            ]
        ] = None,
        *,
        floor_setting: typing.Optional[
            google.cloud.modelarmor_v1.types.service.FloorSetting
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
    ) -> google.cloud.modelarmor_v1.types.service.FloorSetting

Updates the parameters of a single floor setting of a project.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.update_floor_setting](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_update_floor_setting)

### google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.update_template
    
    
    update_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1.types.service.UpdateTemplateRequest, dict
            ]
        ] = None,
        *,
        template: typing.Optional[google.cloud.modelarmor_v1.types.service.Template] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1.types.service.Template

Updates the parameters of a single Template.

See more: [google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.update_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_update_template)

### google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesAsyncPager
    
    
    ListTemplatesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.modelarmor_v1.types.service.ListTemplatesResponse
            ],
        ],
        request: google.cloud.modelarmor_v1.types.service.ListTemplatesRequest,
        response: google.cloud.modelarmor_v1.types.service.ListTemplatesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesAsyncPager#google_cloud_modelarmor_v1_services_model_armor_pagers_ListTemplatesAsyncPager_ListTemplatesAsyncPager)

### google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesPager
    
    
    ListTemplatesPager(
        method: typing.Callable[
            [...], google.cloud.modelarmor_v1.types.service.ListTemplatesResponse
        ],
        request: google.cloud.modelarmor_v1.types.service.ListTemplatesRequest,
        response: google.cloud.modelarmor_v1.types.service.ListTemplatesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesPager](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesPager#google_cloud_modelarmor_v1_services_model_armor_pagers_ListTemplatesPager_ListTemplatesPager)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient
    
    
    ModelArmorAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.modelarmor_v1beta.services.model_armor.transports.base.ModelArmorTransport,
                typing.Callable[
                    [...],
                    google.cloud.modelarmor_v1beta.services.model_armor.transports.base.ModelArmorTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the model armor async client.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_ModelArmorAsyncClient)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_common_billing_account_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_common_folder_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_common_location_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_common_organization_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_common_project_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.create_template
    
    
    create_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.CreateTemplateRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        template: typing.Optional[
            google.cloud.modelarmor_v1beta.types.service.Template
        ] = None,
        template_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1beta.types.service.Template

Creates a new Template in a given project and location.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.create_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_create_template)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.delete_template
    
    
    delete_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.DeleteTemplateRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a single Template.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.delete_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_delete_template)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.floor_setting_path
    
    
    floor_setting_path(project: str, location: str) -> str

Returns a fully-qualified floor_setting string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.floor_setting_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_floor_setting_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_from_service_account_file)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_from_service_account_info)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_from_service_account_json)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_floor_setting
    
    
    get_floor_setting(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.GetFloorSettingRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1beta.types.service.FloorSetting

Gets details of a single floor setting of a project.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_floor_setting](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_get_floor_setting)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_get_location)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_template
    
    
    get_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.GetTemplateRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1beta.types.service.Template

Gets details of a single Template.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_get_template)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.modelarmor_v1beta.services.model_armor.transports.base.ModelArmorTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_get_transport_class)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
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
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_list_locations)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.list_templates
    
    
    list_templates(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.ListTemplatesRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesAsyncPager

Lists Templates in a given project and location.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.list_templates](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_list_templates)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_parse_common_billing_account_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_parse_common_folder_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_parse_common_location_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_parse_common_organization_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_parse_common_project_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_floor_setting_path
    
    
    parse_floor_setting_path(path: str) -> typing.Dict[str, str]

Parses a floor_setting path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_floor_setting_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_parse_floor_setting_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_template_path
    
    
    parse_template_path(path: str) -> typing.Dict[str, str]

Parses a template path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.parse_template_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_parse_template_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.sanitize_model_response
    
    
    sanitize_model_response(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.SanitizeModelResponseRequest,
                dict,
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
    ) -> google.cloud.modelarmor_v1beta.types.service.SanitizeModelResponseResponse

Sanitizes Model Response.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.sanitize_model_response](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_sanitize_model_response)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.sanitize_user_prompt
    
    
    sanitize_user_prompt(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.SanitizeUserPromptRequest, dict
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
    ) -> google.cloud.modelarmor_v1beta.types.service.SanitizeUserPromptResponse

Sanitizes User Prompt.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.sanitize_user_prompt](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_sanitize_user_prompt)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.stream_sanitize_model_response
    
    
    stream_sanitize_model_response(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.modelarmor_v1beta.types.service.SanitizeModelResponseRequest
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
            google.cloud.modelarmor_v1beta.types.service.SanitizeModelResponseResponse
        ]
    ]

Streaming version of Sanitizes Model Response.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.stream_sanitize_model_response](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_stream_sanitize_model_response)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.stream_sanitize_user_prompt
    
    
    stream_sanitize_user_prompt(
        requests: typing.Optional[
            typing.AsyncIterator[
                google.cloud.modelarmor_v1beta.types.service.SanitizeUserPromptRequest
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
            google.cloud.modelarmor_v1beta.types.service.SanitizeUserPromptResponse
        ]
    ]

Streaming version of Sanitize User Prompt.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.stream_sanitize_user_prompt](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_stream_sanitize_user_prompt)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.template_path
    
    
    template_path(project: str, location: str, template: str) -> str

Returns a fully-qualified template string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.template_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_template_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.update_floor_setting
    
    
    update_floor_setting(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.UpdateFloorSettingRequest, dict
            ]
        ] = None,
        *,
        floor_setting: typing.Optional[
            google.cloud.modelarmor_v1beta.types.service.FloorSetting
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1beta.types.service.FloorSetting

Updates the parameters of a single floor setting of a project.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.update_floor_setting](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_update_floor_setting)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.update_template
    
    
    update_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.UpdateTemplateRequest, dict
            ]
        ] = None,
        *,
        template: typing.Optional[
            google.cloud.modelarmor_v1beta.types.service.Template
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1beta.types.service.Template

Updates the parameters of a single Template.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient.update_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorAsyncClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorAsyncClient_update_template)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient
    
    
    ModelArmorClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.modelarmor_v1beta.services.model_armor.transports.base.ModelArmorTransport,
                typing.Callable[
                    [...],
                    google.cloud.modelarmor_v1beta.services.model_armor.transports.base.ModelArmorTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the model armor client.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_ModelArmorClient)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient___exit__)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_common_billing_account_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_common_folder_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_common_location_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_common_organization_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_common_project_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.create_template
    
    
    create_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.CreateTemplateRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        template: typing.Optional[
            google.cloud.modelarmor_v1beta.types.service.Template
        ] = None,
        template_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.modelarmor_v1beta.types.service.Template

Creates a new Template in a given project and location.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.create_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_create_template)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.delete_template
    
    
    delete_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.DeleteTemplateRequest, dict
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

Deletes a single Template.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.delete_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_delete_template)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.floor_setting_path
    
    
    floor_setting_path(project: str, location: str) -> str

Returns a fully-qualified floor_setting string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.floor_setting_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_floor_setting_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_from_service_account_file)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_from_service_account_info)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_from_service_account_json)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.get_floor_setting
    
    
    get_floor_setting(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.GetFloorSettingRequest, dict
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
    ) -> google.cloud.modelarmor_v1beta.types.service.FloorSetting

Gets details of a single floor setting of a project.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.get_floor_setting](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_get_floor_setting)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.get_location
    
    
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

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_get_location)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_get_mtls_endpoint_and_cert_source)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.get_template
    
    
    get_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.GetTemplateRequest, dict
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
    ) -> google.cloud.modelarmor_v1beta.types.service.Template

Gets details of a single Template.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.get_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_get_template)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.list_locations
    
    
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

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_list_locations)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.list_templates
    
    
    list_templates(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.ListTemplatesRequest, dict
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
    ) -> google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesPager

Lists Templates in a given project and location.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.list_templates](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_list_templates)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_parse_common_billing_account_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_parse_common_folder_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_parse_common_location_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_parse_common_organization_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_parse_common_project_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_floor_setting_path
    
    
    parse_floor_setting_path(path: str) -> typing.Dict[str, str]

Parses a floor_setting path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_floor_setting_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_parse_floor_setting_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_template_path
    
    
    parse_template_path(path: str) -> typing.Dict[str, str]

Parses a template path into its component segments.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.parse_template_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_parse_template_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.sanitize_model_response
    
    
    sanitize_model_response(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.SanitizeModelResponseRequest,
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
    ) -> google.cloud.modelarmor_v1beta.types.service.SanitizeModelResponseResponse

Sanitizes Model Response.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.sanitize_model_response](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_sanitize_model_response)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.sanitize_user_prompt
    
    
    sanitize_user_prompt(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.SanitizeUserPromptRequest, dict
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
    ) -> google.cloud.modelarmor_v1beta.types.service.SanitizeUserPromptResponse

Sanitizes User Prompt.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.sanitize_user_prompt](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_sanitize_user_prompt)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.stream_sanitize_model_response
    
    
    stream_sanitize_model_response(
        requests: typing.Optional[
            typing.Iterator[
                google.cloud.modelarmor_v1beta.types.service.SanitizeModelResponseRequest
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
        google.cloud.modelarmor_v1beta.types.service.SanitizeModelResponseResponse
    ]

Streaming version of Sanitizes Model Response.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.stream_sanitize_model_response](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_stream_sanitize_model_response)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.stream_sanitize_user_prompt
    
    
    stream_sanitize_user_prompt(
        requests: typing.Optional[
            typing.Iterator[
                google.cloud.modelarmor_v1beta.types.service.SanitizeUserPromptRequest
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
        google.cloud.modelarmor_v1beta.types.service.SanitizeUserPromptResponse
    ]

Streaming version of Sanitize User Prompt.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.stream_sanitize_user_prompt](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_stream_sanitize_user_prompt)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.template_path
    
    
    template_path(project: str, location: str, template: str) -> str

Returns a fully-qualified template string.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.template_path](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_template_path)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.update_floor_setting
    
    
    update_floor_setting(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.UpdateFloorSettingRequest, dict
            ]
        ] = None,
        *,
        floor_setting: typing.Optional[
            google.cloud.modelarmor_v1beta.types.service.FloorSetting
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
    ) -> google.cloud.modelarmor_v1beta.types.service.FloorSetting

Updates the parameters of a single floor setting of a project.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.update_floor_setting](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_update_floor_setting)

### google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.update_template
    
    
    update_template(
        request: typing.Optional[
            typing.Union[
                google.cloud.modelarmor_v1beta.types.service.UpdateTemplateRequest, dict
            ]
        ] = None,
        *,
        template: typing.Optional[
            google.cloud.modelarmor_v1beta.types.service.Template
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
    ) -> google.cloud.modelarmor_v1beta.types.service.Template

Updates the parameters of a single Template.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient.update_template](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.ModelArmorClient#google_cloud_modelarmor_v1beta_services_model_armor_ModelArmorClient_update_template)

### google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesAsyncPager
    
    
    ListTemplatesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.modelarmor_v1beta.types.service.ListTemplatesResponse
            ],
        ],
        request: google.cloud.modelarmor_v1beta.types.service.ListTemplatesRequest,
        response: google.cloud.modelarmor_v1beta.types.service.ListTemplatesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesAsyncPager#google_cloud_modelarmor_v1beta_services_model_armor_pagers_ListTemplatesAsyncPager_ListTemplatesAsyncPager)

### google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesPager
    
    
    ListTemplatesPager(
        method: typing.Callable[
            [...], google.cloud.modelarmor_v1beta.types.service.ListTemplatesResponse
        ],
        request: google.cloud.modelarmor_v1beta.types.service.ListTemplatesRequest,
        response: google.cloud.modelarmor_v1beta.types.service.ListTemplatesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesPager](https://cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesPager#google_cloud_modelarmor_v1beta_services_model_armor_pagers_ListTemplatesPager_ListTemplatesPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
