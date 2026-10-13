---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/summary_method/
title: Package Methods (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:40.746380+00:00
---

# Package Methods (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 

Summary of entries of Methods for cloudasset.

## 

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient
    
    
    AssetServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.asset_v1.services.asset_service.transports.base.AssetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.asset_v1.services.asset_service.transports.base.AssetServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the asset service async client.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_AssetServiceAsyncClient)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.access_level_path
    
    
    access_level_path(access_policy: str, access_level: str) -> str

Returns a fully-qualified access_level string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.access_level_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_access_level_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.access_policy_path
    
    
    access_policy_path(access_policy: str) -> str

Returns a fully-qualified access_policy string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.access_policy_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_access_policy_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_iam_policy
    
    
    analyze_iam_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeIamPolicyRequest, dict
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
    ) -> google.cloud.asset_v1.types.asset_service.AnalyzeIamPolicyResponse

Analyzes IAM policies to answer which identities have what accesses on which resources.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_iam_policy](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_iam_policy)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_iam_policy_longrunning
    
    
    analyze_iam_policy_longrunning(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeIamPolicyLongrunningRequest,
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

Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_iam_policy_longrunning](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_iam_policy_longrunning)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_move
    
    
    analyze_move(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.AnalyzeMoveRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.AnalyzeMoveResponse

Analyze moving a resource to a specified destination without kicking off the actual move.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_move](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_move)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_org_policies
    
    
    analyze_org_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesRequest, dict
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        constraint: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager

Analyzes organization policies under a scope.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_org_policies](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_org_policies)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_org_policy_governed_assets
    
    
    analyze_org_policy_governed_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
                dict,
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        constraint: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager
    )

Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_org_policy_governed_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_org_policy_governed_assets)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_org_policy_governed_containers
    
    
    analyze_org_policy_governed_containers(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
                dict,
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        constraint: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager
    )

Analyzes organization policies governed containers (projects, folders or organization) under a scope.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.analyze_org_policy_governed_containers](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_org_policy_governed_containers)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.asset_path
    
    
    asset_path() -> str

Returns a fully-qualified asset string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.asset_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_asset_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.batch_get_assets_history
    
    
    batch_get_assets_history(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.BatchGetAssetsHistoryRequest, dict
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
    ) -> google.cloud.asset_v1.types.asset_service.BatchGetAssetsHistoryResponse

Batch gets the update history of assets that overlap a time window.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.batch_get_assets_history](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_batch_get_assets_history)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.batch_get_effective_iam_policies
    
    
    batch_get_effective_iam_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.BatchGetEffectiveIamPoliciesRequest,
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
    ) -> google.cloud.asset_v1.types.asset_service.BatchGetEffectiveIamPoliciesResponse

Gets effective IAM policies for a batch of resources.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.batch_get_effective_iam_policies](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_batch_get_effective_iam_policies)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_common_billing_account_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_common_folder_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_common_location_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_common_organization_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_common_project_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.create_feed
    
    
    create_feed(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.CreateFeedRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.Feed

Creates a feed in a parent project/folder/organization to listen to its asset updates.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.create_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_create_feed)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.create_saved_query
    
    
    create_saved_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.CreateSavedQueryRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        saved_query: typing.Optional[
            google.cloud.asset_v1.types.asset_service.SavedQuery
        ] = None,
        saved_query_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.types.asset_service.SavedQuery

Creates a saved query in a parent project/folder/organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.create_saved_query](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_create_saved_query)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.delete_feed
    
    
    delete_feed(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.DeleteFeedRequest, dict]
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

Deletes an asset feed.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.delete_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_delete_feed)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.delete_saved_query
    
    
    delete_saved_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.DeleteSavedQueryRequest, dict
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

Deletes a saved query.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.delete_saved_query](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_delete_saved_query)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.export_assets
    
    
    export_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.ExportAssetsRequest, dict
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

Exports assets with time and resource types to a given Cloud Storage location/BigQuery table.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.export_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_export_assets)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.feed_path
    
    
    feed_path(project: str, feed: str) -> str

Returns a fully-qualified feed string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.feed_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_feed_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_from_service_account_file)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_from_service_account_info)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_from_service_account_json)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_feed
    
    
    get_feed(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.GetFeedRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.Feed

Gets details about an asset feed.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_get_feed)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_get_operation)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_saved_query
    
    
    get_saved_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.GetSavedQueryRequest, dict
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
    ) -> google.cloud.asset_v1.types.asset_service.SavedQuery

Gets details about a saved query.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_saved_query](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_get_saved_query)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.asset_v1.services.asset_service.transports.base.AssetServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_get_transport_class)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.inventory_path
    
    
    inventory_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified inventory string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.inventory_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_inventory_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.list_assets
    
    
    list_assets(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.ListAssetsRequest, dict]
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
    ) -> google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager

Lists assets with time and resource types and returns paged results in response.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.list_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_list_assets)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.list_feeds
    
    
    list_feeds(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.ListFeedsRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.ListFeedsResponse

Lists all asset feeds in a parent project/folder/organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.list_feeds](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_list_feeds)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.list_saved_queries
    
    
    list_saved_queries(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.ListSavedQueriesRequest, dict
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
    ) -> google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager

Lists all saved queries in a parent project/folder/organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.list_saved_queries](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_list_saved_queries)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_access_level_path
    
    
    parse_access_level_path(path: str) -> typing.Dict[str, str]

Parses a access_level path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_access_level_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_access_level_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_access_policy_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_access_policy_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_asset_path
    
    
    parse_asset_path(path: str) -> typing.Dict[str, str]

Parses a asset path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_asset_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_asset_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_common_folder_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_common_location_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_common_organization_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_common_project_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_feed_path
    
    
    parse_feed_path(path: str) -> typing.Dict[str, str]

Parses a feed path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_feed_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_feed_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_inventory_path
    
    
    parse_inventory_path(path: str) -> typing.Dict[str, str]

Parses a inventory path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_inventory_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_inventory_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_saved_query_path
    
    
    parse_saved_query_path(path: str) -> typing.Dict[str, str]

Parses a saved_query path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_saved_query_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_saved_query_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_service_perimeter_path
    
    
    parse_service_perimeter_path(path: str) -> typing.Dict[str, str]

Parses a service_perimeter path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.parse_service_perimeter_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_parse_service_perimeter_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.query_assets
    
    
    query_assets(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.QueryAssetsRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.QueryAssetsResponse

Issue a job that queries assets using a SQL statement compatible with `BigQuery SQL <https://cloud.google.com/bigquery/docs/introduction-sql>`__.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.query_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_query_assets)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.saved_query_path
    
    
    saved_query_path(project: str, saved_query: str) -> str

Returns a fully-qualified saved_query string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.saved_query_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_saved_query_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.search_all_iam_policies
    
    
    search_all_iam_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesRequest, dict
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager

Searches all IAM policies within the specified scope, such as a project, folder, or organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.search_all_iam_policies](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_search_all_iam_policies)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.search_all_resources
    
    
    search_all_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.SearchAllResourcesRequest, dict
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        asset_types: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager

Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.search_all_resources](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_search_all_resources)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.service_perimeter_path
    
    
    service_perimeter_path(access_policy: str, service_perimeter: str) -> str

Returns a fully-qualified service_perimeter string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.service_perimeter_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_service_perimeter_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.update_feed
    
    
    update_feed(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.UpdateFeedRequest, dict]
        ] = None,
        *,
        feed: typing.Optional[google.cloud.asset_v1.types.asset_service.Feed] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.types.asset_service.Feed

Updates an asset feed configuration.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.update_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_update_feed)

### google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.update_saved_query
    
    
    update_saved_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.UpdateSavedQueryRequest, dict
            ]
        ] = None,
        *,
        saved_query: typing.Optional[
            google.cloud.asset_v1.types.asset_service.SavedQuery
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
    ) -> google.cloud.asset_v1.types.asset_service.SavedQuery

Updates a saved query.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.update_saved_query](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_update_saved_query)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient
    
    
    AssetServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.asset_v1.services.asset_service.transports.base.AssetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.asset_v1.services.asset_service.transports.base.AssetServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the asset service client.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_AssetServiceClient)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.**exit**](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient___exit__)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.access_level_path
    
    
    access_level_path(access_policy: str, access_level: str) -> str

Returns a fully-qualified access_level string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.access_level_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_access_level_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.access_policy_path
    
    
    access_policy_path(access_policy: str) -> str

Returns a fully-qualified access_policy string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.access_policy_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_access_policy_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_iam_policy
    
    
    analyze_iam_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeIamPolicyRequest, dict
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
    ) -> google.cloud.asset_v1.types.asset_service.AnalyzeIamPolicyResponse

Analyzes IAM policies to answer which identities have what accesses on which resources.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_iam_policy](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_analyze_iam_policy)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_iam_policy_longrunning
    
    
    analyze_iam_policy_longrunning(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeIamPolicyLongrunningRequest,
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

Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_iam_policy_longrunning](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_analyze_iam_policy_longrunning)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_move
    
    
    analyze_move(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.AnalyzeMoveRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.AnalyzeMoveResponse

Analyze moving a resource to a specified destination without kicking off the actual move.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_move](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_analyze_move)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_org_policies
    
    
    analyze_org_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesRequest, dict
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        constraint: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesPager

Analyzes organization policies under a scope.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_org_policies](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_analyze_org_policies)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_org_policy_governed_assets
    
    
    analyze_org_policy_governed_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
                dict,
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        constraint: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsPager
    )

Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_org_policy_governed_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_analyze_org_policy_governed_assets)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_org_policy_governed_containers
    
    
    analyze_org_policy_governed_containers(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
                dict,
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        constraint: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersPager
    )

Analyzes organization policies governed containers (projects, folders or organization) under a scope.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.analyze_org_policy_governed_containers](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_analyze_org_policy_governed_containers)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.asset_path
    
    
    asset_path() -> str

Returns a fully-qualified asset string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.asset_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_asset_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.batch_get_assets_history
    
    
    batch_get_assets_history(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.BatchGetAssetsHistoryRequest, dict
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
    ) -> google.cloud.asset_v1.types.asset_service.BatchGetAssetsHistoryResponse

Batch gets the update history of assets that overlap a time window.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.batch_get_assets_history](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_batch_get_assets_history)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.batch_get_effective_iam_policies
    
    
    batch_get_effective_iam_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.BatchGetEffectiveIamPoliciesRequest,
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
    ) -> google.cloud.asset_v1.types.asset_service.BatchGetEffectiveIamPoliciesResponse

Gets effective IAM policies for a batch of resources.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.batch_get_effective_iam_policies](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_batch_get_effective_iam_policies)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_common_billing_account_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_common_folder_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_common_location_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_common_organization_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_common_project_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.create_feed
    
    
    create_feed(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.CreateFeedRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.Feed

Creates a feed in a parent project/folder/organization to listen to its asset updates.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.create_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_create_feed)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.create_saved_query
    
    
    create_saved_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.CreateSavedQueryRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        saved_query: typing.Optional[
            google.cloud.asset_v1.types.asset_service.SavedQuery
        ] = None,
        saved_query_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.types.asset_service.SavedQuery

Creates a saved query in a parent project/folder/organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.create_saved_query](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_create_saved_query)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.delete_feed
    
    
    delete_feed(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.DeleteFeedRequest, dict]
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

Deletes an asset feed.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.delete_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_delete_feed)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.delete_saved_query
    
    
    delete_saved_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.DeleteSavedQueryRequest, dict
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

Deletes a saved query.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.delete_saved_query](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_delete_saved_query)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.export_assets
    
    
    export_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.ExportAssetsRequest, dict
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

Exports assets with time and resource types to a given Cloud Storage location/BigQuery table.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.export_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_export_assets)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.feed_path
    
    
    feed_path(project: str, feed: str) -> str

Returns a fully-qualified feed string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.feed_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_feed_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_from_service_account_file)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_from_service_account_info)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_from_service_account_json)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.get_feed
    
    
    get_feed(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.GetFeedRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.Feed

Gets details about an asset feed.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.get_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_get_feed)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.get_operation
    
    
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

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.get_operation](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_get_operation)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.get_saved_query
    
    
    get_saved_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.GetSavedQueryRequest, dict
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
    ) -> google.cloud.asset_v1.types.asset_service.SavedQuery

Gets details about a saved query.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.get_saved_query](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_get_saved_query)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.inventory_path
    
    
    inventory_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified inventory string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.inventory_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_inventory_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.list_assets
    
    
    list_assets(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.ListAssetsRequest, dict]
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
    ) -> google.cloud.asset_v1.services.asset_service.pagers.ListAssetsPager

Lists assets with time and resource types and returns paged results in response.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.list_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_list_assets)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.list_feeds
    
    
    list_feeds(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.ListFeedsRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.ListFeedsResponse

Lists all asset feeds in a parent project/folder/organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.list_feeds](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_list_feeds)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.list_saved_queries
    
    
    list_saved_queries(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.ListSavedQueriesRequest, dict
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
    ) -> google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesPager

Lists all saved queries in a parent project/folder/organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.list_saved_queries](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_list_saved_queries)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_access_level_path
    
    
    parse_access_level_path(path: str) -> typing.Dict[str, str]

Parses a access_level path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_access_level_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_access_level_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_access_policy_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_access_policy_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_asset_path
    
    
    parse_asset_path(path: str) -> typing.Dict[str, str]

Parses a asset path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_asset_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_asset_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_common_billing_account_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_common_folder_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_common_location_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_common_organization_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_common_project_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_feed_path
    
    
    parse_feed_path(path: str) -> typing.Dict[str, str]

Parses a feed path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_feed_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_feed_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_inventory_path
    
    
    parse_inventory_path(path: str) -> typing.Dict[str, str]

Parses a inventory path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_inventory_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_inventory_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_saved_query_path
    
    
    parse_saved_query_path(path: str) -> typing.Dict[str, str]

Parses a saved_query path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_saved_query_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_saved_query_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_service_perimeter_path
    
    
    parse_service_perimeter_path(path: str) -> typing.Dict[str, str]

Parses a service_perimeter path into its component segments.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.parse_service_perimeter_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_parse_service_perimeter_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.query_assets
    
    
    query_assets(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.QueryAssetsRequest, dict]
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
    ) -> google.cloud.asset_v1.types.asset_service.QueryAssetsResponse

Issue a job that queries assets using a SQL statement compatible with `BigQuery SQL <https://cloud.google.com/bigquery/docs/introduction-sql>`__.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.query_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_query_assets)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.saved_query_path
    
    
    saved_query_path(project: str, saved_query: str) -> str

Returns a fully-qualified saved_query string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.saved_query_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_saved_query_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.search_all_iam_policies
    
    
    search_all_iam_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesRequest, dict
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesPager

Searches all IAM policies within the specified scope, such as a project, folder, or organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.search_all_iam_policies](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_search_all_iam_policies)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.search_all_resources
    
    
    search_all_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.SearchAllResourcesRequest, dict
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        asset_types: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesPager

Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.search_all_resources](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_search_all_resources)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.service_perimeter_path
    
    
    service_perimeter_path(access_policy: str, service_perimeter: str) -> str

Returns a fully-qualified service_perimeter string.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.service_perimeter_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_service_perimeter_path)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.update_feed
    
    
    update_feed(
        request: typing.Optional[
            typing.Union[google.cloud.asset_v1.types.asset_service.UpdateFeedRequest, dict]
        ] = None,
        *,
        feed: typing.Optional[google.cloud.asset_v1.types.asset_service.Feed] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1.types.asset_service.Feed

Updates an asset feed configuration.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.update_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_update_feed)

### google.cloud.asset_v1.services.asset_service.AssetServiceClient.update_saved_query
    
    
    update_saved_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1.types.asset_service.UpdateSavedQueryRequest, dict
            ]
        ] = None,
        *,
        saved_query: typing.Optional[
            google.cloud.asset_v1.types.asset_service.SavedQuery
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
    ) -> google.cloud.asset_v1.types.asset_service.SavedQuery

Updates a saved query.

See more: [google.cloud.asset_v1.services.asset_service.AssetServiceClient.update_saved_query](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient#google_cloud_asset_v1_services_asset_service_AssetServiceClient_update_saved_query)

### google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager
    
    
    AnalyzeOrgPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager#google_cloud_asset_v1_services_asset_service_pagers_AnalyzeOrgPoliciesAsyncPager_AnalyzeOrgPoliciesAsyncPager)

### google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesPager
    
    
    AnalyzeOrgPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesPager#google_cloud_asset_v1_services_asset_service_pagers_AnalyzeOrgPoliciesPager_AnalyzeOrgPoliciesPager)

### google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager
    
    
    AnalyzeOrgPolicyGovernedAssetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager#google_cloud_asset_v1_services_asset_service_pagers_AnalyzeOrgPolicyGovernedAssetsAsyncPager_AnalyzeOrgPolicyGovernedAssetsAsyncPager)

### google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsPager
    
    
    AnalyzeOrgPolicyGovernedAssetsPager(
        method: typing.Callable[
            [...],
            google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsPager#google_cloud_asset_v1_services_asset_service_pagers_AnalyzeOrgPolicyGovernedAssetsPager_AnalyzeOrgPolicyGovernedAssetsPager)

### google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager
    
    
    AnalyzeOrgPolicyGovernedContainersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager#google_cloud_asset_v1_services_asset_service_pagers_AnalyzeOrgPolicyGovernedContainersAsyncPager_AnalyzeOrgPolicyGovernedContainersAsyncPager)

### google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersPager
    
    
    AnalyzeOrgPolicyGovernedContainersPager(
        method: typing.Callable[
            [...],
            google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersPager#google_cloud_asset_v1_services_asset_service_pagers_AnalyzeOrgPolicyGovernedContainersPager_AnalyzeOrgPolicyGovernedContainersPager)

### google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager
    
    
    ListAssetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.asset_v1.types.asset_service.ListAssetsResponse],
        ],
        request: google.cloud.asset_v1.types.asset_service.ListAssetsRequest,
        response: google.cloud.asset_v1.types.asset_service.ListAssetsResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager#google_cloud_asset_v1_services_asset_service_pagers_ListAssetsAsyncPager_ListAssetsAsyncPager)

### google.cloud.asset_v1.services.asset_service.pagers.ListAssetsPager
    
    
    ListAssetsPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.ListAssetsResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.ListAssetsRequest,
        response: google.cloud.asset_v1.types.asset_service.ListAssetsResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.ListAssetsPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListAssetsPager#google_cloud_asset_v1_services_asset_service_pagers_ListAssetsPager_ListAssetsPager)

### google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager
    
    
    ListSavedQueriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.ListSavedQueriesResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.ListSavedQueriesRequest,
        response: google.cloud.asset_v1.types.asset_service.ListSavedQueriesResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager#google_cloud_asset_v1_services_asset_service_pagers_ListSavedQueriesAsyncPager_ListSavedQueriesAsyncPager)

### google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesPager
    
    
    ListSavedQueriesPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.ListSavedQueriesResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.ListSavedQueriesRequest,
        response: google.cloud.asset_v1.types.asset_service.ListSavedQueriesResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesPager#google_cloud_asset_v1_services_asset_service_pagers_ListSavedQueriesPager_ListSavedQueriesPager)

### google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager
    
    
    SearchAllIamPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesRequest,
        response: google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager#google_cloud_asset_v1_services_asset_service_pagers_SearchAllIamPoliciesAsyncPager_SearchAllIamPoliciesAsyncPager)

### google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesPager
    
    
    SearchAllIamPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesRequest,
        response: google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesPager#google_cloud_asset_v1_services_asset_service_pagers_SearchAllIamPoliciesPager_SearchAllIamPoliciesPager)

### google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager
    
    
    SearchAllResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.SearchAllResourcesResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.SearchAllResourcesRequest,
        response: google.cloud.asset_v1.types.asset_service.SearchAllResourcesResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager#google_cloud_asset_v1_services_asset_service_pagers_SearchAllResourcesAsyncPager_SearchAllResourcesAsyncPager)

### google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesPager
    
    
    SearchAllResourcesPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.SearchAllResourcesResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.SearchAllResourcesRequest,
        response: google.cloud.asset_v1.types.asset_service.SearchAllResourcesResponse,
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

See more: [google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesPager#google_cloud_asset_v1_services_asset_service_pagers_SearchAllResourcesPager_SearchAllResourcesPager)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient
    
    
    AssetServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.asset_v1p1beta1.services.asset_service.transports.base.AssetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.asset_v1p1beta1.services.asset_service.transports.base.AssetServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the asset service async client.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_AssetServiceAsyncClient)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_common_billing_account_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_common_folder_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_common_location_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_common_organization_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_common_project_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_file)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_info)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_json)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.asset_v1p1beta1.services.asset_service.transports.base.AssetServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_get_transport_class)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_parse_common_folder_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_parse_common_location_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_parse_common_organization_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_parse_common_project_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.search_all_iam_policies
    
    
    search_all_iam_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p1beta1.types.asset_service.SearchAllIamPoliciesRequest,
                dict,
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager
    )

Searches all the IAM policies within a given accessible Resource Manager scope (project/folder/organization).

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.search_all_iam_policies](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_search_all_iam_policies)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.search_all_resources
    
    
    search_all_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesRequest,
                dict,
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        asset_types: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesAsyncPager
    )

Searches all the resources within a given accessible Resource Manager scope (project/folder/organization).

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient.search_all_resources](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceAsyncClient_search_all_resources)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient
    
    
    AssetServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.asset_v1p1beta1.services.asset_service.transports.base.AssetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.asset_v1p1beta1.services.asset_service.transports.base.AssetServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the asset service client.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_AssetServiceClient)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.**exit**](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient___exit__)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_common_billing_account_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_common_folder_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_common_location_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_common_organization_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_common_project_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_from_service_account_file)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_from_service_account_info)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_from_service_account_json)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_parse_common_billing_account_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_parse_common_folder_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_parse_common_location_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_parse_common_organization_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_parse_common_project_path)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.search_all_iam_policies
    
    
    search_all_iam_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p1beta1.types.asset_service.SearchAllIamPoliciesRequest,
                dict,
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesPager
    )

Searches all the IAM policies within a given accessible Resource Manager scope (project/folder/organization).

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.search_all_iam_policies](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_search_all_iam_policies)

### google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.search_all_resources
    
    
    search_all_resources(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesRequest,
                dict,
            ]
        ] = None,
        *,
        scope: typing.Optional[str] = None,
        query: typing.Optional[str] = None,
        asset_types: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesPager

Searches all the resources within a given accessible Resource Manager scope (project/folder/organization).

See more: [google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient.search_all_resources](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p1beta1_services_asset_service_AssetServiceClient_search_all_resources)

### google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager
    
    
    SearchAllIamPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1p1beta1.types.asset_service.SearchAllIamPoliciesResponse
            ],
        ],
        request: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllIamPoliciesRequest,
        response: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllIamPoliciesResponse,
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

See more: [google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager#google_cloud_asset_v1p1beta1_services_asset_service_pagers_SearchAllIamPoliciesAsyncPager_SearchAllIamPoliciesAsyncPager)

### google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesPager
    
    
    SearchAllIamPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.asset_v1p1beta1.types.asset_service.SearchAllIamPoliciesResponse,
        ],
        request: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllIamPoliciesRequest,
        response: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllIamPoliciesResponse,
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

See more: [google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesPager#google_cloud_asset_v1p1beta1_services_asset_service_pagers_SearchAllIamPoliciesPager_SearchAllIamPoliciesPager)

### google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesAsyncPager
    
    
    SearchAllResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesResponse
            ],
        ],
        request: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesRequest,
        response: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesResponse,
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

See more: [google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesAsyncPager#google_cloud_asset_v1p1beta1_services_asset_service_pagers_SearchAllResourcesAsyncPager_SearchAllResourcesAsyncPager)

### google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesPager
    
    
    SearchAllResourcesPager(
        method: typing.Callable[
            [...],
            google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesResponse,
        ],
        request: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesRequest,
        response: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesResponse,
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

See more: [google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesPager#google_cloud_asset_v1p1beta1_services_asset_service_pagers_SearchAllResourcesPager_SearchAllResourcesPager)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient
    
    
    AssetServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.asset_v1p2beta1.services.asset_service.transports.base.AssetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.asset_v1p2beta1.services.asset_service.transports.base.AssetServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the asset service async client.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_AssetServiceAsyncClient)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_common_billing_account_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_common_folder_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_common_location_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_common_organization_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_common_project_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.create_feed
    
    
    create_feed(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.CreateFeedRequest, dict
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
    ) -> google.cloud.asset_v1p2beta1.types.asset_service.Feed

Creates a feed in a parent project/folder/organization to listen to its asset updates.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.create_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_create_feed)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.delete_feed
    
    
    delete_feed(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.DeleteFeedRequest, dict
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

Deletes an asset feed.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.delete_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_delete_feed)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.feed_path
    
    
    feed_path(project: str, feed: str) -> str

Returns a fully-qualified feed string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.feed_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_feed_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_file)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_info)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_json)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.get_feed
    
    
    get_feed(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.GetFeedRequest, dict
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
    ) -> google.cloud.asset_v1p2beta1.types.asset_service.Feed

Gets details about an asset feed.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.get_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_get_feed)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_get_operation)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.asset_v1p2beta1.services.asset_service.transports.base.AssetServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_get_transport_class)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.list_feeds
    
    
    list_feeds(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.ListFeedsRequest, dict
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
    ) -> google.cloud.asset_v1p2beta1.types.asset_service.ListFeedsResponse

Lists all asset feeds in a parent project/folder/organization.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.list_feeds](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_list_feeds)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_parse_common_folder_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_parse_common_location_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_parse_common_organization_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_parse_common_project_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_feed_path
    
    
    parse_feed_path(path: str) -> typing.Dict[str, str]

Parses a feed path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.parse_feed_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_parse_feed_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.update_feed
    
    
    update_feed(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.UpdateFeedRequest, dict
            ]
        ] = None,
        *,
        feed: typing.Optional[google.cloud.asset_v1p2beta1.types.asset_service.Feed] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1p2beta1.types.asset_service.Feed

Updates an asset feed configuration.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient.update_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceAsyncClient_update_feed)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient
    
    
    AssetServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.asset_v1p2beta1.services.asset_service.transports.base.AssetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.asset_v1p2beta1.services.asset_service.transports.base.AssetServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the asset service client.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_AssetServiceClient)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.**exit**](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient___exit__)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_common_billing_account_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_common_folder_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_common_location_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_common_organization_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_common_project_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.create_feed
    
    
    create_feed(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.CreateFeedRequest, dict
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
    ) -> google.cloud.asset_v1p2beta1.types.asset_service.Feed

Creates a feed in a parent project/folder/organization to listen to its asset updates.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.create_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_create_feed)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.delete_feed
    
    
    delete_feed(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.DeleteFeedRequest, dict
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

Deletes an asset feed.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.delete_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_delete_feed)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.feed_path
    
    
    feed_path(project: str, feed: str) -> str

Returns a fully-qualified feed string.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.feed_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_feed_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_from_service_account_file)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_from_service_account_info)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_from_service_account_json)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.get_feed
    
    
    get_feed(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.GetFeedRequest, dict
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
    ) -> google.cloud.asset_v1p2beta1.types.asset_service.Feed

Gets details about an asset feed.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.get_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_get_feed)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.get_operation
    
    
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

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.get_operation](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_get_operation)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.list_feeds
    
    
    list_feeds(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.ListFeedsRequest, dict
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
    ) -> google.cloud.asset_v1p2beta1.types.asset_service.ListFeedsResponse

Lists all asset feeds in a parent project/folder/organization.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.list_feeds](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_list_feeds)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_parse_common_billing_account_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_parse_common_folder_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_parse_common_location_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_parse_common_organization_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_parse_common_project_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_feed_path
    
    
    parse_feed_path(path: str) -> typing.Dict[str, str]

Parses a feed path into its component segments.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.parse_feed_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_parse_feed_path)

### google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.update_feed
    
    
    update_feed(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p2beta1.types.asset_service.UpdateFeedRequest, dict
            ]
        ] = None,
        *,
        feed: typing.Optional[google.cloud.asset_v1p2beta1.types.asset_service.Feed] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.asset_v1p2beta1.types.asset_service.Feed

Updates an asset feed configuration.

See more: [google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient.update_feed](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p2beta1_services_asset_service_AssetServiceClient_update_feed)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient
    
    
    AssetServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.asset_v1p5beta1.services.asset_service.transports.base.AssetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.asset_v1p5beta1.services.asset_service.transports.base.AssetServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the asset service async client.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_AssetServiceAsyncClient)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.access_level_path
    
    
    access_level_path(access_policy: str, access_level: str) -> str

Returns a fully-qualified access_level string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.access_level_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_access_level_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.access_policy_path
    
    
    access_policy_path(access_policy: str) -> str

Returns a fully-qualified access_policy string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.access_policy_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_access_policy_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.asset_path
    
    
    asset_path() -> str

Returns a fully-qualified asset string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.asset_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_asset_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_common_billing_account_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_common_folder_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_common_location_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_common_organization_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_common_project_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_file)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_info)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_from_service_account_json)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.asset_v1p5beta1.services.asset_service.transports.base.AssetServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_get_transport_class)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.list_assets
    
    
    list_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p5beta1.types.asset_service.ListAssetsRequest, dict
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
    ) -> google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsAsyncPager

Lists assets with time and resource types and returns paged results in response.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.list_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_list_assets)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_access_level_path
    
    
    parse_access_level_path(path: str) -> typing.Dict[str, str]

Parses a access_level path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_access_level_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_access_level_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_access_policy_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_access_policy_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_asset_path
    
    
    parse_asset_path(path: str) -> typing.Dict[str, str]

Parses a asset path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_asset_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_asset_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_common_folder_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_common_location_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_common_organization_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_common_project_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_service_perimeter_path
    
    
    parse_service_perimeter_path(path: str) -> typing.Dict[str, str]

Parses a service_perimeter path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.parse_service_perimeter_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_parse_service_perimeter_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.service_perimeter_path
    
    
    service_perimeter_path(access_policy: str, service_perimeter: str) -> str

Returns a fully-qualified service_perimeter string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient.service_perimeter_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceAsyncClient_service_perimeter_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient
    
    
    AssetServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.asset_v1p5beta1.services.asset_service.transports.base.AssetServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.asset_v1p5beta1.services.asset_service.transports.base.AssetServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the asset service client.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_AssetServiceClient)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.**exit**](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient___exit__)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.access_level_path
    
    
    access_level_path(access_policy: str, access_level: str) -> str

Returns a fully-qualified access_level string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.access_level_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_access_level_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.access_policy_path
    
    
    access_policy_path(access_policy: str) -> str

Returns a fully-qualified access_policy string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.access_policy_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_access_policy_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.asset_path
    
    
    asset_path() -> str

Returns a fully-qualified asset string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.asset_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_asset_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_common_billing_account_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_common_folder_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_common_location_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_common_organization_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_common_project_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_from_service_account_file)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_from_service_account_info)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_from_service_account_json)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.list_assets
    
    
    list_assets(
        request: typing.Optional[
            typing.Union[
                google.cloud.asset_v1p5beta1.types.asset_service.ListAssetsRequest, dict
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
    ) -> google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsPager

Lists assets with time and resource types and returns paged results in response.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.list_assets](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_list_assets)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_access_level_path
    
    
    parse_access_level_path(path: str) -> typing.Dict[str, str]

Parses a access_level path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_access_level_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_access_level_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_access_policy_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_access_policy_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_asset_path
    
    
    parse_asset_path(path: str) -> typing.Dict[str, str]

Parses a asset path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_asset_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_asset_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_common_billing_account_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_common_folder_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_common_location_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_common_organization_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_common_project_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_service_perimeter_path
    
    
    parse_service_perimeter_path(path: str) -> typing.Dict[str, str]

Parses a service_perimeter path into its component segments.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.parse_service_perimeter_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_parse_service_perimeter_path)

### google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.service_perimeter_path
    
    
    service_perimeter_path(access_policy: str, service_perimeter: str) -> str

Returns a fully-qualified service_perimeter string.

See more: [google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient.service_perimeter_path](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient#google_cloud_asset_v1p5beta1_services_asset_service_AssetServiceClient_service_perimeter_path)

### google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsAsyncPager
    
    
    ListAssetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1p5beta1.types.asset_service.ListAssetsResponse
            ],
        ],
        request: google.cloud.asset_v1p5beta1.types.asset_service.ListAssetsRequest,
        response: google.cloud.asset_v1p5beta1.types.asset_service.ListAssetsResponse,
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

See more: [google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsAsyncPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsAsyncPager#google_cloud_asset_v1p5beta1_services_asset_service_pagers_ListAssetsAsyncPager_ListAssetsAsyncPager)

### google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsPager
    
    
    ListAssetsPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1p5beta1.types.asset_service.ListAssetsResponse
        ],
        request: google.cloud.asset_v1p5beta1.types.asset_service.ListAssetsRequest,
        response: google.cloud.asset_v1p5beta1.types.asset_service.ListAssetsResponse,
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

See more: [google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsPager](https://cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsPager#google_cloud_asset_v1p5beta1_services_asset_service_pagers_ListAssetsPager_ListAssetsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
