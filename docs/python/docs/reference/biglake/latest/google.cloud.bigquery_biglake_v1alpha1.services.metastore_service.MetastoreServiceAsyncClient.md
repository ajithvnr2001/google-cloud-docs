---
url: https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient
title: Class MetastoreServiceAsyncClient (0.8.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:35.258396+00:00
---

# Class MetastoreServiceAsyncClient (0.8.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MetastoreServiceAsyncClient (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.8.0  0.7.0  0.6.0  0.5.0  0.4.15  0.3.0  0.2.0  0.1.1 
    
    
    MetastoreServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.transports.base.MetastoreServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.transports.base.MetastoreServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

BigLake Metastore is a serverless, highly available, multi-tenant runtime metastore for Google Cloud Data Analytics products.

The BigLake Metastore API defines the following resource model:

  * A collection of Google Cloud projects: `/projects/*`
  * Each project has a collection of available locations: `/locations/*`
  * Each location has a collection of catalogs: `/catalogs/*`
  * Each catalog has a collection of databases: `/databases/*`
  * Each database has a collection of tables: `/tables/*`



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
`MetastoreServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### MetastoreServiceAsyncClient
    
    
    MetastoreServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.transports.base.MetastoreServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.transports.base.MetastoreServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the metastore service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,MetastoreServiceTransport,Callable[..., MetastoreServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the MetastoreServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### catalog_path
    
    
    catalog_path(project: str, location: str, catalog: str) -> str

Returns a fully-qualified catalog string.

### check_lock
    
    
    check_lock(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.CheckLockRequest,
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Lock

Checks the state of a lock specified by the lock ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_check_lock():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[CheckLockRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CheckLockRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[check_lock](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_check_lock)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.CheckLockRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CheckLockRequest), dict]]`   
The request object. Request message for the CheckLock method.  
`name` |  ``str``   
Required. The name of the lock to check. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/locks/{lock_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Lock](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Lock)` | Represents a lock.  
  
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

### create_catalog
    
    
    create_catalog(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.CreateCatalogRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        catalog: typing.Optional[
            google.cloud.bigquery_biglake_v1alpha1.types.metastore.Catalog
        ] = None,
        catalog_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Catalog

Creates a new catalog.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_create_catalog():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[CreateCatalogRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CreateCatalogRequest.html)(
            parent="parent_value",
            catalog_id="catalog_id_value",
        )
    
        # Make the request
        response = await client.[create_catalog](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_create_catalog)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.CreateCatalogRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CreateCatalogRequest), dict]]`   
The request object. Request message for the CreateCatalog method.  
`parent` |  ``str``   
Required. The parent resource where this catalog will be created. Format: projects/{project_id_or_number}/locations/{location_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`catalog` |  `[Catalog](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Catalog)`   
Required. The catalog to create. The `name` field does not need to be provided. This corresponds to the `catalog` field on the `request` instance; if `request` is provided, this should not be set.  
`catalog_id` |  ``str``   
Required. The ID to use for the catalog, which will become the final component of the catalog's resource name. This corresponds to the `catalog_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Catalog](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Catalog)` | Catalog is the container of databases.  
  
### create_database
    
    
    create_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.CreateDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        database: typing.Optional[
            google.cloud.bigquery_biglake_v1alpha1.types.metastore.Database
        ] = None,
        database_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Database

Creates a new database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_create_database():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[CreateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CreateDatabaseRequest.html)(
            parent="parent_value",
            database_id="database_id_value",
        )
    
        # Make the request
        response = await client.[create_database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_create_database)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.CreateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CreateDatabaseRequest), dict]]`   
The request object. Request message for the CreateDatabase method.  
`parent` |  ``str``   
Required. The parent resource where this database will be created. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`database` |  `[Database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Database)`   
Required. The database to create. The `name` field does not need to be provided. This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`database_id` |  ``str``   
Required. The ID to use for the database, which will become the final component of the database's resource name. This corresponds to the `database_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Database)` | Database is the container of tables.  
  
### create_lock
    
    
    create_lock(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.CreateLockRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        lock: typing.Optional[
            google.cloud.bigquery_biglake_v1alpha1.types.metastore.Lock
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Lock

Creates a new lock.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_create_lock():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        lock = bigquery_biglake_v1alpha1.[Lock](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Lock.html)()
        lock.table_id = "table_id_value"
    
        request = bigquery_biglake_v1alpha1.[CreateLockRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CreateLockRequest.html)(
            parent="parent_value",
            lock=lock,
        )
    
        # Make the request
        response = await client.[create_lock](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_create_lock)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.CreateLockRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CreateLockRequest), dict]]`   
The request object. Request message for the CreateLock method.  
`parent` |  ``str``   
Required. The parent resource where this lock will be created. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`lock` |  `[Lock](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Lock)`   
Required. The lock to create. The `name` field does not need to be provided for the lock creation. This corresponds to the `lock` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Lock](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Lock)` | Represents a lock.  
  
### create_table
    
    
    create_table(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.CreateTableRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        table: typing.Optional[
            google.cloud.bigquery_biglake_v1alpha1.types.metastore.Table
        ] = None,
        table_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Table

Creates a new table.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_create_table():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[CreateTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CreateTableRequest.html)(
            parent="parent_value",
            table_id="table_id_value",
        )
    
        # Make the request
        response = await client.[create_table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_create_table)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.CreateTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.CreateTableRequest), dict]]`   
The request object. Request message for the CreateTable method.  
`parent` |  ``str``   
Required. The parent resource where this table will be created. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`table` |  `[Table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Table)`   
Required. The table to create. The `name` field does not need to be provided for the table creation. This corresponds to the `table` field on the `request` instance; if `request` is provided, this should not be set.  
`table_id` |  ``str``   
Required. The ID to use for the table, which will become the final component of the table's resource name. This corresponds to the `table_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Table)` | Represents a table.  
  
### database_path
    
    
    database_path(project: str, location: str, catalog: str, database: str) -> str

Returns a fully-qualified database string.

### delete_catalog
    
    
    delete_catalog(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.DeleteCatalogRequest,
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Catalog

Deletes an existing catalog specified by the catalog ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_delete_catalog():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[DeleteCatalogRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.DeleteCatalogRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[delete_catalog](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_delete_catalog)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.DeleteCatalogRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.DeleteCatalogRequest), dict]]`   
The request object. Request message for the DeleteCatalog method.  
`name` |  ``str``   
Required. The name of the catalog to delete. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Catalog](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Catalog)` | Catalog is the container of databases.  
  
### delete_database
    
    
    delete_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.DeleteDatabaseRequest,
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Database

Deletes an existing database specified by the database ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_delete_database():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[DeleteDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.DeleteDatabaseRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[delete_database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_delete_database)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.DeleteDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.DeleteDatabaseRequest), dict]]`   
The request object. Request message for the DeleteDatabase method.  
`name` |  ``str``   
Required. The name of the database to delete. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Database)` | Database is the container of tables.  
  
### delete_lock
    
    
    delete_lock(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.DeleteLockRequest,
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

Deletes an existing lock specified by the lock ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_delete_lock():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[DeleteLockRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.DeleteLockRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_lock](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_delete_lock)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.DeleteLockRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.DeleteLockRequest), dict]]`   
The request object. Request message for the DeleteLock method.  
`name` |  ``str``   
Required. The name of the lock to delete. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/locks/{lock_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_table
    
    
    delete_table(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.DeleteTableRequest,
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Table

Deletes an existing table specified by the table ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_delete_table():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[DeleteTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.DeleteTableRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[delete_table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_delete_table)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.DeleteTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.DeleteTableRequest), dict]]`   
The request object. Request message for the DeleteTable method.  
`name` |  ``str``   
Required. The name of the table to delete. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Table)` | Represents a table.  
  
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
`MetastoreServiceAsyncClient` | The constructed client.  
  
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
`MetastoreServiceAsyncClient` | The constructed client.  
  
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
`MetastoreServiceAsyncClient` | The constructed client.  
  
### get_catalog
    
    
    get_catalog(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.GetCatalogRequest,
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Catalog

Gets the catalog specified by the resource name.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_get_catalog():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[GetCatalogRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.GetCatalogRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_catalog](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_get_catalog)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.GetCatalogRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.GetCatalogRequest), dict]]`   
The request object. Request message for the GetCatalog method.  
`name` |  ``str``   
Required. The name of the catalog to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Catalog](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Catalog)` | Catalog is the container of databases.  
  
### get_database
    
    
    get_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.GetDatabaseRequest,
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Database

Gets the database specified by the resource name.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_get_database():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[GetDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.GetDatabaseRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_get_database)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.GetDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.GetDatabaseRequest), dict]]`   
The request object. Request message for the GetDatabase method.  
`name` |  ``str``   
Required. The name of the database to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Database)` | Database is the container of tables.  
  
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
  
### get_table
    
    
    get_table(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.GetTableRequest, dict
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Table

Gets the table specified by the resource name.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_get_table():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[GetTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.GetTableRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_get_table)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.GetTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.GetTableRequest), dict]]`   
The request object. Request message for the GetTable method.  
`name` |  ``str``   
Required. The name of the table to retrieve. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Table)` | Represents a table.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.transports.base.MetastoreServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_catalogs
    
    
    list_catalogs(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.ListCatalogsRequest,
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
        google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListCatalogsAsyncPager
    )

List all catalogs in a specified project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_list_catalogs():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[ListCatalogsRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_catalogs](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_list_catalogs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.ListCatalogsRequest), dict]]`   
The request object. Request message for the ListCatalogs method.  
`parent` |  ``str``   
Required. The parent, which owns this collection of catalogs. Format: projects/{project_id_or_number}/locations/{location_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListCatalogsAsyncPager](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListCatalogsAsyncPager)` | Response message for the ListCatalogs method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_databases
    
    
    list_databases(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.ListDatabasesRequest,
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
        google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListDatabasesAsyncPager
    )

List all databases in a specified catalog.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_list_databases():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[ListDatabasesRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_databases](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_list_databases)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.ListDatabasesRequest), dict]]`   
The request object. Request message for the ListDatabases method.  
`parent` |  ``str``   
Required. The parent, which owns this collection of databases. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListDatabasesAsyncPager](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListDatabasesAsyncPager)` | Response message for the ListDatabases method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locks
    
    
    list_locks(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.ListLocksRequest,
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
        google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListLocksAsyncPager
    )

List all locks in a specified database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_list_locks():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[ListLocksRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.ListLocksRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_locks](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_list_locks)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.ListLocksRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.ListLocksRequest), dict]]`   
The request object. Request message for the ListLocks method.  
`parent` |  ``str``   
Required. The parent, which owns this collection of locks. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListLocksAsyncPager](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListLocksAsyncPager)` | Response message for the ListLocks method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_tables
    
    
    list_tables(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.ListTablesRequest,
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
        google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListTablesAsyncPager
    )

List all tables in a specified database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_list_tables():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[ListTablesRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.ListTablesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_tables](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_list_tables)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.ListTablesRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.ListTablesRequest), dict]]`   
The request object. Request message for the ListTables method.  
`parent` |  ``str``   
Required. The parent, which owns this collection of tables. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListTablesAsyncPager](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.pagers.ListTablesAsyncPager)` | Response message for the ListTables method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### lock_path
    
    
    lock_path(
        project: str, location: str, catalog: str, database: str, lock: str
    ) -> str

Returns a fully-qualified lock string.

### parse_catalog_path
    
    
    parse_catalog_path(path: str) -> typing.Dict[str, str]

Parses a catalog path into its component segments.

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

### parse_database_path
    
    
    parse_database_path(path: str) -> typing.Dict[str, str]

Parses a database path into its component segments.

### parse_lock_path
    
    
    parse_lock_path(path: str) -> typing.Dict[str, str]

Parses a lock path into its component segments.

### parse_table_path
    
    
    parse_table_path(path: str) -> typing.Dict[str, str]

Parses a table path into its component segments.

### rename_table
    
    
    rename_table(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.RenameTableRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        new_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Table

Renames an existing table specified by the table ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_rename_table():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[RenameTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.RenameTableRequest.html)(
            name="name_value",
            new_name="new_name_value",
        )
    
        # Make the request
        response = await client.[rename_table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_rename_table)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.RenameTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.RenameTableRequest), dict]]`   
The request object. Request message for the RenameTable method in MetastoreService  
`name` |  ``str``   
Required. The table's `name` field is used to identify the table to rename. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`new_name` |  ``str``   
Required. The new `name` for the specified table, must be in the same database. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id} This corresponds to the `new_name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Table)` | Represents a table.  
  
### table_path
    
    
    table_path(
        project: str, location: str, catalog: str, database: str, table: str
    ) -> str

Returns a fully-qualified table string.

### update_database
    
    
    update_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.UpdateDatabaseRequest,
                dict,
            ]
        ] = None,
        *,
        database: typing.Optional[
            google.cloud.bigquery_biglake_v1alpha1.types.metastore.Database
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Database

Updates an existing database specified by the database ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_update_database():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[UpdateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.UpdateDatabaseRequest.html)(
        )
    
        # Make the request
        response = await client.[update_database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_update_database)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.UpdateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.UpdateDatabaseRequest), dict]]`   
The request object. Request message for the UpdateDatabase method.  
`database` |  `[Database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Database)`   
Required. The database to update. The database's `name` field is used to identify the database to update. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id} This corresponds to the `database` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The list of fields to update. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask> If not set, defaults to all of the fields that are allowed to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Database](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Database)` | Database is the container of tables.  
  
### update_table
    
    
    update_table(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_biglake_v1alpha1.types.metastore.UpdateTableRequest,
                dict,
            ]
        ] = None,
        *,
        table: typing.Optional[
            google.cloud.bigquery_biglake_v1alpha1.types.metastore.Table
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
    ) -> google.cloud.bigquery_biglake_v1alpha1.types.metastore.Table

Updates an existing table specified by the table ID.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import bigquery_biglake_v1alpha1
    
    async def sample_update_table():
        # Create a client
        client = bigquery_biglake_v1alpha1.[MetastoreServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = bigquery_biglake_v1alpha1.[UpdateTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.UpdateTableRequest.html)(
        )
    
        # Make the request
        response = await client.[update_table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.services.metastore_service.MetastoreServiceAsyncClient.html#google_cloud_bigquery_biglake_v1alpha1_services_metastore_service_MetastoreServiceAsyncClient_update_table)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_biglake_v1alpha1.types.UpdateTableRequest](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.UpdateTableRequest), dict]]`   
The request object. Request message for the UpdateTable method.  
`table` |  `[Table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Table)`   
Required. The table to update. The table's `name` field is used to identify the table to update. Format: projects/{project_id_or_number}/locations/{location_id}/catalogs/{catalog_id}/databases/{database_id}/tables/{table_id} This corresponds to the `table` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
The list of fields to update. For the `FieldMask` definition, see <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask> If not set, defaults to all of the fields that are allowed to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_biglake_v1alpha1.types.Table](https://docs.cloud.google.com/python/docs/reference/biglake/latest/google.cloud.bigquery_biglake_v1alpha1.types.Table)` | Represents a table.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
