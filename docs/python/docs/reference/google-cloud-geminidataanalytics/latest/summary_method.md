---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/summary_method/
title: Package Methods (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:43.342633+00:00
---

# Package Methods (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Summary of entries of Methods for google-cloud-geminidataanalytics.

## 

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient
    
    
    DataAgentServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1.services.data_agent_service.transports.base.DataAgentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1.services.data_agent_service.transports.base.DataAgentServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data agent service async client.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_DataAgentServiceAsyncClient)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_cancel_operation)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_common_folder_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_common_location_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_common_organization_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_common_project_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent
    
    
    create_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new DataAgent in a given project and location.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_create_data_agent)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent_sync
    
    
    create_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent

Creates a new DataAgent in a given project and location synchronously.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_create_data_agent_sync)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_data_agent_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent
    
    
    delete_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_delete_data_agent)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent_sync
    
    
    delete_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_delete_data_agent_sync)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_delete_operation)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_data_agent
    
    
    get_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.GetDataAgentRequest,
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
    ) -> google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent

Gets details of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_get_data_agent)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM policy for DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_get_iam_policy)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_get_location)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_get_operation)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.geminidataanalytics_v1.services.data_agent_service.transports.base.DataAgentServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_get_transport_class)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.list_accessible_data_agents
    
    
    list_accessible_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.ListAccessibleDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager
    )

Lists DataAgents that are accessible to the caller in a given project and location.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.list_accessible_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_list_accessible_data_agents)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.list_data_agents
    
    
    list_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.ListDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListDataAgentsAsyncPager
    )

Lists DataAgents in a given project and location.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.list_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_list_data_agents)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_list_locations)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_list_operations)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.retrieve_agent_ops_observability
    
    
    retrieve_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.RetrieveAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1.types.data_agent_service.RetrieveAgentOpsObservabilityResponse
    )

Gets AgentOps observability settings and status of required services.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.retrieve_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_retrieve_agent_ops_observability)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.set_agent_ops_observability
    
    
    set_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.SetAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        telemetry_enabled: typing.Optional[bool] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.set_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_set_agent_ops_observability)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM policy for a DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_set_iam_policy)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent
    
    
    update_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_update_data_agent)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent_sync
    
    
    update_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent
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
    ) -> google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent

Updates the parameters of a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceAsyncClient_update_data_agent_sync)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient
    
    
    DataAgentServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1.services.data_agent_service.transports.base.DataAgentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1.services.data_agent_service.transports.base.DataAgentServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data agent service client.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_DataAgentServiceClient)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient___exit__)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_cancel_operation)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_common_folder_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_common_location_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_common_organization_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_common_project_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.create_data_agent
    
    
    create_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new DataAgent in a given project and location.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.create_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_create_data_agent)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.create_data_agent_sync
    
    
    create_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent

Creates a new DataAgent in a given project and location synchronously.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.create_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_create_data_agent_sync)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_data_agent_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.delete_data_agent
    
    
    delete_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.delete_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_delete_data_agent)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.delete_data_agent_sync
    
    
    delete_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.delete_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_delete_data_agent_sync)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_delete_operation)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_data_agent
    
    
    get_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.GetDataAgentRequest,
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
    ) -> google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent

Gets details of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_get_data_agent)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM policy for DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_get_iam_policy)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_get_location)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_get_operation)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.list_accessible_data_agents
    
    
    list_accessible_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.ListAccessibleDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListAccessibleDataAgentsPager
    )

Lists DataAgents that are accessible to the caller in a given project and location.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.list_accessible_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_list_accessible_data_agents)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.list_data_agents
    
    
    list_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.ListDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListDataAgentsPager
    )

Lists DataAgents in a given project and location.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.list_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_list_data_agents)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_list_locations)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_list_operations)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.retrieve_agent_ops_observability
    
    
    retrieve_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.RetrieveAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1.types.data_agent_service.RetrieveAgentOpsObservabilityResponse
    )

Gets AgentOps observability settings and status of required services.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.retrieve_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_retrieve_agent_ops_observability)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.set_agent_ops_observability
    
    
    set_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.SetAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        telemetry_enabled: typing.Optional[bool] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.set_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_set_agent_ops_observability)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM policy for a DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_set_iam_policy)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.update_data_agent
    
    
    update_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent
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
    ) -> google.api_core.operation.Operation

Updates the parameters of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.update_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_update_data_agent)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.update_data_agent_sync
    
    
    update_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent
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
    ) -> google.cloud.geminidataanalytics_v1.types.data_agent.DataAgent

Updates the parameters of a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.update_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1_services_data_agent_service_DataAgentServiceClient_update_data_agent_sync)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager
    
    
    ListAccessibleDataAgentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.ListAccessibleDataAgentsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1.types.data_agent_service.ListAccessibleDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1.types.data_agent_service.ListAccessibleDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager#google_cloud_geminidataanalytics_v1_services_data_agent_service_pagers_ListAccessibleDataAgentsAsyncPager_ListAccessibleDataAgentsAsyncPager)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListAccessibleDataAgentsPager
    
    
    ListAccessibleDataAgentsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1.types.data_agent_service.ListAccessibleDataAgentsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1.types.data_agent_service.ListAccessibleDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1.types.data_agent_service.ListAccessibleDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListAccessibleDataAgentsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListAccessibleDataAgentsPager#google_cloud_geminidataanalytics_v1_services_data_agent_service_pagers_ListAccessibleDataAgentsPager_ListAccessibleDataAgentsPager)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListDataAgentsAsyncPager
    
    
    ListDataAgentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1.types.data_agent_service.ListDataAgentsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1.types.data_agent_service.ListDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1.types.data_agent_service.ListDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListDataAgentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListDataAgentsAsyncPager#google_cloud_geminidataanalytics_v1_services_data_agent_service_pagers_ListDataAgentsAsyncPager_ListDataAgentsAsyncPager)

### google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListDataAgentsPager
    
    
    ListDataAgentsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1.types.data_agent_service.ListDataAgentsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1.types.data_agent_service.ListDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1.types.data_agent_service.ListDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListDataAgentsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.pagers.ListDataAgentsPager#google_cloud_geminidataanalytics_v1_services_data_agent_service_pagers_ListDataAgentsPager_ListDataAgentsPager)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient
    
    
    DataChatServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1.services.data_chat_service.transports.base.DataChatServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1.services.data_chat_service.transports.base.DataChatServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data chat service async client.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_DataChatServiceAsyncClient)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_cancel_operation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.chat
    
    
    chat(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_chat_service.ChatRequest,
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
    ) -> typing.Awaitable[
        typing.AsyncIterable[
            google.cloud.geminidataanalytics_v1.types.data_chat_service.Message
        ]
    ]

Answers a data question by generating a stream of xref_Message objects.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.chat](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_chat)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_common_folder_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_common_location_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_common_organization_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_common_project_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.conversation_path
    
    
    conversation_path(project: str, location: str, conversation: str) -> str

Returns a fully-qualified conversation string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_conversation_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.create_conversation
    
    
    create_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.CreateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.conversation.Conversation
        ] = None,
        conversation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1.types.conversation.Conversation

Creates a new conversation to persist the conversation history.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.create_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_create_conversation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_data_agent_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.delete_conversation
    
    
    delete_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.DeleteConversationRequest,
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

Deletes a conversation.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.delete_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_delete_conversation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_delete_operation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_conversation
    
    
    get_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.GetConversationRequest,
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
    ) -> google.cloud.geminidataanalytics_v1.types.conversation.Conversation

Gets details of a single conversation by using conversation id and parent.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_get_conversation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_get_location)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_get_operation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.geminidataanalytics_v1.services.data_chat_service.transports.base.DataChatServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_get_transport_class)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.list_conversations
    
    
    list_conversations(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsRequest,
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
        google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsAsyncPager
    )

Lists all conversations for a given parent.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.list_conversations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_list_conversations)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_list_locations)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.list_messages
    
    
    list_messages(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesRequest,
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
        google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesAsyncPager
    )

Lists all messages for a given conversation.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.list_messages](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_list_messages)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_list_operations)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_conversation_path
    
    
    parse_conversation_path(path: str) -> typing.Dict[str, str]

Parses a conversation path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_parse_conversation_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.update_conversation
    
    
    update_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.UpdateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.conversation.Conversation
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
    ) -> google.cloud.geminidataanalytics_v1.types.conversation.Conversation

Updates a conversation.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient.update_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceAsyncClient_update_conversation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient
    
    
    DataChatServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1.services.data_chat_service.transports.base.DataChatServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1.services.data_chat_service.transports.base.DataChatServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data chat service client.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_DataChatServiceClient)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient___exit__)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_cancel_operation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.chat
    
    
    chat(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_chat_service.ChatRequest,
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
    ) -> typing.Iterable[
        google.cloud.geminidataanalytics_v1.types.data_chat_service.Message
    ]

Answers a data question by generating a stream of xref_Message objects.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.chat](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_chat)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_common_folder_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_common_location_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_common_organization_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_common_project_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.conversation_path
    
    
    conversation_path(project: str, location: str, conversation: str) -> str

Returns a fully-qualified conversation string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_conversation_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.create_conversation
    
    
    create_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.CreateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.conversation.Conversation
        ] = None,
        conversation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1.types.conversation.Conversation

Creates a new conversation to persist the conversation history.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.create_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_create_conversation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_data_agent_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.delete_conversation
    
    
    delete_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.DeleteConversationRequest,
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

Deletes a conversation.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.delete_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_delete_conversation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_delete_operation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.get_conversation
    
    
    get_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.GetConversationRequest,
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
    ) -> google.cloud.geminidataanalytics_v1.types.conversation.Conversation

Gets details of a single conversation by using conversation id and parent.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.get_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_get_conversation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_get_location)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_get_operation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.list_conversations
    
    
    list_conversations(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsRequest,
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
        google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsPager
    )

Lists all conversations for a given parent.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.list_conversations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_list_conversations)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_list_locations)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.list_messages
    
    
    list_messages(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesRequest,
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
        google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesPager
    )

Lists all messages for a given conversation.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.list_messages](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_list_messages)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_list_operations)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_conversation_path
    
    
    parse_conversation_path(path: str) -> typing.Dict[str, str]

Parses a conversation path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_parse_conversation_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.update_conversation
    
    
    update_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1.types.conversation.UpdateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1.types.conversation.Conversation
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
    ) -> google.cloud.geminidataanalytics_v1.types.conversation.Conversation

Updates a conversation.

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.update_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1_services_data_chat_service_DataChatServiceClient_update_conversation)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsAsyncPager
    
    
    ListConversationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsRequest,
        response: google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsResponse,
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsAsyncPager#google_cloud_geminidataanalytics_v1_services_data_chat_service_pagers_ListConversationsAsyncPager_ListConversationsAsyncPager)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsPager
    
    
    ListConversationsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsRequest,
        response: google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsResponse,
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsPager#google_cloud_geminidataanalytics_v1_services_data_chat_service_pagers_ListConversationsPager_ListConversationsPager)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesAsyncPager
    
    
    ListMessagesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesRequest,
        response: google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesResponse,
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesAsyncPager#google_cloud_geminidataanalytics_v1_services_data_chat_service_pagers_ListMessagesAsyncPager_ListMessagesAsyncPager)

### google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesPager
    
    
    ListMessagesPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesResponse,
        ],
        request: google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesRequest,
        response: google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesResponse,
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

See more: [google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesPager#google_cloud_geminidataanalytics_v1_services_data_chat_service_pagers_ListMessagesPager_ListMessagesPager)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient
    
    
    DataA2AServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.transports.base.DataA2AServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.transports.base.DataA2AServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data a2a service async client.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_DataA2AServiceAsyncClient)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_cancel_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_delete_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_agent_card
    
    
    get_agent_card(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.GetAgentCardRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.AgentCard

GetAgentCard returns the agent card for the agent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_agent_card](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_get_agent_card)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_get_location)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_get_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.transports.base.DataA2AServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_get_transport_class)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_list_locations)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_list_operations)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.send_message
    
    
    send_message(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.SendMessageRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        message: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.A2AMessage
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
        google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.SendMessageResponse
    )

Send a message to the agent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.send_message](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_send_message)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.send_streaming_message
    
    
    send_streaming_message(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.SendMessageRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        message: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.A2AMessage
        ] = None,
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
            google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.StreamResponse
        ]
    ]

SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient.send_streaming_message](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceAsyncClient_send_streaming_message)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient
    
    
    DataA2AServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.transports.base.DataA2AServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.transports.base.DataA2AServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data a2a service client.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_DataA2AServiceClient)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient___exit__)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_cancel_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_delete_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.get_agent_card
    
    
    get_agent_card(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.GetAgentCardRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.AgentCard

GetAgentCard returns the agent card for the agent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.get_agent_card](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_get_agent_card)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_get_location)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_get_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_list_locations)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_list_operations)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.send_message
    
    
    send_message(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.SendMessageRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        message: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.A2AMessage
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
        google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.SendMessageResponse
    )

Send a message to the agent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.send_message](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_send_message)

### google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.send_streaming_message
    
    
    send_streaming_message(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.SendMessageRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        message: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.A2AMessage
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> typing.Iterable[
        google.cloud.geminidataanalytics_v1alpha.types.data_a2a_service.StreamResponse
    ]

SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.send_streaming_message](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_send_streaming_message)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient
    
    
    DataAgentServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data agent service async client.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_DataAgentServiceAsyncClient)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_cancel_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent
    
    
    create_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new DataAgent in a given project and location.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_create_data_agent)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent_sync
    
    
    create_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Creates a new DataAgent in a given project and location synchronously.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_create_data_agent_sync)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_data_agent_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent
    
    
    delete_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_delete_data_agent)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent_sync
    
    
    delete_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_delete_data_agent_sync)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_delete_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_data_agent
    
    
    get_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.GetDataAgentRequest,
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Gets details of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_get_data_agent)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM policy for DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_get_iam_policy)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_get_location)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_get_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_get_transport_class)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.list_accessible_data_agents
    
    
    list_accessible_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager
    )

Lists DataAgents that are accessible to the caller in a given project and location.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.list_accessible_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_list_accessible_data_agents)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.list_data_agents
    
    
    list_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsAsyncPager
    )

Lists DataAgents in a given project and location.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.list_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_list_data_agents)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_list_locations)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_list_operations)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.retrieve_agent_ops_observability
    
    
    retrieve_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.RetrieveAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.RetrieveAgentOpsObservabilityResponse
    )

Gets AgentOps observability settings and status of required services.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.retrieve_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_retrieve_agent_ops_observability)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.set_agent_ops_observability
    
    
    set_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.SetAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        telemetry_enabled: typing.Optional[bool] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.set_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_set_agent_ops_observability)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM policy for a DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_set_iam_policy)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent
    
    
    update_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_update_data_agent)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent_sync
    
    
    update_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Updates the parameters of a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceAsyncClient_update_data_agent_sync)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient
    
    
    DataAgentServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data agent service client.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_DataAgentServiceClient)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient___exit__)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_cancel_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.create_data_agent
    
    
    create_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new DataAgent in a given project and location.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.create_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_create_data_agent)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.create_data_agent_sync
    
    
    create_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Creates a new DataAgent in a given project and location synchronously.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.create_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_create_data_agent_sync)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_data_agent_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.delete_data_agent
    
    
    delete_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.delete_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_delete_data_agent)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.delete_data_agent_sync
    
    
    delete_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.delete_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_delete_data_agent_sync)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_delete_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_data_agent
    
    
    get_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.GetDataAgentRequest,
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Gets details of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_get_data_agent)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM policy for DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_get_iam_policy)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_get_location)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_get_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.list_accessible_data_agents
    
    
    list_accessible_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsPager
    )

Lists DataAgents that are accessible to the caller in a given project and location.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.list_accessible_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_list_accessible_data_agents)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.list_data_agents
    
    
    list_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsPager
    )

Lists DataAgents in a given project and location.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.list_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_list_data_agents)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_list_locations)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_list_operations)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.retrieve_agent_ops_observability
    
    
    retrieve_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.RetrieveAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.RetrieveAgentOpsObservabilityResponse
    )

Gets AgentOps observability settings and status of required services.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.retrieve_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_retrieve_agent_ops_observability)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.set_agent_ops_observability
    
    
    set_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.SetAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        telemetry_enabled: typing.Optional[bool] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.set_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_set_agent_ops_observability)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM policy for a DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_set_iam_policy)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.update_data_agent
    
    
    update_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
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
    ) -> google.api_core.operation.Operation

Updates the parameters of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.update_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_update_data_agent)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.update_data_agent_sync
    
    
    update_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Updates the parameters of a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.update_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_update_data_agent_sync)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager
    
    
    ListAccessibleDataAgentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_pagers_ListAccessibleDataAgentsAsyncPager_ListAccessibleDataAgentsAsyncPager)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsPager
    
    
    ListAccessibleDataAgentsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsPager#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_pagers_ListAccessibleDataAgentsPager_ListAccessibleDataAgentsPager)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsAsyncPager
    
    
    ListDataAgentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsAsyncPager#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_pagers_ListDataAgentsAsyncPager_ListDataAgentsAsyncPager)

### google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsPager
    
    
    ListDataAgentsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsPager#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_pagers_ListDataAgentsPager_ListDataAgentsPager)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient
    
    
    DataChatServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.transports.base.DataChatServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.transports.base.DataChatServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data chat service async client.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_DataChatServiceAsyncClient)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_cancel_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.chat
    
    
    chat(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ChatRequest,
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
    ) -> typing.Awaitable[
        typing.AsyncIterable[
            google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.Message
        ]
    ]

Answers a data question by generating a stream of xref_Message objects.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.chat](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_chat)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.conversation_path
    
    
    conversation_path(project: str, location: str, conversation: str) -> str

Returns a fully-qualified conversation string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_conversation_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.create_conversation
    
    
    create_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.CreateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation
        ] = None,
        conversation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation

Creates a new conversation to persist the conversation history.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.create_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_create_conversation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_data_agent_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.delete_conversation
    
    
    delete_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.DeleteConversationRequest,
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

Deletes a conversation.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.delete_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_delete_conversation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_delete_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_conversation
    
    
    get_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.GetConversationRequest,
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation

Gets details of a single conversation by using conversation id and parent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_get_conversation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_get_location)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_get_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.transports.base.DataChatServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_get_transport_class)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.list_conversations
    
    
    list_conversations(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.ListConversationsRequest,
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
        google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListConversationsAsyncPager
    )

Lists all conversations for a given parent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.list_conversations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_list_conversations)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_list_locations)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.list_messages
    
    
    list_messages(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ListMessagesRequest,
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
        google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListMessagesAsyncPager
    )

Lists all messages for a given conversation.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.list_messages](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_list_messages)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_list_operations)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_conversation_path
    
    
    parse_conversation_path(path: str) -> typing.Dict[str, str]

Parses a conversation path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_parse_conversation_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.query_data
    
    
    query_data(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.QueryDataRequest,
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.QueryDataResponse

Queries data from a natural language user query.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.query_data](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_query_data)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.update_conversation
    
    
    update_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.UpdateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation

Updates a conversation.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient.update_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceAsyncClient_update_conversation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient
    
    
    DataChatServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.transports.base.DataChatServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.transports.base.DataChatServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data chat service client.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_DataChatServiceClient)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient___exit__)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_cancel_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.chat
    
    
    chat(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ChatRequest,
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
    ) -> typing.Iterable[
        google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.Message
    ]

Answers a data question by generating a stream of xref_Message objects.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.chat](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_chat)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.conversation_path
    
    
    conversation_path(project: str, location: str, conversation: str) -> str

Returns a fully-qualified conversation string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_conversation_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.create_conversation
    
    
    create_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.CreateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation
        ] = None,
        conversation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation

Creates a new conversation to persist the conversation history.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.create_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_create_conversation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_data_agent_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.delete_conversation
    
    
    delete_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.DeleteConversationRequest,
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

Deletes a conversation.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.delete_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_delete_conversation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_delete_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.get_conversation
    
    
    get_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.GetConversationRequest,
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation

Gets details of a single conversation by using conversation id and parent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.get_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_get_conversation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_get_location)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_get_operation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.list_conversations
    
    
    list_conversations(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.ListConversationsRequest,
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
        google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListConversationsPager
    )

Lists all conversations for a given parent.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.list_conversations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_list_conversations)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_list_locations)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.list_messages
    
    
    list_messages(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ListMessagesRequest,
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
        google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListMessagesPager
    )

Lists all messages for a given conversation.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.list_messages](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_list_messages)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_list_operations)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_conversation_path
    
    
    parse_conversation_path(path: str) -> typing.Dict[str, str]

Parses a conversation path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_parse_conversation_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.query_data
    
    
    query_data(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.QueryDataRequest,
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.QueryDataResponse

Queries data from a natural language user query.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.query_data](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_query_data)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.update_conversation
    
    
    update_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.UpdateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation
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
    ) -> google.cloud.geminidataanalytics_v1alpha.types.conversation.Conversation

Updates a conversation.

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient.update_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_DataChatServiceClient_update_conversation)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListConversationsAsyncPager
    
    
    ListConversationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1alpha.types.conversation.ListConversationsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.conversation.ListConversationsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.conversation.ListConversationsResponse,
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListConversationsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListConversationsAsyncPager#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_pagers_ListConversationsAsyncPager_ListConversationsAsyncPager)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListConversationsPager
    
    
    ListConversationsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1alpha.types.conversation.ListConversationsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.conversation.ListConversationsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.conversation.ListConversationsResponse,
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListConversationsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListConversationsPager#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_pagers_ListConversationsPager_ListConversationsPager)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListMessagesAsyncPager
    
    
    ListMessagesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ListMessagesResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ListMessagesRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ListMessagesResponse,
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListMessagesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListMessagesAsyncPager#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_pagers_ListMessagesAsyncPager_ListMessagesAsyncPager)

### google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListMessagesPager
    
    
    ListMessagesPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ListMessagesResponse,
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ListMessagesRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_chat_service.ListMessagesResponse,
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

See more: [google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListMessagesPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_chat_service.pagers.ListMessagesPager#google_cloud_geminidataanalytics_v1alpha_services_data_chat_service_pagers_ListMessagesPager_ListMessagesPager)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient
    
    
    DataA2AServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.transports.base.DataA2AServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.transports.base.DataA2AServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data a2a service async client.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_DataA2AServiceAsyncClient)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_cancel_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_delete_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_agent_card
    
    
    get_agent_card(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.GetAgentCardRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.AgentCard

GetAgentCard returns the agent card for the agent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_agent_card](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_get_agent_card)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_get_location)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_get_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.transports.base.DataA2AServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_get_transport_class)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_list_locations)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_list_operations)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.send_message
    
    
    send_message(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.SendMessageRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        message: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.A2AMessage
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.SendMessageResponse

Send a message to the agent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.send_message](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_send_message)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.send_streaming_message
    
    
    send_streaming_message(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.SendMessageRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        message: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.A2AMessage
        ] = None,
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
            google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.StreamResponse
        ]
    ]

SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient.send_streaming_message](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceAsyncClient_send_streaming_message)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient
    
    
    DataA2AServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.transports.base.DataA2AServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.transports.base.DataA2AServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data a2a service client.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_DataA2AServiceClient)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient___exit__)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_cancel_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_delete_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.get_agent_card
    
    
    get_agent_card(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.GetAgentCardRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.AgentCard

GetAgentCard returns the agent card for the agent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.get_agent_card](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_get_agent_card)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_get_location)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_get_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_list_locations)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_list_operations)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.send_message
    
    
    send_message(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.SendMessageRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        message: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.A2AMessage
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.SendMessageResponse

Send a message to the agent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.send_message](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_send_message)

### google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.send_streaming_message
    
    
    send_streaming_message(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.SendMessageRequest,
                dict,
            ]
        ] = None,
        *,
        tenant: typing.Optional[str] = None,
        message: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.A2AMessage
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> typing.Iterable[
        google.cloud.geminidataanalytics_v1beta.types.data_a2a_service.StreamResponse
    ]

SendStreamingMessage is a streaming call that will return a stream of task update events until the Task is in an interrupted or terminal state.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient.send_streaming_message](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_a2a_service.DataA2AServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_a2a_service_DataA2AServiceClient_send_streaming_message)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient
    
    
    DataAgentServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1beta.services.data_agent_service.transports.base.DataAgentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1beta.services.data_agent_service.transports.base.DataAgentServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data agent service async client.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_DataAgentServiceAsyncClient)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_cancel_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent
    
    
    create_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new DataAgent in a given project and location.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_create_data_agent)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent_sync
    
    
    create_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent

Creates a new DataAgent in a given project and location synchronously.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.create_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_create_data_agent_sync)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_data_agent_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent
    
    
    delete_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_delete_data_agent)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent_sync
    
    
    delete_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.delete_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_delete_data_agent_sync)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_delete_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_data_agent
    
    
    get_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.GetDataAgentRequest,
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent

Gets details of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_get_data_agent)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM policy for DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_get_iam_policy)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_get_location)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_get_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.geminidataanalytics_v1beta.services.data_agent_service.transports.base.DataAgentServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_get_transport_class)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.list_accessible_data_agents
    
    
    list_accessible_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListAccessibleDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager
    )

Lists DataAgents that are accessible to the caller in a given project and location.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.list_accessible_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_list_accessible_data_agents)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.list_data_agents
    
    
    list_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListDataAgentsAsyncPager
    )

Lists DataAgents in a given project and location.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.list_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_list_data_agents)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_list_locations)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_list_operations)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.retrieve_agent_ops_observability
    
    
    retrieve_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.RetrieveAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1beta.types.data_agent_service.RetrieveAgentOpsObservabilityResponse
    )

Gets AgentOps observability settings and status of required services.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.retrieve_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_retrieve_agent_ops_observability)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.set_agent_ops_observability
    
    
    set_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.SetAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        telemetry_enabled: typing.Optional[bool] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.set_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_set_agent_ops_observability)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM policy for a DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_set_iam_policy)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent
    
    
    update_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the parameters of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_update_data_agent)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent_sync
    
    
    update_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent

Updates the parameters of a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient.update_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceAsyncClient_update_data_agent_sync)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient
    
    
    DataAgentServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1beta.services.data_agent_service.transports.base.DataAgentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1beta.services.data_agent_service.transports.base.DataAgentServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data agent service client.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_DataAgentServiceClient)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient___exit__)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_cancel_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.create_data_agent
    
    
    create_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new DataAgent in a given project and location.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.create_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_create_data_agent)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.create_data_agent_sync
    
    
    create_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent

Creates a new DataAgent in a given project and location synchronously.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.create_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_create_data_agent_sync)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_data_agent_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.delete_data_agent
    
    
    delete_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.delete_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_delete_data_agent)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.delete_data_agent_sync
    
    
    delete_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.DeleteDataAgentRequest,
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

Deletes a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.delete_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_delete_data_agent_sync)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_delete_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_data_agent
    
    
    get_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.GetDataAgentRequest,
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent

Gets details of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_get_data_agent)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM policy for DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_get_iam_policy)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_get_location)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_get_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.list_accessible_data_agents
    
    
    list_accessible_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListAccessibleDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListAccessibleDataAgentsPager
    )

Lists DataAgents that are accessible to the caller in a given project and location.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.list_accessible_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_list_accessible_data_agents)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.list_data_agents
    
    
    list_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListDataAgentsRequest,
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
        google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListDataAgentsPager
    )

Lists DataAgents in a given project and location.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.list_data_agents](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_list_data_agents)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_list_locations)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_list_operations)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.retrieve_agent_ops_observability
    
    
    retrieve_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.RetrieveAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1beta.types.data_agent_service.RetrieveAgentOpsObservabilityResponse
    )

Gets AgentOps observability settings and status of required services.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.retrieve_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_retrieve_agent_ops_observability)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.set_agent_ops_observability
    
    
    set_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.SetAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        telemetry_enabled: typing.Optional[bool] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.set_agent_ops_observability](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_set_agent_ops_observability)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM policy for a DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_set_iam_policy)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.update_data_agent
    
    
    update_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent
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
    ) -> google.api_core.operation.Operation

Updates the parameters of a single DataAgent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.update_data_agent](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_update_data_agent)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.update_data_agent_sync
    
    
    update_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_agent.DataAgent

Updates the parameters of a single DataAgent synchronously.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient.update_data_agent_sync](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.DataAgentServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_DataAgentServiceClient_update_data_agent_sync)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager
    
    
    ListAccessibleDataAgentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListAccessibleDataAgentsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListAccessibleDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListAccessibleDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_pagers_ListAccessibleDataAgentsAsyncPager_ListAccessibleDataAgentsAsyncPager)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListAccessibleDataAgentsPager
    
    
    ListAccessibleDataAgentsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListAccessibleDataAgentsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListAccessibleDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListAccessibleDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListAccessibleDataAgentsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListAccessibleDataAgentsPager#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_pagers_ListAccessibleDataAgentsPager_ListAccessibleDataAgentsPager)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListDataAgentsAsyncPager
    
    
    ListDataAgentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListDataAgentsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListDataAgentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListDataAgentsAsyncPager#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_pagers_ListDataAgentsAsyncPager_ListDataAgentsAsyncPager)

### google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListDataAgentsPager
    
    
    ListDataAgentsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListDataAgentsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1beta.types.data_agent_service.ListDataAgentsResponse,
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListDataAgentsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_agent_service.pagers.ListDataAgentsPager#google_cloud_geminidataanalytics_v1beta_services_data_agent_service_pagers_ListDataAgentsPager_ListDataAgentsPager)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient
    
    
    DataChatServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1beta.services.data_chat_service.transports.base.DataChatServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1beta.services.data_chat_service.transports.base.DataChatServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data chat service async client.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_DataChatServiceAsyncClient)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_cancel_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.chat
    
    
    chat(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ChatRequest,
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
    ) -> typing.Awaitable[
        typing.AsyncIterable[
            google.cloud.geminidataanalytics_v1beta.types.data_chat_service.Message
        ]
    ]

Answers a data question by generating a stream of xref_Message objects.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.chat](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_chat)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.conversation_path
    
    
    conversation_path(project: str, location: str, conversation: str) -> str

Returns a fully-qualified conversation string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_conversation_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.create_conversation
    
    
    create_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.CreateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation
        ] = None,
        conversation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation

Creates a new conversation to persist the conversation history.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.create_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_create_conversation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_data_agent_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.delete_conversation
    
    
    delete_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.DeleteConversationRequest,
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

Deletes a conversation.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.delete_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_delete_conversation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_delete_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_conversation
    
    
    get_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.GetConversationRequest,
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation

Gets details of a single conversation by using conversation id and parent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_get_conversation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_get_location)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_get_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.geminidataanalytics_v1beta.services.data_chat_service.transports.base.DataChatServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_get_transport_class)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.list_conversations
    
    
    list_conversations(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.ListConversationsRequest,
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
        google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListConversationsAsyncPager
    )

Lists all conversations for a given parent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.list_conversations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_list_conversations)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_list_locations)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.list_messages
    
    
    list_messages(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ListMessagesRequest,
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
        google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListMessagesAsyncPager
    )

Lists all messages for a given conversation.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.list_messages](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_list_messages)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_list_operations)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_conversation_path
    
    
    parse_conversation_path(path: str) -> typing.Dict[str, str]

Parses a conversation path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_parse_conversation_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.query_data
    
    
    query_data(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_chat_service.QueryDataRequest,
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_chat_service.QueryDataResponse

Queries data from a natural language user query.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.query_data](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_query_data)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.update_conversation
    
    
    update_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.UpdateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation

Updates a conversation.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient.update_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceAsyncClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceAsyncClient_update_conversation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient
    
    
    DataChatServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1beta.services.data_chat_service.transports.base.DataChatServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1beta.services.data_chat_service.transports.base.DataChatServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data chat service client.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_DataChatServiceClient)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient___exit__)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.cancel_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_cancel_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.chat
    
    
    chat(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ChatRequest,
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
    ) -> typing.Iterable[
        google.cloud.geminidataanalytics_v1beta.types.data_chat_service.Message
    ]

Answers a data question by generating a stream of xref_Message objects.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.chat](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_chat)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.conversation_path
    
    
    conversation_path(project: str, location: str, conversation: str) -> str

Returns a fully-qualified conversation string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_conversation_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.create_conversation
    
    
    create_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.CreateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation
        ] = None,
        conversation_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation

Creates a new conversation to persist the conversation history.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.create_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_create_conversation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_crypto_key_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_data_agent_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.delete_conversation
    
    
    delete_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.DeleteConversationRequest,
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

Deletes a conversation.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.delete_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_delete_conversation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.delete_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_delete_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_from_service_account_file)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_from_service_account_info)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_from_service_account_json)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.get_conversation
    
    
    get_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.GetConversationRequest,
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation

Gets details of a single conversation by using conversation id and parent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.get_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_get_conversation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.get_location
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_get_location)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.get_operation
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_get_operation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.list_conversations
    
    
    list_conversations(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.ListConversationsRequest,
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
        google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListConversationsPager
    )

Lists all conversations for a given parent.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.list_conversations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_list_conversations)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.list_locations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_list_locations)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.list_messages
    
    
    list_messages(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ListMessagesRequest,
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
        google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListMessagesPager
    )

Lists all messages for a given conversation.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.list_messages](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_list_messages)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.list_operations
    
    
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_list_operations)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_parse_common_billing_account_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_parse_common_folder_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_parse_common_location_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_parse_common_organization_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_parse_common_project_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_conversation_path
    
    
    parse_conversation_path(path: str) -> typing.Dict[str, str]

Parses a conversation path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_conversation_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_parse_conversation_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_parse_crypto_key_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.parse_data_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_parse_data_agent_path)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.query_data
    
    
    query_data(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.data_chat_service.QueryDataRequest,
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.data_chat_service.QueryDataResponse

Queries data from a natural language user query.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.query_data](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_query_data)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.update_conversation
    
    
    update_conversation(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1beta.types.conversation.UpdateConversationRequest,
                dict,
            ]
        ] = None,
        *,
        conversation: typing.Optional[
            google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation
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
    ) -> google.cloud.geminidataanalytics_v1beta.types.conversation.Conversation

Updates a conversation.

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient.update_conversation](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.DataChatServiceClient#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_DataChatServiceClient_update_conversation)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListConversationsAsyncPager
    
    
    ListConversationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1beta.types.conversation.ListConversationsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1beta.types.conversation.ListConversationsRequest,
        response: google.cloud.geminidataanalytics_v1beta.types.conversation.ListConversationsResponse,
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListConversationsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListConversationsAsyncPager#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_pagers_ListConversationsAsyncPager_ListConversationsAsyncPager)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListConversationsPager
    
    
    ListConversationsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1beta.types.conversation.ListConversationsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1beta.types.conversation.ListConversationsRequest,
        response: google.cloud.geminidataanalytics_v1beta.types.conversation.ListConversationsResponse,
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListConversationsPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListConversationsPager#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_pagers_ListConversationsPager_ListConversationsPager)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListMessagesAsyncPager
    
    
    ListMessagesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ListMessagesResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ListMessagesRequest,
        response: google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ListMessagesResponse,
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListMessagesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListMessagesAsyncPager#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_pagers_ListMessagesAsyncPager_ListMessagesAsyncPager)

### google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListMessagesPager
    
    
    ListMessagesPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ListMessagesResponse,
        ],
        request: google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ListMessagesRequest,
        response: google.cloud.geminidataanalytics_v1beta.types.data_chat_service.ListMessagesResponse,
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

See more: [google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListMessagesPager](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.services.data_chat_service.pagers.ListMessagesPager#google_cloud_geminidataanalytics_v1beta_services_data_chat_service_pagers_ListMessagesPager_ListMessagesPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
