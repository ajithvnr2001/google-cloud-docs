---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient
title: Class SaasRolloutsClient (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:42.081858+00:00
---

# Class SaasRolloutsClient (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SaasRolloutsClient (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    SaasRolloutsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.transports.base.SaasRolloutsTransport,
                typing.Callable[
                    [...],
                    google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.transports.base.SaasRolloutsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Manages the rollout of SaaS services.

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
`SaasRolloutsTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### SaasRolloutsClient
    
    
    SaasRolloutsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.transports.base.SaasRolloutsTransport,
                typing.Callable[
                    [...],
                    google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.transports.base.SaasRolloutsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the saas rollouts client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,SaasRolloutsTransport,Callable[..., SaasRolloutsTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the SaasRolloutsTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_rollout
    
    
    create_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.CreateRolloutRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        rollout: typing.Optional[
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.Rollout
        ] = None,
        rollout_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.Rollout

Create a new rollout.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_create_rollout():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        rollout = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[Rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout.html)()
        rollout.rollout_kind = "rollout_kind_value"
    
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[CreateRolloutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateRolloutRequest.html)(
            parent="parent_value",
            rollout_id="rollout_id_value",
            rollout=rollout,
        )
    
        # Make the request
        response = client.[create_rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_create_rollout)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateRolloutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateRolloutRequest), dict]`   
The request object. The request structure for the CreateRollout method.  
`parent` |  `str`   
Required. The parent of the rollout. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`rollout` |  `[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout)`   
Required. The desired state for the rollout. This corresponds to the `rollout` field on the `request` instance; if `request` is provided, this should not be set.  
`rollout_id` |  `str`   
Required. The ID value for the new rollout. This corresponds to the `rollout_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout)` | Represents a single rollout execution and its results  
  
### create_rollout_kind
    
    
    create_rollout_kind(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.CreateRolloutKindRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        rollout_kind: typing.Optional[
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.RolloutKind
        ] = None,
        rollout_kind_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.RolloutKind
    )

Create a new rollout kind.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_create_rollout_kind():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        rollout_kind = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[RolloutKind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind.html)()
        rollout_kind.unit_kind = "unit_kind_value"
    
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[CreateRolloutKindRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateRolloutKindRequest.html)(
            parent="parent_value",
            rollout_kind_id="rollout_kind_id_value",
            rollout_kind=rollout_kind,
        )
    
        # Make the request
        response = client.[create_rollout_kind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_create_rollout_kind)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateRolloutKindRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.CreateRolloutKindRequest), dict]`   
The request object. The request structure for the CreateRolloutKind method.  
`parent` |  `str`   
Required. The parent of the rollout kind. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`rollout_kind` |  `[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind)`   
Required. The desired state for the rollout kind. This corresponds to the `rollout_kind` field on the `request` instance; if `request` is provided, this should not be set.  
`rollout_kind_id` |  `str`   
Required. The ID value for the new rollout kind. This corresponds to the `rollout_kind_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind)` | An object that describes various settings of Rollout execution. Includes built-in policies across GCP and GDC, and customizable policies.  
  
### delete_rollout
    
    
    delete_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.DeleteRolloutRequest,
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

Delete a single rollout.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_delete_rollout():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[DeleteRolloutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteRolloutRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_delete_rollout)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteRolloutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteRolloutRequest), dict]`   
The request object. The request structure for the DeleteRollout method.  
`name` |  `str`   
Required. The resource name of the resource within a service. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_rollout_kind
    
    
    delete_rollout_kind(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.DeleteRolloutKindRequest,
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

Delete a single rollout kind.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_delete_rollout_kind():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[DeleteRolloutKindRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteRolloutKindRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_rollout_kind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_delete_rollout_kind)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteRolloutKindRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.DeleteRolloutKindRequest), dict]`   
The request object. The request structure for the DeleteRolloutKind method.  
`name` |  `str`   
Required. The resource name of the resource within a service. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`SaasRolloutsClient` | The constructed client.  
  
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
`SaasRolloutsClient` | The constructed client.  
  
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
`SaasRolloutsClient` | The constructed client.  
  
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
  
### get_rollout
    
    
    get_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.GetRolloutRequest,
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
    ) -> google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.Rollout

Retrieve a single rollout.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_get_rollout():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[GetRolloutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetRolloutRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_get_rollout)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetRolloutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetRolloutRequest), dict]`   
The request object. The request structure for the GetRollout method.  
`name` |  `str`   
Required. The resource name of the resource within a service. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout)` | Represents a single rollout execution and its results  
  
### get_rollout_kind
    
    
    get_rollout_kind(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.GetRolloutKindRequest,
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
        google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.RolloutKind
    )

Retrieve a single rollout kind.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_get_rollout_kind():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[GetRolloutKindRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetRolloutKindRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_rollout_kind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_get_rollout_kind)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetRolloutKindRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.GetRolloutKindRequest), dict]`   
The request object. The request structure for the GetRolloutKind method.  
`name` |  `str`   
Required. The resource name of the resource within a service. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind)` | An object that describes various settings of Rollout execution. Includes built-in policies across GCP and GDC, and customizable policies.  
  
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
  
### list_rollout_kinds
    
    
    list_rollout_kinds(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.ListRolloutKindsRequest,
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
    ) -> (
        google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.pagers.ListRolloutKindsPager
    )

Retrieve a collection of rollout kinds.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_list_rollout_kinds():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[ListRolloutKindsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListRolloutKindsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_rollout_kinds](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_list_rollout_kinds)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListRolloutKindsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListRolloutKindsRequest), dict]`   
The request object. The request structure for the ListRolloutKinds method.  
`parent` |  `str`   
Required. The parent of the rollout kind. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.pagers.ListRolloutKindsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.pagers.ListRolloutKindsPager)` | The response structure for the ListRolloutKinds method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_rollouts
    
    
    list_rollouts(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.ListRolloutsRequest,
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
    ) -> (
        google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.pagers.ListRolloutsPager
    )

Retrieve a collection of rollouts.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_list_rollouts():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[ListRolloutsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListRolloutsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_rollouts](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_list_rollouts)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListRolloutsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.ListRolloutsRequest), dict]`   
The request object. The request structure for the ListRollouts method.  
`parent` |  `str`   
Required. The parent of the rollout. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.pagers.ListRolloutsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.pagers.ListRolloutsPager)` | The response structure for the ListRollouts method. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_release_path
    
    
    parse_release_path(path: str) -> typing.Dict[str, str]

Parses a release path into its component segments.

### parse_rollout_kind_path
    
    
    parse_rollout_kind_path(path: str) -> typing.Dict[str, str]

Parses a rollout_kind path into its component segments.

### parse_rollout_path
    
    
    parse_rollout_path(path: str) -> typing.Dict[str, str]

Parses a rollout path into its component segments.

### parse_unit_kind_path
    
    
    parse_unit_kind_path(path: str) -> typing.Dict[str, str]

Parses a unit_kind path into its component segments.

### release_path
    
    
    release_path(project: str, location: str, release: str) -> str

Returns a fully-qualified release string.

### rollout_kind_path
    
    
    rollout_kind_path(project: str, location: str, rollout_kind_id: str) -> str

Returns a fully-qualified rollout_kind string.

### rollout_path
    
    
    rollout_path(project: str, location: str, rollout_id: str) -> str

Returns a fully-qualified rollout string.

### unit_kind_path
    
    
    unit_kind_path(project: str, location: str, unitKind: str) -> str

Returns a fully-qualified unit_kind string.

### update_rollout
    
    
    update_rollout(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.UpdateRolloutRequest,
                dict,
            ]
        ] = None,
        *,
        rollout: typing.Optional[
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.Rollout
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
    ) -> google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.Rollout

Update a single rollout.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_update_rollout():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        rollout = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[Rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout.html)()
        rollout.rollout_kind = "rollout_kind_value"
    
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[UpdateRolloutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateRolloutRequest.html)(
            rollout=rollout,
        )
    
        # Make the request
        response = client.[update_rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_update_rollout)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateRolloutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateRolloutRequest), dict]`   
The request object. The request structure for the UpdateRollout method.  
`rollout` |  `[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout)`   
Required. The desired state for the rollout. This corresponds to the `rollout` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Field mask is used to specify the fields to be overwritten in the Rollout resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the Rollout will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.Rollout)` | Represents a single rollout execution and its results  
  
### update_rollout_kind
    
    
    update_rollout_kind(
        request: typing.Optional[
            typing.Union[
                google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_service.UpdateRolloutKindRequest,
                dict,
            ]
        ] = None,
        *,
        rollout_kind: typing.Optional[
            google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.RolloutKind
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
    ) -> (
        google.cloud.saasplatform_saasservicemgmt_v1beta1.types.rollouts_resources.RolloutKind
    )

Update a single rollout kind.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest)
    
    def sample_update_rollout_kind():
        # Create a client
        client = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[SaasRolloutsClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html)()
    
        # Initialize request argument(s)
        rollout_kind = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[RolloutKind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind.html)()
        rollout_kind.unit_kind = "unit_kind_value"
    
        request = [saasplatform_saasservicemgmt_v1beta1](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest).[UpdateRolloutKindRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateRolloutKindRequest.html)(
            rollout_kind=rollout_kind,
        )
    
        # Make the request
        response = client.[update_rollout_kind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.services.saas_rollouts.SaasRolloutsClient.html#google_cloud_saasplatform_saasservicemgmt_v1beta1_services_saas_rollouts_SaasRolloutsClient_update_rollout_kind)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateRolloutKindRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.UpdateRolloutKindRequest), dict]`   
The request object. The request structure for the UpdateRolloutKind method.  
`rollout_kind` |  `[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind)`   
Required. The desired state for the rollout kind. This corresponds to the `rollout_kind` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Field mask is used to specify the fields to be overwritten in the RolloutKind resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields in the RolloutKind will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind](https://docs.cloud.google.com/python/docs/reference/google-cloud-saasplatform-saasservicemgmt/latest/google.cloud.saasplatform_saasservicemgmt_v1beta1.types.RolloutKind)` | An object that describes various settings of Rollout execution. Includes built-in policies across GCP and GDC, and customizable policies.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
