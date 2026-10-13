---
url: https://docs.cloud.google.com/python/docs/reference/edgecontainer/latest/summary_method/
title: Package Methods (0.8.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:34.768612+00:00
---

# Package Methods (0.8.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/edgecontainer/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.2 (latest)  0.8.1  0.7.0  0.6.0  0.5.18  0.4.1  0.3.0  0.2.1  0.1.0 

Summary of entries of Methods for edgecontainer.

## 

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient
    
    
    EdgeContainerAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.edgecontainer_v1.services.edge_container.transports.base.EdgeContainerTransport,
                typing.Callable[
                    [...],
                    google.cloud.edgecontainer_v1.services.edge_container.transports.base.EdgeContainerTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the edge container async client.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_EdgeContainerAsyncClient)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_cancel_operation)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.cluster_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_cluster_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_common_billing_account_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_common_folder_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_common_location_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_common_organization_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_common_project_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.create_cluster
    
    
    create_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.CreateClusterRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        cluster: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.Cluster
        ] = None,
        cluster_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Cluster in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.create_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_create_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.create_node_pool
    
    
    create_node_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.CreateNodePoolRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        node_pool: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.NodePool
        ] = None,
        node_pool_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new NodePool in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.create_node_pool](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_create_node_pool)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.create_vpn_connection
    
    
    create_vpn_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.CreateVpnConnectionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        vpn_connection: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.VpnConnection
        ] = None,
        vpn_connection_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new VPN connection in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.create_vpn_connection](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_create_vpn_connection)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.crypto_key_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_crypto_key_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.crypto_key_version_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_crypto_key_version_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.delete_cluster
    
    
    delete_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.DeleteClusterRequest, dict
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

Deletes a single Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.delete_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_delete_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.delete_node_pool
    
    
    delete_node_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.DeleteNodePoolRequest, dict
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

Deletes a single NodePool.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.delete_node_pool](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_delete_node_pool)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.delete_operation
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_delete_operation)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.delete_vpn_connection
    
    
    delete_vpn_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.DeleteVpnConnectionRequest, dict
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

Deletes a single VPN connection.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.delete_vpn_connection](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_delete_vpn_connection)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_from_service_account_file)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_from_service_account_info)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_from_service_account_json)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.generate_access_token
    
    
    generate_access_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GenerateAccessTokenRequest, dict
            ]
        ] = None,
        *,
        cluster: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.edgecontainer_v1.types.service.GenerateAccessTokenResponse

Generates an access token for a Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.generate_access_token](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_generate_access_token)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.generate_offline_credential
    
    
    generate_offline_credential(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GenerateOfflineCredentialRequest,
                dict,
            ]
        ] = None,
        *,
        cluster: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.edgecontainer_v1.types.service.GenerateOfflineCredentialResponse

Generates an offline credential for a Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.generate_offline_credential](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_generate_offline_credential)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_cluster
    
    
    get_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetClusterRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.Cluster

Gets details of a single Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_location
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_location](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_location)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_machine
    
    
    get_machine(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetMachineRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.Machine

Gets details of a single Machine.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_machine](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_machine)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_node_pool
    
    
    get_node_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetNodePoolRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.NodePool

Gets details of a single NodePool.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_node_pool](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_node_pool)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_operation
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_operation)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_server_config
    
    
    get_server_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetServerConfigRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.ServerConfig

Gets the server config.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_server_config](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_server_config)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.edgecontainer_v1.services.edge_container.transports.base.EdgeContainerTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_transport_class)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_vpn_connection
    
    
    get_vpn_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetVpnConnectionRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.VpnConnection

Gets details of a single VPN connection.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.get_vpn_connection](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_get_vpn_connection)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_clusters
    
    
    list_clusters(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.ListClustersRequest, dict
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
        google.cloud.edgecontainer_v1.services.edge_container.pagers.ListClustersAsyncPager
    )

Lists Clusters in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_clusters](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_list_clusters)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_locations
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_list_locations)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_machines
    
    
    list_machines(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.ListMachinesRequest, dict
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
        google.cloud.edgecontainer_v1.services.edge_container.pagers.ListMachinesAsyncPager
    )

Lists Machines in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_machines](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_list_machines)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_node_pools
    
    
    list_node_pools(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.ListNodePoolsRequest, dict
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
        google.cloud.edgecontainer_v1.services.edge_container.pagers.ListNodePoolsAsyncPager
    )

Lists NodePools in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_node_pools](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_list_node_pools)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_operations
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_list_operations)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_vpn_connections
    
    
    list_vpn_connections(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.ListVpnConnectionsRequest, dict
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
        google.cloud.edgecontainer_v1.services.edge_container.pagers.ListVpnConnectionsAsyncPager
    )

Lists VPN connections in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.list_vpn_connections](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_list_vpn_connections)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.machine_path
    
    
    machine_path(project: str, location: str, machine: str) -> str

Returns a fully-qualified machine string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.machine_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_machine_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.node_pool_path
    
    
    node_pool_path(project: str, location: str, cluster: str, node_pool: str) -> str

Returns a fully-qualified node_pool string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.node_pool_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_node_pool_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_cluster_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_cluster_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_common_billing_account_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_common_folder_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_common_location_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_common_organization_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_common_project_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_crypto_key_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_crypto_key_version_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_crypto_key_version_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_machine_path
    
    
    parse_machine_path(path: str) -> typing.Dict[str, str]

Parses a machine path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_machine_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_machine_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_node_pool_path
    
    
    parse_node_pool_path(path: str) -> typing.Dict[str, str]

Parses a node_pool path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_node_pool_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_node_pool_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_vpn_connection_path
    
    
    parse_vpn_connection_path(path: str) -> typing.Dict[str, str]

Parses a vpn_connection path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.parse_vpn_connection_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_parse_vpn_connection_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.update_cluster
    
    
    update_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.UpdateClusterRequest, dict
            ]
        ] = None,
        *,
        cluster: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.Cluster
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

Updates the parameters of a single Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.update_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_update_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.update_node_pool
    
    
    update_node_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.UpdateNodePoolRequest, dict
            ]
        ] = None,
        *,
        node_pool: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.NodePool
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

Updates the parameters of a single NodePool.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.update_node_pool](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_update_node_pool)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.upgrade_cluster
    
    
    upgrade_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.UpgradeClusterRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        target_version: typing.Optional[str] = None,
        schedule: typing.Optional[
            google.cloud.edgecontainer_v1.types.service.UpgradeClusterRequest.Schedule
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

Upgrades a single cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.upgrade_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_upgrade_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.vpn_connection_path
    
    
    vpn_connection_path(project: str, location: str, vpn_connection: str) -> str

Returns a fully-qualified vpn_connection string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient.vpn_connection_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerAsyncClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerAsyncClient_vpn_connection_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient
    
    
    EdgeContainerClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.edgecontainer_v1.services.edge_container.transports.base.EdgeContainerTransport,
                typing.Callable[
                    [...],
                    google.cloud.edgecontainer_v1.services.edge_container.transports.base.EdgeContainerTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the edge container client.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_EdgeContainerClient)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.**exit**](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient___exit__)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.cancel_operation
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.cancel_operation](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_cancel_operation)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.cluster_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_cluster_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_common_billing_account_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_folder_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_common_folder_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_location_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_common_location_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_organization_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_common_organization_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.common_project_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_common_project_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.create_cluster
    
    
    create_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.CreateClusterRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        cluster: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.Cluster
        ] = None,
        cluster_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Cluster in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.create_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_create_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.create_node_pool
    
    
    create_node_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.CreateNodePoolRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        node_pool: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.NodePool
        ] = None,
        node_pool_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new NodePool in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.create_node_pool](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_create_node_pool)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.create_vpn_connection
    
    
    create_vpn_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.CreateVpnConnectionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        vpn_connection: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.VpnConnection
        ] = None,
        vpn_connection_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new VPN connection in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.create_vpn_connection](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_create_vpn_connection)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.crypto_key_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_crypto_key_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.crypto_key_version_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_crypto_key_version_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.delete_cluster
    
    
    delete_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.DeleteClusterRequest, dict
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

Deletes a single Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.delete_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_delete_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.delete_node_pool
    
    
    delete_node_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.DeleteNodePoolRequest, dict
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

Deletes a single NodePool.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.delete_node_pool](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_delete_node_pool)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.delete_operation
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.delete_operation](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_delete_operation)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.delete_vpn_connection
    
    
    delete_vpn_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.DeleteVpnConnectionRequest, dict
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

Deletes a single VPN connection.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.delete_vpn_connection](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_delete_vpn_connection)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.from_service_account_file](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_from_service_account_file)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.from_service_account_info](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_from_service_account_info)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.from_service_account_json](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_from_service_account_json)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.generate_access_token
    
    
    generate_access_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GenerateAccessTokenRequest, dict
            ]
        ] = None,
        *,
        cluster: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.edgecontainer_v1.types.service.GenerateAccessTokenResponse

Generates an access token for a Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.generate_access_token](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_generate_access_token)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.generate_offline_credential
    
    
    generate_offline_credential(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GenerateOfflineCredentialRequest,
                dict,
            ]
        ] = None,
        *,
        cluster: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.edgecontainer_v1.types.service.GenerateOfflineCredentialResponse

Generates an offline credential for a Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.generate_offline_credential](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_generate_offline_credential)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_cluster
    
    
    get_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetClusterRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.Cluster

Gets details of a single Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_get_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_location
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_location](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_get_location)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_machine
    
    
    get_machine(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetMachineRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.Machine

Gets details of a single Machine.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_machine](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_get_machine)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_get_mtls_endpoint_and_cert_source)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_node_pool
    
    
    get_node_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetNodePoolRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.NodePool

Gets details of a single NodePool.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_node_pool](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_get_node_pool)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_operation
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_operation](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_get_operation)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_server_config
    
    
    get_server_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetServerConfigRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.ServerConfig

Gets the server config.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_server_config](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_get_server_config)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_vpn_connection
    
    
    get_vpn_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.GetVpnConnectionRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.types.resources.VpnConnection

Gets details of a single VPN connection.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.get_vpn_connection](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_get_vpn_connection)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_clusters
    
    
    list_clusters(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.ListClustersRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.services.edge_container.pagers.ListClustersPager

Lists Clusters in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_clusters](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_list_clusters)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_locations
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_locations](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_list_locations)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_machines
    
    
    list_machines(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.ListMachinesRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.services.edge_container.pagers.ListMachinesPager

Lists Machines in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_machines](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_list_machines)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_node_pools
    
    
    list_node_pools(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.ListNodePoolsRequest, dict
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
    ) -> google.cloud.edgecontainer_v1.services.edge_container.pagers.ListNodePoolsPager

Lists NodePools in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_node_pools](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_list_node_pools)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_operations
    
    
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_operations](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_list_operations)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_vpn_connections
    
    
    list_vpn_connections(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.ListVpnConnectionsRequest, dict
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
        google.cloud.edgecontainer_v1.services.edge_container.pagers.ListVpnConnectionsPager
    )

Lists VPN connections in a given project and location.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.list_vpn_connections](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_list_vpn_connections)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.machine_path
    
    
    machine_path(project: str, location: str, machine: str) -> str

Returns a fully-qualified machine string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.machine_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_machine_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.node_pool_path
    
    
    node_pool_path(project: str, location: str, cluster: str, node_pool: str) -> str

Returns a fully-qualified node_pool string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.node_pool_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_node_pool_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_cluster_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_cluster_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_common_billing_account_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_common_folder_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_common_location_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_common_organization_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_common_project_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_crypto_key_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_crypto_key_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_crypto_key_version_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_crypto_key_version_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_machine_path
    
    
    parse_machine_path(path: str) -> typing.Dict[str, str]

Parses a machine path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_machine_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_machine_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_node_pool_path
    
    
    parse_node_pool_path(path: str) -> typing.Dict[str, str]

Parses a node_pool path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_node_pool_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_node_pool_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_vpn_connection_path
    
    
    parse_vpn_connection_path(path: str) -> typing.Dict[str, str]

Parses a vpn_connection path into its component segments.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.parse_vpn_connection_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_parse_vpn_connection_path)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.update_cluster
    
    
    update_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.UpdateClusterRequest, dict
            ]
        ] = None,
        *,
        cluster: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.Cluster
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

Updates the parameters of a single Cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.update_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_update_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.update_node_pool
    
    
    update_node_pool(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.UpdateNodePoolRequest, dict
            ]
        ] = None,
        *,
        node_pool: typing.Optional[
            google.cloud.edgecontainer_v1.types.resources.NodePool
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

Updates the parameters of a single NodePool.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.update_node_pool](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_update_node_pool)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.upgrade_cluster
    
    
    upgrade_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.edgecontainer_v1.types.service.UpgradeClusterRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        target_version: typing.Optional[str] = None,
        schedule: typing.Optional[
            google.cloud.edgecontainer_v1.types.service.UpgradeClusterRequest.Schedule
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

Upgrades a single cluster.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.upgrade_cluster](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_upgrade_cluster)

### google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.vpn_connection_path
    
    
    vpn_connection_path(project: str, location: str, vpn_connection: str) -> str

Returns a fully-qualified vpn_connection string.

See more: [google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient.vpn_connection_path](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.EdgeContainerClient#google_cloud_edgecontainer_v1_services_edge_container_EdgeContainerClient_vpn_connection_path)

### google.cloud.edgecontainer_v1.services.edge_container.pagers.ListClustersAsyncPager
    
    
    ListClustersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.edgecontainer_v1.types.service.ListClustersResponse
            ],
        ],
        request: google.cloud.edgecontainer_v1.types.service.ListClustersRequest,
        response: google.cloud.edgecontainer_v1.types.service.ListClustersResponse,
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.pagers.ListClustersAsyncPager](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.pagers.ListClustersAsyncPager#google_cloud_edgecontainer_v1_services_edge_container_pagers_ListClustersAsyncPager_ListClustersAsyncPager)

### google.cloud.edgecontainer_v1.services.edge_container.pagers.ListClustersPager
    
    
    ListClustersPager(
        method: typing.Callable[
            [...], google.cloud.edgecontainer_v1.types.service.ListClustersResponse
        ],
        request: google.cloud.edgecontainer_v1.types.service.ListClustersRequest,
        response: google.cloud.edgecontainer_v1.types.service.ListClustersResponse,
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.pagers.ListClustersPager](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.pagers.ListClustersPager#google_cloud_edgecontainer_v1_services_edge_container_pagers_ListClustersPager_ListClustersPager)

### google.cloud.edgecontainer_v1.services.edge_container.pagers.ListMachinesAsyncPager
    
    
    ListMachinesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.edgecontainer_v1.types.service.ListMachinesResponse
            ],
        ],
        request: google.cloud.edgecontainer_v1.types.service.ListMachinesRequest,
        response: google.cloud.edgecontainer_v1.types.service.ListMachinesResponse,
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.pagers.ListMachinesAsyncPager](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.pagers.ListMachinesAsyncPager#google_cloud_edgecontainer_v1_services_edge_container_pagers_ListMachinesAsyncPager_ListMachinesAsyncPager)

### google.cloud.edgecontainer_v1.services.edge_container.pagers.ListMachinesPager
    
    
    ListMachinesPager(
        method: typing.Callable[
            [...], google.cloud.edgecontainer_v1.types.service.ListMachinesResponse
        ],
        request: google.cloud.edgecontainer_v1.types.service.ListMachinesRequest,
        response: google.cloud.edgecontainer_v1.types.service.ListMachinesResponse,
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.pagers.ListMachinesPager](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.pagers.ListMachinesPager#google_cloud_edgecontainer_v1_services_edge_container_pagers_ListMachinesPager_ListMachinesPager)

### google.cloud.edgecontainer_v1.services.edge_container.pagers.ListNodePoolsAsyncPager
    
    
    ListNodePoolsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.edgecontainer_v1.types.service.ListNodePoolsResponse
            ],
        ],
        request: google.cloud.edgecontainer_v1.types.service.ListNodePoolsRequest,
        response: google.cloud.edgecontainer_v1.types.service.ListNodePoolsResponse,
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.pagers.ListNodePoolsAsyncPager](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.pagers.ListNodePoolsAsyncPager#google_cloud_edgecontainer_v1_services_edge_container_pagers_ListNodePoolsAsyncPager_ListNodePoolsAsyncPager)

### google.cloud.edgecontainer_v1.services.edge_container.pagers.ListNodePoolsPager
    
    
    ListNodePoolsPager(
        method: typing.Callable[
            [...], google.cloud.edgecontainer_v1.types.service.ListNodePoolsResponse
        ],
        request: google.cloud.edgecontainer_v1.types.service.ListNodePoolsRequest,
        response: google.cloud.edgecontainer_v1.types.service.ListNodePoolsResponse,
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.pagers.ListNodePoolsPager](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.pagers.ListNodePoolsPager#google_cloud_edgecontainer_v1_services_edge_container_pagers_ListNodePoolsPager_ListNodePoolsPager)

### google.cloud.edgecontainer_v1.services.edge_container.pagers.ListVpnConnectionsAsyncPager
    
    
    ListVpnConnectionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.edgecontainer_v1.types.service.ListVpnConnectionsResponse
            ],
        ],
        request: google.cloud.edgecontainer_v1.types.service.ListVpnConnectionsRequest,
        response: google.cloud.edgecontainer_v1.types.service.ListVpnConnectionsResponse,
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.pagers.ListVpnConnectionsAsyncPager](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.pagers.ListVpnConnectionsAsyncPager#google_cloud_edgecontainer_v1_services_edge_container_pagers_ListVpnConnectionsAsyncPager_ListVpnConnectionsAsyncPager)

### google.cloud.edgecontainer_v1.services.edge_container.pagers.ListVpnConnectionsPager
    
    
    ListVpnConnectionsPager(
        method: typing.Callable[
            [...], google.cloud.edgecontainer_v1.types.service.ListVpnConnectionsResponse
        ],
        request: google.cloud.edgecontainer_v1.types.service.ListVpnConnectionsRequest,
        response: google.cloud.edgecontainer_v1.types.service.ListVpnConnectionsResponse,
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

See more: [google.cloud.edgecontainer_v1.services.edge_container.pagers.ListVpnConnectionsPager](https://cloud.google.com/python/docs/reference/edgecontainer/latest/google.cloud.edgecontainer_v1.services.edge_container.pagers.ListVpnConnectionsPager#google_cloud_edgecontainer_v1_services_edge_container_pagers_ListVpnConnectionsPager_ListVpnConnectionsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
