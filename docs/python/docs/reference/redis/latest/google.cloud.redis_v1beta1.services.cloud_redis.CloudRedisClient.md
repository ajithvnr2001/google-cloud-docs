---
url: https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient
title: Class CloudRedisClient (2.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:22.471916+00:00
---

# Class CloudRedisClient (2.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CloudRedisClient (2.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.23.0 (latest)  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.1  2.15.5  2.14.0  2.13.1  2.12.1  2.11.1  2.10.0  2.9.3  2.8.1  2.7.1  2.6.0  2.5.1  2.4.1  2.3.0  2.2.4  2.1.1  2.0.0  1.0.2  0.4.0  0.3.0 
    
    
    CloudRedisClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.redis_v1beta1.services.cloud_redis.transports.base.CloudRedisTransport,
                typing.Callable[
                    [...],
                    google.cloud.redis_v1beta1.services.cloud_redis.transports.base.CloudRedisTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Configures and manages Cloud Memorystore for Redis instances

Google Cloud Memorystore for Redis v1beta1

The `redis.googleapis.com` service implements the Google Cloud Memorystore for Redis API and defines the following resource model for managing Redis instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Redis instances, named: `/instances/*`
  * As such, Redis instances are resources of the form: `/projects/{project_id}/locations/{location_id}/instances/{instance_id}`



Note that location_id must be referring to a GCP `region`; for example:

  * `projects/redpepper-1290/locations/us-central1/instances/my-redis`



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
`CloudRedisTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CloudRedisClient
    
    
    CloudRedisClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.redis_v1beta1.services.cloud_redis.transports.base.CloudRedisTransport,
                typing.Callable[
                    [...],
                    google.cloud.redis_v1beta1.services.cloud_redis.transports.base.CloudRedisTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud redis client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CloudRedisTransport,Callable[..., CloudRedisTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the CloudRedisTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.CreateInstanceRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance_id: typing.Optional[str] = None,
        instance: typing.Optional[
            google.cloud.redis_v1beta1.types.cloud_redis.Instance
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

Creates a Redis instance based on the specified tier and memory size.

By default, the instance is accessible from the project's `default network <https://cloud.google.com/vpc/docs/vpc>`__.

The creation is executed asynchronously and callers may check the returned operation to track its progress. Once the operation is completed the Redis instance will be fully functional. The completed longrunning.Operation will contain the new instance object in the response field.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_create_instance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        instance = redis_v1beta1.[Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance.html)()
        instance.name = "name_value"
        instance.tier = "STANDARD_HA"
        instance.memory_size_gb = 1499
    
        request = redis_v1beta1.[CreateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.CreateInstanceRequest.html)(
            parent="parent_value",
            instance_id="instance_id_value",
            instance=instance,
        )
    
        # Make the request
        operation = client.[create_instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_create_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.CreateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.CreateInstanceRequest), dict]`   
The request object. Request for CreateInstance.  
`parent` |  `str`   
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`instance_id` |  `str`   
Required. The logical name of the Redis instance in the customer project with the following restrictions: - Must contain only lowercase letters, numbers, and hyphens. - Must start with a letter. - Must be between 1-40 characters. - Must end with a number or a letter. - Must be unique within the customer project / location This corresponds to the `instance_id` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `[google.cloud.redis_v1beta1.types.Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance)`   
Required. A Redis [Instance] resource This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance) A Memorystore for Redis instance.  
  
### delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.DeleteInstanceRequest, dict
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

Deletes a specific Redis instance. Instance stops serving and data is deleted.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_delete_instance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        request = redis_v1beta1.[DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.DeleteInstanceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_delete_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.DeleteInstanceRequest), dict]`   
The request object. Request for DeleteInstance.  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### export_instance
    
    
    export_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.ExportInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.redis_v1beta1.types.cloud_redis.OutputConfig
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

Export Redis instance data into a Redis RDB format file in Cloud Storage. Redis will continue serving during this operation.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_export_instance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        output_config = redis_v1beta1.[OutputConfig](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.OutputConfig.html)()
        output_config.gcs_destination.uri = "uri_value"
    
        request = redis_v1beta1.[ExportInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.ExportInstanceRequest.html)(
            name="name_value",
            output_config=output_config,
        )
    
        # Make the request
        operation = client.[export_instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_export_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.ExportInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.ExportInstanceRequest), dict]`   
The request object. Request for Export.  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`output_config` |  `[google.cloud.redis_v1beta1.types.OutputConfig](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.OutputConfig)`   
Required. Specify data to be exported. This corresponds to the `output_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance) A Memorystore for Redis instance.  
  
### failover_instance
    
    
    failover_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.FailoverInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        data_protection_mode: typing.Optional[
            google.cloud.redis_v1beta1.types.cloud_redis.FailoverInstanceRequest.DataProtectionMode
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

Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_failover_instance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        request = redis_v1beta1.[FailoverInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.FailoverInstanceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[failover_instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_failover_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.FailoverInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.FailoverInstanceRequest), dict]`   
The request object. Request for Failover.  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`data_protection_mode` |  `[google.cloud.redis_v1beta1.types.FailoverInstanceRequest.DataProtectionMode](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.FailoverInstanceRequest.DataProtectionMode)`   
Optional. Available data protection modes that the user can choose. If it's unspecified, data protection mode will be LIMITED_DATA_LOSS by default. This corresponds to the `data_protection_mode` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance) A Memorystore for Redis instance.  
  
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
`CloudRedisClient` | The constructed client.  
  
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
`CloudRedisClient` | The constructed client.  
  
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
`CloudRedisClient` | The constructed client.  
  
### get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.GetInstanceRequest, dict
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
    ) -> google.cloud.redis_v1beta1.types.cloud_redis.Instance

Gets the details of a specific Redis instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_get_instance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        request = redis_v1beta1.[GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.GetInstanceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_get_instance)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.GetInstanceRequest), dict]`   
The request object. Request for GetInstance.  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_v1beta1.types.Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance)` | A Memorystore for Redis instance.  
  
### get_instance_auth_string
    
    
    get_instance_auth_string(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.GetInstanceAuthStringRequest,
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
    ) -> google.cloud.redis_v1beta1.types.cloud_redis.InstanceAuthString

Gets the AUTH string for a Redis instance. If AUTH is not enabled for the instance the response will be empty. This information is not included in the details returned to GetInstance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_get_instance_auth_string():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        request = redis_v1beta1.[GetInstanceAuthStringRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.GetInstanceAuthStringRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_instance_auth_string](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_get_instance_auth_string)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.GetInstanceAuthStringRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.GetInstanceAuthStringRequest), dict]`   
The request object. Request for GetInstanceAuthString.  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_v1beta1.types.InstanceAuthString](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.InstanceAuthString)` | Instance AUTH string details.  
  
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
  
### import_instance
    
    
    import_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.ImportInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.redis_v1beta1.types.cloud_redis.InputConfig
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

Import a Redis RDB snapshot file from Cloud Storage into a Redis instance. Redis may stop serving during this operation. Instance state will be IMPORTING for entire operation. When complete, the instance will contain only data from the imported file.

The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_import_instance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        input_config = redis_v1beta1.[InputConfig](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.InputConfig.html)()
        input_config.gcs_source.uri = "uri_value"
    
        request = redis_v1beta1.[ImportInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.ImportInstanceRequest.html)(
            name="name_value",
            input_config=input_config,
        )
    
        # Make the request
        operation = client.[import_instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_import_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.ImportInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.ImportInstanceRequest), dict]`   
The request object. Request for Import.  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`input_config` |  `[google.cloud.redis_v1beta1.types.InputConfig](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.InputConfig)`   
Required. Specify data to be imported. This corresponds to the `input_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance) A Memorystore for Redis instance.  
  
### instance_path
    
    
    instance_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified instance string.

### list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.ListInstancesRequest, dict
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
    ) -> google.cloud.redis_v1beta1.services.cloud_redis.pagers.ListInstancesPager

Lists all Redis instances owned by a project in either the specified location (region) or all locations.

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
    from google.cloud import redis_v1beta1
    
    def sample_list_instances():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        request = redis_v1beta1.[ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.ListInstancesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_instances](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_list_instances)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.ListInstancesRequest), dict]`   
The request object. Request for ListInstances.  
`parent` |  `str`   
Required. The resource name of the instance location using the form: `projects/{project_id}/locations/{location_id}` where `location_id` refers to a GCP region. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.redis_v1beta1.services.cloud_redis.pagers.ListInstancesPager](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.pagers.ListInstancesPager)` | Response for ListInstances. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

### reschedule_maintenance
    
    
    reschedule_maintenance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.RescheduleMaintenanceRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        reschedule_type: typing.Optional[
            google.cloud.redis_v1beta1.types.cloud_redis.RescheduleMaintenanceRequest.RescheduleType
        ] = None,
        schedule_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Reschedule maintenance for a given instance in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_reschedule_maintenance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        request = redis_v1beta1.[RescheduleMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.RescheduleMaintenanceRequest.html)(
            name="name_value",
            reschedule_type="SPECIFIC_TIME",
        )
    
        # Make the request
        operation = client.[reschedule_maintenance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_reschedule_maintenance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.RescheduleMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.RescheduleMaintenanceRequest), dict]`   
The request object. Request for RescheduleMaintenance.  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`reschedule_type` |  `[google.cloud.redis_v1beta1.types.RescheduleMaintenanceRequest.RescheduleType](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.RescheduleMaintenanceRequest.RescheduleType)`   
Required. If reschedule type is SPECIFIC_TIME, must set up schedule_time as well. This corresponds to the `reschedule_type` field on the `request` instance; if `request` is provided, this should not be set.  
`schedule_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format, for example `2012-11-15T16:19:00.094Z`. This corresponds to the `schedule_time` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance) A Memorystore for Redis instance.  
  
### update_instance
    
    
    update_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.UpdateInstanceRequest, dict
            ]
        ] = None,
        *,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        instance: typing.Optional[
            google.cloud.redis_v1beta1.types.cloud_redis.Instance
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

Updates the metadata and configuration of a specific Redis instance. Completed longrunning.Operation will contain the new instance object in the response field. The returned operation is automatically deleted after a few hours, so there is no need to call DeleteOperation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_update_instance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        instance = redis_v1beta1.[Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance.html)()
        instance.name = "name_value"
        instance.tier = "STANDARD_HA"
        instance.memory_size_gb = 1499
    
        request = redis_v1beta1.[UpdateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.UpdateInstanceRequest.html)(
            instance=instance,
        )
    
        # Make the request
        operation = client.[update_instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_update_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.UpdateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.UpdateInstanceRequest), dict]`   
The request object. Request for UpdateInstance.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. Mask of fields to update. At least one path must be supplied in this field. The elements of the repeated paths field may only include these fields from Instance: - `displayName` \- `labels` \- `memorySizeGb` \- `redisConfig` \- `replica_count` This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`instance` |  `[google.cloud.redis_v1beta1.types.Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance)`   
Required. Update description. Only fields specified in update_mask are updated. This corresponds to the `instance` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be Instance A Memorystore for Redis instance.  
  
### upgrade_instance
    
    
    upgrade_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.redis_v1beta1.types.cloud_redis.UpgradeInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        redis_version: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Upgrades Redis instance to the newer Redis version specified in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import redis_v1beta1
    
    def sample_upgrade_instance():
        # Create a client
        client = redis_v1beta1.[CloudRedisClient](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html)()
    
        # Initialize request argument(s)
        request = redis_v1beta1.[UpgradeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.UpgradeInstanceRequest.html)(
            name="name_value",
            redis_version="redis_version_value",
        )
    
        # Make the request
        operation = client.[upgrade_instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.services.cloud_redis.CloudRedisClient.html#google_cloud_redis_v1beta1_services_cloud_redis_CloudRedisClient_upgrade_instance)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.redis_v1beta1.types.UpgradeInstanceRequest](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.UpgradeInstanceRequest), dict]`   
The request object. Request for UpgradeInstance.  
`name` |  `str`   
Required. Redis instance resource name using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}` where `location_id` refers to a GCP region. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`redis_version` |  `str`   
Required. Specifies the target version of Redis software to upgrade to. This corresponds to the `redis_version` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Instance](https://docs.cloud.google.com/python/docs/reference/redis/latest/google.cloud.redis_v1beta1.types.Instance) A Memorystore for Redis instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
