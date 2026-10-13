---
url: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/summary_method/
title: Package Methods (0.10.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:27.461173+00:00
---

# Package Methods (0.10.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.10.0  0.9.0  0.8.0  0.7.0  0.6.16  0.5.3  0.4.0  0.3.2  0.2.0  0.1.1 

Summary of entries of Methods for bigquerydatapolicy.

## 

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient
    
    
    DataPolicyServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_datapolicies_v1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_datapolicies_v1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data policy service async client.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_DataPolicyServiceAsyncClient)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_common_folder_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_common_location_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_common_organization_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_common_project_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.create_data_policy
    
    
    create_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.CreateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy

Creates a new data policy under a project with the given `dataPolicyId` (used as the display name), policy tag, and data policy type.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.create_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_create_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.data_policy_path
    
    
    data_policy_path(project: str, location: str, data_policy: str) -> str

Returns a fully-qualified data_policy string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_data_policy_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.delete_data_policy
    
    
    delete_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.DeleteDataPolicyRequest,
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

Deletes the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.delete_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_delete_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_file)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_info)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_json)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.get_data_policy
    
    
    get_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.GetDataPolicyRequest,
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
    ) -> google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy

Gets the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.get_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_get_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.get_iam_policy
    
    
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

Gets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_get_iam_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.bigquery_datapolicies_v1.services.data_policy_service.transports.base.DataPolicyServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_get_transport_class)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.list_data_policies
    
    
    list_data_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.ListDataPoliciesRequest,
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
        google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager
    )

List all of the data policies in the specified parent project.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.list_data_policies](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_list_data_policies)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_folder_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_location_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_organization_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_project_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_data_policy_path
    
    
    parse_data_policy_path(path: str) -> typing.Dict[str, str]

Parses a data_policy path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_data_policy_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.rename_data_policy
    
    
    rename_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.RenameDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        new_data_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy

Renames the id (display name) of the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.rename_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_rename_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.set_iam_policy
    
    
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

Sets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_set_iam_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.test_iam_permissions
    
    
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

Returns the caller's permission on the specified data policy resource.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_test_iam_permissions)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.update_data_policy
    
    
    update_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.UpdateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy
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
    ) -> google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy

Updates the metadata for an existing data policy.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient.update_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceAsyncClient_update_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient
    
    
    DataPolicyServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_datapolicies_v1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_datapolicies_v1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data policy service client.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_DataPolicyServiceClient)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.**exit**](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient___exit__)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_common_folder_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_common_location_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_common_organization_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_common_project_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.create_data_policy
    
    
    create_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.CreateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy

Creates a new data policy under a project with the given `dataPolicyId` (used as the display name), policy tag, and data policy type.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.create_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_create_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.data_policy_path
    
    
    data_policy_path(project: str, location: str, data_policy: str) -> str

Returns a fully-qualified data_policy string.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_data_policy_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.delete_data_policy
    
    
    delete_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.DeleteDataPolicyRequest,
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

Deletes the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.delete_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_delete_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_from_service_account_file)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_from_service_account_info)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_from_service_account_json)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.get_data_policy
    
    
    get_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.GetDataPolicyRequest,
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
    ) -> google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy

Gets the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.get_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_get_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.get_iam_policy
    
    
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

Gets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_get_iam_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.list_data_policies
    
    
    list_data_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.ListDataPoliciesRequest,
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
        google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesPager
    )

List all of the data policies in the specified parent project.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.list_data_policies](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_list_data_policies)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_parse_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_parse_common_folder_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_parse_common_location_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_parse_common_organization_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_parse_common_project_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_data_policy_path
    
    
    parse_data_policy_path(path: str) -> typing.Dict[str, str]

Parses a data_policy path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.parse_data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_parse_data_policy_path)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.rename_data_policy
    
    
    rename_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.RenameDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        new_data_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy

Renames the id (display name) of the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.rename_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_rename_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.set_iam_policy
    
    
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

Sets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_set_iam_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.test_iam_permissions
    
    
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

Returns the caller's permission on the specified data policy resource.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_test_iam_permissions)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.update_data_policy
    
    
    update_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.UpdateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy
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
    ) -> google.cloud.bigquery_datapolicies_v1.types.datapolicy.DataPolicy

Updates the metadata for an existing data policy.

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient.update_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_DataPolicyServiceClient_update_data_policy)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager
    
    
    ListDataPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.bigquery_datapolicies_v1.types.datapolicy.ListDataPoliciesResponse
            ],
        ],
        request: google.cloud.bigquery_datapolicies_v1.types.datapolicy.ListDataPoliciesRequest,
        response: google.cloud.bigquery_datapolicies_v1.types.datapolicy.ListDataPoliciesResponse,
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

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_pagers_ListDataPoliciesAsyncPager_ListDataPoliciesAsyncPager)

### google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesPager
    
    
    ListDataPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.bigquery_datapolicies_v1.types.datapolicy.ListDataPoliciesResponse,
        ],
        request: google.cloud.bigquery_datapolicies_v1.types.datapolicy.ListDataPoliciesRequest,
        response: google.cloud.bigquery_datapolicies_v1.types.datapolicy.ListDataPoliciesResponse,
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

See more: [google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesPager](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1.services.data_policy_service.pagers.ListDataPoliciesPager#google_cloud_bigquery_datapolicies_v1_services_data_policy_service_pagers_ListDataPoliciesPager_ListDataPoliciesPager)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient
    
    
    DataPolicyServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data policy service async client.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_DataPolicyServiceAsyncClient)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_folder_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_location_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_organization_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_project_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.create_data_policy
    
    
    create_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.CreateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy

Creates a new data policy under a project with the given `dataPolicyId` (used as the display name), policy tag, and data policy type.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.create_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_create_data_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.data_policy_path
    
    
    data_policy_path(project: str, location: str, data_policy: str) -> str

Returns a fully-qualified data_policy string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_data_policy_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.delete_data_policy
    
    
    delete_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DeleteDataPolicyRequest,
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

Deletes the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.delete_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_delete_data_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_file)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_info)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_json)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_data_policy
    
    
    get_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.GetDataPolicyRequest,
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
    ) -> google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy

Gets the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_get_data_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_iam_policy
    
    
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

Gets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_get_iam_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_get_transport_class)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.list_data_policies
    
    
    list_data_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.ListDataPoliciesRequest,
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
        google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager
    )

List all of the data policies in the specified parent project.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.list_data_policies](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_list_data_policies)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_folder_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_location_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_organization_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_project_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_data_policy_path
    
    
    parse_data_policy_path(path: str) -> typing.Dict[str, str]

Parses a data_policy path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_data_policy_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.set_iam_policy
    
    
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

Sets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_set_iam_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.test_iam_permissions
    
    
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

Returns the caller's permission on the specified data policy resource.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_test_iam_permissions)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.update_data_policy
    
    
    update_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.UpdateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy
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
    ) -> google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy

Updates the metadata for an existing data policy.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient.update_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceAsyncClient_update_data_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient
    
    
    DataPolicyServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data policy service client.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_DataPolicyServiceClient)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.**exit**](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient___exit__)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_common_folder_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_common_location_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_common_organization_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_common_project_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.create_data_policy
    
    
    create_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.CreateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy

Creates a new data policy under a project with the given `dataPolicyId` (used as the display name), policy tag, and data policy type.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.create_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_create_data_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.data_policy_path
    
    
    data_policy_path(project: str, location: str, data_policy: str) -> str

Returns a fully-qualified data_policy string.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_data_policy_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.delete_data_policy
    
    
    delete_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DeleteDataPolicyRequest,
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

Deletes the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.delete_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_delete_data_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_from_service_account_file)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_from_service_account_info)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_from_service_account_json)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.get_data_policy
    
    
    get_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.GetDataPolicyRequest,
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
    ) -> google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy

Gets the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.get_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_get_data_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.get_iam_policy
    
    
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

Gets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_get_iam_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.list_data_policies
    
    
    list_data_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.ListDataPoliciesRequest,
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
        google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesPager
    )

List all of the data policies in the specified parent project.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.list_data_policies](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_list_data_policies)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_folder_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_location_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_organization_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_project_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_data_policy_path
    
    
    parse_data_policy_path(path: str) -> typing.Dict[str, str]

Parses a data_policy path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.parse_data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_parse_data_policy_path)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.set_iam_policy
    
    
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

Sets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_set_iam_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.test_iam_permissions
    
    
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

Returns the caller's permission on the specified data policy resource.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_test_iam_permissions)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.update_data_policy
    
    
    update_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.UpdateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy
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
    ) -> google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.DataPolicy

Updates the metadata for an existing data policy.

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient.update_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_DataPolicyServiceClient_update_data_policy)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager
    
    
    ListDataPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.ListDataPoliciesResponse
            ],
        ],
        request: google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.ListDataPoliciesRequest,
        response: google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.ListDataPoliciesResponse,
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

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_pagers_ListDataPoliciesAsyncPager_ListDataPoliciesAsyncPager)

### google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesPager
    
    
    ListDataPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.ListDataPoliciesResponse,
        ],
        request: google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.ListDataPoliciesRequest,
        response: google.cloud.bigquery_datapolicies_v1beta1.types.datapolicy.ListDataPoliciesResponse,
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

See more: [google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesPager](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v1beta1.services.data_policy_service.pagers.ListDataPoliciesPager#google_cloud_bigquery_datapolicies_v1beta1_services_data_policy_service_pagers_ListDataPoliciesPager_ListDataPoliciesPager)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient
    
    
    DataPolicyServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_datapolicies_v2.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_datapolicies_v2.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data policy service async client.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_DataPolicyServiceAsyncClient)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.add_grantees
    
    
    add_grantees(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.AddGranteesRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[str] = None,
        grantees: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Adds new grantees to a data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.add_grantees](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_add_grantees)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_common_folder_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_common_location_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_common_organization_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_common_project_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.create_data_policy
    
    
    create_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.CreateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy
        ] = None,
        data_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Creates a new data policy under a project with the given `data_policy_id` (used as the display name), and data policy type.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.create_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_create_data_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.data_policy_path
    
    
    data_policy_path(project: str, location: str, data_policy: str) -> str

Returns a fully-qualified data_policy string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_data_policy_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.delete_data_policy
    
    
    delete_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.DeleteDataPolicyRequest,
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

Deletes the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.delete_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_delete_data_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_file)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_info)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_json)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.get_data_policy
    
    
    get_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.GetDataPolicyRequest,
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
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Gets the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.get_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_get_data_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.get_iam_policy
    
    
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

Gets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_get_iam_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.bigquery_datapolicies_v2.services.data_policy_service.transports.base.DataPolicyServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_get_transport_class)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.list_data_policies
    
    
    list_data_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.ListDataPoliciesRequest,
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
        google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesAsyncPager
    )

List all of the data policies in the specified parent project.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.list_data_policies](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_list_data_policies)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_folder_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_location_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_organization_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_project_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_data_policy_path
    
    
    parse_data_policy_path(path: str) -> typing.Dict[str, str]

Parses a data_policy path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_parse_data_policy_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_policy_tag_path
    
    
    parse_policy_tag_path(path: str) -> typing.Dict[str, str]

Parses a policy_tag path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_policy_tag_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_parse_policy_tag_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_routine_path
    
    
    parse_routine_path(path: str) -> typing.Dict[str, str]

Parses a routine path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.parse_routine_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_parse_routine_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.policy_tag_path
    
    
    policy_tag_path(project: str, location: str, taxonomy: str, policy_tag: str) -> str

Returns a fully-qualified policy_tag string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.policy_tag_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_policy_tag_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.remove_grantees
    
    
    remove_grantees(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.RemoveGranteesRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[str] = None,
        grantees: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Removes grantees from a data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.remove_grantees](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_remove_grantees)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.routine_path
    
    
    routine_path(project: str, dataset: str, routine: str) -> str

Returns a fully-qualified routine string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.routine_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_routine_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.set_iam_policy
    
    
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

Sets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_set_iam_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.test_iam_permissions
    
    
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

Returns the caller's permission on the specified data policy resource.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_test_iam_permissions)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.update_data_policy
    
    
    update_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.UpdateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy
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
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Updates the metadata for an existing data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient.update_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceAsyncClient_update_data_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient
    
    
    DataPolicyServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_datapolicies_v2.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_datapolicies_v2.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data policy service client.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_DataPolicyServiceClient)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.**exit**](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient___exit__)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.add_grantees
    
    
    add_grantees(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.AddGranteesRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[str] = None,
        grantees: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Adds new grantees to a data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.add_grantees](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_add_grantees)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_common_folder_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_common_location_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_common_organization_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_common_project_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.create_data_policy
    
    
    create_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.CreateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy
        ] = None,
        data_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Creates a new data policy under a project with the given `data_policy_id` (used as the display name), and data policy type.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.create_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_create_data_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.data_policy_path
    
    
    data_policy_path(project: str, location: str, data_policy: str) -> str

Returns a fully-qualified data_policy string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_data_policy_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.delete_data_policy
    
    
    delete_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.DeleteDataPolicyRequest,
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

Deletes the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.delete_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_delete_data_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_from_service_account_file)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_from_service_account_info)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_from_service_account_json)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.get_data_policy
    
    
    get_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.GetDataPolicyRequest,
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
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Gets the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.get_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_get_data_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.get_iam_policy
    
    
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

Gets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_get_iam_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.list_data_policies
    
    
    list_data_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.ListDataPoliciesRequest,
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
        google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesPager
    )

List all of the data policies in the specified parent project.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.list_data_policies](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_list_data_policies)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_parse_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_parse_common_folder_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_parse_common_location_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_parse_common_organization_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_parse_common_project_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_data_policy_path
    
    
    parse_data_policy_path(path: str) -> typing.Dict[str, str]

Parses a data_policy path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_parse_data_policy_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_policy_tag_path
    
    
    parse_policy_tag_path(path: str) -> typing.Dict[str, str]

Parses a policy_tag path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_policy_tag_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_parse_policy_tag_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_routine_path
    
    
    parse_routine_path(path: str) -> typing.Dict[str, str]

Parses a routine path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.parse_routine_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_parse_routine_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.policy_tag_path
    
    
    policy_tag_path(project: str, location: str, taxonomy: str, policy_tag: str) -> str

Returns a fully-qualified policy_tag string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.policy_tag_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_policy_tag_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.remove_grantees
    
    
    remove_grantees(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.RemoveGranteesRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[str] = None,
        grantees: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Removes grantees from a data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.remove_grantees](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_remove_grantees)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.routine_path
    
    
    routine_path(project: str, dataset: str, routine: str) -> str

Returns a fully-qualified routine string.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.routine_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_routine_path)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.set_iam_policy
    
    
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

Sets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_set_iam_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.test_iam_permissions
    
    
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

Returns the caller's permission on the specified data policy resource.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_test_iam_permissions)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.update_data_policy
    
    
    update_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.UpdateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy
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
    ) -> google.cloud.bigquery_datapolicies_v2.types.datapolicy.DataPolicy

Updates the metadata for an existing data policy.

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient.update_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_DataPolicyServiceClient_update_data_policy)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesAsyncPager
    
    
    ListDataPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.bigquery_datapolicies_v2.types.datapolicy.ListDataPoliciesResponse
            ],
        ],
        request: google.cloud.bigquery_datapolicies_v2.types.datapolicy.ListDataPoliciesRequest,
        response: google.cloud.bigquery_datapolicies_v2.types.datapolicy.ListDataPoliciesResponse,
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

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesAsyncPager#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_pagers_ListDataPoliciesAsyncPager_ListDataPoliciesAsyncPager)

### google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesPager
    
    
    ListDataPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.bigquery_datapolicies_v2.types.datapolicy.ListDataPoliciesResponse,
        ],
        request: google.cloud.bigquery_datapolicies_v2.types.datapolicy.ListDataPoliciesRequest,
        response: google.cloud.bigquery_datapolicies_v2.types.datapolicy.ListDataPoliciesResponse,
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

See more: [google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesPager](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2.services.data_policy_service.pagers.ListDataPoliciesPager#google_cloud_bigquery_datapolicies_v2_services_data_policy_service_pagers_ListDataPoliciesPager_ListDataPoliciesPager)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient
    
    
    DataPolicyServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data policy service async client.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_DataPolicyServiceAsyncClient)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.add_grantees
    
    
    add_grantees(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.AddGranteesRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[str] = None,
        grantees: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Adds new grantees to a data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.add_grantees](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_add_grantees)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_folder_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_location_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_organization_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_common_project_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.create_data_policy
    
    
    create_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.CreateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy
        ] = None,
        data_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Creates a new data policy under a project with the given `data_policy_id` (used as the display name), and data policy type.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.create_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_create_data_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.data_policy_path
    
    
    data_policy_path(project: str, location: str, data_policy: str) -> str

Returns a fully-qualified data_policy string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_data_policy_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.delete_data_policy
    
    
    delete_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DeleteDataPolicyRequest,
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

Deletes the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.delete_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_delete_data_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_file)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_info)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_from_service_account_json)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_data_policy
    
    
    get_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.GetDataPolicyRequest,
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
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Gets the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_get_data_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_iam_policy
    
    
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

Gets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_get_iam_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_get_transport_class)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.list_data_policies
    
    
    list_data_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.ListDataPoliciesRequest,
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
        google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager
    )

List all of the data policies in the specified parent project.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.list_data_policies](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_list_data_policies)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_folder_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_location_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_organization_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_common_project_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_data_policy_path
    
    
    parse_data_policy_path(path: str) -> typing.Dict[str, str]

Parses a data_policy path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_data_policy_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_policy_tag_path
    
    
    parse_policy_tag_path(path: str) -> typing.Dict[str, str]

Parses a policy_tag path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.parse_policy_tag_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_parse_policy_tag_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.policy_tag_path
    
    
    policy_tag_path(project: str, location: str, taxonomy: str, policy_tag: str) -> str

Returns a fully-qualified policy_tag string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.policy_tag_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_policy_tag_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.remove_grantees
    
    
    remove_grantees(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.RemoveGranteesRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[str] = None,
        grantees: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Removes grantees from a data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.remove_grantees](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_remove_grantees)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.set_iam_policy
    
    
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

Sets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_set_iam_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.test_iam_permissions
    
    
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

Returns the caller's permission on the specified data policy resource.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_test_iam_permissions)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.update_data_policy
    
    
    update_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.UpdateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy
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
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Updates the metadata for an existing data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient.update_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceAsyncClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceAsyncClient_update_data_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient
    
    
    DataPolicyServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.transports.base.DataPolicyServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data policy service client.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_DataPolicyServiceClient)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.**exit**](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient___exit__)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.add_grantees
    
    
    add_grantees(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.AddGranteesRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[str] = None,
        grantees: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Adds new grantees to a data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.add_grantees](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_add_grantees)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_common_folder_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_common_location_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_common_organization_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_common_project_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.create_data_policy
    
    
    create_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.CreateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy
        ] = None,
        data_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Creates a new data policy under a project with the given `data_policy_id` (used as the display name), and data policy type.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.create_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_create_data_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.data_policy_path
    
    
    data_policy_path(project: str, location: str, data_policy: str) -> str

Returns a fully-qualified data_policy string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_data_policy_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.delete_data_policy
    
    
    delete_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DeleteDataPolicyRequest,
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

Deletes the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.delete_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_delete_data_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_from_service_account_file)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_from_service_account_info)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_from_service_account_json)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.get_data_policy
    
    
    get_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.GetDataPolicyRequest,
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
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Gets the data policy specified by its resource name.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.get_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_get_data_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.get_iam_policy
    
    
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

Gets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_get_iam_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.list_data_policies
    
    
    list_data_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.ListDataPoliciesRequest,
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
        google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesPager
    )

List all of the data policies in the specified parent project.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.list_data_policies](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_list_data_policies)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_billing_account_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_folder_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_location_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_organization_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_parse_common_project_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_data_policy_path
    
    
    parse_data_policy_path(path: str) -> typing.Dict[str, str]

Parses a data_policy path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_data_policy_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_parse_data_policy_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_policy_tag_path
    
    
    parse_policy_tag_path(path: str) -> typing.Dict[str, str]

Parses a policy_tag path into its component segments.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.parse_policy_tag_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_parse_policy_tag_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.policy_tag_path
    
    
    policy_tag_path(project: str, location: str, taxonomy: str, policy_tag: str) -> str

Returns a fully-qualified policy_tag string.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.policy_tag_path](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_policy_tag_path)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.remove_grantees
    
    
    remove_grantees(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.RemoveGranteesRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[str] = None,
        grantees: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Removes grantees from a data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.remove_grantees](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_remove_grantees)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.set_iam_policy
    
    
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

Sets the IAM policy for the specified data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_set_iam_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.test_iam_permissions
    
    
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

Returns the caller's permission on the specified data policy resource.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_test_iam_permissions)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.update_data_policy
    
    
    update_data_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.UpdateDataPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        data_policy: typing.Optional[
            google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy
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
    ) -> google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.DataPolicy

Updates the metadata for an existing data policy.

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient.update_data_policy](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.DataPolicyServiceClient#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_DataPolicyServiceClient_update_data_policy)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager
    
    
    ListDataPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.ListDataPoliciesResponse
            ],
        ],
        request: google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.ListDataPoliciesRequest,
        response: google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.ListDataPoliciesResponse,
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

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesAsyncPager#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_pagers_ListDataPoliciesAsyncPager_ListDataPoliciesAsyncPager)

### google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesPager
    
    
    ListDataPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.ListDataPoliciesResponse,
        ],
        request: google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.ListDataPoliciesRequest,
        response: google.cloud.bigquery_datapolicies_v2beta1.types.datapolicy.ListDataPoliciesResponse,
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

See more: [google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesPager](https://cloud.google.com/python/docs/reference/bigquerydatapolicy/latest/google.cloud.bigquery_datapolicies_v2beta1.services.data_policy_service.pagers.ListDataPoliciesPager#google_cloud_bigquery_datapolicies_v2beta1_services_data_policy_service_pagers_ListDataPoliciesPager_ListDataPoliciesPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
