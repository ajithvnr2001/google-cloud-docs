---
url: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient
title: Class DataprocMetastoreClient (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:26.442727+00:00
---

# Class DataprocMetastoreClient (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataprocMetastoreClient (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.3  1.17.0  1.16.1  1.15.5  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.3  1.5.1  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.3.3  0.2.2  0.1.0 
    
    
    DataprocMetastoreClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.metastore_v1.services.dataproc_metastore.transports.base.DataprocMetastoreTransport,
                typing.Callable[
                    [...],
                    google.cloud.metastore_v1.services.dataproc_metastore.transports.base.DataprocMetastoreTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Configures and manages metastore services. Metastore services are fully managed, highly available, autoscaled, autohealing, OSS-native deployments of technical metadata management software. Each metastore service exposes a network endpoint through which metadata queries are served. Metadata queries can originate from a variety of sources, including Apache Hive, Apache Presto, and Apache Spark.

The Dataproc Metastore API defines the following resource model:

  * The service works with a collection of Google Cloud projects, named: `/projects/*`

  * Each project has a collection of available locations, named: `/locations/*` (a location must refer to a Google Cloud `region`)

  * Each location has a collection of services, named: `/services/*`

  * Dataproc Metastore services are resources with names of the form:

`/projects/{project_number}/locations/{location_id}/services/{service_id}`.




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
`DataprocMetastoreTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DataprocMetastoreClient
    
    
    DataprocMetastoreClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.metastore_v1.services.dataproc_metastore.transports.base.DataprocMetastoreTransport,
                typing.Callable[
                    [...],
                    google.cloud.metastore_v1.services.dataproc_metastore.transports.base.DataprocMetastoreTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the dataproc metastore client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DataprocMetastoreTransport,Callable[..., DataprocMetastoreTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the DataprocMetastoreTransport constructor. If set to None, a transport is chosen automatically.  
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

### alter_metadata_resource_location
    
    
    alter_metadata_resource_location(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.AlterMetadataResourceLocationRequest,
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
    ) -> google.api_core.operation.Operation

Alter metadata resource location. The metadata resource can be a database, table, or partition. This functionality only updates the parent directory for the respective metadata resource and does not transfer any existing data to the new location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_alter_metadata_resource_location():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.AlterMetadataResourceLocationRequest.html)(
            service="service_value",
            resource_name="resource_name_value",
            location_uri="location_uri_value",
        )
    
        # Make the request
        operation = client.[alter_metadata_resource_location](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_alter_metadata_resource_location)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.AlterMetadataResourceLocationRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.AlterMetadataResourceLocationRequest), dict]`   
The request object. Request message for DataprocMetastore.AlterMetadataResourceLocation.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [AlterMetadataResourceLocationResponse](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.AlterMetadataResourceLocationResponse) Response message for DataprocMetastore.AlterMetadataResourceLocation.  
  
### backup_path
    
    
    backup_path(project: str, location: str, service: str, backup: str) -> str

Returns a fully-qualified backup string.

### cancel_operation
    
    
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

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.CancelOperationRequest``   
The request object. Request message for `CancelOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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

### create_backup
    
    
    create_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.CreateBackupRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        backup: typing.Optional[google.cloud.metastore_v1.types.metastore.Backup] = None,
        backup_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new backup in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_create_backup():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.CreateBackupRequest.html)(
            parent="parent_value",
            backup_id="backup_id_value",
        )
    
        # Make the request
        operation = client.[create_backup](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_create_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.CreateBackupRequest), dict]`   
The request object. Request message for DataprocMetastore.CreateBackup.  
`parent` |  `str`   
Required. The relative resource name of the service in which to create a backup of the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`backup` |  `[google.cloud.metastore_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Backup)`   
Required. The backup to create. The `name` field is ignored. The ID of the created backup must be provided in the request's `backup_id` field. This corresponds to the `backup` field on the `request` instance; if `request` is provided, this should not be set.  
`backup_id` |  `str`   
Required. The ID of the backup, which is used as the final component of the backup's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens. This corresponds to the `backup_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Backup](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Backup) The details of a backup resource.  
  
### create_metadata_import
    
    
    create_metadata_import(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.CreateMetadataImportRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        metadata_import: typing.Optional[
            google.cloud.metastore_v1.types.metastore.MetadataImport
        ] = None,
        metadata_import_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new MetadataImport in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_create_metadata_import():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[CreateMetadataImportRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.CreateMetadataImportRequest.html)(
            parent="parent_value",
            metadata_import_id="metadata_import_id_value",
        )
    
        # Make the request
        operation = client.[create_metadata_import](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_create_metadata_import)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.CreateMetadataImportRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.CreateMetadataImportRequest), dict]`   
The request object. Request message for DataprocMetastore.CreateMetadataImport.  
`parent` |  `str`   
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`metadata_import` |  `[google.cloud.metastore_v1.types.MetadataImport](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MetadataImport)`   
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field. This corresponds to the `metadata_import` field on the `request` instance; if `request` is provided, this should not be set.  
`metadata_import_id` |  `str`   
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens. This corresponds to the `metadata_import_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [MetadataImport](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MetadataImport) A metastore resource that imports metadata.  
  
### create_service
    
    
    create_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.CreateServiceRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        service: typing.Optional[google.cloud.metastore_v1.types.metastore.Service] = None,
        service_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a metastore service in a project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_create_service():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[CreateServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.CreateServiceRequest.html)(
            parent="parent_value",
            service_id="service_id_value",
        )
    
        # Make the request
        operation = client.[create_service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_create_service)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.CreateServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.CreateServiceRequest), dict]`   
The request object. Request message for DataprocMetastore.CreateService.  
`parent` |  `str`   
Required. The relative resource name of the location in which to create a metastore service, in the following form: `projects/{project_number}/locations/{location_id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`service` |  `[google.cloud.metastore_v1.types.Service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Service)`   
Required. The Metastore service to create. The `name` field is ignored. The ID of the created metastore service must be provided in the request's `service_id` field. This corresponds to the `service` field on the `request` instance; if `request` is provided, this should not be set.  
`service_id` |  `str`   
Required. The ID of the metastore service, which is used as the final component of the metastore service's name. This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens. This corresponds to the `service_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Service) A managed metastore service that serves metadata queries.  
  
### delete_backup
    
    
    delete_backup(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.DeleteBackupRequest, dict
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

Deletes a single backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_delete_backup():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.DeleteBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_backup](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_delete_backup)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.DeleteBackupRequest), dict]`   
The request object. Request message for DataprocMetastore.DeleteBackup.  
`name` |  `str`   
Required. The relative resource name of the backup to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_operation
    
    
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

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.DeleteOperationRequest``   
The request object. Request message for `DeleteOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_service
    
    
    delete_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.DeleteServiceRequest, dict
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

Deletes a single service.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_delete_service():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DeleteServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.DeleteServiceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_delete_service)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.DeleteServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.DeleteServiceRequest), dict]`   
The request object. Request message for DataprocMetastore.DeleteService.  
`name` |  `str`   
Required. The relative resource name of the metastore service to delete, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### export_metadata
    
    
    export_metadata(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.ExportMetadataRequest, dict
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
    ) -> google.api_core.operation.Operation

Exports metadata from a service.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_export_metadata():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[ExportMetadataRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.ExportMetadataRequest.html)(
            destination_gcs_folder="destination_gcs_folder_value",
            service="service_value",
        )
    
        # Make the request
        operation = client.[export_metadata](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_export_metadata)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.ExportMetadataRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.ExportMetadataRequest), dict]`   
The request object. Request message for DataprocMetastore.ExportMetadata.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [MetadataExport](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MetadataExport) The details of a metadata export operation.  
  
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
`DataprocMetastoreClient` | The constructed client.  
  
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
`DataprocMetastoreClient` | The constructed client.  
  
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
`DataprocMetastoreClient` | The constructed client.  
  
### get_backup
    
    
    get_backup(
        request: typing.Optional[
            typing.Union[google.cloud.metastore_v1.types.metastore.GetBackupRequest, dict]
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
    ) -> google.cloud.metastore_v1.types.metastore.Backup

Gets details of a single backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_get_backup():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.GetBackupRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_backup](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_get_backup)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.GetBackupRequest), dict]`   
The request object. Request message for DataprocMetastore.GetBackup.  
`name` |  `str`   
Required. The relative resource name of the backup to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups/{backup_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.metastore_v1.types.Backup](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Backup)` | The details of a backup resource.  
  
### get_iam_policy
    
    
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

Returns an empty policy if the function exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.GetIamPolicyRequest``   
The request object. Request message for `GetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
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
  
### get_metadata_import
    
    
    get_metadata_import(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.GetMetadataImportRequest, dict
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
    ) -> google.cloud.metastore_v1.types.metastore.MetadataImport

Gets details of a single import.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_get_metadata_import():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[GetMetadataImportRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.GetMetadataImportRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_metadata_import](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_get_metadata_import)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.GetMetadataImportRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.GetMetadataImportRequest), dict]`   
The request object. Request message for DataprocMetastore.GetMetadataImport.  
`name` |  `str`   
Required. The relative resource name of the metadata import to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{import_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.metastore_v1.types.MetadataImport](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MetadataImport)` | A metastore resource that imports metadata.  
  
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
  
### get_operation
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.GetOperationRequest``   
The request object. Request message for `GetOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### get_service
    
    
    get_service(
        request: typing.Optional[
            typing.Union[google.cloud.metastore_v1.types.metastore.GetServiceRequest, dict]
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
    ) -> google.cloud.metastore_v1.types.metastore.Service

Gets the details of a single service.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_get_service():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[GetServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.GetServiceRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_get_service)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.GetServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.GetServiceRequest), dict]`   
The request object. Request message for DataprocMetastore.GetService.  
`name` |  `str`   
Required. The relative resource name of the metastore service to retrieve, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.metastore_v1.types.Service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Service)` | A managed metastore service that serves metadata queries.  
  
### list_backups
    
    
    list_backups(
        request: typing.Optional[
            typing.Union[google.cloud.metastore_v1.types.metastore.ListBackupsRequest, dict]
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
    ) -> google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListBackupsPager

Lists backups in a service.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_list_backups():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.ListBackupsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_backups](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_list_backups)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.ListBackupsRequest), dict]`   
The request object. Request message for DataprocMetastore.ListBackups.  
`parent` |  `str`   
Required. The relative resource name of the service whose backups to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/backups`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListBackupsPager)` | Response message for DataprocMetastore.ListBackups. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
  
### list_metadata_imports
    
    
    list_metadata_imports(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.ListMetadataImportsRequest, dict
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
        google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListMetadataImportsPager
    )

Lists imports in a service.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_list_metadata_imports():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[ListMetadataImportsRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.ListMetadataImportsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_metadata_imports](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_list_metadata_imports)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.ListMetadataImportsRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.ListMetadataImportsRequest), dict]`   
The request object. Request message for DataprocMetastore.ListMetadataImports.  
`parent` |  `str`   
Required. The relative resource name of the service whose metadata imports to list, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListMetadataImportsPager](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListMetadataImportsPager)` | Response message for DataprocMetastore.ListMetadataImports. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_operations
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.ListOperationsRequest``   
The request object. Request message for `ListOperations` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
### list_services
    
    
    list_services(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.ListServicesRequest, dict
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
    ) -> google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListServicesPager

Lists services in a project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_list_services():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[ListServicesRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.ListServicesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_services](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_list_services)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.ListServicesRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.ListServicesRequest), dict]`   
The request object. Request message for DataprocMetastore.ListServices.  
`parent` |  `str`   
Required. The relative resource name of the location of metastore services to list, in the following form: `projects/{project_number}/locations/{location_id}`. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListServicesPager](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.pagers.ListServicesPager)` | Response message for DataprocMetastore.ListServices. Iterating over this object will yield results and resolve additional pages automatically.  
  
### metadata_import_path
    
    
    metadata_import_path(
        project: str, location: str, service: str, metadata_import: str
    ) -> str

Returns a fully-qualified metadata_import string.

### move_table_to_database
    
    
    move_table_to_database(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.MoveTableToDatabaseRequest, dict
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
    ) -> google.api_core.operation.Operation

Move a table to another database.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_move_table_to_database():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[MoveTableToDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MoveTableToDatabaseRequest.html)(
            service="service_value",
            table_name="table_name_value",
            db_name="db_name_value",
            destination_db_name="destination_db_name_value",
        )
    
        # Make the request
        operation = client.[move_table_to_database](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_move_table_to_database)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.MoveTableToDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MoveTableToDatabaseRequest), dict]`   
The request object. Request message for DataprocMetastore.MoveTableToDatabase.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [MoveTableToDatabaseResponse](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MoveTableToDatabaseResponse) Response message for DataprocMetastore.MoveTableToDatabase.  
  
### network_path
    
    
    network_path(project: str, network: str) -> str

Returns a fully-qualified network string.

### parse_backup_path
    
    
    parse_backup_path(path: str) -> typing.Dict[str, str]

Parses a backup path into its component segments.

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

### parse_metadata_import_path
    
    
    parse_metadata_import_path(path: str) -> typing.Dict[str, str]

Parses a metadata_import path into its component segments.

### parse_network_path
    
    
    parse_network_path(path: str) -> typing.Dict[str, str]

Parses a network path into its component segments.

### parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

### parse_subnetwork_path
    
    
    parse_subnetwork_path(path: str) -> typing.Dict[str, str]

Parses a subnetwork path into its component segments.

### query_metadata
    
    
    query_metadata(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.QueryMetadataRequest, dict
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
    ) -> google.api_core.operation.Operation

Query DPMS metadata.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_query_metadata():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[QueryMetadataRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.QueryMetadataRequest.html)(
            service="service_value",
            query="query_value",
        )
    
        # Make the request
        operation = client.[query_metadata](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_query_metadata)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.QueryMetadataRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.QueryMetadataRequest), dict]`   
The request object. Request message for DataprocMetastore.QueryMetadata.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [QueryMetadataResponse](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.QueryMetadataResponse) Response message for DataprocMetastore.QueryMetadata.  
  
### restore_service
    
    
    restore_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.RestoreServiceRequest, dict
            ]
        ] = None,
        *,
        service: typing.Optional[str] = None,
        backup: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Restores a service from a backup.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_restore_service():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[RestoreServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.RestoreServiceRequest.html)(
            service="service_value",
            backup="backup_value",
        )
    
        # Make the request
        operation = client.[restore_service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_restore_service)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.RestoreServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.RestoreServiceRequest), dict]`   
The request object. Request message for [DataprocMetastore.Restore][].  
`service` |  `str`   
Required. The relative resource name of the metastore service to run restore, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}`. This corresponds to the `service` field on the `request` instance; if `request` is provided, this should not be set.  
`backup` |  `str`   
Required. The relative resource name of the metastore service backup to restore from, in the following form: `projects/{project_id}/locations/{location_id}/services/{service_id}/backups/{backup_id}`. This corresponds to the `backup` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Restore](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Restore) The details of a metadata restore operation.  
  
### service_path
    
    
    service_path(project: str, location: str, service: str) -> str

Returns a fully-qualified service string.

### set_iam_policy
    
    
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

Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.SetIamPolicyRequest``   
The request object. Request message for `SetIamPolicy` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### subnetwork_path
    
    
    subnetwork_path(project: str, region: str, subnetwork: str) -> str

Returns a fully-qualified subnetwork string.

### test_iam_permissions
    
    
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

If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.TestIamPermissionsRequest``   
The request object. Request message for `TestIamPermissions` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.iam_policy_pb2.TestIamPermissionsResponse`` | Response message for `TestIamPermissions` method.  
  
### update_metadata_import
    
    
    update_metadata_import(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.UpdateMetadataImportRequest, dict
            ]
        ] = None,
        *,
        metadata_import: typing.Optional[
            google.cloud.metastore_v1.types.metastore.MetadataImport
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

Updates a single import. Only the description field of MetadataImport is supported to be updated.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_update_metadata_import():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[UpdateMetadataImportRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.UpdateMetadataImportRequest.html)(
        )
    
        # Make the request
        operation = client.[update_metadata_import](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_update_metadata_import)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.UpdateMetadataImportRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.UpdateMetadataImportRequest), dict]`   
The request object. Request message for DataprocMetastore.UpdateMetadataImport.  
`metadata_import` |  `[google.cloud.metastore_v1.types.MetadataImport](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MetadataImport)`   
Required. The metadata import to update. The server only merges fields in the import if they are specified in `update_mask`. The metadata import's `name` field is used to identify the metastore import to be updated. This corresponds to the `metadata_import` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. A field mask used to specify the fields to be overwritten in the metadata import resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [MetadataImport](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.MetadataImport) A metastore resource that imports metadata.  
  
### update_service
    
    
    update_service(
        request: typing.Optional[
            typing.Union[
                google.cloud.metastore_v1.types.metastore.UpdateServiceRequest, dict
            ]
        ] = None,
        *,
        service: typing.Optional[google.cloud.metastore_v1.types.metastore.Service] = None,
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

Updates the parameters of a single service.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest)
    
    def sample_update_service():
        # Create a client
        client = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[DataprocMetastoreClient](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html)()
    
        # Initialize request argument(s)
        request = [metastore_v1](https://docs.cloud.google.com/python/docs/reference/metastore/latest).[UpdateServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.UpdateServiceRequest.html)(
        )
    
        # Make the request
        operation = client.[update_service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.services.dataproc_metastore.DataprocMetastoreClient.html#google_cloud_metastore_v1_services_dataproc_metastore_DataprocMetastoreClient_update_service)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.metastore_v1.types.UpdateServiceRequest](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.UpdateServiceRequest), dict]`   
The request object. Request message for DataprocMetastore.UpdateService.  
`service` |  `[google.cloud.metastore_v1.types.Service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Service)`   
Required. The metastore service to update. The server only merges fields in the service if they are specified in `update_mask`. The metastore service's `name` field is used to identify the metastore service to be updated. This corresponds to the `service` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Required. A field mask used to specify the fields to be overwritten in the metastore service resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [Service](https://docs.cloud.google.com/python/docs/reference/metastore/latest/google.cloud.metastore_v1.types.Service) A managed metastore service that serves metadata queries.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
