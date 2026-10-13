---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient
title: Class AssetServiceAsyncClient (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:18.300115+00:00
---

# Class AssetServiceAsyncClient (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AssetServiceAsyncClient (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
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

Asset service definition.

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
`AssetServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### AssetServiceAsyncClient
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,AssetServiceTransport,Callable[..., AssetServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the AssetServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### access_level_path
    
    
    access_level_path(access_policy: str, access_level: str) -> str

Returns a fully-qualified access_level string.

### access_policy_path
    
    
    access_policy_path(access_policy: str) -> str

Returns a fully-qualified access_policy string.

### analyze_iam_policy
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_analyze_iam_policy():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        analysis_query = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[IamPolicyAnalysisQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.html)()
        analysis_query.scope = "scope_value"
    
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AnalyzeIamPolicyRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyRequest.html)(
            analysis_query=analysis_query,
        )
    
        # Make the request
        response = await client.[analyze_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.AnalyzeIamPolicyRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyRequest), dict]]`   
The request object. A request message for AssetService.AnalyzeIamPolicy.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.AnalyzeIamPolicyResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyResponse)` | A response message for AssetService.AnalyzeIamPolicy.  
  
### analyze_iam_policy_longrunning
    
    
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

Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination. For Cloud Storage destination, the output format is the JSON format that represents a xref_AnalyzeIamPolicyResponse. This method implements the `google.longrunning.Operation][google.longrunning.Operation]`, which allows you to track the operation status. We recommend intervals of at least 2 seconds with exponential backoff retry to poll the operation result. The metadata contains the metadata for the long-running operation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_analyze_iam_policy_longrunning():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        analysis_query = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[IamPolicyAnalysisQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.html)()
        analysis_query.scope = "scope_value"
    
        output_config = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig.html)()
        output_config.gcs_destination.uri = "uri_value"
    
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AnalyzeIamPolicyLongrunningRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningRequest.html)(
            analysis_query=analysis_query,
            output_config=output_config,
        )
    
        # Make the request
        operation = await client.[analyze_iam_policy_longrunning](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_iam_policy_longrunning)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningRequest), dict]]`   
The request object. A request message for AssetService.AnalyzeIamPolicyLongrunning.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [AnalyzeIamPolicyLongrunningResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningResponse) A response message for AssetService.AnalyzeIamPolicyLongrunning.  
  
### analyze_move
    
    
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

Analyze moving a resource to a specified destination without kicking off the actual move. The analysis is best effort depending on the user's permissions of viewing different hierarchical policies and configurations. The policies and configuration are subject to change before the actual resource migration takes place.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_analyze_move():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AnalyzeMoveRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeMoveRequest.html)(
            resource="resource_value",
            destination_parent="destination_parent_value",
        )
    
        # Make the request
        response = await client.[analyze_move](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_move)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.AnalyzeMoveRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeMoveRequest), dict]]`   
The request object. The request message for performing resource move analysis.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.AnalyzeMoveResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeMoveResponse)` | The response message for resource move analysis.  
  
### analyze_org_policies
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_analyze_org_policies():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AnalyzeOrgPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesRequest.html)(
            scope="scope_value",
            constraint="constraint_value",
        )
    
        # Make the request
        page_result = client.[analyze_org_policies](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_org_policies)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.AnalyzeOrgPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesRequest), dict]]`   
The request object. A request message for AssetService.AnalyzeOrgPolicies.  
`scope` |  ``str``   
Required. The organization to scope the request. Only organization policies within the scope will be analyzed. - organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456") This corresponds to the `scope` field on the `request` instance; if `request` is provided, this should not be set.  
`constraint` |  ``str``   
Required. The name of the constraint to analyze organization policies for. The response only contains analyzed organization policies for the provided constraint. This corresponds to the `constraint` field on the `request` instance; if `request` is provided, this should not be set.  
`filter` |  ``str``   
The expression to filter AnalyzeOrgPoliciesResponse.org_policy_results. Filtering is currently available for bare literal values and the following fields: - consolidated_policy.attached_resource - consolidated_policy.rules.enforce When filtering by a specific field, the only supported operator is `=`. For example, filtering by consolidated_policy.attached_resource="//cloudresourcemanager.googleapis.com/folders/001" will return all the Organization Policy results attached to "folders/001". This corresponds to the `filter` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager)` | The response message for AssetService.AnalyzeOrgPolicies. Iterating over this object will yield results and resolve additional pages automatically.  
  
### analyze_org_policy_governed_assets
    
    
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

Analyzes organization policies governed assets (Google Cloud resources or policies) under a scope. This RPC supports custom constraints and the following canned constraints:

  * constraints/ainotebooks.accessMode
  * constraints/ainotebooks.disableFileDownloads
  * constraints/ainotebooks.disableRootAccess
  * constraints/ainotebooks.disableTerminal
  * constraints/ainotebooks.environmentOptions
  * constraints/ainotebooks.requireAutoUpgradeSchedule
  * constraints/ainotebooks.restrictVpcNetworks
  * constraints/compute.disableGuestAttributesAccess
  * constraints/compute.disableInstanceDataAccessApis
  * constraints/compute.disableNestedVirtualization
  * constraints/compute.disableSerialPortAccess
  * constraints/compute.disableSerialPortLogging
  * constraints/compute.disableVpcExternalIpv6
  * constraints/compute.requireOsLogin
  * constraints/compute.requireShieldedVm
  * constraints/compute.restrictLoadBalancerCreationForTypes
  * constraints/compute.restrictProtocolForwardingCreationForTypes
  * constraints/compute.restrictXpnProjectLienRemoval
  * constraints/compute.setNewProjectDefaultToZonalDNSOnly
  * constraints/compute.skipDefaultNetworkCreation
  * constraints/compute.trustedImageProjects
  * constraints/compute.vmCanIpForward
  * constraints/compute.vmExternalIpAccess
  * constraints/gcp.detailedAuditLoggingMode
  * constraints/gcp.resourceLocations
  * constraints/iam.allowedPolicyMemberDomains
  * constraints/iam.automaticIamGrantsForDefaultServiceAccounts
  * constraints/iam.disableServiceAccountCreation
  * constraints/iam.disableServiceAccountKeyCreation
  * constraints/iam.disableServiceAccountKeyUpload
  * constraints/iam.restrictCrossProjectServiceAccountLienRemoval
  * constraints/iam.serviceAccountKeyExpiryHours
  * constraints/resourcemanager.accessBoundaries
  * constraints/resourcemanager.allowedExportDestinations
  * constraints/sql.restrictAuthorizedNetworks
  * constraints/sql.restrictNoncompliantDiagnosticDataAccess
  * constraints/sql.restrictNoncompliantResourceCreation
  * constraints/sql.restrictPublicIp
  * constraints/storage.publicAccessPrevention
  * constraints/storage.restrictAuthTypes
  * constraints/storage.uniformBucketLevelAccess



This RPC only returns either resources of types `supported by search APIs <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__ or IAM policies.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_analyze_org_policy_governed_assets():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AnalyzeOrgPolicyGovernedAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsRequest.html)(
            scope="scope_value",
            constraint="constraint_value",
        )
    
        # Make the request
        page_result = client.[analyze_org_policy_governed_assets](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_org_policy_governed_assets)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsRequest), dict]]`   
The request object. A request message for AssetService.AnalyzeOrgPolicyGovernedAssets.  
`scope` |  ``str``   
Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output assets will also be limited to the ones governed by those in-scope organization policies. - organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456") This corresponds to the `scope` field on the `request` instance; if `request` is provided, this should not be set.  
`constraint` |  ``str``   
Required. The name of the constraint to analyze governed assets for. The analysis only contains analyzed organization policies for the provided constraint. This corresponds to the `constraint` field on the `request` instance; if `request` is provided, this should not be set.  
`filter` |  ``str``   
The expression to filter AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets. For governed resources, filtering is currently available for bare literal values and the following fields: - governed_resource.project - governed_resource.folders - consolidated_policy.rules.enforce When filtering by `governed_resource.project` or `consolidated_policy.rules.enforce`, the only supported operator is `=`. When filtering by `governed_resource.folders`, the supported operators are `=` and `:`. For example, filtering by `governed_resource.project="projects/12345678"` will return all the governed resources under "projects/12345678", including the project itself if applicable. For governed IAM policies, filtering is currently available for bare literal values and the following fields: - governed_iam_policy.project - governed_iam_policy.folders - consolidated_policy.rules.enforce When filtering by `governed_iam_policy.project` or `consolidated_policy.rules.enforce`, the only supported operator is `=`. When filtering by `governed_iam_policy.folders`, the supported operators are `=` and `:`. For example, filtering by `governed_iam_policy.folders:"folders/12345678"` will return all the governed IAM policies under "folders/001". This corresponds to the `filter` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager)` | The response message for AssetService.AnalyzeOrgPolicyGovernedAssets. Iterating over this object will yield results and resolve additional pages automatically.  
  
### analyze_org_policy_governed_containers
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_analyze_org_policy_governed_containers():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AnalyzeOrgPolicyGovernedContainersRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersRequest.html)(
            scope="scope_value",
            constraint="constraint_value",
        )
    
        # Make the request
        page_result = client.[analyze_org_policy_governed_containers](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_analyze_org_policy_governed_containers)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersRequest), dict]]`   
The request object. A request message for AssetService.AnalyzeOrgPolicyGovernedContainers.  
`scope` |  ``str``   
Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output containers will also be limited to the ones governed by those in-scope organization policies. - organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456") This corresponds to the `scope` field on the `request` instance; if `request` is provided, this should not be set.  
`constraint` |  ``str``   
Required. The name of the constraint to analyze governed containers for. The analysis only contains organization policies for the provided constraint. This corresponds to the `constraint` field on the `request` instance; if `request` is provided, this should not be set.  
`filter` |  ``str``   
The expression to filter AnalyzeOrgPolicyGovernedContainersResponse.governed_containers. Filtering is currently available for bare literal values and the following fields: - parent - consolidated_policy.rules.enforce When filtering by a specific field, the only supported operator is `=`. For example, filtering by parent="//cloudresourcemanager.googleapis.com/folders/001" will return all the containers under "folders/001". This corresponds to the `filter` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager)` | The response message for AssetService.AnalyzeOrgPolicyGovernedContainers. Iterating over this object will yield results and resolve additional pages automatically.  
  
### asset_path
    
    
    asset_path() -> str

Returns a fully-qualified asset string.

### batch_get_assets_history
    
    
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

Batch gets the update history of assets that overlap a time window. For IAM_POLICY content, this API outputs history when the asset and its attached IAM POLICY both exist. This can create gaps in the output history. Otherwise, this API outputs history with asset in both non-delete or deleted status. If a specified asset does not exist, this API returns an INVALID_ARGUMENT error.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_batch_get_assets_history():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[BatchGetAssetsHistoryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetAssetsHistoryRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[batch_get_assets_history](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_batch_get_assets_history)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.BatchGetAssetsHistoryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetAssetsHistoryRequest), dict]]`   
The request object. Batch get assets history request.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetAssetsHistoryResponse)` | Batch get assets history response.  
  
### batch_get_effective_iam_policies
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_batch_get_effective_iam_policies():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[BatchGetEffectiveIamPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesRequest.html)(
            scope="scope_value",
            names=['names_value1', 'names_value2'],
        )
    
        # Make the request
        response = await client.[batch_get_effective_iam_policies](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_batch_get_effective_iam_policies)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesRequest), dict]]`   
The request object. A request message for AssetService.BatchGetEffectiveIamPolicies.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesResponse)` | A response message for AssetService.BatchGetEffectiveIamPolicies.  
  
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

### create_feed
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_create_feed():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        feed = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed.html)()
        feed.name = "name_value"
    
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[CreateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.CreateFeedRequest.html)(
            parent="parent_value",
            feed_id="feed_id_value",
            feed=feed,
        )
    
        # Make the request
        response = await client.[create_feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_create_feed)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.CreateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.CreateFeedRequest), dict]]`   
The request object. Create asset feed request.  
`parent` |  ``str``   
Required. The name of the project/folder/organization where this feed should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"). This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed)` | An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are: Pub/Sub topics.  
  
### create_saved_query
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_create_saved_query():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[CreateSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.CreateSavedQueryRequest.html)(
            parent="parent_value",
            saved_query_id="saved_query_id_value",
        )
    
        # Make the request
        response = await client.[create_saved_query](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_create_saved_query)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.CreateSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.CreateSavedQueryRequest), dict]]`   
The request object. Request to create a saved query.  
`parent` |  ``str``   
Required. The name of the project/folder/organization where this saved_query should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"). This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`saved_query` |  `[SavedQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery)`   
Required. The saved_query details. The `name` field must be empty as it will be generated based on the parent and saved_query_id. This corresponds to the `saved_query` field on the `request` instance; if `request` is provided, this should not be set.  
`saved_query_id` |  ``str``   
Required. The ID to use for the saved query, which must be unique in the specified parent. It will become the final component of the saved query's resource name. This value should be 4-63 characters, and valid characters are ``<code>a-z][0-9]</code>-``. Notice that this field is required in the saved query creation, and the `name` field of the `saved_query` will be ignored. This corresponds to the `saved_query_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.SavedQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery)` | A saved query which can be shared with others or used later.  
  
### delete_feed
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_delete_feed():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[DeleteFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.DeleteFeedRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_delete_feed)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.DeleteFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.DeleteFeedRequest), dict]]`   
The request object.  
`name` |  ``str``   
Required. The name of the feed and it must be in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_saved_query
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_delete_saved_query():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[DeleteSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.DeleteSavedQueryRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_saved_query](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_delete_saved_query)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.DeleteSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.DeleteSavedQueryRequest), dict]]`   
The request object. Request to delete a saved query.  
`name` |  ``str``   
Required. The name of the saved query to delete. It must be in the format of: - projects/project_number/savedQueries/saved_query_id - folders/folder_number/savedQueries/saved_query_id - organizations/organization_number/savedQueries/saved_query_id This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### export_assets
    
    
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

Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a xref_google.cloud.asset.v1.Asset in the JSON format; for BigQuery table destinations, the output table stores the fields in asset Protobuf as columns. This API implements the `google.longrunning.Operation][google.longrunning.Operation]` API, which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_export_assets():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        output_config = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[OutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.OutputConfig.html)()
        output_config.gcs_destination.uri = "uri_value"
    
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[ExportAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ExportAssetsRequest.html)(
            parent="parent_value",
            output_config=output_config,
        )
    
        # Make the request
        operation = await client.[export_assets](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_export_assets)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.ExportAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ExportAssetsRequest), dict]]`   
The request object. Export asset request.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ExportAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ExportAssetsResponse) The export asset response. This message is returned by the `google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]` method in the returned `google.longrunning.Operation.response][google.longrunning.Operation.response]` field.  
  
### feed_path
    
    
    feed_path(project: str, feed: str) -> str

Returns a fully-qualified feed string.

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
`AssetServiceAsyncClient` | The constructed client.  
  
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
`AssetServiceAsyncClient` | The constructed client.  
  
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
`AssetServiceAsyncClient` | The constructed client.  
  
### get_feed
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_get_feed():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[GetFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.GetFeedRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_get_feed)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.GetFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.GetFeedRequest), dict]]`   
The request object. Get asset feed request.  
`name` |  ``str``   
Required. The name of the Feed and it must be in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed)` | An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are: Pub/Sub topics.  
  
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
  
### get_saved_query
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_get_saved_query():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[GetSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.GetSavedQueryRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_saved_query](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_get_saved_query)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.GetSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.GetSavedQueryRequest), dict]]`   
The request object. Request to get a saved query.  
`name` |  ``str``   
Required. The name of the saved query and it must be in the format of: - projects/project_number/savedQueries/saved_query_id - folders/folder_number/savedQueries/saved_query_id - organizations/organization_number/savedQueries/saved_query_id This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.SavedQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery)` | A saved query which can be shared with others or used later.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.asset_v1.services.asset_service.transports.base.AssetServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### inventory_path
    
    
    inventory_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified inventory string.

### list_assets
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_list_assets():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[ListAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_assets](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_list_assets)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.ListAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsRequest), dict]]`   
The request object. ListAssets request.  
`parent` |  ``str``   
Required. Name of the organization, folder, or project the assets belong to. Format: "organizations/[organization-number]" (such as "organizations/123"), "projects/[project-id]" (such as "projects/my-project-id"), "projects/[project-number]" (such as "projects/12345"), or "folders/[folder-number]" (such as "folders/12345"). This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager)` | ListAssets response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_feeds
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_list_feeds():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[ListFeedsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListFeedsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[list_feeds](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_list_feeds)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.ListFeedsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListFeedsRequest), dict]]`   
The request object. List asset feeds request.  
`parent` |  ``str``   
Required. The parent project/folder/organization whose feeds are to be listed. It can only be using project/folder/organization number (such as "folders/12345")", or a project ID (such as "projects/my-project-id"). This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### list_saved_queries
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_list_saved_queries():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[ListSavedQueriesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_saved_queries](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_list_saved_queries)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.ListSavedQueriesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesRequest), dict]]`   
The request object. Request to list saved queries.  
`parent` |  ``str``   
Required. The parent project/folder/organization whose savedQueries are to be listed. It can only be using project/folder/organization number (such as "folders/12345")", or a project ID (such as "projects/my-project-id"). This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager)` | Response of listing saved queries. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_access_level_path
    
    
    parse_access_level_path(path: str) -> typing.Dict[str, str]

Parses a access_level path into its component segments.

### parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

### parse_asset_path
    
    
    parse_asset_path(path: str) -> typing.Dict[str, str]

Parses a asset path into its component segments.

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

### parse_feed_path
    
    
    parse_feed_path(path: str) -> typing.Dict[str, str]

Parses a feed path into its component segments.

### parse_inventory_path
    
    
    parse_inventory_path(path: str) -> typing.Dict[str, str]

Parses a inventory path into its component segments.

### parse_saved_query_path
    
    
    parse_saved_query_path(path: str) -> typing.Dict[str, str]

Parses a saved_query path into its component segments.

### parse_service_perimeter_path
    
    
    parse_service_perimeter_path(path: str) -> typing.Dict[str, str]

Parses a service_perimeter path into its component segments.

### query_assets
    
    
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

If the query execution finishes within timeout and there's no pagination, the full query results will be returned in the `QueryAssetsResponse`.

Otherwise, full query results can be obtained by issuing extra requests with the `job_reference` from the a previous `QueryAssets` call.

Note, the query result has approximately 10 GB limitation enforced by `BigQuery <https://cloud.google.com/bigquery/docs/best-practices-performance-output>`__. Queries return larger results will result in errors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_query_assets():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[QueryAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.QueryAssetsRequest.html)(
            statement="statement_value",
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[query_assets](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_query_assets)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.QueryAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.QueryAssetsRequest), dict]]`   
The request object. QueryAssets request.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.QueryAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.QueryAssetsResponse)` | QueryAssets response.  
  
### saved_query_path
    
    
    saved_query_path(project: str, saved_query: str) -> str

Returns a fully-qualified saved_query string.

### search_all_iam_policies
    
    
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

Searches all IAM policies within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllIamPolicies` permission on the desired scope, otherwise the request will be rejected.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_search_all_iam_policies():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[SearchAllIamPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesRequest.html)(
            scope="scope_value",
        )
    
        # Make the request
        page_result = client.[search_all_iam_policies](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_search_all_iam_policies)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.SearchAllIamPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesRequest), dict]]`   
The request object. Search all IAM policies request.  
`scope` |  ``str``   
Required. A scope can be a project, a folder, or an organization. The search is limited to the IAM policies within the `scope`. The caller must be granted the ```cloudasset.assets.searchAllIamPolicies`` <https://cloud.google.com/asset-inventory/docs/access-control#required_permissions>`__ permission on the desired scope. The allowed values are: - projects/{PROJECT_ID} (e.g., "projects/foo-bar") - projects/{PROJECT_NUMBER} (e.g., "projects/12345678") - folders/{FOLDER_NUMBER} (e.g., "folders/1234567") - organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456") This corresponds to the `scope` field on the `request` instance; if `request` is provided, this should not be set.  
`query` |  ``str``   
Optional. The query statement. See `how to construct a query <https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query>`**for more information. If not specified or empty, it will search all the IAM policies within the specified`scope`. Note that the query string is compared against each IAM policy binding, including its principals, roles, and IAM conditions. The returned IAM policies will only contain the bindings that match your query. To learn more about the IAM policy structure, see the `IAM policy documentation <https://cloud.google.com/iam/help/allow-policies/structure>`**. Examples: - `policy:amy@gmail.com` to find IAM policy bindings that specify user "amy@gmail.com". - `policy:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role. - `policy:comp __`to find IAM policy bindings that contain "comp" as a prefix of any word in the binding. -`policy.role.permissions:storage.buckets.update` to find IAM policy bindings that specify a role containing "storage.buckets.update" permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results. - `policy.role.permissions:upd` to find IAM policy bindings that specify a role containing "upd" as a prefix of any word in the role permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results. - `resource:organizations/123456` to find IAM policy bindings that are set on "organizations/123456". - `resource=//cloudresourcemanager.googleapis.com/projects/myproject` to find IAM policy bindings that are set on the project named "myproject". - `Important` to find IAM policy bindings that contain "Important" as a word in any of the searchable fields (except for the included permissions). - `resource:(instance1 OR instance2) policy:amy` to find IAM policy bindings that are set on resources "instance1" or "instance2" and also specify user "amy". - `roles:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role. - `memberTypes:user` to find IAM policy bindings that contain the principal type "user". This corresponds to the `query` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager)` | Search all IAM policies response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### search_all_resources
    
    
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

Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllResources` permission on the desired scope, otherwise the request will be rejected.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_search_all_resources():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[SearchAllResourcesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesRequest.html)(
            scope="scope_value",
        )
    
        # Make the request
        page_result = client.[search_all_resources](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_search_all_resources)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.SearchAllResourcesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesRequest), dict]]`   
The request object. Search all resources request.  
`scope` |  ``str``   
Required. A scope can be a project, a folder, or an organization. The search is limited to the resources within the `scope`. The caller must be granted the ```cloudasset.assets.searchAllResources`` <https://cloud.google.com/asset-inventory/docs/access-control#required_permissions>`__ permission on the desired scope. The allowed values are: - projects/{PROJECT_ID} (e.g., "projects/foo-bar") - projects/{PROJECT_NUMBER} (e.g., "projects/12345678") - folders/{FOLDER_NUMBER} (e.g., "folders/1234567") - organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456") This corresponds to the `scope` field on the `request` instance; if `request` is provided, this should not be set.  
`query` |  ``str``   
Optional. The query statement. See `how to construct a query <https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query>`**for more information. If not specified or empty, it will search all the resources within the specified`scope`. Examples: - `name:Important` to find Google Cloud resources whose name contains `Important` as a word. - `name=Important` to find the Google Cloud resource whose name is exactly `Important`. - `displayName:Impor __`to find Google Cloud resources whose display name contains`Impor` as a prefix of any word in the field. - `location:us-west` to find Google Cloud resources whose location contains both `us` and `west` as prefixes. - `labels:prod` to find Google Cloud resources whose labels contain `prod` as a key or value. - `labels.env:prod` to find Google Cloud resources that have a label `env` and its value is `prod`. - `labels.env:*` to find Google Cloud resources that have a label `env`. - `tagKeys:env` to find Google Cloud resources that have directly attached tags where the **
    
    
    **TagKey.namespacedName` <https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey>**

contains `env`. - `tagValues:prod __`to find Google Cloud resources that have directly attached tags where the TagValue.namespacedName`<code> <https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue></code>__ contains a word prefixed by <code>prod</code>. - <code>tagValueIds=tagValues/123</code> to find Google Cloud resources that have directly attached tags where the <pre>TagValue.name`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue>`**is exactly`tagValues/123`. - `effectiveTagKeys:env` to find Google Cloud resources that have directly attached or inherited tags where the TagKey.namespacedName`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey>`** contains `env`. - `effectiveTagValues:prod` to find Google Cloud resources that have directly attached or inherited tags where the 
    
    
    TagValue.namespacedName` __ contains a word prefixed by prod. - effectiveTagValueIds=tagValues/123 to find Google Cloud resources that have directly attached or inherited tags where the 

TagValue.name`` <https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue>`__ is exactly `tagValues/123`. - `kmsKey:key` to find Google Cloud resources encrypted with a customer-managed encryption key whose name contains `key` as a word. This field is deprecated. Use the `kmsKeys` field to retrieve Cloud KMS key information. - `kmsKeys:key` to find Google Cloud resources encrypted with customer-managed encryption keys whose name contains the word `key`. - `relationships:instance-group-1` to find Google Cloud resources that have relationships with `instance-group-1` in the related resource name. - `relationships:INSTANCE_TO_INSTANCEGROUP` to find Compute Engine instances that have relationships of type `INSTANCE_TO_INSTANCEGROUP`. - `relationships.INSTANCE_TO_INSTANCEGROUP:instance-group-1` to find Compute Engine instances that have relationships with `instance-group-1` in the Compute Engine instance group resource name, for relationship type `INSTANCE_TO_INSTANCEGROUP`. - `sccSecurityMarks.key=value` to find Cloud resources that are attached with security marks whose key is `key` and value is `value`. - `sccSecurityMarks.key:__`to find Cloud resources that are attached with security marks whose key is`key`. - `state:ACTIVE` to find Google Cloud resources whose state contains `ACTIVE` as a word. - `NOT state:ACTIVE` to find Google Cloud resources whose state doesn't contain `ACTIVE` as a word. - `createTime<1609459200` to find Google Cloud resources that were created before `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds. - `updateTime>1609459200` to find Google Cloud resources that were updated after `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds. - `Important` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields. - `Impor` to find Google Cloud resources that contain `Impor` as a prefix of any word in any of the searchable fields. - `Important location:(us-west1 OR global)` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields and are also located in the `us-west1` region or the `global` location. This corresponds to the `query` field on the `request` instance; if `request` is provided, this should not be set.  
`asset_types` |  `:class:`MutableSequence[str]``   
Optional. A list of asset types that this request searches for. If empty, it will search all the asset types `supported by search APIs <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`**. Regular expressions are also supported. For example: - "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com". - "._Instance" snapshots resources whose asset type ends with "Instance". - ".\ *Instance._ " snapshots resources whose asset type contains "Instance". See `RE2 <https://github.com/google/re2/wiki/Syntax>`** for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned. This corresponds to the `asset_types` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager)` | Search all resources response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### service_perimeter_path
    
    
    service_perimeter_path(access_policy: str, service_perimeter: str) -> str

Returns a fully-qualified service_perimeter string.

### update_feed
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_update_feed():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        feed = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed.html)()
        feed.name = "name_value"
    
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[UpdateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.UpdateFeedRequest.html)(
            feed=feed,
        )
    
        # Make the request
        response = await client.[update_feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_update_feed)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.UpdateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.UpdateFeedRequest), dict]]`   
The request object. Update asset feed request.  
`feed` |  `[Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed)`   
Required. The new values of feed details. It must match an existing feed and the field `name` must be in the format of: projects/project_number/feeds/feed_id or folders/folder_number/feeds/feed_id or organizations/organization_number/feeds/feed_id. This corresponds to the `feed` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed)` | An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are: Pub/Sub topics.  
  
### update_saved_query
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest)
    
    async def sample_update_saved_query():
        # Create a client
        client = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [asset_v1](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest).[UpdateSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.UpdateSavedQueryRequest.html)(
        )
    
        # Make the request
        response = await client.[update_saved_query](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient.html#google_cloud_asset_v1_services_asset_service_AssetServiceAsyncClient_update_saved_query)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.asset_v1.types.UpdateSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.UpdateSavedQueryRequest), dict]]`   
The request object. Request to update a saved query.  
`saved_query` |  `[SavedQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery)`   
Required. The saved query to update. The saved query's `name` field is used to identify the one to update, which has format as below: - projects/project_number/savedQueries/saved_query_id - folders/folder_number/savedQueries/saved_query_id - organizations/organization_number/savedQueries/saved_query_id This corresponds to the `saved_query` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. The list of fields to update. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.asset_v1.types.SavedQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery)` | A saved query which can be shared with others or used later.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
