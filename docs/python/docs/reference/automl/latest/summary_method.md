---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/summary_method/
title: Package Methods (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:18.584733+00:00
---

# Package Methods (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 

Summary of entries of Methods for automl.

## 

### google.cloud.automl_v1beta1.services.tables.tables_client.to_proto_value
    
    
    to_proto_value(value)

translates a Python value to a google.protobuf.Value.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.to_proto_value](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client#google_cloud_automl_v1beta1_services_tables_tables_client_to_proto_value)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient
    
    
    AutoMlAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1.services.auto_ml.transports.base.AutoMlTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1.services.auto_ml.transports.base.AutoMlTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the auto ml async client.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_AutoMlAsyncClient)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.annotation_spec_path
    
    
    annotation_spec_path(
        project: str, location: str, dataset: str, annotation_spec: str
    ) -> str

Returns a fully-qualified annotation_spec string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.annotation_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_annotation_spec_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_common_billing_account_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_common_folder_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_common_location_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_common_organization_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_common_project_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.create_dataset
    
    
    create_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.CreateDatasetRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        dataset: typing.Optional[google.cloud.automl_v1.types.dataset.Dataset] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a dataset.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.create_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_create_dataset)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.create_model
    
    
    create_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.CreateModelRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        model: typing.Optional[google.cloud.automl_v1.types.model.Model] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.create_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_create_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.dataset_path
    
    
    dataset_path(project: str, location: str, dataset: str) -> str

Returns a fully-qualified dataset string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.dataset_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_dataset_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.delete_dataset
    
    
    delete_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.DeleteDatasetRequest, dict]
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

Deletes a dataset and all of its contents.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.delete_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_delete_dataset)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.delete_model
    
    
    delete_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.DeleteModelRequest, dict]
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

Deletes a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.delete_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_delete_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.deploy_model
    
    
    deploy_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.DeployModelRequest, dict]
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

Deploys a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.deploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_deploy_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.export_data
    
    
    export_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ExportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[google.cloud.automl_v1.types.io.OutputConfig] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Exports dataset's data to the provided output location.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.export_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_export_data)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.export_model
    
    
    export_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ExportModelRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1.types.io.ModelExportOutputConfig
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

Exports a trained, "export-able", model to a user specified Google Cloud Storage location.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.export_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_export_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_from_service_account_file)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_from_service_account_info)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_from_service_account_json)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_annotation_spec
    
    
    get_annotation_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.service.GetAnnotationSpecRequest, dict
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
    ) -> google.cloud.automl_v1.types.annotation_spec.AnnotationSpec

Gets an annotation spec.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_annotation_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_get_annotation_spec)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_dataset
    
    
    get_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.GetDatasetRequest, dict]
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
    ) -> google.cloud.automl_v1.types.dataset.Dataset

Gets a dataset.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_get_dataset)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_model
    
    
    get_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.GetModelRequest, dict]
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
    ) -> google.cloud.automl_v1.types.model.Model

Gets a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_get_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_model_evaluation
    
    
    get_model_evaluation(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.service.GetModelEvaluationRequest, dict
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
    ) -> google.cloud.automl_v1.types.model_evaluation.ModelEvaluation

Gets a model evaluation.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_model_evaluation](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_get_model_evaluation)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.automl_v1.services.auto_ml.transports.base.AutoMlTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_get_transport_class)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.import_data
    
    
    import_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ImportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[google.cloud.automl_v1.types.io.InputConfig] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Imports data into a dataset.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.import_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_import_data)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.list_datasets
    
    
    list_datasets(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ListDatasetsRequest, dict]
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
    ) -> google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsAsyncPager

Lists datasets in a project.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.list_datasets](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_list_datasets)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.list_model_evaluations
    
    
    list_model_evaluations(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.service.ListModelEvaluationsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager

Lists model evaluations.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.list_model_evaluations](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_list_model_evaluations)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.list_models
    
    
    list_models(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ListModelsRequest, dict]
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
    ) -> google.cloud.automl_v1.services.auto_ml.pagers.ListModelsAsyncPager

Lists models.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.list_models](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_list_models)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.model_evaluation_path
    
    
    model_evaluation_path(
        project: str, location: str, model: str, model_evaluation: str
    ) -> str

Returns a fully-qualified model_evaluation string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.model_evaluation_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_model_evaluation_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_model_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_annotation_spec_path
    
    
    parse_annotation_spec_path(path: str) -> typing.Dict[str, str]

Parses a annotation_spec path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_annotation_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_annotation_spec_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_common_billing_account_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_common_folder_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_common_location_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_common_organization_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_common_project_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_dataset_path
    
    
    parse_dataset_path(path: str) -> typing.Dict[str, str]

Parses a dataset path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_dataset_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_dataset_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_model_evaluation_path
    
    
    parse_model_evaluation_path(path: str) -> typing.Dict[str, str]

Parses a model_evaluation path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_model_evaluation_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_model_evaluation_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.parse_model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_parse_model_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.undeploy_model
    
    
    undeploy_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.UndeployModelRequest, dict]
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

Undeploys a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.undeploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_undeploy_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.update_dataset
    
    
    update_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.UpdateDatasetRequest, dict]
        ] = None,
        *,
        dataset: typing.Optional[google.cloud.automl_v1.types.dataset.Dataset] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1.types.dataset.Dataset

Updates a dataset.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.update_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_update_dataset)

### google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.update_model
    
    
    update_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.UpdateModelRequest, dict]
        ] = None,
        *,
        model: typing.Optional[google.cloud.automl_v1.types.model.Model] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1.types.model.Model

Updates a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient.update_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1_services_auto_ml_AutoMlAsyncClient_update_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient
    
    
    AutoMlClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1.services.auto_ml.transports.base.AutoMlTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1.services.auto_ml.transports.base.AutoMlTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the auto ml client.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_AutoMlClient)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.**exit**](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient___exit__)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.annotation_spec_path
    
    
    annotation_spec_path(
        project: str, location: str, dataset: str, annotation_spec: str
    ) -> str

Returns a fully-qualified annotation_spec string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.annotation_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_annotation_spec_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_common_billing_account_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_common_folder_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_common_location_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_common_organization_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_common_project_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.create_dataset
    
    
    create_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.CreateDatasetRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        dataset: typing.Optional[google.cloud.automl_v1.types.dataset.Dataset] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a dataset.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.create_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_create_dataset)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.create_model
    
    
    create_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.CreateModelRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        model: typing.Optional[google.cloud.automl_v1.types.model.Model] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.create_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_create_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.dataset_path
    
    
    dataset_path(project: str, location: str, dataset: str) -> str

Returns a fully-qualified dataset string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.dataset_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_dataset_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.delete_dataset
    
    
    delete_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.DeleteDatasetRequest, dict]
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

Deletes a dataset and all of its contents.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.delete_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_delete_dataset)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.delete_model
    
    
    delete_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.DeleteModelRequest, dict]
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

Deletes a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.delete_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_delete_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.deploy_model
    
    
    deploy_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.DeployModelRequest, dict]
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

Deploys a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.deploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_deploy_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.export_data
    
    
    export_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ExportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[google.cloud.automl_v1.types.io.OutputConfig] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Exports dataset's data to the provided output location.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.export_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_export_data)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.export_model
    
    
    export_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ExportModelRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1.types.io.ModelExportOutputConfig
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

Exports a trained, "export-able", model to a user specified Google Cloud Storage location.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.export_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_export_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.from_service_account_file](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_from_service_account_file)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.from_service_account_info](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_from_service_account_info)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.from_service_account_json](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_from_service_account_json)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_annotation_spec
    
    
    get_annotation_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.service.GetAnnotationSpecRequest, dict
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
    ) -> google.cloud.automl_v1.types.annotation_spec.AnnotationSpec

Gets an annotation spec.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_annotation_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_get_annotation_spec)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_dataset
    
    
    get_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.GetDatasetRequest, dict]
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
    ) -> google.cloud.automl_v1.types.dataset.Dataset

Gets a dataset.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_get_dataset)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_model
    
    
    get_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.GetModelRequest, dict]
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
    ) -> google.cloud.automl_v1.types.model.Model

Gets a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_get_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_model_evaluation
    
    
    get_model_evaluation(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.service.GetModelEvaluationRequest, dict
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
    ) -> google.cloud.automl_v1.types.model_evaluation.ModelEvaluation

Gets a model evaluation.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_model_evaluation](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_get_model_evaluation)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_get_mtls_endpoint_and_cert_source)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.import_data
    
    
    import_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ImportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[google.cloud.automl_v1.types.io.InputConfig] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Imports data into a dataset.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.import_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_import_data)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.list_datasets
    
    
    list_datasets(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ListDatasetsRequest, dict]
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
    ) -> google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsPager

Lists datasets in a project.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.list_datasets](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_list_datasets)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.list_model_evaluations
    
    
    list_model_evaluations(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.service.ListModelEvaluationsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsPager

Lists model evaluations.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.list_model_evaluations](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_list_model_evaluations)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.list_models
    
    
    list_models(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.ListModelsRequest, dict]
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
    ) -> google.cloud.automl_v1.services.auto_ml.pagers.ListModelsPager

Lists models.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.list_models](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_list_models)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.model_evaluation_path
    
    
    model_evaluation_path(
        project: str, location: str, model: str, model_evaluation: str
    ) -> str

Returns a fully-qualified model_evaluation string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.model_evaluation_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_model_evaluation_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_model_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_annotation_spec_path
    
    
    parse_annotation_spec_path(path: str) -> typing.Dict[str, str]

Parses a annotation_spec path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_annotation_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_annotation_spec_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_common_billing_account_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_common_folder_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_common_location_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_common_organization_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_common_project_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_dataset_path
    
    
    parse_dataset_path(path: str) -> typing.Dict[str, str]

Parses a dataset path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_dataset_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_dataset_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_model_evaluation_path
    
    
    parse_model_evaluation_path(path: str) -> typing.Dict[str, str]

Parses a model_evaluation path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_model_evaluation_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_model_evaluation_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.parse_model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_parse_model_path)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.undeploy_model
    
    
    undeploy_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.UndeployModelRequest, dict]
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

Undeploys a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.undeploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_undeploy_model)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.update_dataset
    
    
    update_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.UpdateDatasetRequest, dict]
        ] = None,
        *,
        dataset: typing.Optional[google.cloud.automl_v1.types.dataset.Dataset] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1.types.dataset.Dataset

Updates a dataset.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.update_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_update_dataset)

### google.cloud.automl_v1.services.auto_ml.AutoMlClient.update_model
    
    
    update_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1.types.service.UpdateModelRequest, dict]
        ] = None,
        *,
        model: typing.Optional[google.cloud.automl_v1.types.model.Model] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1.types.model.Model

Updates a model.

See more: [google.cloud.automl_v1.services.auto_ml.AutoMlClient.update_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.AutoMlClient#google_cloud_automl_v1_services_auto_ml_AutoMlClient_update_model)

### google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsAsyncPager
    
    
    ListDatasetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.automl_v1.types.service.ListDatasetsResponse],
        ],
        request: google.cloud.automl_v1.types.service.ListDatasetsRequest,
        response: google.cloud.automl_v1.types.service.ListDatasetsResponse,
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

See more: [google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsAsyncPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsAsyncPager#google_cloud_automl_v1_services_auto_ml_pagers_ListDatasetsAsyncPager_ListDatasetsAsyncPager)

### google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsPager
    
    
    ListDatasetsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1.types.service.ListDatasetsResponse
        ],
        request: google.cloud.automl_v1.types.service.ListDatasetsRequest,
        response: google.cloud.automl_v1.types.service.ListDatasetsResponse,
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

See more: [google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListDatasetsPager#google_cloud_automl_v1_services_auto_ml_pagers_ListDatasetsPager_ListDatasetsPager)

### google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager
    
    
    ListModelEvaluationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1.types.service.ListModelEvaluationsResponse
            ],
        ],
        request: google.cloud.automl_v1.types.service.ListModelEvaluationsRequest,
        response: google.cloud.automl_v1.types.service.ListModelEvaluationsResponse,
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

See more: [google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager#google_cloud_automl_v1_services_auto_ml_pagers_ListModelEvaluationsAsyncPager_ListModelEvaluationsAsyncPager)

### google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsPager
    
    
    ListModelEvaluationsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1.types.service.ListModelEvaluationsResponse
        ],
        request: google.cloud.automl_v1.types.service.ListModelEvaluationsRequest,
        response: google.cloud.automl_v1.types.service.ListModelEvaluationsResponse,
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

See more: [google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListModelEvaluationsPager#google_cloud_automl_v1_services_auto_ml_pagers_ListModelEvaluationsPager_ListModelEvaluationsPager)

### google.cloud.automl_v1.services.auto_ml.pagers.ListModelsAsyncPager
    
    
    ListModelsAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.automl_v1.types.service.ListModelsResponse]
        ],
        request: google.cloud.automl_v1.types.service.ListModelsRequest,
        response: google.cloud.automl_v1.types.service.ListModelsResponse,
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

See more: [google.cloud.automl_v1.services.auto_ml.pagers.ListModelsAsyncPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListModelsAsyncPager#google_cloud_automl_v1_services_auto_ml_pagers_ListModelsAsyncPager_ListModelsAsyncPager)

### google.cloud.automl_v1.services.auto_ml.pagers.ListModelsPager
    
    
    ListModelsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1.types.service.ListModelsResponse
        ],
        request: google.cloud.automl_v1.types.service.ListModelsRequest,
        response: google.cloud.automl_v1.types.service.ListModelsResponse,
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

See more: [google.cloud.automl_v1.services.auto_ml.pagers.ListModelsPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.auto_ml.pagers.ListModelsPager#google_cloud_automl_v1_services_auto_ml_pagers_ListModelsPager_ListModelsPager)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient
    
    
    PredictionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1.services.prediction_service.transports.base.PredictionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1.services.prediction_service.transports.base.PredictionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the prediction service async client.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_PredictionServiceAsyncClient)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.batch_predict
    
    
    batch_predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.prediction_service.BatchPredictRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.automl_v1.types.io.BatchPredictInputConfig
        ] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1.types.io.BatchPredictOutputConfig
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Perform a batch prediction.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.batch_predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_batch_predict)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_common_billing_account_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_common_folder_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_common_location_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_common_organization_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_common_project_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_from_service_account_file)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_from_service_account_info)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_from_service_account_json)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.automl_v1.services.prediction_service.transports.base.PredictionServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_get_transport_class)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_model_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_parse_common_folder_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_parse_common_location_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_parse_common_organization_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_parse_common_project_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.parse_model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_parse_model_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.predict
    
    
    predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.prediction_service.PredictRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        payload: typing.Optional[
            google.cloud.automl_v1.types.data_items.ExamplePayload
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1.types.prediction_service.PredictResponse

Perform an online prediction.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient.predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceAsyncClient_predict)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient
    
    
    PredictionServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1.services.prediction_service.transports.base.PredictionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1.services.prediction_service.transports.base.PredictionServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the prediction service client.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_PredictionServiceClient)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.**exit**](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient___exit__)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.batch_predict
    
    
    batch_predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.prediction_service.BatchPredictRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.automl_v1.types.io.BatchPredictInputConfig
        ] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1.types.io.BatchPredictOutputConfig
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Perform a batch prediction.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.batch_predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_batch_predict)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_common_billing_account_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_common_folder_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_common_location_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_common_organization_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_common_project_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_from_service_account_file)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_from_service_account_info)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_from_service_account_json)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_model_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_parse_common_billing_account_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_parse_common_folder_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_parse_common_location_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_parse_common_organization_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_parse_common_project_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.parse_model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_parse_model_path)

### google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.predict
    
    
    predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1.types.prediction_service.PredictRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        payload: typing.Optional[
            google.cloud.automl_v1.types.data_items.ExamplePayload
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1.types.prediction_service.PredictResponse

Perform an online prediction.

See more: [google.cloud.automl_v1.services.prediction_service.PredictionServiceClient.predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1_services_prediction_service_PredictionServiceClient_predict)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient
    
    
    AutoMlAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the auto ml async client.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_AutoMlAsyncClient)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.annotation_spec_path
    
    
    annotation_spec_path(
        project: str, location: str, dataset: str, annotation_spec: str
    ) -> str

Returns a fully-qualified annotation_spec string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.annotation_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_annotation_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.column_spec_path
    
    
    column_spec_path(
        project: str, location: str, dataset: str, table_spec: str, column_spec: str
    ) -> str

Returns a fully-qualified column_spec string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.column_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_column_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_common_billing_account_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_common_folder_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_common_location_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_common_organization_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_common_project_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.create_dataset
    
    
    create_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.CreateDatasetRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        dataset: typing.Optional[google.cloud.automl_v1beta1.types.dataset.Dataset] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Creates a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.create_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_create_dataset)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.create_model
    
    
    create_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.CreateModelRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        model: typing.Optional[google.cloud.automl_v1beta1.types.model.Model] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.create_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_create_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.dataset_path
    
    
    dataset_path(project: str, location: str, dataset: str) -> str

Returns a fully-qualified dataset string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.dataset_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_dataset_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.delete_dataset
    
    
    delete_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.DeleteDatasetRequest, dict
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

Deletes a dataset and all of its contents.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.delete_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_delete_dataset)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.delete_model
    
    
    delete_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.DeleteModelRequest, dict]
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

Deletes a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.delete_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_delete_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.deploy_model
    
    
    deploy_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.DeployModelRequest, dict]
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

Deploys a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.deploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_deploy_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.export_data
    
    
    export_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ExportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.OutputConfig
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

Exports dataset's data to the provided output location.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.export_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_export_data)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.export_evaluated_examples
    
    
    export_evaluated_examples(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ExportEvaluatedExamplesRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.ExportEvaluatedExamplesOutputConfig
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

Exports examples on which the model was evaluated (i.e.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.export_evaluated_examples](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_export_evaluated_examples)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.export_model
    
    
    export_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ExportModelRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.ModelExportOutputConfig
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

Exports a trained, "export-able", model to a user specified Google Cloud Storage location.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.export_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_export_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_from_service_account_file)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_from_service_account_info)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_from_service_account_json)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_annotation_spec
    
    
    get_annotation_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetAnnotationSpecRequest, dict
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
    ) -> google.cloud.automl_v1beta1.types.annotation_spec.AnnotationSpec

Gets an annotation spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_annotation_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_annotation_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_column_spec
    
    
    get_column_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetColumnSpecRequest, dict
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
    ) -> google.cloud.automl_v1beta1.types.column_spec.ColumnSpec

Gets a column spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_column_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_column_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_dataset
    
    
    get_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.GetDatasetRequest, dict]
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
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Gets a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_dataset)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_model
    
    
    get_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.GetModelRequest, dict]
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
    ) -> google.cloud.automl_v1beta1.types.model.Model

Gets a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_model_evaluation
    
    
    get_model_evaluation(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetModelEvaluationRequest, dict
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
    ) -> google.cloud.automl_v1beta1.types.model_evaluation.ModelEvaluation

Gets a model evaluation.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_model_evaluation](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_model_evaluation)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_table_spec
    
    
    get_table_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetTableSpecRequest, dict
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
    ) -> google.cloud.automl_v1beta1.types.table_spec.TableSpec

Gets a table spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_table_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_table_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_transport_class)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.import_data
    
    
    import_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ImportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.InputConfig
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

Imports data into a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.import_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_import_data)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_column_specs
    
    
    list_column_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListColumnSpecsRequest, dict
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager

Lists column specs in a table spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_column_specs](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_column_specs)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_datasets
    
    
    list_datasets(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListDatasetsRequest, dict
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager

Lists datasets in a project.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_datasets](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_datasets)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_model_evaluations
    
    
    list_model_evaluations(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListModelEvaluationsRequest, dict
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager

Lists model evaluations.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_model_evaluations](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_model_evaluations)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_models
    
    
    list_models(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ListModelsRequest, dict]
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager

Lists models.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_models](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_models)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_table_specs
    
    
    list_table_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListTableSpecsRequest, dict
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager

Lists table specs in a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.list_table_specs](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_table_specs)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.model_evaluation_path
    
    
    model_evaluation_path(
        project: str, location: str, model: str, model_evaluation: str
    ) -> str

Returns a fully-qualified model_evaluation string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.model_evaluation_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_model_evaluation_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_model_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_annotation_spec_path
    
    
    parse_annotation_spec_path(path: str) -> typing.Dict[str, str]

Parses a annotation_spec path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_annotation_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_annotation_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_column_spec_path
    
    
    parse_column_spec_path(path: str) -> typing.Dict[str, str]

Parses a column_spec path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_column_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_column_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_common_billing_account_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_common_folder_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_common_location_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_common_organization_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_common_project_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_dataset_path
    
    
    parse_dataset_path(path: str) -> typing.Dict[str, str]

Parses a dataset path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_dataset_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_dataset_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_model_evaluation_path
    
    
    parse_model_evaluation_path(path: str) -> typing.Dict[str, str]

Parses a model_evaluation path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_model_evaluation_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_model_evaluation_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_model_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_table_spec_path
    
    
    parse_table_spec_path(path: str) -> typing.Dict[str, str]

Parses a table_spec path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.parse_table_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_parse_table_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.table_spec_path
    
    
    table_spec_path(project: str, location: str, dataset: str, table_spec: str) -> str

Returns a fully-qualified table_spec string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.table_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_table_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.undeploy_model
    
    
    undeploy_model(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UndeployModelRequest, dict
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

Undeploys a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.undeploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_undeploy_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.update_column_spec
    
    
    update_column_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateColumnSpecRequest, dict
            ]
        ] = None,
        *,
        column_spec: typing.Optional[
            google.cloud.automl_v1beta1.types.column_spec.ColumnSpec
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.column_spec.ColumnSpec

Updates a column spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.update_column_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_update_column_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.update_dataset
    
    
    update_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateDatasetRequest, dict
            ]
        ] = None,
        *,
        dataset: typing.Optional[google.cloud.automl_v1beta1.types.dataset.Dataset] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Updates a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.update_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_update_dataset)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.update_table_spec
    
    
    update_table_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateTableSpecRequest, dict
            ]
        ] = None,
        *,
        table_spec: typing.Optional[
            google.cloud.automl_v1beta1.types.table_spec.TableSpec
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.table_spec.TableSpec

Updates a table spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.update_table_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_update_table_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient
    
    
    AutoMlClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the auto ml client.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_AutoMlClient)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.**exit**](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient___exit__)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.annotation_spec_path
    
    
    annotation_spec_path(
        project: str, location: str, dataset: str, annotation_spec: str
    ) -> str

Returns a fully-qualified annotation_spec string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.annotation_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_annotation_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.column_spec_path
    
    
    column_spec_path(
        project: str, location: str, dataset: str, table_spec: str, column_spec: str
    ) -> str

Returns a fully-qualified column_spec string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.column_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_column_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_common_billing_account_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_common_folder_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_common_location_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_common_organization_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_common_project_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.create_dataset
    
    
    create_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.CreateDatasetRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        dataset: typing.Optional[google.cloud.automl_v1beta1.types.dataset.Dataset] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Creates a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.create_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_create_dataset)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.create_model
    
    
    create_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.CreateModelRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        model: typing.Optional[google.cloud.automl_v1beta1.types.model.Model] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.create_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_create_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.dataset_path
    
    
    dataset_path(project: str, location: str, dataset: str) -> str

Returns a fully-qualified dataset string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.dataset_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_dataset_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.delete_dataset
    
    
    delete_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.DeleteDatasetRequest, dict
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

Deletes a dataset and all of its contents.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.delete_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_delete_dataset)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.delete_model
    
    
    delete_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.DeleteModelRequest, dict]
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

Deletes a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.delete_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_delete_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.deploy_model
    
    
    deploy_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.DeployModelRequest, dict]
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

Deploys a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.deploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_deploy_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.export_data
    
    
    export_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ExportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.OutputConfig
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

Exports dataset's data to the provided output location.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.export_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_export_data)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.export_evaluated_examples
    
    
    export_evaluated_examples(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ExportEvaluatedExamplesRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.ExportEvaluatedExamplesOutputConfig
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

Exports examples on which the model was evaluated (i.e.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.export_evaluated_examples](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_export_evaluated_examples)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.export_model
    
    
    export_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ExportModelRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.ModelExportOutputConfig
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

Exports a trained, "export-able", model to a user specified Google Cloud Storage location.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.export_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_export_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.from_service_account_file](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_from_service_account_file)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.from_service_account_info](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_from_service_account_info)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.from_service_account_json](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_from_service_account_json)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_annotation_spec
    
    
    get_annotation_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetAnnotationSpecRequest, dict
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
    ) -> google.cloud.automl_v1beta1.types.annotation_spec.AnnotationSpec

Gets an annotation spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_annotation_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_get_annotation_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_column_spec
    
    
    get_column_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetColumnSpecRequest, dict
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
    ) -> google.cloud.automl_v1beta1.types.column_spec.ColumnSpec

Gets a column spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_column_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_get_column_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_dataset
    
    
    get_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.GetDatasetRequest, dict]
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
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Gets a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_get_dataset)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_model
    
    
    get_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.GetModelRequest, dict]
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
    ) -> google.cloud.automl_v1beta1.types.model.Model

Gets a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_get_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_model_evaluation
    
    
    get_model_evaluation(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetModelEvaluationRequest, dict
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
    ) -> google.cloud.automl_v1beta1.types.model_evaluation.ModelEvaluation

Gets a model evaluation.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_model_evaluation](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_get_model_evaluation)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_get_mtls_endpoint_and_cert_source)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_table_spec
    
    
    get_table_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetTableSpecRequest, dict
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
    ) -> google.cloud.automl_v1beta1.types.table_spec.TableSpec

Gets a table spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.get_table_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_get_table_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.import_data
    
    
    import_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ImportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.InputConfig
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

Imports data into a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.import_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_import_data)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_column_specs
    
    
    list_column_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListColumnSpecsRequest, dict
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsPager

Lists column specs in a table spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_column_specs](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_list_column_specs)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_datasets
    
    
    list_datasets(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListDatasetsRequest, dict
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsPager

Lists datasets in a project.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_datasets](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_list_datasets)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_model_evaluations
    
    
    list_model_evaluations(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListModelEvaluationsRequest, dict
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsPager

Lists model evaluations.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_model_evaluations](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_list_model_evaluations)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_models
    
    
    list_models(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ListModelsRequest, dict]
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsPager

Lists models.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_models](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_list_models)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_table_specs
    
    
    list_table_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListTableSpecsRequest, dict
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
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsPager

Lists table specs in a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.list_table_specs](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_list_table_specs)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.model_evaluation_path
    
    
    model_evaluation_path(
        project: str, location: str, model: str, model_evaluation: str
    ) -> str

Returns a fully-qualified model_evaluation string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.model_evaluation_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_model_evaluation_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_model_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_annotation_spec_path
    
    
    parse_annotation_spec_path(path: str) -> typing.Dict[str, str]

Parses a annotation_spec path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_annotation_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_annotation_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_column_spec_path
    
    
    parse_column_spec_path(path: str) -> typing.Dict[str, str]

Parses a column_spec path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_column_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_column_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_common_billing_account_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_common_folder_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_common_location_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_common_organization_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_common_project_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_dataset_path
    
    
    parse_dataset_path(path: str) -> typing.Dict[str, str]

Parses a dataset path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_dataset_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_dataset_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_model_evaluation_path
    
    
    parse_model_evaluation_path(path: str) -> typing.Dict[str, str]

Parses a model_evaluation path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_model_evaluation_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_model_evaluation_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_model_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_table_spec_path
    
    
    parse_table_spec_path(path: str) -> typing.Dict[str, str]

Parses a table_spec path into its component segments.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.parse_table_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_parse_table_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.table_spec_path
    
    
    table_spec_path(project: str, location: str, dataset: str, table_spec: str) -> str

Returns a fully-qualified table_spec string.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.table_spec_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_table_spec_path)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.undeploy_model
    
    
    undeploy_model(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UndeployModelRequest, dict
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

Undeploys a model.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.undeploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_undeploy_model)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.update_column_spec
    
    
    update_column_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateColumnSpecRequest, dict
            ]
        ] = None,
        *,
        column_spec: typing.Optional[
            google.cloud.automl_v1beta1.types.column_spec.ColumnSpec
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.column_spec.ColumnSpec

Updates a column spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.update_column_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_update_column_spec)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.update_dataset
    
    
    update_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateDatasetRequest, dict
            ]
        ] = None,
        *,
        dataset: typing.Optional[google.cloud.automl_v1beta1.types.dataset.Dataset] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Updates a dataset.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.update_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_update_dataset)

### google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.update_table_spec
    
    
    update_table_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateTableSpecRequest, dict
            ]
        ] = None,
        *,
        table_spec: typing.Optional[
            google.cloud.automl_v1beta1.types.table_spec.TableSpec
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.table_spec.TableSpec

Updates a table spec.

See more: [google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient.update_table_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlClient#google_cloud_automl_v1beta1_services_auto_ml_AutoMlClient_update_table_spec)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager
    
    
    ListColumnSpecsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1beta1.types.service.ListColumnSpecsResponse
            ],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListColumnSpecsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListColumnSpecsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListColumnSpecsAsyncPager_ListColumnSpecsAsyncPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsPager
    
    
    ListColumnSpecsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListColumnSpecsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListColumnSpecsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListColumnSpecsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListColumnSpecsPager_ListColumnSpecsPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager
    
    
    ListDatasetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1beta1.types.service.ListDatasetsResponse
            ],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListDatasetsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListDatasetsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListDatasetsAsyncPager_ListDatasetsAsyncPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsPager
    
    
    ListDatasetsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListDatasetsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListDatasetsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListDatasetsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListDatasetsPager_ListDatasetsPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager
    
    
    ListModelEvaluationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1beta1.types.service.ListModelEvaluationsResponse
            ],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListModelEvaluationsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListModelEvaluationsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListModelEvaluationsAsyncPager_ListModelEvaluationsAsyncPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsPager
    
    
    ListModelEvaluationsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListModelEvaluationsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListModelEvaluationsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListModelEvaluationsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListModelEvaluationsPager_ListModelEvaluationsPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager
    
    
    ListModelsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.automl_v1beta1.types.service.ListModelsResponse],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListModelsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListModelsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListModelsAsyncPager_ListModelsAsyncPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsPager
    
    
    ListModelsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListModelsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListModelsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListModelsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListModelsPager_ListModelsPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager
    
    
    ListTableSpecsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1beta1.types.service.ListTableSpecsResponse
            ],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListTableSpecsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListTableSpecsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListTableSpecsAsyncPager_ListTableSpecsAsyncPager)

### google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsPager
    
    
    ListTableSpecsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListTableSpecsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListTableSpecsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListTableSpecsResponse,
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

See more: [google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsPager](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsPager#google_cloud_automl_v1beta1_services_auto_ml_pagers_ListTableSpecsPager_ListTableSpecsPager)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient
    
    
    PredictionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the prediction service async client.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_PredictionServiceAsyncClient)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.batch_predict
    
    
    batch_predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.prediction_service.BatchPredictRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.BatchPredictInputConfig
        ] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.BatchPredictOutputConfig
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Perform a batch prediction.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.batch_predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_batch_predict)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_common_billing_account_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_common_folder_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_common_location_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_common_organization_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_common_project_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_from_service_account_file)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_from_service_account_info)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_from_service_account_json)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_get_transport_class)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_model_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_parse_common_folder_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_parse_common_location_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_parse_common_organization_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_parse_common_project_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.parse_model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_parse_model_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.predict
    
    
    predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.prediction_service.PredictRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        payload: typing.Optional[
            google.cloud.automl_v1beta1.types.data_items.ExamplePayload
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.prediction_service.PredictResponse

Perform an online prediction.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient.predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceAsyncClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceAsyncClient_predict)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient
    
    
    PredictionServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1beta1.services.prediction_service.transports.base.PredictionServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the prediction service client.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_PredictionServiceClient)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.**exit**](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient___exit__)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.batch_predict
    
    
    batch_predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.prediction_service.BatchPredictRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.BatchPredictInputConfig
        ] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.BatchPredictOutputConfig
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Perform a batch prediction.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.batch_predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_batch_predict)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_common_billing_account_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_common_folder_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_common_location_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_common_organization_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_common_project_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_from_service_account_file)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_from_service_account_info)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_from_service_account_json)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_model_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_parse_common_billing_account_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_parse_common_folder_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_parse_common_location_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_parse_common_organization_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_parse_common_project_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.parse_model_path](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_parse_model_path)

### google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.predict
    
    
    predict(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.prediction_service.PredictRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        payload: typing.Optional[
            google.cloud.automl_v1beta1.types.data_items.ExamplePayload
        ] = None,
        params: typing.Optional[typing.MutableMapping[str, str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.prediction_service.PredictResponse

Perform an online prediction.

See more: [google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient.predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.prediction_service.PredictionServiceClient#google_cloud_automl_v1beta1_services_prediction_service_PredictionServiceClient_predict)

### google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient
    
    
    GcsClient(bucket_name=None, client=None, credentials=None, project=None)

Constructor.

See more: [google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient#google_cloud_automl_v1beta1_services_tables_gcs_client_GcsClient_GcsClient)

### google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient.ensure_bucket_exists
    
    
    ensure_bucket_exists(project, region)

Checks if a bucket named '{project}-automl-tables-staging' exists.

See more: [google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient.ensure_bucket_exists](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient#google_cloud_automl_v1beta1_services_tables_gcs_client_GcsClient_ensure_bucket_exists)

### google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient.upload_pandas_dataframe
    
    
    upload_pandas_dataframe(dataframe, uploaded_csv_name=None)

Uploads a Pandas DataFrame as CSV to the bucket.

See more: [google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient.upload_pandas_dataframe](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.gcs_client.GcsClient#google_cloud_automl_v1beta1_services_tables_gcs_client_GcsClient_upload_pandas_dataframe)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient
    
    
    TablesClient(
        *,
        project=None,
        region="us-central1",
        credentials=None,
        client=None,
        prediction_client=None,
        gcs_client=None,
        **kwargs
    )

Constructor.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_TablesClient)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.batch_predict
    
    
    batch_predict(
        *,
        pandas_dataframe=None,
        bigquery_input_uri=None,
        bigquery_output_uri=None,
        gcs_input_uris=None,
        gcs_output_uri_prefix=None,
        model=None,
        model_name=None,
        model_display_name=None,
        project=None,
        region=None,
        credentials=None,
        inputs=None,
        params={},
        **kwargs
    )

Makes a batch prediction on a model.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.batch_predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_batch_predict)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.clear_test_train_column
    
    
    clear_test_train_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Clears the test/train (ml_use) column which designates which data belongs to the test and train sets.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.clear_test_train_column](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_clear_test_train_column)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.clear_time_column
    
    
    clear_time_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Clears the time column which designates which data will be of type timestamp and will be used for the timeseries data.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.clear_time_column](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_clear_time_column)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.clear_weight_column
    
    
    clear_weight_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Clears the weight column for a given dataset.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.clear_weight_column](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_clear_weight_column)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.create_dataset
    
    
    create_dataset(
        dataset_display_name, *, metadata={}, project=None, region=None, **kwargs
    )

Create a dataset.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.create_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_create_dataset)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.create_model
    
    
    create_model(
        model_display_name,
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        train_budget_milli_node_hours=None,
        optimization_objective=None,
        project=None,
        region=None,
        model_metadata=None,
        include_column_spec_names=None,
        exclude_column_spec_names=None,
        disable_early_stopping=False,
        **kwargs
    )

Create a model.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.create_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_create_model)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.delete_dataset
    
    
    delete_dataset(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Deletes a dataset.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.delete_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_delete_dataset)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.delete_model
    
    
    delete_model(
        *,
        model=None,
        model_display_name=None,
        model_name=None,
        project=None,
        region=None,
        **kwargs
    )

Deletes a model.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.delete_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_delete_model)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.deploy_model
    
    
    deploy_model(
        *,
        model=None,
        model_name=None,
        model_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Deploys a model.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.deploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_deploy_model)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.export_data
    
    
    export_data(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        gcs_output_uri_prefix=None,
        bigquery_output_uri=None,
        project=None,
        region=None,
        **kwargs
    )

Exports data from a dataset.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.export_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_export_data)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_column_spec
    
    
    get_column_spec(column_spec_name, *, project=None, region=None, **kwargs)

Gets a single column spec in a particular project and region.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_column_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_get_column_spec)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_dataset
    
    
    get_dataset(
        *, project=None, region=None, dataset_name=None, dataset_display_name=None, **kwargs
    )

Gets a single dataset in a particular project and region.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_dataset](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_get_dataset)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_model
    
    
    get_model(
        *, project=None, region=None, model_name=None, model_display_name=None, **kwargs
    )

Gets a single model in a particular project and region.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_get_model)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_model_evaluation
    
    
    get_model_evaluation(model_evaluation_name, *, project=None, region=None, **kwargs)

Gets a single evaluation model in a particular project and region.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_model_evaluation](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_get_model_evaluation)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_table_spec
    
    
    get_table_spec(table_spec_name, *, project=None, region=None, **kwargs)

Gets a single table spec in a particular project and region.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.get_table_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_get_table_spec)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.import_data
    
    
    import_data(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        pandas_dataframe=None,
        gcs_input_uris=None,
        bigquery_input_uri=None,
        project=None,
        region=None,
        credentials=None,
        **kwargs
    )

Imports data into a dataset.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.import_data](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_import_data)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_column_specs
    
    
    list_column_specs(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        project=None,
        region=None,
        **kwargs
    )

Lists column specs.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_column_specs](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_list_column_specs)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_datasets
    
    
    list_datasets(*, project=None, region=None, **kwargs)

List all datasets in a particular project and region.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_datasets](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_list_datasets)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_model_evaluations
    
    
    list_model_evaluations(
        *,
        project=None,
        region=None,
        model=None,
        model_display_name=None,
        model_name=None,
        **kwargs
    )

List all model evaluations for a given model.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_model_evaluations](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_list_model_evaluations)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_models
    
    
    list_models(*, project=None, region=None, **kwargs)

List all models in a particular project and region.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_models](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_list_models)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_table_specs
    
    
    list_table_specs(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        project=None,
        region=None,
        **kwargs
    )

Lists table specs.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.list_table_specs](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_list_table_specs)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.predict
    
    
    predict(
        inputs,
        *,
        model=None,
        model_name=None,
        model_display_name=None,
        feature_importance=False,
        project=None,
        region=None,
        **kwargs
    )

Makes a prediction on a deployed model.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.predict](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_predict)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.set_target_column
    
    
    set_target_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Sets the target column for a given table.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.set_target_column](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_set_target_column)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.set_test_train_column
    
    
    set_test_train_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Sets the test/train (ml_use) column which designates which data belongs to the test and train sets.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.set_test_train_column](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_set_test_train_column)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.set_time_column
    
    
    set_time_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Sets the time column which designates which data will be of type timestamp and will be used for the timeseries data.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.set_time_column](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_set_time_column)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.set_weight_column
    
    
    set_weight_column(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Sets the weight column for a given table.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.set_weight_column](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_set_weight_column)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.undeploy_model
    
    
    undeploy_model(
        *,
        model=None,
        model_name=None,
        model_display_name=None,
        project=None,
        region=None,
        **kwargs
    )

Undeploys a model.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.undeploy_model](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_undeploy_model)

### google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.update_column_spec
    
    
    update_column_spec(
        *,
        dataset=None,
        dataset_display_name=None,
        dataset_name=None,
        table_spec_name=None,
        table_spec_index=0,
        column_spec_name=None,
        column_spec_display_name=None,
        type_code=None,
        nullable=None,
        project=None,
        region=None,
        **kwargs
    )

Updates a column's specs.

See more: [google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient.update_column_spec](https://cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.tables.tables_client.TablesClient#google_cloud_automl_v1beta1_services_tables_tables_client_TablesClient_update_column_spec)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
