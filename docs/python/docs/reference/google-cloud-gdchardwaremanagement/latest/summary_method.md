---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/summary_method/
title: Package Methods (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:16:38.472331+00:00
---

# Package Methods (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.3.0  0.2.0  0.1.13 

Summary of entries of Methods for google-cloud-gdchardwaremanagement.

## 

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient
    
    
    GDCHardwareManagementAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport,
                typing.Callable[
                    [...],
                    google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the gdc hardware management async client.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_GDCHardwareManagementAsyncClient)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_cancel_operation)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.cancel_order
    
    
    cancel_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CancelOrderRequest,
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

Cancels an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.cancel_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_cancel_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.change_log_entry_path
    
    
    change_log_entry_path(
        project: str, location: str, order: str, change_log_entry: str
    ) -> str

Returns a fully-qualified change_log_entry string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.change_log_entry_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_change_log_entry_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.comment_path
    
    
    comment_path(project: str, location: str, order: str, comment: str) -> str

Returns a fully-qualified comment string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.comment_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_comment_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_common_billing_account_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_common_folder_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_common_location_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_common_organization_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_common_project_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_comment
    
    
    create_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateCommentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        comment: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment
        ] = None,
        comment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new comment on an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_comment](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_comment)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_hardware
    
    
    create_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateHardwareRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        hardware: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware
        ] = None,
        hardware_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates new hardware in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_hardware_group
    
    
    create_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateHardwareGroupRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        hardware_group: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup
        ] = None,
        hardware_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new hardware group in a given order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_hardware_group](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_hardware_group)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_order
    
    
    create_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateOrderRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        order: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order
        ] = None,
        order_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new order in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_site
    
    
    create_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateSiteRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        site: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site
        ] = None,
        site_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new site in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_site](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_site)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_zone
    
    
    create_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateZoneRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        zone: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone
        ] = None,
        zone_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new zone in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.create_zone](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_create_zone)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_hardware
    
    
    delete_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteHardwareRequest,
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

Deletes hardware.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_hardware_group
    
    
    delete_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteHardwareGroupRequest,
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

Deletes a hardware group.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_hardware_group](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_hardware_group)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_operation
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_operation)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_order
    
    
    delete_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteOrderRequest,
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

Deletes an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_site
    
    
    delete_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteSiteRequest,
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

Deletes a site.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_site](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_site)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_zone
    
    
    delete_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteZoneRequest,
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

Deletes a zone.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.delete_zone](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_delete_zone)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_from_service_account_file)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_from_service_account_info)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_from_service_account_json)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_change_log_entry
    
    
    get_change_log_entry(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetChangeLogEntryRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.ChangeLogEntry

Gets details of a change to an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_change_log_entry](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_change_log_entry)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_comment
    
    
    get_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetCommentRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment

Gets the content of a comment.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_comment](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_comment)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_hardware
    
    
    get_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetHardwareRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware

Gets hardware details.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_hardware_group
    
    
    get_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetHardwareGroupRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup

Gets details of a hardware group.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_hardware_group](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_hardware_group)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_location
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_location)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_operation
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_operation)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_order
    
    
    get_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetOrderRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order

Gets details of an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_site
    
    
    get_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetSiteRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site

Gets details of a site.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_site](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_site)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_sku
    
    
    get_sku(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetSkuRequest, dict
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Sku

Gets details of an SKU.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_sku](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_sku)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_transport_class)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_zone
    
    
    get_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetZoneRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone

Gets details of a zone.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.get_zone](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_get_zone)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.hardware_group_path
    
    
    hardware_group_path(
        project: str, location: str, order: str, hardware_group: str
    ) -> str

Returns a fully-qualified hardware_group string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.hardware_group_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_hardware_group_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.hardware_path
    
    
    hardware_path(project: str, location: str, hardware: str) -> str

Returns a fully-qualified hardware string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.hardware_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_hardware_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_change_log_entries
    
    
    list_change_log_entries(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesAsyncPager
    )

Lists the changes made to an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_change_log_entries](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_change_log_entries)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_comments
    
    
    list_comments(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsAsyncPager
    )

Lists the comments on an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_comments](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_comments)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_hardware
    
    
    list_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareAsyncPager
    )

Lists hardware in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_hardware_groups
    
    
    list_hardware_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsAsyncPager
    )

Lists hardware groups in a given order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_hardware_groups](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_hardware_groups)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_locations
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_locations)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_operations
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_operations)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_orders
    
    
    list_orders(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersAsyncPager
    )

Lists orders in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_orders](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_orders)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_sites
    
    
    list_sites(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesAsyncPager
    )

Lists sites in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_sites](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_sites)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_skus
    
    
    list_skus(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusAsyncPager
    )

Lists SKUs for a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_skus](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_skus)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_zones
    
    
    list_zones(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesAsyncPager
    )

Lists zones in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.list_zones](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_list_zones)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.order_path
    
    
    order_path(project: str, location: str, order: str) -> str

Returns a fully-qualified order string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.order_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_order_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_change_log_entry_path
    
    
    parse_change_log_entry_path(path: str) -> typing.Dict[str, str]

Parses a change_log_entry path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_change_log_entry_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_change_log_entry_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_comment_path
    
    
    parse_comment_path(path: str) -> typing.Dict[str, str]

Parses a comment path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_comment_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_comment_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_common_billing_account_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_common_folder_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_common_location_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_common_organization_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_common_project_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_hardware_group_path
    
    
    parse_hardware_group_path(path: str) -> typing.Dict[str, str]

Parses a hardware_group path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_hardware_group_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_hardware_group_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_hardware_path
    
    
    parse_hardware_path(path: str) -> typing.Dict[str, str]

Parses a hardware path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_hardware_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_hardware_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_order_path
    
    
    parse_order_path(path: str) -> typing.Dict[str, str]

Parses a order path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_order_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_order_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_site_path
    
    
    parse_site_path(path: str) -> typing.Dict[str, str]

Parses a site path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_site_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_site_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_sku_path
    
    
    parse_sku_path(path: str) -> typing.Dict[str, str]

Parses a sku path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_sku_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_sku_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_zone_path
    
    
    parse_zone_path(path: str) -> typing.Dict[str, str]

Parses a zone path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.parse_zone_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_parse_zone_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.record_action_on_comment
    
    
    record_action_on_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.RecordActionOnCommentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_type: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.service.RecordActionOnCommentRequest.ActionType
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment

Record Action on a Comment.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.record_action_on_comment](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_record_action_on_comment)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.request_order_date_change
    
    
    request_order_date_change(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.RequestOrderDateChangeRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        requested_date: typing.Optional[google.type.date_pb2.Date] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Updates the requested date change of a single Order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.request_order_date_change](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_request_order_date_change)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.signal_zone_state
    
    
    signal_zone_state(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.SignalZoneStateRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        state_signal: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.service.SignalZoneStateRequest.StateSignal
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

Signals the state of a zone.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.signal_zone_state](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_signal_zone_state)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.site_path
    
    
    site_path(project: str, location: str, site: str) -> str

Returns a fully-qualified site string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.site_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_site_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.sku_path
    
    
    sku_path(project: str, location: str, sku: str) -> str

Returns a fully-qualified sku string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.sku_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_sku_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.submit_order
    
    
    submit_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.SubmitOrderRequest,
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

Submits an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.submit_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_submit_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_hardware
    
    
    update_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateHardwareRequest,
                dict,
            ]
        ] = None,
        *,
        hardware: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware
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

Updates hardware parameters.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_hardware_group
    
    
    update_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateHardwareGroupRequest,
                dict,
            ]
        ] = None,
        *,
        hardware_group: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup
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

Updates the parameters of a hardware group.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_hardware_group](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_hardware_group)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_order
    
    
    update_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateOrderRequest,
                dict,
            ]
        ] = None,
        *,
        order: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order
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

Updates the parameters of an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_site
    
    
    update_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateSiteRequest,
                dict,
            ]
        ] = None,
        *,
        site: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site
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

Updates the parameters of a site.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_site](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_site)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_zone
    
    
    update_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateZoneRequest,
                dict,
            ]
        ] = None,
        *,
        zone: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone
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

Updates the parameters of a zone.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.update_zone](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_update_zone)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.zone_path
    
    
    zone_path(project: str, location: str, zone: str) -> str

Returns a fully-qualified zone string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient.zone_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementAsyncClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementAsyncClient_zone_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient
    
    
    GDCHardwareManagementClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport,
                typing.Callable[
                    [...],
                    google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.transports.base.GDCHardwareManagementTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the gdc hardware management client.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_GDCHardwareManagementClient)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient___exit__)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.cancel_operation
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_cancel_operation)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.cancel_order
    
    
    cancel_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CancelOrderRequest,
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

Cancels an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.cancel_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_cancel_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.change_log_entry_path
    
    
    change_log_entry_path(
        project: str, location: str, order: str, change_log_entry: str
    ) -> str

Returns a fully-qualified change_log_entry string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.change_log_entry_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_change_log_entry_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.comment_path
    
    
    comment_path(project: str, location: str, order: str, comment: str) -> str

Returns a fully-qualified comment string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.comment_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_comment_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_common_billing_account_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_common_folder_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_common_location_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_common_organization_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_common_project_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_comment
    
    
    create_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateCommentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        comment: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment
        ] = None,
        comment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new comment on an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_comment](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_create_comment)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_hardware
    
    
    create_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateHardwareRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        hardware: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware
        ] = None,
        hardware_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates new hardware in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_create_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_hardware_group
    
    
    create_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateHardwareGroupRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        hardware_group: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup
        ] = None,
        hardware_group_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new hardware group in a given order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_hardware_group](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_create_hardware_group)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_order
    
    
    create_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateOrderRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        order: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order
        ] = None,
        order_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new order in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_create_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_site
    
    
    create_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateSiteRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        site: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site
        ] = None,
        site_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new site in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_site](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_create_site)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_zone
    
    
    create_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.CreateZoneRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        zone: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone
        ] = None,
        zone_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new zone in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.create_zone](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_create_zone)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_hardware
    
    
    delete_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteHardwareRequest,
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

Deletes hardware.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_delete_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_hardware_group
    
    
    delete_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteHardwareGroupRequest,
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

Deletes a hardware group.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_hardware_group](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_delete_hardware_group)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_operation
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_delete_operation)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_order
    
    
    delete_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteOrderRequest,
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

Deletes an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_delete_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_site
    
    
    delete_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteSiteRequest,
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

Deletes a site.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_site](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_delete_site)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_zone
    
    
    delete_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.DeleteZoneRequest,
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

Deletes a zone.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.delete_zone](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_delete_zone)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_from_service_account_file)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_from_service_account_info)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_from_service_account_json)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_change_log_entry
    
    
    get_change_log_entry(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetChangeLogEntryRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.ChangeLogEntry

Gets details of a change to an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_change_log_entry](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_change_log_entry)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_comment
    
    
    get_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetCommentRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment

Gets the content of a comment.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_comment](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_comment)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_hardware
    
    
    get_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetHardwareRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware

Gets hardware details.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_hardware_group
    
    
    get_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetHardwareGroupRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup

Gets details of a hardware group.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_hardware_group](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_hardware_group)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_location
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_location)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_mtls_endpoint_and_cert_source)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_operation
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_operation)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_order
    
    
    get_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetOrderRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order

Gets details of an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_site
    
    
    get_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetSiteRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site

Gets details of a site.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_site](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_site)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_sku
    
    
    get_sku(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetSkuRequest, dict
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Sku

Gets details of an SKU.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_sku](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_sku)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_zone
    
    
    get_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.GetZoneRequest,
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
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone

Gets details of a zone.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.get_zone](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_get_zone)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.hardware_group_path
    
    
    hardware_group_path(
        project: str, location: str, order: str, hardware_group: str
    ) -> str

Returns a fully-qualified hardware_group string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.hardware_group_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_hardware_group_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.hardware_path
    
    
    hardware_path(project: str, location: str, hardware: str) -> str

Returns a fully-qualified hardware string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.hardware_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_hardware_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_change_log_entries
    
    
    list_change_log_entries(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesPager
    )

Lists the changes made to an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_change_log_entries](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_change_log_entries)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_comments
    
    
    list_comments(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsPager
    )

Lists the comments on an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_comments](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_comments)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_hardware
    
    
    list_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwarePager
    )

Lists hardware in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_hardware_groups
    
    
    list_hardware_groups(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsPager
    )

Lists hardware groups in a given order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_hardware_groups](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_hardware_groups)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_locations
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_locations)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_operations
    
    
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_operations)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_orders
    
    
    list_orders(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersPager
    )

Lists orders in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_orders](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_orders)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_sites
    
    
    list_sites(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesPager
    )

Lists sites in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_sites](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_sites)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_skus
    
    
    list_skus(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusPager
    )

Lists SKUs for a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_skus](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_skus)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_zones
    
    
    list_zones(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesRequest,
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
        google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesPager
    )

Lists zones in a given project and location.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.list_zones](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_list_zones)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.order_path
    
    
    order_path(project: str, location: str, order: str) -> str

Returns a fully-qualified order string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.order_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_order_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_change_log_entry_path
    
    
    parse_change_log_entry_path(path: str) -> typing.Dict[str, str]

Parses a change_log_entry path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_change_log_entry_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_change_log_entry_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_comment_path
    
    
    parse_comment_path(path: str) -> typing.Dict[str, str]

Parses a comment path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_comment_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_comment_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_common_billing_account_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_common_folder_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_common_location_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_common_organization_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_common_project_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_hardware_group_path
    
    
    parse_hardware_group_path(path: str) -> typing.Dict[str, str]

Parses a hardware_group path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_hardware_group_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_hardware_group_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_hardware_path
    
    
    parse_hardware_path(path: str) -> typing.Dict[str, str]

Parses a hardware path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_hardware_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_hardware_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_order_path
    
    
    parse_order_path(path: str) -> typing.Dict[str, str]

Parses a order path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_order_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_order_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_site_path
    
    
    parse_site_path(path: str) -> typing.Dict[str, str]

Parses a site path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_site_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_site_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_sku_path
    
    
    parse_sku_path(path: str) -> typing.Dict[str, str]

Parses a sku path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_sku_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_sku_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_zone_path
    
    
    parse_zone_path(path: str) -> typing.Dict[str, str]

Parses a zone path into its component segments.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.parse_zone_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_parse_zone_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.record_action_on_comment
    
    
    record_action_on_comment(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.RecordActionOnCommentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        action_type: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.service.RecordActionOnCommentRequest.ActionType
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.gdchardwaremanagement_v1alpha.types.resources.Comment

Record Action on a Comment.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.record_action_on_comment](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_record_action_on_comment)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.request_order_date_change
    
    
    request_order_date_change(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.RequestOrderDateChangeRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        requested_date: typing.Optional[google.type.date_pb2.Date] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates the requested date change of a single Order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.request_order_date_change](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_request_order_date_change)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.signal_zone_state
    
    
    signal_zone_state(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.SignalZoneStateRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        state_signal: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.service.SignalZoneStateRequest.StateSignal
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

Signals the state of a zone.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.signal_zone_state](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_signal_zone_state)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.site_path
    
    
    site_path(project: str, location: str, site: str) -> str

Returns a fully-qualified site string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.site_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_site_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.sku_path
    
    
    sku_path(project: str, location: str, sku: str) -> str

Returns a fully-qualified sku string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.sku_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_sku_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.submit_order
    
    
    submit_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.SubmitOrderRequest,
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

Submits an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.submit_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_submit_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_hardware
    
    
    update_hardware(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateHardwareRequest,
                dict,
            ]
        ] = None,
        *,
        hardware: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Hardware
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

Updates hardware parameters.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_hardware](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_update_hardware)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_hardware_group
    
    
    update_hardware_group(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateHardwareGroupRequest,
                dict,
            ]
        ] = None,
        *,
        hardware_group: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.HardwareGroup
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

Updates the parameters of a hardware group.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_hardware_group](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_update_hardware_group)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_order
    
    
    update_order(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateOrderRequest,
                dict,
            ]
        ] = None,
        *,
        order: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Order
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

Updates the parameters of an order.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_order](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_update_order)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_site
    
    
    update_site(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateSiteRequest,
                dict,
            ]
        ] = None,
        *,
        site: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Site
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

Updates the parameters of a site.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_site](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_update_site)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_zone
    
    
    update_zone(
        request: typing.Optional[
            typing.Union[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.UpdateZoneRequest,
                dict,
            ]
        ] = None,
        *,
        zone: typing.Optional[
            google.cloud.gdchardwaremanagement_v1alpha.types.resources.Zone
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

Updates the parameters of a zone.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.update_zone](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_update_zone)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.zone_path
    
    
    zone_path(project: str, location: str, zone: str) -> str

Returns a fully-qualified zone string.

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient.zone_path](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.GDCHardwareManagementClient#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_GDCHardwareManagementClient_zone_path)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesAsyncPager
    
    
    ListChangeLogEntriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesResponse
            ],
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesAsyncPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListChangeLogEntriesAsyncPager_ListChangeLogEntriesAsyncPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesPager
    
    
    ListChangeLogEntriesPager(
        method: typing.Callable[
            [...],
            google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesResponse,
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListChangeLogEntriesResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListChangeLogEntriesPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListChangeLogEntriesPager_ListChangeLogEntriesPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsAsyncPager
    
    
    ListCommentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsResponse
            ],
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsAsyncPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListCommentsAsyncPager_ListCommentsAsyncPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsPager
    
    
    ListCommentsPager(
        method: typing.Callable[
            [...],
            google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsResponse,
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListCommentsResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListCommentsPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListCommentsPager_ListCommentsPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareAsyncPager
    
    
    ListHardwareAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareResponse
            ],
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareAsyncPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListHardwareAsyncPager_ListHardwareAsyncPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsAsyncPager
    
    
    ListHardwareGroupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsResponse
            ],
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsAsyncPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListHardwareGroupsAsyncPager_ListHardwareGroupsAsyncPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsPager
    
    
    ListHardwareGroupsPager(
        method: typing.Callable[
            [...],
            google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsResponse,
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareGroupsResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwareGroupsPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListHardwareGroupsPager_ListHardwareGroupsPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwarePager
    
    
    ListHardwarePager(
        method: typing.Callable[
            [...],
            google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareResponse,
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListHardwareResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwarePager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListHardwarePager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListHardwarePager_ListHardwarePager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersAsyncPager
    
    
    ListOrdersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersResponse
            ],
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersAsyncPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListOrdersAsyncPager_ListOrdersAsyncPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersPager
    
    
    ListOrdersPager(
        method: typing.Callable[
            [...],
            google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersResponse,
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListOrdersResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListOrdersPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListOrdersPager_ListOrdersPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesAsyncPager
    
    
    ListSitesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesResponse
            ],
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesAsyncPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListSitesAsyncPager_ListSitesAsyncPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesPager
    
    
    ListSitesPager(
        method: typing.Callable[
            [...],
            google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesResponse,
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSitesResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSitesPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListSitesPager_ListSitesPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusAsyncPager
    
    
    ListSkusAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusResponse
            ],
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusAsyncPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListSkusAsyncPager_ListSkusAsyncPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusPager
    
    
    ListSkusPager(
        method: typing.Callable[
            [...], google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusResponse
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListSkusResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListSkusPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListSkusPager_ListSkusPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesAsyncPager
    
    
    ListZonesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesResponse
            ],
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesAsyncPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListZonesAsyncPager_ListZonesAsyncPager)

### google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesPager
    
    
    ListZonesPager(
        method: typing.Callable[
            [...],
            google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesResponse,
        ],
        request: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesRequest,
        response: google.cloud.gdchardwaremanagement_v1alpha.types.service.ListZonesResponse,
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

See more: [google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesPager](https://cloud.google.com/python/docs/reference/google-cloud-gdchardwaremanagement/latest/google.cloud.gdchardwaremanagement_v1alpha.services.gdc_hardware_management.pagers.ListZonesPager#google_cloud_gdchardwaremanagement_v1alpha_services_gdc_hardware_management_pagers_ListZonesPager_ListZonesPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
