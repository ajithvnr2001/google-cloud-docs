---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient
title: Class ModelArmorClient (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:54.296633+00:00
---

# Class ModelArmorClient (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModelArmorClient (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 
    
    
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

Service describing handlers for resources

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
`ModelArmorTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ModelArmorClient
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ModelArmorTransport,Callable[..., ModelArmorTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the ModelArmorTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_template
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_create_template():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[CreateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.CreateTemplateRequest.html)(
            parent="parent_value",
            template_id="template_id_value",
        )
    
        # Make the request
        response = client.[create_template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_create_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.CreateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.CreateTemplateRequest), dict]`   
The request object. Message for creating a Template  
`parent` |  `str`   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`template` |  `[google.cloud.modelarmor_v1.types.Template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template)`   
Required. The resource being created This corresponds to the `template` field on the `request` instance; if `request` is provided, this should not be set.  
`template_id` |  `str`   
Required. Id of the requesting object If auto-generating Id server-side, remove this field and template_id from the method_signature of Create RPC This corresponds to the `template_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.modelarmor_v1.types.Template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template)` | Message describing Template resource  
  
### delete_template
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_delete_template():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[DeleteTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DeleteTemplateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_delete_template)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.DeleteTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DeleteTemplateRequest), dict]`   
The request object. Message for deleting a Template  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### floor_setting_path
    
    
    floor_setting_path(project: str, location: str) -> str

Returns a fully-qualified floor_setting string.

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
`ModelArmorClient` | The constructed client.  
  
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
`ModelArmorClient` | The constructed client.  
  
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
`ModelArmorClient` | The constructed client.  
  
### get_floor_setting
    
    
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

Gets details of a single floor setting of a project
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_get_floor_setting():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[GetFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetFloorSettingRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_floor_setting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_floor_setting)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.GetFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetFloorSettingRequest), dict]`   
The request object. Message for getting a Floor Setting  
`name` |  `str`   
Required. The name of the floor setting to get, example projects/123/floorsetting. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.modelarmor_v1.types.FloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting)` | Message describing FloorSetting resource  
  
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
  
### get_template
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_get_template():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[GetTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetTemplateRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_get_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.GetTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.GetTemplateRequest), dict]`   
The request object. Message for getting a Template  
`name` |  `str`   
Required. Name of the resource This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.modelarmor_v1.types.Template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template)` | Message describing Template resource  
  
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
  
### list_templates
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_list_templates():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ListTemplatesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ListTemplatesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_templates](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_list_templates)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.ListTemplatesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.ListTemplatesRequest), dict]`   
The request object. Message for requesting list of Templates  
`parent` |  `str`   
Required. Parent value for ListTemplatesRequest This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.pagers.ListTemplatesPager)` | Message for response to listing Templates Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_floor_setting_path
    
    
    parse_floor_setting_path(path: str) -> typing.Dict[str, str]

Parses a floor_setting path into its component segments.

### parse_template_path
    
    
    parse_template_path(path: str) -> typing.Dict[str, str]

Parses a template path into its component segments.

### sanitize_model_response
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_sanitize_model_response():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        model_response_data = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[DataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DataItem.html)()
        model_response_data.text = "text_value"
    
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[SanitizeModelResponseRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeModelResponseRequest.html)(
            name="name_value",
            model_response_data=model_response_data,
        )
    
        # Make the request
        response = client.[sanitize_model_response](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_sanitize_model_response)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.SanitizeModelResponseRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeModelResponseRequest), dict]`   
The request object. Sanitize Model Response request.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.modelarmor_v1.types.SanitizeModelResponseResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeModelResponseResponse)` | Sanitized Model Response Response.  
  
### sanitize_user_prompt
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_sanitize_user_prompt():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        user_prompt_data = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[DataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DataItem.html)()
        user_prompt_data.text = "text_value"
    
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[SanitizeUserPromptRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeUserPromptRequest.html)(
            name="name_value",
            user_prompt_data=user_prompt_data,
        )
    
        # Make the request
        response = client.[sanitize_user_prompt](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_sanitize_user_prompt)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.SanitizeUserPromptRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeUserPromptRequest), dict]`   
The request object. Sanitize User Prompt request.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.modelarmor_v1.types.SanitizeUserPromptResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeUserPromptResponse)` | Sanitized User Prompt Response.  
  
### stream_sanitize_model_response
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_stream_sanitize_model_response():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        model_response_data = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[DataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DataItem.html)()
        model_response_data.text = "text_value"
    
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[SanitizeModelResponseRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeModelResponseRequest.html)(
            name="name_value",
            model_response_data=model_response_data,
        )
    
        # This method expects an iterator which contains
        # 'modelarmor_v1.SanitizeModelResponseRequest' objects
        # Here we create a generator that yields a single `request` for
        # demonstrative purposes.
        requests = [request]
    
        def request_generator():
            for request in requests:
                yield request
    
        # Make the request
        stream = client.[stream_sanitize_model_response](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_stream_sanitize_model_response)(requests=request_generator())
    
        # Handle the response
        for response in stream:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`requests` |  `Iterator[[google.cloud.modelarmor_v1.types.SanitizeModelResponseRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeModelResponseRequest)]`   
The request object iterator. Sanitize Model Response request.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`Iterable[[google.cloud.modelarmor_v1.types.SanitizeModelResponseResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeModelResponseResponse)]` | Sanitized Model Response Response.  
  
### stream_sanitize_user_prompt
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_stream_sanitize_user_prompt():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        user_prompt_data = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[DataItem](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.DataItem.html)()
        user_prompt_data.text = "text_value"
    
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[SanitizeUserPromptRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeUserPromptRequest.html)(
            name="name_value",
            user_prompt_data=user_prompt_data,
        )
    
        # This method expects an iterator which contains
        # 'modelarmor_v1.SanitizeUserPromptRequest' objects
        # Here we create a generator that yields a single `request` for
        # demonstrative purposes.
        requests = [request]
    
        def request_generator():
            for request in requests:
                yield request
    
        # Make the request
        stream = client.[stream_sanitize_user_prompt](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_stream_sanitize_user_prompt)(requests=request_generator())
    
        # Handle the response
        for response in stream:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`requests` |  `Iterator[[google.cloud.modelarmor_v1.types.SanitizeUserPromptRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeUserPromptRequest)]`   
The request object iterator. Sanitize User Prompt request.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`Iterable[[google.cloud.modelarmor_v1.types.SanitizeUserPromptResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.SanitizeUserPromptResponse)]` | Sanitized User Prompt Response.  
  
### template_path
    
    
    template_path(project: str, location: str, template: str) -> str

Returns a fully-qualified template string.

### update_floor_setting
    
    
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

Updates the parameters of a single floor setting of a project
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_update_floor_setting():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[UpdateFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateFloorSettingRequest.html)(
        )
    
        # Make the request
        response = client.[update_floor_setting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_update_floor_setting)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.UpdateFloorSettingRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateFloorSettingRequest), dict]`   
The request object. Message for Updating a Floor Setting  
`floor_setting` |  `[google.cloud.modelarmor_v1.types.FloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting)`   
Required. The floor setting being updated. This corresponds to the `floor_setting` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. Field mask is used to specify the fields to be overwritten in the FloorSetting resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.modelarmor_v1.types.FloorSetting](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.FloorSetting)` | Message describing FloorSetting resource  
  
### update_template
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest)
    
    def sample_update_template():
        # Create a client
        client = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[ModelArmorClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html)()
    
        # Initialize request argument(s)
        request = [modelarmor_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest).[UpdateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateTemplateRequest.html)(
        )
    
        # Make the request
        response = client.[update_template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.services.model_armor.ModelArmorClient.html#google_cloud_modelarmor_v1_services_model_armor_ModelArmorClient_update_template)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.modelarmor_v1.types.UpdateTemplateRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.UpdateTemplateRequest), dict]`   
The request object. Message for updating a Template  
`template` |  `[google.cloud.modelarmor_v1.types.Template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template)`   
Required. The resource being updated This corresponds to the `template` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Field mask is used to specify the fields to be overwritten in the Template resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.modelarmor_v1.types.Template](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1.types.Template)` | Message describing Template resource  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
