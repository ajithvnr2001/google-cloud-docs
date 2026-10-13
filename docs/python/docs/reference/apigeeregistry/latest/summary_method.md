---
url: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/summary_method/
title: Package Methods (0.10.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:03.005156+00:00
---

# Package Methods (0.10.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.0  0.8.0  0.7.0  0.6.18  0.5.1  0.4.0  0.3.2  0.2.1  0.1.2 

Summary of entries of Methods for apigeeregistry.

## 

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient
    
    
    ProvisioningAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apigee_registry_v1.services.provisioning.transports.base.ProvisioningTransport,
                typing.Callable[
                    [...],
                    google.cloud.apigee_registry_v1.services.provisioning.transports.base.ProvisioningTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the provisioning async client.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_ProvisioningAsyncClient)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
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
    ) -> None

Starts asynchronous cancellation on a long-running operation.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_cancel_operation)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_common_billing_account_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_common_folder_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_common_location_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_common_organization_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_common_project_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.provisioning_service.CreateInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance: typing.Optional[
            google.cloud.apigee_registry_v1.types.provisioning_service.Instance
        ] = None,
        instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Provisions instance resources for the Registry.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.create_instance](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_create_instance)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.provisioning_service.DeleteInstanceRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Deletes the Registry instance.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.delete_instance](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_delete_instance)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
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
    ) -> None

Deletes a long-running operation.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_delete_operation)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_from_service_account_file)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_from_service_account_info)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_from_service_account_json)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_get_iam_policy)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.provisioning_service.GetInstanceRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.provisioning_service.Instance

Gets details of a single Instance.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_instance](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_get_instance)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_location
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_location](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_get_location)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_operation
    
    
    get_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.GetOperationRequest, dict]
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
    ) -> google.longrunning.operations_pb2.Operation

Gets the latest state of a long-running operation.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_get_operation)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apigee_registry_v1.services.provisioning.transports.base.ProvisioningTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_get_transport_class)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.instance_path
    
    
    instance_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_instance_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.list_locations
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_list_locations)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.list_operations
    
    
    list_operations(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.ListOperationsRequest, dict]
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
    ) -> google.longrunning.operations_pb2.ListOperationsResponse

Lists operations that match the specified filter in the request.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_list_operations)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_parse_common_billing_account_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_parse_common_folder_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_parse_common_location_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_parse_common_organization_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_parse_common_project_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_parse_instance_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_set_iam_policy)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningAsyncClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningAsyncClient_test_iam_permissions)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient
    
    
    ProvisioningClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apigee_registry_v1.services.provisioning.transports.base.ProvisioningTransport,
                typing.Callable[
                    [...],
                    google.cloud.apigee_registry_v1.services.provisioning.transports.base.ProvisioningTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the provisioning client.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_ProvisioningClient)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.**exit**](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient___exit__)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.cancel_operation
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.cancel_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_cancel_operation)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_common_billing_account_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_folder_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_common_folder_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_location_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_common_location_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_organization_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_common_organization_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.common_project_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_common_project_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.provisioning_service.CreateInstanceRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance: typing.Optional[
            google.cloud.apigee_registry_v1.types.provisioning_service.Instance
        ] = None,
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

Provisions instance resources for the Registry.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.create_instance](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_create_instance)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.provisioning_service.DeleteInstanceRequest,
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
    ) -> google.api_core.operation.Operation

Deletes the Registry instance.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.delete_instance](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_delete_instance)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.delete_operation
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.delete_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_delete_operation)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.from_service_account_file](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_from_service_account_file)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.from_service_account_info](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_from_service_account_info)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.from_service_account_json](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_from_service_account_json)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_iam_policy
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_iam_policy](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_get_iam_policy)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.provisioning_service.GetInstanceRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.provisioning_service.Instance

Gets details of a single Instance.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_instance](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_get_instance)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_location
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_location](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_get_location)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_operation
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.get_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_get_operation)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.instance_path
    
    
    instance_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.instance_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_instance_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.list_locations
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.list_locations](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_list_locations)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.list_operations
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.list_operations](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_list_operations)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_parse_common_billing_account_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_parse_common_folder_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_parse_common_location_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_parse_common_organization_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_parse_common_project_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.parse_instance_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_parse_instance_path)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.set_iam_policy
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.set_iam_policy](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_set_iam_policy)

### google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.test_iam_permissions
    
    
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

See more: [google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.provisioning.ProvisioningClient#google_cloud_apigee_registry_v1_services_provisioning_ProvisioningClient_test_iam_permissions)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient
    
    
    RegistryAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport,
                typing.Callable[
                    [...],
                    google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the registry async client.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_RegistryAsyncClient)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.api_deployment_path
    
    
    api_deployment_path(project: str, location: str, api: str, deployment: str) -> str

Returns a fully-qualified api_deployment string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.api_deployment_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_api_deployment_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.api_path
    
    
    api_path(project: str, location: str, api: str) -> str

Returns a fully-qualified api string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.api_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_api_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.api_spec_path
    
    
    api_spec_path(
        project: str, location: str, api: str, version: str, spec: str
    ) -> str

Returns a fully-qualified api_spec string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.api_spec_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_api_spec_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.api_version_path
    
    
    api_version_path(project: str, location: str, api: str, version: str) -> str

Returns a fully-qualified api_version string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.api_version_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_api_version_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.artifact_path
    
    
    artifact_path(project: str, location: str, artifact: str) -> str

Returns a fully-qualified artifact string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.artifact_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_artifact_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
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
    ) -> None

Starts asynchronous cancellation on a long-running operation.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_cancel_operation)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_common_billing_account_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_common_folder_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_common_location_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_common_organization_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_common_project_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_api
    
    
    create_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Api
        ] = None,
        api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Creates a specified API.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_api](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_api)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_api_deployment
    
    
    create_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_deployment: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment
        ] = None,
        api_deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Creates a specified deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_api_spec
    
    
    create_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiSpecRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_spec: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiSpec
        ] = None,
        api_spec_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Creates a specified spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_api_version
    
    
    create_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiVersionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_version: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiVersion
        ] = None,
        api_version_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Creates a specified version.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_api_version](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_api_version)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_artifact
    
    
    create_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateArtifactRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        artifact: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Artifact
        ] = None,
        artifact_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Creates a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.create_artifact](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_create_artifact)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api
    
    
    delete_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiRequest,
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

Removes a specified API and all of the resources that it owns.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_deployment
    
    
    delete_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiDeploymentRequest,
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

Removes a specified deployment, all revisions, and all child resources (e.g., artifacts).

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_deployment_revision
    
    
    delete_api_deployment_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiDeploymentRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Deletes a revision of a deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_deployment_revision](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_deployment_revision)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_spec
    
    
    delete_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiSpecRequest,
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

Removes a specified spec, all revisions, and all child resources (e.g., artifacts).

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_spec_revision
    
    
    delete_api_spec_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiSpecRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Deletes a revision of a spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_spec_revision](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_spec_revision)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_version
    
    
    delete_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiVersionRequest,
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

Removes a specified version and all of the resources that it owns.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_api_version](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_api_version)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_artifact
    
    
    delete_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteArtifactRequest,
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

Removes a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_artifact](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_artifact)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
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
    ) -> None

Deletes a long-running operation.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_delete_operation)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_from_service_account_file)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_from_service_account_info)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_from_service_account_json)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api
    
    
    get_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiRequest, dict
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Returns a specified API.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api_deployment
    
    
    get_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiDeploymentRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Returns a specified deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api_spec
    
    
    get_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiSpecRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Returns a specified spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api_spec_contents
    
    
    get_api_spec_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiSpecContentsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Returns the contents of a specified spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api_spec_contents](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api_spec_contents)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api_version
    
    
    get_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiVersionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Returns a specified version.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_api_version](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_api_version)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_artifact
    
    
    get_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetArtifactRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Returns a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_artifact](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_artifact)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_artifact_contents
    
    
    get_artifact_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetArtifactContentsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Returns the contents of a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_artifact_contents](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_artifact_contents)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_iam_policy)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_location
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_location](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_location)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_operation
    
    
    get_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.GetOperationRequest, dict]
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
    ) -> google.longrunning.operations_pb2.Operation

Gets the latest state of a long-running operation.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_operation)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_get_transport_class)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_deployment_revisions
    
    
    list_api_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsRequest,
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
    ) -> (
        google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsAsyncPager
    )

Lists all revisions of a deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_deployment_revisions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_deployment_revisions)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_deployments
    
    
    list_api_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsRequest,
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
        google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsAsyncPager
    )

Returns matching deployments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_deployments](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_deployments)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_spec_revisions
    
    
    list_api_spec_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsRequest,
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
    ) -> (
        google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsAsyncPager
    )

Lists all revisions of a spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_spec_revisions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_spec_revisions)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_specs
    
    
    list_api_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsAsyncPager

Returns matching specs.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_specs](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_specs)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_versions
    
    
    list_api_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsAsyncPager

Returns matching versions.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_api_versions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_api_versions)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_apis
    
    
    list_apis(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApisRequest, dict
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApisAsyncPager

Returns matching APIs.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_apis](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_apis)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_artifacts
    
    
    list_artifacts(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsAsyncPager

Returns matching artifacts.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_artifacts](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_artifacts)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_locations
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_locations)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_operations
    
    
    list_operations(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.ListOperationsRequest, dict]
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
    ) -> google.longrunning.operations_pb2.ListOperationsResponse

Lists operations that match the specified filter in the request.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_list_operations)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_api_deployment_path
    
    
    parse_api_deployment_path(path: str) -> typing.Dict[str, str]

Parses a api_deployment path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_api_deployment_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_api_deployment_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_api_path
    
    
    parse_api_path(path: str) -> typing.Dict[str, str]

Parses a api path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_api_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_api_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_api_spec_path
    
    
    parse_api_spec_path(path: str) -> typing.Dict[str, str]

Parses a api_spec path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_api_spec_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_api_spec_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_api_version_path
    
    
    parse_api_version_path(path: str) -> typing.Dict[str, str]

Parses a api_version path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_api_version_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_api_version_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_artifact_path
    
    
    parse_artifact_path(path: str) -> typing.Dict[str, str]

Parses a artifact path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_artifact_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_artifact_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_common_billing_account_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_common_folder_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_common_location_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_common_organization_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_parse_common_project_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.replace_artifact
    
    
    replace_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ReplaceArtifactRequest,
                dict,
            ]
        ] = None,
        *,
        artifact: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Artifact
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Used to replace a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.replace_artifact](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_replace_artifact)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.rollback_api_deployment
    
    
    rollback_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.RollbackApiDeploymentRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Sets the current revision to a specified prior revision.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.rollback_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_rollback_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.rollback_api_spec
    
    
    rollback_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.RollbackApiSpecRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Sets the current revision to a specified prior revision.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.rollback_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_rollback_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_set_iam_policy)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.tag_api_deployment_revision
    
    
    tag_api_deployment_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.TagApiDeploymentRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Adds a tag to a specified revision of a deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.tag_api_deployment_revision](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_tag_api_deployment_revision)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.tag_api_spec_revision
    
    
    tag_api_spec_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.TagApiSpecRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Adds a tag to a specified revision of a spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.tag_api_spec_revision](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_tag_api_spec_revision)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_test_iam_permissions)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.update_api
    
    
    update_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiRequest,
                dict,
            ]
        ] = None,
        *,
        api: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Api
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Used to modify a specified API.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.update_api](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_update_api)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.update_api_deployment
    
    
    update_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        api_deployment: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Used to modify a specified deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.update_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_update_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.update_api_spec
    
    
    update_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiSpecRequest,
                dict,
            ]
        ] = None,
        *,
        api_spec: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiSpec
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Used to modify a specified spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.update_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_update_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.update_api_version
    
    
    update_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiVersionRequest,
                dict,
            ]
        ] = None,
        *,
        api_version: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiVersion
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Used to modify a specified version.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient.update_api_version](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryAsyncClient#google_cloud_apigee_registry_v1_services_registry_RegistryAsyncClient_update_api_version)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient
    
    
    RegistryClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport,
                typing.Callable[
                    [...],
                    google.cloud.apigee_registry_v1.services.registry.transports.base.RegistryTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the registry client.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_RegistryClient)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.**exit**](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient___exit__)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.api_deployment_path
    
    
    api_deployment_path(project: str, location: str, api: str, deployment: str) -> str

Returns a fully-qualified api_deployment string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.api_deployment_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_api_deployment_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.api_path
    
    
    api_path(project: str, location: str, api: str) -> str

Returns a fully-qualified api string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.api_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_api_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.api_spec_path
    
    
    api_spec_path(
        project: str, location: str, api: str, version: str, spec: str
    ) -> str

Returns a fully-qualified api_spec string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.api_spec_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_api_spec_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.api_version_path
    
    
    api_version_path(project: str, location: str, api: str, version: str) -> str

Returns a fully-qualified api_version string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.api_version_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_api_version_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.artifact_path
    
    
    artifact_path(project: str, location: str, artifact: str) -> str

Returns a fully-qualified artifact string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.artifact_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_artifact_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.cancel_operation
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.cancel_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_cancel_operation)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_common_billing_account_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_folder_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_common_folder_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_location_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_common_location_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_organization_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_common_organization_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.common_project_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_common_project_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_api
    
    
    create_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Api
        ] = None,
        api_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Creates a specified API.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_api](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_create_api)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_api_deployment
    
    
    create_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_deployment: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment
        ] = None,
        api_deployment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Creates a specified deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_create_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_api_spec
    
    
    create_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiSpecRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_spec: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiSpec
        ] = None,
        api_spec_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Creates a specified spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_create_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_api_version
    
    
    create_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateApiVersionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        api_version: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiVersion
        ] = None,
        api_version_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Creates a specified version.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_api_version](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_create_api_version)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_artifact
    
    
    create_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.CreateArtifactRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        artifact: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Artifact
        ] = None,
        artifact_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Creates a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.create_artifact](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_create_artifact)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api
    
    
    delete_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiRequest,
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

Removes a specified API and all of the resources that it owns.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_delete_api)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_deployment
    
    
    delete_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiDeploymentRequest,
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

Removes a specified deployment, all revisions, and all child resources (e.g., artifacts).

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_delete_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_deployment_revision
    
    
    delete_api_deployment_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiDeploymentRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Deletes a revision of a deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_deployment_revision](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_delete_api_deployment_revision)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_spec
    
    
    delete_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiSpecRequest,
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

Removes a specified spec, all revisions, and all child resources (e.g., artifacts).

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_delete_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_spec_revision
    
    
    delete_api_spec_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiSpecRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Deletes a revision of a spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_spec_revision](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_delete_api_spec_revision)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_version
    
    
    delete_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteApiVersionRequest,
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

Removes a specified version and all of the resources that it owns.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_api_version](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_delete_api_version)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_artifact
    
    
    delete_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.DeleteArtifactRequest,
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

Removes a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_artifact](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_delete_artifact)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_operation
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.delete_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_delete_operation)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.from_service_account_file](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_from_service_account_file)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.from_service_account_info](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_from_service_account_info)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.from_service_account_json](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_from_service_account_json)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api
    
    
    get_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiRequest, dict
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Returns a specified API.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_api)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api_deployment
    
    
    get_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiDeploymentRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Returns a specified deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api_spec
    
    
    get_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiSpecRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Returns a specified spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api_spec_contents
    
    
    get_api_spec_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiSpecContentsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Returns the contents of a specified spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api_spec_contents](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_api_spec_contents)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api_version
    
    
    get_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetApiVersionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Returns a specified version.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_api_version](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_api_version)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_artifact
    
    
    get_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetArtifactRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Returns a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_artifact](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_artifact)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_artifact_contents
    
    
    get_artifact_contents(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.GetArtifactContentsRequest,
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
    ) -> google.api.httpbody_pb2.HttpBody

Returns the contents of a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_artifact_contents](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_artifact_contents)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_iam_policy
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_iam_policy](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_iam_policy)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_location
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_location](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_location)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_mtls_endpoint_and_cert_source)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_operation
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.get_operation](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_get_operation)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_deployment_revisions
    
    
    list_api_deployment_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsRequest,
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
        google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsPager
    )

Lists all revisions of a deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_deployment_revisions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_api_deployment_revisions)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_deployments
    
    
    list_api_deployments(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsPager

Returns matching deployments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_deployments](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_api_deployments)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_spec_revisions
    
    
    list_api_spec_revisions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsPager

Lists all revisions of a spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_spec_revisions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_api_spec_revisions)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_specs
    
    
    list_api_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsPager

Returns matching specs.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_specs](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_api_specs)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_versions
    
    
    list_api_versions(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsPager

Returns matching versions.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_api_versions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_api_versions)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_apis
    
    
    list_apis(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListApisRequest, dict
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListApisPager

Returns matching APIs.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_apis](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_apis)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_artifacts
    
    
    list_artifacts(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsRequest,
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
    ) -> google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsPager

Returns matching artifacts.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_artifacts](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_artifacts)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_locations
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_locations](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_locations)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_operations
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.list_operations](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_list_operations)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_api_deployment_path
    
    
    parse_api_deployment_path(path: str) -> typing.Dict[str, str]

Parses a api_deployment path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_api_deployment_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_api_deployment_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_api_path
    
    
    parse_api_path(path: str) -> typing.Dict[str, str]

Parses a api path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_api_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_api_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_api_spec_path
    
    
    parse_api_spec_path(path: str) -> typing.Dict[str, str]

Parses a api_spec path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_api_spec_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_api_spec_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_api_version_path
    
    
    parse_api_version_path(path: str) -> typing.Dict[str, str]

Parses a api_version path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_api_version_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_api_version_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_artifact_path
    
    
    parse_artifact_path(path: str) -> typing.Dict[str, str]

Parses a artifact path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_artifact_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_artifact_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_common_billing_account_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_common_folder_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_common_location_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_common_organization_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_parse_common_project_path)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.replace_artifact
    
    
    replace_artifact(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.ReplaceArtifactRequest,
                dict,
            ]
        ] = None,
        *,
        artifact: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Artifact
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Artifact

Used to replace a specified artifact.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.replace_artifact](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_replace_artifact)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.rollback_api_deployment
    
    
    rollback_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.RollbackApiDeploymentRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Sets the current revision to a specified prior revision.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.rollback_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_rollback_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.rollback_api_spec
    
    
    rollback_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.RollbackApiSpecRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Sets the current revision to a specified prior revision.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.rollback_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_rollback_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.set_iam_policy
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.set_iam_policy](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_set_iam_policy)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.tag_api_deployment_revision
    
    
    tag_api_deployment_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.TagApiDeploymentRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Adds a tag to a specified revision of a deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.tag_api_deployment_revision](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_tag_api_deployment_revision)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.tag_api_spec_revision
    
    
    tag_api_spec_revision(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.TagApiSpecRevisionRequest,
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Adds a tag to a specified revision of a spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.tag_api_spec_revision](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_tag_api_spec_revision)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.test_iam_permissions
    
    
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

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_test_iam_permissions)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.update_api
    
    
    update_api(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiRequest,
                dict,
            ]
        ] = None,
        *,
        api: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.Api
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.Api

Used to modify a specified API.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.update_api](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_update_api)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.update_api_deployment
    
    
    update_api_deployment(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiDeploymentRequest,
                dict,
            ]
        ] = None,
        *,
        api_deployment: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiDeployment

Used to modify a specified deployment.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.update_api_deployment](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_update_api_deployment)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.update_api_spec
    
    
    update_api_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiSpecRequest,
                dict,
            ]
        ] = None,
        *,
        api_spec: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiSpec
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiSpec

Used to modify a specified spec.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.update_api_spec](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_update_api_spec)

### google.cloud.apigee_registry_v1.services.registry.RegistryClient.update_api_version
    
    
    update_api_version(
        request: typing.Optional[
            typing.Union[
                google.cloud.apigee_registry_v1.types.registry_service.UpdateApiVersionRequest,
                dict,
            ]
        ] = None,
        *,
        api_version: typing.Optional[
            google.cloud.apigee_registry_v1.types.registry_models.ApiVersion
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
    ) -> google.cloud.apigee_registry_v1.types.registry_models.ApiVersion

Used to modify a specified version.

See more: [google.cloud.apigee_registry_v1.services.registry.RegistryClient.update_api_version](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.RegistryClient#google_cloud_apigee_registry_v1_services_registry_RegistryClient_update_api_version)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsAsyncPager
    
    
    ListApiDeploymentRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsAsyncPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiDeploymentRevisionsAsyncPager_ListApiDeploymentRevisionsAsyncPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsPager
    
    
    ListApiDeploymentRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiDeploymentRevisionsPager_ListApiDeploymentRevisionsPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsAsyncPager
    
    
    ListApiDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsAsyncPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsAsyncPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiDeploymentsAsyncPager_ListApiDeploymentsAsyncPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsPager
    
    
    ListApiDeploymentsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiDeploymentsPager_ListApiDeploymentsPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsAsyncPager
    
    
    ListApiSpecRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsAsyncPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsAsyncPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiSpecRevisionsAsyncPager_ListApiSpecRevisionsAsyncPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsPager
    
    
    ListApiSpecRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiSpecRevisionsPager_ListApiSpecRevisionsPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsAsyncPager
    
    
    ListApiSpecsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsAsyncPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsAsyncPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiSpecsAsyncPager_ListApiSpecsAsyncPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsPager
    
    
    ListApiSpecsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiSpecsPager_ListApiSpecsPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsAsyncPager
    
    
    ListApiVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsAsyncPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsAsyncPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiVersionsAsyncPager_ListApiVersionsAsyncPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsPager
    
    
    ListApiVersionsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApiVersionsPager_ListApiVersionsPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApisAsyncPager
    
    
    ListApisAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApisResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApisRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApisResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApisAsyncPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApisAsyncPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApisAsyncPager_ListApisAsyncPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListApisPager
    
    
    ListApisPager(
        method: typing.Callable[
            [...], google.cloud.apigee_registry_v1.types.registry_service.ListApisResponse
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApisRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApisResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListApisPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApisPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListApisPager_ListApisPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsAsyncPager
    
    
    ListArtifactsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsAsyncPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsAsyncPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListArtifactsAsyncPager_ListArtifactsAsyncPager)

### google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsPager
    
    
    ListArtifactsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsResponse,
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

See more: [google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsPager](https://cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsPager#google_cloud_apigee_registry_v1_services_registry_pagers_ListArtifactsPager_ListArtifactsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
