---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient
title: Class RecaptchaEnterpriseServiceClient (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:52.740576+00:00
---

# Class RecaptchaEnterpriseServiceClient (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RecaptchaEnterpriseServiceClient (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    RecaptchaEnterpriseServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.transports.base.RecaptchaEnterpriseServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.transports.base.RecaptchaEnterpriseServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service to determine the likelihood an event is legitimate.

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
`RecaptchaEnterpriseServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### RecaptchaEnterpriseServiceClient
    
    
    RecaptchaEnterpriseServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.transports.base.RecaptchaEnterpriseServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.transports.base.RecaptchaEnterpriseServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the recaptcha enterprise service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,RecaptchaEnterpriseServiceTransport,Callable[..., RecaptchaEnterpriseServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the RecaptchaEnterpriseServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### add_ip_override
    
    
    add_ip_override(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.AddIpOverrideRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        ip_override_data: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.IpOverrideData
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.AddIpOverrideResponse
    )

Adds an IP override to a key. The following restrictions hold:

  * The maximum number of IP overrides per key is 1000.
  * For any conflict (such as IP already exists or IP part of an existing IP range), an error is returned.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_add_ip_override():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        ip_override_data = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[IpOverrideData](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.IpOverrideData.html)()
        ip_override_data.ip = "ip_value"
        ip_override_data.override_type = "ALLOW"
    
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[AddIpOverrideRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AddIpOverrideRequest.html)(
            name="name_value",
            ip_override_data=ip_override_data,
        )
    
        # Make the request
        response = client.[add_ip_override](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_add_ip_override)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.AddIpOverrideRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AddIpOverrideRequest), dict]`   
The request object. The AddIpOverride request message.  
`name` |  `str`   
Required. The name of the key to which the IP override is added, in the format `projects/{project}/keys/{key}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`ip_override_data` |  `[google.cloud.recaptchaenterprise_v1.types.IpOverrideData](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.IpOverrideData)`   
Required. IP override added to the key. This corresponds to the `ip_override_data` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.AddIpOverrideResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AddIpOverrideResponse)` | Response for AddIpOverride.  
  
### annotate_assessment
    
    
    annotate_assessment(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.AnnotateAssessmentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        annotation: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.AnnotateAssessmentRequest.Annotation
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.AnnotateAssessmentResponse
    )

Annotates a previously created Assessment to provide additional information on whether the event turned out to be authentic or fraudulent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_annotate_assessment():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[AnnotateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[annotate_assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_annotate_assessment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest), dict]`   
The request object. The request message to annotate an Assessment.  
`name` |  `str`   
Required. The resource name of the Assessment, in the format `projects/{project}/assessments/{assessment}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`annotation` |  `[google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Annotation](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentRequest.Annotation)`   
Optional. The annotation that is assigned to the Event. This field can be left empty to provide reasons that apply to an event without concluding whether the event is legitimate or fraudulent. This corresponds to the `annotation` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.AnnotateAssessmentResponse)` | Empty response for AnnotateAssessment.  
  
### assessment_path
    
    
    assessment_path(project: str, assessment: str) -> str

Returns a fully-qualified assessment string.

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

### create_assessment
    
    
    create_assessment(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.CreateAssessmentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        assessment: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Assessment
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Assessment

Creates an Assessment of the likelihood an event is legitimate.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_create_assessment():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[CreateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateAssessmentRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_assessment)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.CreateAssessmentRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateAssessmentRequest), dict]`   
The request object. The create assessment request message.  
`parent` |  `str`   
Required. The name of the project in which the assessment is created, in the format `projects/{project}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`assessment` |  `[google.cloud.recaptchaenterprise_v1.types.Assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment)`   
Required. The assessment details. This corresponds to the `assessment` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.Assessment](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Assessment)` | A reCAPTCHA Enterprise assessment resource.  
  
### create_firewall_policy
    
    
    create_firewall_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.CreateFirewallPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        firewall_policy: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.FirewallPolicy
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.FirewallPolicy

Creates a new FirewallPolicy, specifying conditions at which reCAPTCHA Enterprise actions can be executed. A project may have a maximum of 1000 policies.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_create_firewall_policy():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[CreateFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateFirewallPolicyRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_firewall_policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_firewall_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.CreateFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateFirewallPolicyRequest), dict]`   
The request object. The create firewall policy request message.  
`parent` |  `str`   
Required. The name of the project this policy applies to, in the format `projects/{project}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`firewall_policy` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallPolicy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallPolicy)`   
Required. Information to create the policy. This corresponds to the `firewall_policy` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.FirewallPolicy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallPolicy)` | A FirewallPolicy represents a single matching pattern and resulting actions to take.  
  
### create_key
    
    
    create_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.CreateKeyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        key: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key

Creates a new reCAPTCHA Enterprise key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_create_key():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        key = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key.html)()
        key.web_settings.integration_type = "POLICY_BASED_CHALLENGE"
        key.display_name = "display_name_value"
    
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[CreateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateKeyRequest.html)(
            parent="parent_value",
            key=key,
        )
    
        # Make the request
        response = client.[create_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.CreateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.CreateKeyRequest), dict]`   
The request object. The create key request message.  
`parent` |  `str`   
Required. The name of the project in which the key is created, in the format `projects/{project}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`key` |  `[google.cloud.recaptchaenterprise_v1.types.Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key)`   
Required. Information to create a reCAPTCHA Enterprise key. This corresponds to the `key` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key)` | A key used to identify and configure applications (web and/or mobile) that use reCAPTCHA Enterprise.  
  
### delete_firewall_policy
    
    
    delete_firewall_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.DeleteFirewallPolicyRequest,
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

Deletes the specified firewall policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_delete_firewall_policy():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[DeleteFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.DeleteFirewallPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_firewall_policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_delete_firewall_policy)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.DeleteFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.DeleteFirewallPolicyRequest), dict]`   
The request object. The delete firewall policy request message.  
`name` |  `str`   
Required. The name of the policy to be deleted, in the format `projects/{project}/firewallpolicies/{firewallpolicy}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_key
    
    
    delete_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.DeleteKeyRequest,
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

Deletes the specified key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_delete_key():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[DeleteKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.DeleteKeyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_delete_key)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.DeleteKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.DeleteKeyRequest), dict]`   
The request object. The delete key request message.  
`name` |  `str`   
Required. The name of the key to be deleted, in the format `projects/{project}/keys/{key}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### firewall_policy_path
    
    
    firewall_policy_path(project: str, firewallpolicy: str) -> str

Returns a fully-qualified firewall_policy string.

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
`RecaptchaEnterpriseServiceClient` | The constructed client.  
  
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
`RecaptchaEnterpriseServiceClient` | The constructed client.  
  
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
`RecaptchaEnterpriseServiceClient` | The constructed client.  
  
### get_firewall_policy
    
    
    get_firewall_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.GetFirewallPolicyRequest,
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
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.FirewallPolicy

Returns the specified firewall policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_get_firewall_policy():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[GetFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetFirewallPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_firewall_policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_firewall_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.GetFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetFirewallPolicyRequest), dict]`   
The request object. The get firewall policy request message.  
`name` |  `str`   
Required. The name of the requested policy, in the format `projects/{project}/firewallpolicies/{firewallpolicy}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.FirewallPolicy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallPolicy)` | A FirewallPolicy represents a single matching pattern and resulting actions to take.  
  
### get_key
    
    
    get_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.GetKeyRequest,
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
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key

Returns the specified key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_get_key():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[GetKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetKeyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.GetKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetKeyRequest), dict]`   
The request object. The get key request message.  
`name` |  `str`   
Required. The name of the requested key, in the format `projects/{project}/keys/{key}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key)` | A key used to identify and configure applications (web and/or mobile) that use reCAPTCHA Enterprise.  
  
### get_metrics
    
    
    get_metrics(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.GetMetricsRequest,
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
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Metrics

Get some aggregated metrics for a Key. This data can be used to build dashboards.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_get_metrics():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[GetMetricsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetMetricsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_metrics](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_metrics)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.GetMetricsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetMetricsRequest), dict]`   
The request object. The get metrics request message.  
`name` |  `str`   
Required. The name of the requested metrics, in the format `projects/{project}/keys/{key}/metrics`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.Metrics](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Metrics)` | Metrics for a single Key.  
  
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
  
### get_policy
    
    
    get_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.GetPolicyRequest,
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
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Policy

Get the policy for a key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_get_policy():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[GetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetPolicyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.GetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.GetPolicyRequest), dict]`   
The request object. The request message to get a policy.  
`name` |  `str`   
Required. The name of the policy to get, in the format `projects/{project}/keys/{key}/policy`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.Policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Policy)` | A complete configuration set containing multiple grouped rules defining the behavior of reCAPTCHA for fraud detection and prevention.  
  
### key_path
    
    
    key_path(project: str, key: str) -> str

Returns a fully-qualified key string.

### list_firewall_policies
    
    
    list_firewall_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListFirewallPoliciesRequest,
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
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesPager
    )

Returns the list of all firewall policies that belong to a project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_list_firewall_policies():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[ListFirewallPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_firewall_policies](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_firewall_policies)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListFirewallPoliciesRequest), dict]`   
The request object. The list firewall policies request message.  
`parent` |  `str`   
Required. The name of the project to list the policies for, in the format `projects/{project}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesPager](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesPager)` | Response to request to list firewall policies belonging to a project. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_ip_overrides
    
    
    list_ip_overrides(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListIpOverridesRequest,
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
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesPager
    )

Lists all IP overrides for a key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_list_ip_overrides():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[ListIpOverridesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListIpOverridesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_ip_overrides](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_ip_overrides)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.ListIpOverridesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListIpOverridesRequest), dict]`   
The request object. The ListIpOverrides request message.  
`parent` |  `str`   
Required. The parent key for which the IP overrides are listed, in the format `projects/{project}/keys/{key}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesPager](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesPager)` | Response for ListIpOverrides. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_keys
    
    
    list_keys(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListKeysRequest,
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
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysPager
    )

Returns the list of all keys that belong to a project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_list_keys():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[ListKeysRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListKeysRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_keys](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_keys)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.ListKeysRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListKeysRequest), dict]`   
The request object. The list keys request message.  
`parent` |  `str`   
Required. The name of the project that contains the keys that is listed, in the format `projects/{project}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysPager](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysPager)` | Response to request to list keys in a project. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_related_account_group_memberships
    
    
    list_related_account_group_memberships(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest,
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
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsPager
    )

Get memberships in a group of related accounts.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_list_related_account_group_memberships():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[ListRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_related_account_group_memberships](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_related_account_group_memberships)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupMembershipsRequest), dict]`   
The request object. The request message to list memberships in a related account group.  
`parent` |  `str`   
Required. The resource name for the related account group in the format `projects/{project}/relatedaccountgroups/{relatedaccountgroup}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsPager](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsPager)` | The response to a ListRelatedAccountGroupMemberships call. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_related_account_groups
    
    
    list_related_account_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupsRequest,
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
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsPager
    )

List groups of related accounts.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_list_related_account_groups():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[ListRelatedAccountGroupsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_related_account_groups](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_related_account_groups)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ListRelatedAccountGroupsRequest), dict]`   
The request object. The request message to list related account groups.  
`parent` |  `str`   
Required. The name of the project to list related account groups from, in the format `projects/{project}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsPager](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsPager)` | The response to a ListRelatedAccountGroups call. Iterating over this object will yield results and resolve additional pages automatically.  
  
### metrics_path
    
    
    metrics_path(project: str, key: str) -> str

Returns a fully-qualified metrics string.

### migrate_key
    
    
    migrate_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.MigrateKeyRequest,
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
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key

Migrates an existing key from reCAPTCHA to reCAPTCHA Enterprise. Once a key is migrated, it can be used from either product. SiteVerify requests are billed as CreateAssessment calls. You must be authenticated as one of the current owners of the reCAPTCHA Key, and your user must have the reCAPTCHA Enterprise Admin IAM role in the destination project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_migrate_key():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[MigrateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.MigrateKeyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[migrate_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_migrate_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.MigrateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.MigrateKeyRequest), dict]`   
The request object. The migrate key request message.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key)` | A key used to identify and configure applications (web and/or mobile) that use reCAPTCHA Enterprise.  
  
### parse_assessment_path
    
    
    parse_assessment_path(path: str) -> typing.Dict[str, str]

Parses a assessment path into its component segments.

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

### parse_firewall_policy_path
    
    
    parse_firewall_policy_path(path: str) -> typing.Dict[str, str]

Parses a firewall_policy path into its component segments.

### parse_key_path
    
    
    parse_key_path(path: str) -> typing.Dict[str, str]

Parses a key path into its component segments.

### parse_metrics_path
    
    
    parse_metrics_path(path: str) -> typing.Dict[str, str]

Parses a metrics path into its component segments.

### parse_policy_path
    
    
    parse_policy_path(path: str) -> typing.Dict[str, str]

Parses a policy path into its component segments.

### parse_related_account_group_membership_path
    
    
    parse_related_account_group_membership_path(path: str) -> typing.Dict[str, str]

Parses a related_account_group_membership path into its component segments.

### parse_related_account_group_path
    
    
    parse_related_account_group_path(path: str) -> typing.Dict[str, str]

Parses a related_account_group path into its component segments.

### policy_path
    
    
    policy_path(project: str, key: str) -> str

Returns a fully-qualified policy string.

### related_account_group_membership_path
    
    
    related_account_group_membership_path(
        project: str, relatedaccountgroup: str, membership: str
    ) -> str

Returns a fully-qualified related_account_group_membership string.

### related_account_group_path
    
    
    related_account_group_path(project: str, relatedaccountgroup: str) -> str

Returns a fully-qualified related_account_group string.

### remove_ip_override
    
    
    remove_ip_override(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.RemoveIpOverrideRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        ip_override_data: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.IpOverrideData
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.RemoveIpOverrideResponse
    )

Removes an IP override from a key. The following restrictions hold:

  * If the IP isn't found in an existing IP override, a `NOT_FOUND` error is returned.
  * If the IP is found in an existing IP override, but the override type does not match, a `NOT_FOUND` error is returned.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_remove_ip_override():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        ip_override_data = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[IpOverrideData](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.IpOverrideData.html)()
        ip_override_data.ip = "ip_value"
        ip_override_data.override_type = "ALLOW"
    
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RemoveIpOverrideRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideRequest.html)(
            name="name_value",
            ip_override_data=ip_override_data,
        )
    
        # Make the request
        response = client.[remove_ip_override](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_remove_ip_override)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideRequest), dict]`   
The request object. The RemoveIpOverride request message.  
`name` |  `str`   
Required. The name of the key from which the IP override is removed, in the format `projects/{project}/keys/{key}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`ip_override_data` |  `[google.cloud.recaptchaenterprise_v1.types.IpOverrideData](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.IpOverrideData)`   
Required. IP override to be removed from the key. This corresponds to the `ip_override_data` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RemoveIpOverrideResponse)` | Response for RemoveIpOverride.  
  
### reorder_firewall_policies
    
    
    reorder_firewall_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ReorderFirewallPoliciesRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        names: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ReorderFirewallPoliciesResponse
    )

Reorders all firewall policies.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_reorder_firewall_policies():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[ReorderFirewallPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesRequest.html)(
            parent="parent_value",
            names=['names_value1', 'names_value2'],
        )
    
        # Make the request
        response = client.[reorder_firewall_policies](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_reorder_firewall_policies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesRequest), dict]`   
The request object. The reorder firewall policies request message.  
`parent` |  `str`   
Required. The name of the project to list the policies for, in the format `projects/{project}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`names` |  `MutableSequence[str]`   
Required. A list containing all policy names, in the new order. Each name is in the format `projects/{project}/firewallpolicies/{firewallpolicy}`. This corresponds to the `names` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.ReorderFirewallPoliciesResponse)` | The reorder firewall policies response message.  
  
### retrieve_legacy_secret_key
    
    
    retrieve_legacy_secret_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.RetrieveLegacySecretKeyRequest,
                dict,
            ]
        ] = None,
        *,
        key: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.RetrieveLegacySecretKeyResponse
    )

Returns the secret key related to the specified public key. You must use the legacy secret key only in a 3rd party integration with legacy reCAPTCHA.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_retrieve_legacy_secret_key():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RetrieveLegacySecretKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyRequest.html)(
            key="key_value",
        )
    
        # Make the request
        response = client.[retrieve_legacy_secret_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_retrieve_legacy_secret_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyRequest), dict]`   
The request object. The retrieve legacy secret key request message.  
`key` |  `str`   
Required. The public key name linked to the requested secret key in the format `projects/{project}/keys/{key}`. This corresponds to the `key` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyResponse](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.RetrieveLegacySecretKeyResponse)` | Secret key is used only in legacy reCAPTCHA. It must be used in a 3rd party integration with legacy reCAPTCHA.  
  
### search_related_account_group_memberships
    
    
    search_related_account_group_memberships(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest,
                dict,
            ]
        ] = None,
        *,
        project: typing.Optional[str] = None,
        hashed_account_id: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsPager
    )

Search group memberships related to a given account.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_search_related_account_group_memberships():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[SearchRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsRequest.html)(
            project="project_value",
        )
    
        # Make the request
        page_result = client.[search_related_account_group_memberships](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_search_related_account_group_memberships)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.SearchRelatedAccountGroupMembershipsRequest), dict]`   
The request object. The request message to search related account group memberships.  
`project` |  `str`   
Required. The name of the project to search related account group memberships from. Specify the project name in the following format: `projects/{project}`. This corresponds to the `project` field on the `request` instance; if `request` is provided, this should not be set.  
`hashed_account_id` |  `bytes`   
Optional. Deprecated: use `account_id` instead. The unique stable hashed account identifier used to search connections. The identifier should correspond to a `hashed_account_id` provided in a previous `CreateAssessment` or `AnnotateAssessment` call. Either hashed_account_id or account_id must be set, but not both. This corresponds to the `hashed_account_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsPager](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsPager)` | The response to a SearchRelatedAccountGroupMemberships call. Iterating over this object will yield results and resolve additional pages automatically.  
  
### update_firewall_policy
    
    
    update_firewall_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.UpdateFirewallPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        firewall_policy: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.FirewallPolicy
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
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.FirewallPolicy

Updates the specified firewall policy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_update_firewall_policy():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[UpdateFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdateFirewallPolicyRequest.html)(
        )
    
        # Make the request
        response = client.[update_firewall_policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_update_firewall_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.UpdateFirewallPolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdateFirewallPolicyRequest), dict]`   
The request object. The update firewall policy request message.  
`firewall_policy` |  `[google.cloud.recaptchaenterprise_v1.types.FirewallPolicy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallPolicy)`   
Required. The policy to update. This corresponds to the `firewall_policy` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. The mask to control which fields of the policy get updated. If the mask is not present, all fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.FirewallPolicy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.FirewallPolicy)` | A FirewallPolicy represents a single matching pattern and resulting actions to take.  
  
### update_key
    
    
    update_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.UpdateKeyRequest,
                dict,
            ]
        ] = None,
        *,
        key: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key
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
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key

Updates the specified key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_update_key():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        key = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key.html)()
        key.web_settings.integration_type = "POLICY_BASED_CHALLENGE"
        key.display_name = "display_name_value"
    
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[UpdateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdateKeyRequest.html)(
            key=key,
        )
    
        # Make the request
        response = client.[update_key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_update_key)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.UpdateKeyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdateKeyRequest), dict]`   
The request object. The update key request message.  
`key` |  `[google.cloud.recaptchaenterprise_v1.types.Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key)`   
Required. The key to update. This corresponds to the `key` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. The mask to control which fields of the key get updated. If the mask is not present, all fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.Key](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Key)` | A key used to identify and configure applications (web and/or mobile) that use reCAPTCHA Enterprise.  
  
### update_policy
    
    
    update_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.UpdatePolicyRequest,
                dict,
            ]
        ] = None,
        *,
        policy: typing.Optional[
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Policy
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
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Policy

Updates the policy for a key.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest)
    
    def sample_update_policy():
        # Create a client
        client = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[RecaptchaEnterpriseServiceClient](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html)()
    
        # Initialize request argument(s)
        request = [recaptchaenterprise_v1](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest).[UpdatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdatePolicyRequest.html)(
        )
    
        # Make the request
        response = client.[update_policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.html#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_update_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.recaptchaenterprise_v1.types.UpdatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.UpdatePolicyRequest), dict]`   
The request object. The request message to update a policy.  
`policy` |  `[google.cloud.recaptchaenterprise_v1.types.Policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Policy)`   
Required. The Policy's name is used to identify the policy to update, in the format `projects/{project}/keys/{key}/policy`. This corresponds to the `policy` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. The mask to control which fields of the policy get updated. If the mask is not present, all fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.recaptchaenterprise_v1.types.Policy](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Policy)` | A complete configuration set containing multiple grouped rules defining the behavior of reCAPTCHA for fraud detection and prevention.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
