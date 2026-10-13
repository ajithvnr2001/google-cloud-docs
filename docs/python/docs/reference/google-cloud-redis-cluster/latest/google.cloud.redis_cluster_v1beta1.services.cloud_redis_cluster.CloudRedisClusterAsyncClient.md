---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient
title: Class CloudRedisClusterAsyncClient (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:04.844032+00:00
---

# Class CloudRedisClusterAsyncClient (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudRedisClusterAsyncClient (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.14 
    
    
    CloudRedisClusterAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.transports.base.CloudRedisClusterTransport,
                typing.Callable[
                    [...],
                    google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.transports.base.CloudRedisClusterTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Configures and manages Cloud Memorystore for Redis clusters

Google Cloud Memorystore for Redis Cluster

The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis clusters:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Redis clusters, named: `/clusters/*`
  * As such, Redis clusters are resources of the form: `/projects/{project_id}/locations/{location_id}/clusters/{instance_id}`



Note that location_id must be a GCP `region`; for example:

  * `projects/redpepper-1290/locations/us-central1/clusters/my-redis`



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
`CloudRedisClusterTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CloudRedisClusterAsyncClient
    
    
    CloudRedisClusterAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.transports.base.CloudRedisClusterTransport,
                typing.Callable[
                    [...],
                    google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.transports.base.CloudRedisClusterTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud redis cluster async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CloudRedisClusterTransport,Callable[..., CloudRedisClusterTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the CloudRedisClusterTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### backup_cluster
    
    
    backup_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.BackupClusterRequest,
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

Backup Redis Cluster. If this is the first time a backup is being created, a backup collection will be created at the backend, and this backup belongs to this collection. Both collection and backup will have a resource name. Backup will be executed for each shard. A replica (primary if nonHA) will be selected to perform the execution. Backup call will be rejected if there is an ongoing backup or update operation. Be aware that during preview, if the cluster's internal software version is too old, critical update will be performed before actual backup. Once the internal software version is updated to the minimum version required by the backup feature, subsequent backups will not require critical update. After preview, there will be no critical update needed for backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_backup_cluster():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[BackupClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.BackupClusterRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[backup_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_backup_cluster)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.BackupClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.BackupClusterRequest), dict]]`   
The request object. Request for [BackupCluster].  
`name` |  ``str``   
Required. Redis cluster resource name using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster) A cluster instance.  
  
### backup_collection_path
    
    
    backup_collection_path(project: str, location: str, backup_collection: str) -> str

Returns a fully-qualified backup_collection string.

### backup_path
    
    
    backup_path(
        project: str, location: str, backup_collection: str, backup: str
    ) -> str

Returns a fully-qualified backup string.

### ca_pool_path
    
    
    ca_pool_path(project: str, location: str, ca_pool: str) -> str

Returns a fully-qualified ca_pool string.

### cancel_operation
    
    
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

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.CancelOperationRequest``   
The request object. Request message for `CancelOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### certificate_authority_path
    
    
    certificate_authority_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified certificate_authority string.

### cluster_path
    
    
    cluster_path(project: str, location: str, cluster: str) -> str

Returns a fully-qualified cluster string.

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

### create_cluster
    
    
    create_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.CreateClusterRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        cluster: typing.Optional[
            google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.Cluster
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

Creates a Redis cluster based on the specified properties. The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis cluster will be fully functional. The completed longrunning.Operation will contain the new cluster object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_create_cluster():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        cluster = redis_cluster_v1beta1.[Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster.html)()
        cluster.name = "name_value"
    
        request = redis_cluster_v1beta1.[CreateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CreateClusterRequest.html)(
            parent="parent_value",
            cluster_id="cluster_id_value",
            cluster=cluster,
        )
    
        # Make the request
        operation = await client.[create_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_create_cluster)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.CreateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CreateClusterRequest), dict]]`   
The request object. Request for `CreateCluster][CloudRedis.CreateCluster]`.  
`parent` |  ``str``   
Required. The resource name of the cluster location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`cluster` |  `[Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster)`   
Required. The cluster that is to be created. This corresponds to the `cluster` field on the `request` instance; if `request` is provided, this should not be set.  
`cluster_id` |  ``str``   
Required. The logical name of the Redis cluster in the customer project with the following restrictions: - Must contain only lowercase letters, numbers, and hyphens. - Must start with a letter. - Must be between 1-63 characters. - Must end with a number or a letter. - Must be unique within the customer project / location This corresponds to the `cluster_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster) A cluster instance.  
  
### crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

### crypto_key_version_path
    
    
    crypto_key_version_path(
        project: str, location: str, key_ring: str, crypto_key: str, crypto_key_version: str
    ) -> str

Returns a fully-qualified crypto_key_version string.

### delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.DeleteBackupRequest,
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

Deletes a specific backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_delete_backup():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.DeleteBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_backup](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_delete_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.DeleteBackupRequest), dict]]`   
The request object. Request for [DeleteBackup].  
`name` |  ``str``   
Required. Redis backup resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_cluster
    
    
    delete_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.DeleteClusterRequest,
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

Deletes a specific Redis cluster. Cluster stops serving and data is deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_delete_cluster():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[DeleteClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.DeleteClusterRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_delete_cluster)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.DeleteClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.DeleteClusterRequest), dict]]`   
The request object. Request for `DeleteCluster][CloudRedis.DeleteCluster]`.  
`name` |  ``str``   
Required. Redis cluster resource name using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_operation
    
    
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

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.DeleteOperationRequest``   
The request object. Request message for `DeleteOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### export_backup
    
    
    export_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ExportBackupRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Exports a specific backup to a customer target Cloud Storage URI.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_export_backup():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[ExportBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ExportBackupRequest.html)(
            gcs_bucket="gcs_bucket_value",
            name="name_value",
        )
    
        # Make the request
        operation = await client.[export_backup](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_export_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.ExportBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ExportBackupRequest), dict]]`   
The request object. Request for [ExportBackup].  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Backup](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Backup) Backup of a cluster.  
  
### forwarding_rule_path
    
    
    forwarding_rule_path(project: str, region: str, forwarding_rule: str) -> str

Returns a fully-qualified forwarding_rule string.

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
`CloudRedisClusterAsyncClient` | The constructed client.  
  
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
`CloudRedisClusterAsyncClient` | The constructed client.  
  
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
`CloudRedisClusterAsyncClient` | The constructed client.  
  
### get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.GetBackupRequest,
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
    ) -> google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.Backup

Gets the details of a specific backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_get_backup():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_backup](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_get_backup)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetBackupRequest), dict]]`   
The request object. Request for [GetBackup].  
`name` |  ``str``   
Required. Redis backup resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}/backups/{backup_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_cluster_v1beta1.types.Backup](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Backup)` | Backup of a cluster.  
  
### get_backup_collection
    
    
    get_backup_collection(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.GetBackupCollectionRequest,
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
    ) -> google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.BackupCollection

Get a backup collection.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_get_backup_collection():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[GetBackupCollectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetBackupCollectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_backup_collection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_get_backup_collection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.GetBackupCollectionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetBackupCollectionRequest), dict]]`   
The request object. Request for [GetBackupCollection].  
`name` |  ``str``   
Required. Redis backupCollection resource name using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_cluster_v1beta1.types.BackupCollection](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.BackupCollection)` | BackupCollection of a cluster.  
  
### get_cluster
    
    
    get_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.GetClusterRequest,
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
    ) -> google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.Cluster

Gets the details of a specific Redis cluster.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_get_cluster():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[GetClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetClusterRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_get_cluster)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.GetClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetClusterRequest), dict]]`   
The request object. Request for `GetCluster][CloudRedis.GetCluster]`.  
`name` |  ``str``   
Required. Redis cluster resource name using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_cluster_v1beta1.types.Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster)` | A cluster instance.  
  
### get_cluster_certificate_authority
    
    
    get_cluster_certificate_authority(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.GetClusterCertificateAuthorityRequest,
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
    ) -> google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.CertificateAuthority

Gets the details of certificate authority information for Redis cluster.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_get_cluster_certificate_authority():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetClusterCertificateAuthorityRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_cluster_certificate_authority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_get_cluster_certificate_authority)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.GetClusterCertificateAuthorityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetClusterCertificateAuthorityRequest), dict]]`   
The request object. Request for `GetClusterCertificateAuthorityRequest][CloudRedis.GetClusterCertificateAuthorityRequest]`.  
`name` |  ``str``   
Required. Redis cluster certificate authority resource name using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}/certificateAuthority` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_cluster_v1beta1.types.CertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.CertificateAuthority)` | Redis cluster certificate authority  
  
### get_location
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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

Return the API endpoint and client cert source for mutual TLS.

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
  
### get_operation
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.GetOperationRequest``   
The request object. Request message for `GetOperation` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### get_shared_regional_certificate_authority
    
    
    get_shared_regional_certificate_authority(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.GetSharedRegionalCertificateAuthorityRequest,
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
    ) -> (
        google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.SharedRegionalCertificateAuthority
    )

Gets the details of regional certificate authority information for Redis cluster.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_get_shared_regional_certificate_authority():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetSharedRegionalCertificateAuthorityRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_shared_regional_certificate_authority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_get_shared_regional_certificate_authority)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.GetSharedRegionalCertificateAuthorityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.GetSharedRegionalCertificateAuthorityRequest), dict]]`   
The request object. Request for `GetSharedRegionalCertificateAuthority][CloudRedis.GetSharedRegionalCertificateAuthority]`.  
`name` |  ``str``   
Required. Regional certificate authority resource name using the form: `projects/{project_id}/locations/{location_id}/sharedRegionalCertificateAuthority` where `location_id` refers to a Google Cloud region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_cluster_v1beta1.types.SharedRegionalCertificateAuthority](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.SharedRegionalCertificateAuthority)` | Shared regional certificate authority  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.transports.base.CloudRedisClusterTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_backup_collections
    
    
    list_backup_collections(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupCollectionsRequest,
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
        google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupCollectionsAsyncPager
    )

Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_list_backup_collections():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[ListBackupCollectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backup_collections](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_list_backup_collections)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsRequest), dict]]`   
The request object. Request for [ListBackupCollections]  
`parent` |  ``str``   
Required. The resource name of the backupCollection location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupCollectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupCollectionsAsyncPager)` | Response for [ListBackupCollections]. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupsRequest,
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
        google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupsAsyncPager
    )

Lists all backups owned by a backup collection.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_list_backups():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backups](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_list_backups)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsRequest), dict]]`   
The request object. Request for [ListBackups].  
`parent` |  ``str``   
Required. The resource name of the backupCollection using the form: `projects/{project_id}/locations/{location_id}/backupCollections/{backup_collection_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupsAsyncPager)` | Response for [ListBackups]. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_clusters
    
    
    list_clusters(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListClustersRequest,
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
        google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListClustersAsyncPager
    )

Lists all Redis clusters owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{project_id}/locations/{location_id}`



If `location_id` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_list_clusters():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[ListClustersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_clusters](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_list_clusters)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.ListClustersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersRequest), dict]]`   
The request object. Request for `ListClusters][CloudRedis.ListClusters]`.  
`parent` |  ``str``   
Required. The resource name of the cluster location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListClustersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListClustersAsyncPager)` | Response for `ListClusters][CloudRedis.ListClusters]`. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locations
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.ListLocationsResponse`` | Response message for `ListLocations` method.  
  
### list_operations
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.ListOperationsRequest``   
The request object. Request message for `ListOperations` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
### network_path
    
    
    network_path(project: str, network: str) -> str

Returns a fully-qualified network string.

### parse_backup_collection_path
    
    
    parse_backup_collection_path(path: str) -> typing.Dict[str, str]

Parses a backup_collection path into its component segments.

### parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

### parse_ca_pool_path
    
    
    parse_ca_pool_path(path: str) -> typing.Dict[str, str]

Parses a ca_pool path into its component segments.

### parse_certificate_authority_path
    
    
    parse_certificate_authority_path(path: str) -> typing.Dict[str, str]

Parses a certificate_authority path into its component segments.

### parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

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

### parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

### parse_crypto_key_version_path
    
    
    parse_crypto_key_version_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key_version path into its component segments.

### parse_forwarding_rule_path
    
    
    parse_forwarding_rule_path(path: str) -> typing.Dict[str, str]

Parses a forwarding_rule path into its component segments.

### parse_network_path
    
    
    parse_network_path(path: str) -> typing.Dict[str, str]

Parses a network path into its component segments.

### parse_service_attachment_path
    
    
    parse_service_attachment_path(path: str) -> typing.Dict[str, str]

Parses a service_attachment path into its component segments.

### parse_shared_regional_certificate_authority_path
    
    
    parse_shared_regional_certificate_authority_path(
        path: str,
    ) -> typing.Dict[str, str]

Parses a shared_regional_certificate_authority path into its component segments.

### reschedule_cluster_maintenance
    
    
    reschedule_cluster_maintenance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.RescheduleClusterMaintenanceRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        reschedule_type: typing.Optional[
            google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.RescheduleClusterMaintenanceRequest.RescheduleType
        ] = None,
        schedule_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Reschedules upcoming maintenance event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_reschedule_cluster_maintenance():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        request = redis_cluster_v1beta1.[RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest.html)(
            name="name_value",
            reschedule_type="SPECIFIC_TIME",
        )
    
        # Make the request
        operation = await client.[reschedule_cluster_maintenance](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_reschedule_cluster_maintenance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest), dict]]`   
The request object. Request for rescheduling a cluster maintenance.  
`name` |  ``str``   
Required. Redis Cluster instance resource name using the form: `projects/{project_id}/locations/{location_id}/clusters/{cluster_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`reschedule_type` |  `[RescheduleType](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.RescheduleClusterMaintenanceRequest.RescheduleType)`   
Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well. This corresponds to the `reschedule_type` field on the `request` instance; if `request` is provided, this should not be set.  
`schedule_time` |  ``google.protobuf.timestamp_pb2.Timestamp``   
Optional. Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`. This corresponds to the `schedule_time` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster) A cluster instance.  
  
### service_attachment_path
    
    
    service_attachment_path(project: str, region: str, service_attachment: str) -> str

Returns a fully-qualified service_attachment string.

### shared_regional_certificate_authority_path
    
    
    shared_regional_certificate_authority_path(project: str, location: str) -> str

Returns a fully-qualified shared_regional_certificate_authority string.

### update_cluster
    
    
    update_cluster(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.UpdateClusterRequest,
                dict,
            ]
        ] = None,
        *,
        cluster: typing.Optional[
            google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.Cluster
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

Updates the metadata and configuration of a specific Redis cluster. Completed longrunning.Operation will contain the new cluster object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_cluster_v1beta1
    
    async def sample_update_cluster():
        # Create a client
        client = redis_cluster_v1beta1.[CloudRedisClusterAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html)()
    
        # Initialize request argument(s)
        cluster = redis_cluster_v1beta1.[Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster.html)()
        cluster.name = "name_value"
    
        request = redis_cluster_v1beta1.[UpdateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.UpdateClusterRequest.html)(
            cluster=cluster,
        )
    
        # Make the request
        operation = await client.[update_cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.CloudRedisClusterAsyncClient.html#google_cloud_redis_cluster_v1beta1_services_cloud_redis_cluster_CloudRedisClusterAsyncClient_update_cluster)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.redis_cluster_v1beta1.types.UpdateClusterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.UpdateClusterRequest), dict]]`   
The request object. Request for `UpdateCluster][CloudRedis.UpdateCluster]`.  
`cluster` |  `[Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster)`   
Required. Update description. Only fields specified in update_mask are updated. This corresponds to the `cluster` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from [Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster): - `size_gb` \- `replica_count` This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Cluster](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.Cluster) A cluster instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
