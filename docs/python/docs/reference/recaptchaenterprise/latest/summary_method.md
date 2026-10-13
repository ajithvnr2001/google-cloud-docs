---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/summary_method/
title: Package Methods (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:49.337410+00:00
---

# Package Methods (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 

Summary of entries of Methods for recaptchaenterprise.

## 

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient
    
    
    RecaptchaEnterpriseServiceAsyncClient(
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
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the recaptcha enterprise service async client.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_RecaptchaEnterpriseServiceAsyncClient)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.add_ip_override
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.AddIpOverrideResponse
    )

Adds an IP override to a key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.add_ip_override](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_add_ip_override)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.annotate_assessment
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.AnnotateAssessmentResponse
    )

Annotates a previously created Assessment to provide additional information on whether the event turned out to be authentic or fraudulent.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.annotate_assessment](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_annotate_assessment)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.assessment_path
    
    
    assessment_path(project: str, assessment: str) -> str

Returns a fully-qualified assessment string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.assessment_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_assessment_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_common_billing_account_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_common_folder_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_common_location_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_common_organization_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_common_project_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.create_assessment
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Assessment

Creates an Assessment of the likelihood an event is legitimate.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.create_assessment](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_create_assessment)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.create_firewall_policy
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.FirewallPolicy

Creates a new FirewallPolicy, specifying conditions at which reCAPTCHA Enterprise actions can be executed.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.create_firewall_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_create_firewall_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.create_key
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key

Creates a new reCAPTCHA Enterprise key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.create_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_create_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.delete_firewall_policy
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes the specified firewall policy.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.delete_firewall_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_delete_firewall_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.delete_key
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes the specified key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.delete_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_delete_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.firewall_policy_path
    
    
    firewall_policy_path(project: str, firewallpolicy: str) -> str

Returns a fully-qualified firewall_policy string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.firewall_policy_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_firewall_policy_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_from_service_account_file)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_from_service_account_info)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_from_service_account_json)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_firewall_policy
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.FirewallPolicy

Returns the specified firewall policy.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_firewall_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_get_firewall_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_key
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key

Returns the specified key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_get_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_metrics
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Metrics

Get some aggregated metrics for a Key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_metrics](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_get_metrics)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_policy
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Policy

Get the policy for a key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_get_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.transports.base.RecaptchaEnterpriseServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_get_transport_class)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.key_path
    
    
    key_path(project: str, key: str) -> str

Returns a fully-qualified key string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.key_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_key_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_firewall_policies
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesAsyncPager
    )

Returns the list of all firewall policies that belong to a project.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_firewall_policies](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_list_firewall_policies)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_ip_overrides
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesAsyncPager
    )

Lists all IP overrides for a key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_ip_overrides](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_list_ip_overrides)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_keys
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysAsyncPager
    )

Returns the list of all keys that belong to a project.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_keys](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_list_keys)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_related_account_group_memberships
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsAsyncPager
    )

Get memberships in a group of related accounts.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_related_account_group_memberships](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_list_related_account_group_memberships)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_related_account_groups
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsAsyncPager
    )

List groups of related accounts.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.list_related_account_groups](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_list_related_account_groups)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.metrics_path
    
    
    metrics_path(project: str, key: str) -> str

Returns a fully-qualified metrics string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.metrics_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_metrics_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.migrate_key
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key

Migrates an existing key from reCAPTCHA to reCAPTCHA Enterprise.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.migrate_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_migrate_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_assessment_path
    
    
    parse_assessment_path(path: str) -> typing.Dict[str, str]

Parses a assessment path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_assessment_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_assessment_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_common_folder_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_common_location_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_common_organization_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_common_project_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_firewall_policy_path
    
    
    parse_firewall_policy_path(path: str) -> typing.Dict[str, str]

Parses a firewall_policy path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_firewall_policy_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_firewall_policy_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_key_path
    
    
    parse_key_path(path: str) -> typing.Dict[str, str]

Parses a key path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_key_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_key_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_metrics_path
    
    
    parse_metrics_path(path: str) -> typing.Dict[str, str]

Parses a metrics path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_metrics_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_metrics_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_policy_path
    
    
    parse_policy_path(path: str) -> typing.Dict[str, str]

Parses a policy path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_policy_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_policy_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_related_account_group_membership_path
    
    
    parse_related_account_group_membership_path(path: str) -> typing.Dict[str, str]

Parses a related_account_group_membership path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_related_account_group_membership_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_related_account_group_membership_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_related_account_group_path
    
    
    parse_related_account_group_path(path: str) -> typing.Dict[str, str]

Parses a related_account_group path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.parse_related_account_group_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_parse_related_account_group_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.policy_path
    
    
    policy_path(project: str, key: str) -> str

Returns a fully-qualified policy string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.policy_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_policy_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.related_account_group_membership_path
    
    
    related_account_group_membership_path(
        project: str, relatedaccountgroup: str, membership: str
    ) -> str

Returns a fully-qualified related_account_group_membership string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.related_account_group_membership_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_related_account_group_membership_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.related_account_group_path
    
    
    related_account_group_path(project: str, relatedaccountgroup: str) -> str

Returns a fully-qualified related_account_group string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.related_account_group_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_related_account_group_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.remove_ip_override
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.RemoveIpOverrideResponse
    )

Removes an IP override from a key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.remove_ip_override](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_remove_ip_override)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.reorder_firewall_policies
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ReorderFirewallPoliciesResponse
    )

Reorders all firewall policies.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.reorder_firewall_policies](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_reorder_firewall_policies)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.retrieve_legacy_secret_key
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.RetrieveLegacySecretKeyResponse
    )

Returns the secret key related to the specified public key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.retrieve_legacy_secret_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_retrieve_legacy_secret_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.search_related_account_group_memberships
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsAsyncPager
    )

Search group memberships related to a given account.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.search_related_account_group_memberships](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_search_related_account_group_memberships)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.update_firewall_policy
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.FirewallPolicy

Updates the specified firewall policy.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.update_firewall_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_update_firewall_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.update_key
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Key

Updates the specified key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.update_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_update_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.update_policy
    
    
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.Policy

Updates the policy for a key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient.update_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceAsyncClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceAsyncClient_update_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_RecaptchaEnterpriseServiceClient)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.**exit**](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient___exit__)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.add_ip_override
    
    
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

Adds an IP override to a key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.add_ip_override](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_add_ip_override)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.annotate_assessment
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.annotate_assessment](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_annotate_assessment)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.assessment_path
    
    
    assessment_path(project: str, assessment: str) -> str

Returns a fully-qualified assessment string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.assessment_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_assessment_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_common_billing_account_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_common_folder_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_common_location_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_common_organization_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_common_project_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.create_assessment
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.create_assessment](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_assessment)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.create_firewall_policy
    
    
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

Creates a new FirewallPolicy, specifying conditions at which reCAPTCHA Enterprise actions can be executed.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.create_firewall_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_firewall_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.create_key
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.create_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_create_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.delete_firewall_policy
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.delete_firewall_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_delete_firewall_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.delete_key
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.delete_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_delete_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.firewall_policy_path
    
    
    firewall_policy_path(project: str, firewallpolicy: str) -> str

Returns a fully-qualified firewall_policy string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.firewall_policy_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_firewall_policy_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_from_service_account_file)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_from_service_account_info)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_from_service_account_json)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_firewall_policy
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_firewall_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_firewall_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_key
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_metrics
    
    
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

Get some aggregated metrics for a Key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_metrics](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_metrics)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_policy
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.get_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_get_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.key_path
    
    
    key_path(project: str, key: str) -> str

Returns a fully-qualified key string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.key_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_key_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_firewall_policies
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_firewall_policies](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_firewall_policies)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_ip_overrides
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_ip_overrides](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_ip_overrides)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_keys
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_keys](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_keys)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_related_account_group_memberships
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_related_account_group_memberships](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_related_account_group_memberships)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_related_account_groups
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.list_related_account_groups](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_list_related_account_groups)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.metrics_path
    
    
    metrics_path(project: str, key: str) -> str

Returns a fully-qualified metrics string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.metrics_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_metrics_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.migrate_key
    
    
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

Migrates an existing key from reCAPTCHA to reCAPTCHA Enterprise.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.migrate_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_migrate_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_assessment_path
    
    
    parse_assessment_path(path: str) -> typing.Dict[str, str]

Parses a assessment path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_assessment_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_assessment_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_common_billing_account_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_common_folder_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_common_location_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_common_organization_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_common_project_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_firewall_policy_path
    
    
    parse_firewall_policy_path(path: str) -> typing.Dict[str, str]

Parses a firewall_policy path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_firewall_policy_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_firewall_policy_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_key_path
    
    
    parse_key_path(path: str) -> typing.Dict[str, str]

Parses a key path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_key_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_key_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_metrics_path
    
    
    parse_metrics_path(path: str) -> typing.Dict[str, str]

Parses a metrics path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_metrics_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_metrics_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_policy_path
    
    
    parse_policy_path(path: str) -> typing.Dict[str, str]

Parses a policy path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_policy_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_policy_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_related_account_group_membership_path
    
    
    parse_related_account_group_membership_path(path: str) -> typing.Dict[str, str]

Parses a related_account_group_membership path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_related_account_group_membership_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_related_account_group_membership_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_related_account_group_path
    
    
    parse_related_account_group_path(path: str) -> typing.Dict[str, str]

Parses a related_account_group path into its component segments.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.parse_related_account_group_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_parse_related_account_group_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.policy_path
    
    
    policy_path(project: str, key: str) -> str

Returns a fully-qualified policy string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.policy_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_policy_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.related_account_group_membership_path
    
    
    related_account_group_membership_path(
        project: str, relatedaccountgroup: str, membership: str
    ) -> str

Returns a fully-qualified related_account_group_membership string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.related_account_group_membership_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_related_account_group_membership_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.related_account_group_path
    
    
    related_account_group_path(project: str, relatedaccountgroup: str) -> str

Returns a fully-qualified related_account_group string.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.related_account_group_path](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_related_account_group_path)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.remove_ip_override
    
    
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

Removes an IP override from a key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.remove_ip_override](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_remove_ip_override)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.reorder_firewall_policies
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.reorder_firewall_policies](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_reorder_firewall_policies)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.retrieve_legacy_secret_key
    
    
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

Returns the secret key related to the specified public key.

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.retrieve_legacy_secret_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_retrieve_legacy_secret_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.search_related_account_group_memberships
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.search_related_account_group_memberships](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_search_related_account_group_memberships)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.update_firewall_policy
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.update_firewall_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_update_firewall_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.update_key
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.update_key](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_update_key)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.update_policy
    
    
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient.update_policy](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.RecaptchaEnterpriseServiceClient#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_RecaptchaEnterpriseServiceClient_update_policy)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesAsyncPager
    
    
    ListFirewallPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListFirewallPoliciesResponse
            ],
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListFirewallPoliciesRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListFirewallPoliciesResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesAsyncPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListFirewallPoliciesAsyncPager_ListFirewallPoliciesAsyncPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesPager
    
    
    ListFirewallPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListFirewallPoliciesResponse,
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListFirewallPoliciesRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListFirewallPoliciesResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListFirewallPoliciesPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListFirewallPoliciesPager_ListFirewallPoliciesPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesAsyncPager
    
    
    ListIpOverridesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListIpOverridesResponse
            ],
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListIpOverridesRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListIpOverridesResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesAsyncPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesAsyncPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListIpOverridesAsyncPager_ListIpOverridesAsyncPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesPager
    
    
    ListIpOverridesPager(
        method: typing.Callable[
            [...],
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListIpOverridesResponse,
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListIpOverridesRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListIpOverridesResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListIpOverridesPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListIpOverridesPager_ListIpOverridesPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysAsyncPager
    
    
    ListKeysAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListKeysResponse
            ],
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListKeysRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListKeysResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysAsyncPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysAsyncPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListKeysAsyncPager_ListKeysAsyncPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysPager
    
    
    ListKeysPager(
        method: typing.Callable[
            [...],
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListKeysResponse,
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListKeysRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListKeysResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListKeysPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListKeysPager_ListKeysPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsAsyncPager
    
    
    ListRelatedAccountGroupMembershipsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse
            ],
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsAsyncPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsAsyncPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListRelatedAccountGroupMembershipsAsyncPager_ListRelatedAccountGroupMembershipsAsyncPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsPager
    
    
    ListRelatedAccountGroupMembershipsPager(
        method: typing.Callable[
            [...],
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse,
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupMembershipsRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupMembershipsResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupMembershipsPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListRelatedAccountGroupMembershipsPager_ListRelatedAccountGroupMembershipsPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsAsyncPager
    
    
    ListRelatedAccountGroupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupsResponse
            ],
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupsRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupsResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsAsyncPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsAsyncPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListRelatedAccountGroupsAsyncPager_ListRelatedAccountGroupsAsyncPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsPager
    
    
    ListRelatedAccountGroupsPager(
        method: typing.Callable[
            [...],
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupsResponse,
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupsRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.ListRelatedAccountGroupsResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.ListRelatedAccountGroupsPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_ListRelatedAccountGroupsPager_ListRelatedAccountGroupsPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsAsyncPager
    
    
    SearchRelatedAccountGroupMembershipsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse
            ],
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsAsyncPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsAsyncPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_SearchRelatedAccountGroupMembershipsAsyncPager_SearchRelatedAccountGroupMembershipsAsyncPager)

### google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsPager
    
    
    SearchRelatedAccountGroupMembershipsPager(
        method: typing.Callable[
            [...],
            google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse,
        ],
        request: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.SearchRelatedAccountGroupMembershipsRequest,
        response: google.cloud.recaptchaenterprise_v1.types.recaptchaenterprise.SearchRelatedAccountGroupMembershipsResponse,
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

See more: [google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsPager](https://cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.services.recaptcha_enterprise_service.pagers.SearchRelatedAccountGroupMembershipsPager#google_cloud_recaptchaenterprise_v1_services_recaptcha_enterprise_service_pagers_SearchRelatedAccountGroupMembershipsPager_SearchRelatedAccountGroupMembershipsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
