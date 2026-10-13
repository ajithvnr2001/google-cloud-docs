---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client/
title: Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AssetService::Rest::Client (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:10.695537+00:00
---

# Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AssetService::Rest::Client (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Asset V1 API - Class Google::Cloud::Asset::V1::AssetService::Rest::Client (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.0  1.0.2  0.32.0  0.31.0  0.30.0  0.29.3  0.28.1  0.27.0  0.26.1  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.1  0.19.0  0.18.0  0.17.3 

Reference documentation and code samples for the Cloud Asset V1 API class Google::Cloud::Asset::V1::AssetService::Rest::Client.

REST client for the AssetService service.

Asset service definition.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Asset::V1::AssetService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AssetService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client-Configuration "Google::Cloud::Asset::V1::AssetService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AssetService clients
    ::Google::Cloud::Asset::V1::AssetService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #analyze_iam_policy
    
    
    def analyze_iam_policy(request, options = nil) -> ::Google::Cloud::Asset::V1::AnalyzeIamPolicyResponse
    def analyze_iam_policy(analysis_query: nil, saved_analysis_query: nil, execution_timeout: nil) -> ::Google::Cloud::Asset::V1::AnalyzeIamPolicyResponse

Analyzes IAM policies to answer which identities have what accesses on which resources.

**Overloads**
    
    
    def analyze_iam_policy(request, options = nil) -> ::Google::Cloud::Asset::V1::AnalyzeIamPolicyResponse

Pass arguments to `analyze_iam_policy` via a request object, either of type [Google::Cloud::Asset::V1::AnalyzeIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeIamPolicyRequest "Google::Cloud::Asset::V1::AnalyzeIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::AnalyzeIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def analyze_iam_policy(analysis_query: nil, saved_analysis_query: nil, execution_timeout: nil) -> ::Google::Cloud::Asset::V1::AnalyzeIamPolicyResponse

Pass arguments to `analyze_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **analysis_query** ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery), ::Hash) — Required. The request query. 
  * **saved_analysis_query** (::String) — Optional. The name of a saved query, which must be in the format of:

    * projects/project_number/savedQueries/saved_query_id
    * folders/folder_number/savedQueries/saved_query_id
    * organizations/organization_number/savedQueries/saved_query_id

If both `analysis_query` and `saved_analysis_query` are provided, they will be merged together with the `saved_analysis_query` as base and the `analysis_query` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) page.

Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet. 

  * **execution_timeout** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Duration), ::Hash) — Optional. Amount of time executable has to complete. See JSON representation of [Duration](https://developers.google.com/protocol-buffers/docs/proto3#json).

If this field is set with a value less than the RPC deadline, and the execution of your query hasn't finished in the specified execution timeout, you will get a response with partial result. Otherwise, your query's execution will continue until the RPC deadline. If it's not finished until then, you will get a DEADLINE_EXCEEDED error.

Default is empty. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::AnalyzeIamPolicyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeIamPolicyResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::AnalyzeIamPolicyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeIamPolicyResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::AnalyzeIamPolicyRequest.new
    
    # Call the analyze_iam_policy method.
    result = client.analyze_iam_policy request
    
    # The returned object is of type Google::Cloud::Asset::V1::AnalyzeIamPolicyResponse.
    p result

### #analyze_iam_policy_longrunning
    
    
    def analyze_iam_policy_longrunning(request, options = nil) -> ::Gapic::Operation
    def analyze_iam_policy_longrunning(analysis_query: nil, saved_analysis_query: nil, output_config: nil) -> ::Gapic::Operation

Analyzes IAM policies asynchronously to answer which identities have what accesses on which resources, and writes the analysis results to a Google Cloud Storage or a BigQuery destination. For Cloud Storage destination, the output format is the JSON format that represents a [AnalyzeIamPolicyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeIamPolicyResponse "Google::Cloud::Asset::V1::AnalyzeIamPolicyResponse \(class\)"). This method implements the [google.longrunning.Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)"), which allows you to track the operation status. We recommend intervals of at least 2 seconds with exponential backoff retry to poll the operation result. The metadata contains the metadata for the long-running operation.

**Overloads**
    
    
    def analyze_iam_policy_longrunning(request, options = nil) -> ::Gapic::Operation

Pass arguments to `analyze_iam_policy_longrunning` via a request object, either of type [Google::Cloud::Asset::V1::AnalyzeIamPolicyLongrunningRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeIamPolicyLongrunningRequest "Google::Cloud::Asset::V1::AnalyzeIamPolicyLongrunningRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::AnalyzeIamPolicyLongrunningRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeIamPolicyLongrunningRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def analyze_iam_policy_longrunning(analysis_query: nil, saved_analysis_query: nil, output_config: nil) -> ::Gapic::Operation

Pass arguments to `analyze_iam_policy_longrunning` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **analysis_query** ([::Google::Cloud::Asset::V1::IamPolicyAnalysisQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisQuery), ::Hash) — Required. The request query. 
  * **saved_analysis_query** (::String) — Optional. The name of a saved query, which must be in the format of:

    * projects/project_number/savedQueries/saved_query_id
    * folders/folder_number/savedQueries/saved_query_id
    * organizations/organization_number/savedQueries/saved_query_id

If both `analysis_query` and `saved_analysis_query` are provided, they will be merged together with the `saved_analysis_query` as base and the `analysis_query` as overrides. For more details of the merge behavior, refer to the [MergeFrom](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.message#Message.MergeFrom.details) doc.

Note that you cannot override primitive fields with default value, such as 0 or empty string, etc., because we use proto3, which doesn't support field presence yet. 

  * **output_config** ([::Google::Cloud::Asset::V1::IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicyAnalysisOutputConfig), ::Hash) — Required. Output configuration indicating where the results will be output to. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::AnalyzeIamPolicyLongrunningRequest.new
    
    # Call the analyze_iam_policy_longrunning method.
    result = client.analyze_iam_policy_longrunning request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #analyze_move
    
    
    def analyze_move(request, options = nil) -> ::Google::Cloud::Asset::V1::AnalyzeMoveResponse
    def analyze_move(resource: nil, destination_parent: nil, view: nil) -> ::Google::Cloud::Asset::V1::AnalyzeMoveResponse

Analyze moving a resource to a specified destination without kicking off the actual move. The analysis is best effort depending on the user's permissions of viewing different hierarchical policies and configurations. The policies and configuration are subject to change before the actual resource migration takes place.

**Overloads**
    
    
    def analyze_move(request, options = nil) -> ::Google::Cloud::Asset::V1::AnalyzeMoveResponse

Pass arguments to `analyze_move` via a request object, either of type [Google::Cloud::Asset::V1::AnalyzeMoveRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeMoveRequest "Google::Cloud::Asset::V1::AnalyzeMoveRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::AnalyzeMoveRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeMoveRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def analyze_move(resource: nil, destination_parent: nil, view: nil) -> ::Google::Cloud::Asset::V1::AnalyzeMoveResponse

Pass arguments to `analyze_move` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — Required. Name of the resource to perform the analysis against. Only Google Cloud projects are supported as of today. Hence, this can only be a project ID (such as "projects/my-project-id") or a project number (such as "projects/12345"). 
  * **destination_parent** (::String) — Required. Name of the Google Cloud folder or organization to reparent the target resource. The analysis will be performed against hypothetically moving the resource to this specified destination parent. This can only be a folder number (such as "folders/123") or an organization number (such as "organizations/123"). 
  * **view** ([::Google::Cloud::Asset::V1::AnalyzeMoveRequest::AnalysisView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeMoveRequest-AnalysisView)) — Analysis view indicating what information should be included in the analysis response. If unspecified, the default view is FULL. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::AnalyzeMoveResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeMoveResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::AnalyzeMoveResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeMoveResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::AnalyzeMoveRequest.new
    
    # Call the analyze_move method.
    result = client.analyze_move request
    
    # The returned object is of type Google::Cloud::Asset::V1::AnalyzeMoveResponse.
    p result

### #analyze_org_policies
    
    
    def analyze_org_policies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse::OrgPolicyResult>
    def analyze_org_policies(scope: nil, constraint: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse::OrgPolicyResult>

Analyzes organization policies under a scope.

**Overloads**
    
    
    def analyze_org_policies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse::OrgPolicyResult>

Pass arguments to `analyze_org_policies` via a request object, either of type [Google::Cloud::Asset::V1::AnalyzeOrgPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPoliciesRequest "Google::Cloud::Asset::V1::AnalyzeOrgPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::AnalyzeOrgPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def analyze_org_policies(scope: nil, constraint: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse::OrgPolicyResult>

Pass arguments to `analyze_org_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **scope** (::String) — 

Required. The organization to scope the request. Only organization policies within the scope will be analyzed.

    * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")
  * **constraint** (::String) — Required. The name of the constraint to analyze organization policies for. The response only contains analyzed organization policies for the provided constraint. 
  * **filter** (::String) — The expression to filter [AnalyzeOrgPoliciesResponse.org_policy_results](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPoliciesResponse#Google__Cloud__Asset__V1__AnalyzeOrgPoliciesResponse_org_policy_results_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse#org_policy_results \(method\)"). Filtering is currently available for bare literal values and the following fields:

    * consolidated_policy.attached_resource
    * consolidated_policy.rules.enforce

When filtering by a specific field, the only supported operator is `=`. For example, filtering by consolidated_policy.attached_resource="//cloudresourcemanager.googleapis.com/folders/001" will return all the Organization Policy results attached to "folders/001". 

  * **page_size** (::Integer) — The maximum number of items to return per page. If unspecified, [AnalyzeOrgPoliciesResponse.org_policy_results](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPoliciesResponse#Google__Cloud__Asset__V1__AnalyzeOrgPoliciesResponse_org_policy_results_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse#org_policy_results \(method\)") will contain 20 items with a maximum of 200. 
  * **page_token** (::String) — The pagination token to retrieve the next page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse::OrgPolicyResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPoliciesResponse-OrgPolicyResult)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse::OrgPolicyResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPoliciesResponse-OrgPolicyResult)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::AnalyzeOrgPoliciesRequest.new
    
    # Call the analyze_org_policies method.
    result = client.analyze_org_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Asset::V1::AnalyzeOrgPoliciesResponse::OrgPolicyResult.
      p item
    end

### #analyze_org_policy_governed_assets
    
    
    def analyze_org_policy_governed_assets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse::GovernedAsset>
    def analyze_org_policy_governed_assets(scope: nil, constraint: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse::GovernedAsset>

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



This RPC only returns either resources of types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types) or IAM policies.

**Overloads**
    
    
    def analyze_org_policy_governed_assets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse::GovernedAsset>

Pass arguments to `analyze_org_policy_governed_assets` via a request object, either of type [Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedAssetsRequest "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedAssetsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def analyze_org_policy_governed_assets(scope: nil, constraint: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse::GovernedAsset>

Pass arguments to `analyze_org_policy_governed_assets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **scope** (::String) — 

Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output assets will also be limited to the ones governed by those in-scope organization policies.

    * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")
  * **constraint** (::String) — Required. The name of the constraint to analyze governed assets for. The analysis only contains analyzed organization policies for the provided constraint. 
  * **filter** (::String) — 

The expression to filter [AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedAssetsResponse#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedAssetsResponse_governed_assets_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse#governed_assets \(method\)").

For governed resources, filtering is currently available for bare literal values and the following fields:

    * governed_resource.project
    * governed_resource.folders
    * consolidated_policy.rules.enforce When filtering by `governed_resource.project` or `consolidated_policy.rules.enforce`, the only supported operator is `=`. When filtering by `governed_resource.folders`, the supported operators are `=` and `:`. For example, filtering by `governed_resource.project="projects/12345678"` will return all the governed resources under "projects/12345678", including the project itself if applicable.

For governed IAM policies, filtering is currently available for bare literal values and the following fields:

    * governed_iam_policy.project
    * governed_iam_policy.folders
    * consolidated_policy.rules.enforce When filtering by `governed_iam_policy.project` or `consolidated_policy.rules.enforce`, the only supported operator is `=`. When filtering by `governed_iam_policy.folders`, the supported operators are `=` and `:`. For example, filtering by `governed_iam_policy.folders:"folders/12345678"` will return all the governed IAM policies under "folders/001".
  * **page_size** (::Integer) — The maximum number of items to return per page. If unspecified, [AnalyzeOrgPolicyGovernedAssetsResponse.governed_assets](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedAssetsResponse#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedAssetsResponse_governed_assets_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse#governed_assets \(method\)") will contain 100 items with a maximum of 200. 
  * **page_token** (::String) — The pagination token to retrieve the next page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse::GovernedAsset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedAssetsResponse-GovernedAsset)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse::GovernedAsset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedAssetsResponse-GovernedAsset)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsRequest.new
    
    # Call the analyze_org_policy_governed_assets method.
    result = client.analyze_org_policy_governed_assets request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedAssetsResponse::GovernedAsset.
      p item
    end

### #analyze_org_policy_governed_containers
    
    
    def analyze_org_policy_governed_containers(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer>
    def analyze_org_policy_governed_containers(scope: nil, constraint: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer>

Analyzes organization policies governed containers (projects, folders or organization) under a scope.

**Overloads**
    
    
    def analyze_org_policy_governed_containers(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer>

Pass arguments to `analyze_org_policy_governed_containers` via a request object, either of type [Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersRequest "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def analyze_org_policy_governed_containers(scope: nil, constraint: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer>

Pass arguments to `analyze_org_policy_governed_containers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **scope** (::String) — 

Required. The organization to scope the request. Only organization policies within the scope will be analyzed. The output containers will also be limited to the ones governed by those in-scope organization policies.

    * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")
  * **constraint** (::String) — Required. The name of the constraint to analyze governed containers for. The analysis only contains organization policies for the provided constraint. 
  * **filter** (::String) — The expression to filter [AnalyzeOrgPolicyGovernedContainersResponse.governed_containers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersResponse_governed_containers_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse#governed_containers \(method\)"). Filtering is currently available for bare literal values and the following fields:

    * parent
    * consolidated_policy.rules.enforce

When filtering by a specific field, the only supported operator is `=`. For example, filtering by parent="//cloudresourcemanager.googleapis.com/folders/001" will return all the containers under "folders/001". 

  * **page_size** (::Integer) — The maximum number of items to return per page. If unspecified, [AnalyzeOrgPolicyGovernedContainersResponse.governed_containers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse#Google__Cloud__Asset__V1__AnalyzeOrgPolicyGovernedContainersResponse_governed_containers_instance_ "Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse#governed_containers \(method\)") will contain 100 items with a maximum of 200. 
  * **page_token** (::String) — The pagination token to retrieve the next page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AnalyzeOrgPolicyGovernedContainersResponse-GovernedContainer)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersRequest.new
    
    # Call the analyze_org_policy_governed_containers method.
    result = client.analyze_org_policy_governed_containers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Asset::V1::AnalyzeOrgPolicyGovernedContainersResponse::GovernedContainer.
      p item
    end

### #batch_get_assets_history
    
    
    def batch_get_assets_history(request, options = nil) -> ::Google::Cloud::Asset::V1::BatchGetAssetsHistoryResponse
    def batch_get_assets_history(parent: nil, asset_names: nil, content_type: nil, read_time_window: nil, relationship_types: nil) -> ::Google::Cloud::Asset::V1::BatchGetAssetsHistoryResponse

Batch gets the update history of assets that overlap a time window. For IAM_POLICY content, this API outputs history when the asset and its attached IAM POLICY both exist. This can create gaps in the output history. Otherwise, this API outputs history with asset in both non-delete or deleted status. If a specified asset does not exist, this API returns an INVALID_ARGUMENT error.

**Overloads**
    
    
    def batch_get_assets_history(request, options = nil) -> ::Google::Cloud::Asset::V1::BatchGetAssetsHistoryResponse

Pass arguments to `batch_get_assets_history` via a request object, either of type [BatchGetAssetsHistoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-BatchGetAssetsHistoryRequest "Google::Cloud::Asset::V1::BatchGetAssetsHistoryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::BatchGetAssetsHistoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-BatchGetAssetsHistoryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def batch_get_assets_history(parent: nil, asset_names: nil, content_type: nil, read_time_window: nil, relationship_types: nil) -> ::Google::Cloud::Asset::V1::BatchGetAssetsHistoryResponse

Pass arguments to `batch_get_assets_history` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The relative name of the root asset. It can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id")", or a project number (such as "projects/12345"). 
  * **asset_names** (::Array<::String>) — A list of the full names of the assets. See: https://cloud.google.com/asset-inventory/docs/resource-name-format Example:

`//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`.

The request becomes a no-op if the asset name list is empty, and the max size of the asset name list is 100 in one request. 

  * **content_type** ([::Google::Cloud::Asset::V1::ContentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ContentType)) — Optional. The content type. 
  * **read_time_window** ([::Google::Cloud::Asset::V1::TimeWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-TimeWindow), ::Hash) — Optional. The time window for the asset history. Both start_time and end_time are optional and if set, it must be after the current time minus 35 days. If end_time is not set, it is default to current timestamp. If start_time is not set, the snapshot of the assets at end_time will be returned. The returned results contain all temporal assets whose time window overlap with read_time_window. 
  * **relationship_types** (::Array<::String>) — 

Optional. A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP.

    * If specified: it outputs specified relationships' history on the [asset_names]. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_names] or if any of the [asset_names]'s types doesn't belong to the source types of the [relationship_types].
    * Otherwise: it outputs the supported relationships' history on the [asset_names] or returns an error if any of the [asset_names]'s types has no relationship support. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-BatchGetAssetsHistoryResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-BatchGetAssetsHistoryResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::BatchGetAssetsHistoryRequest.new
    
    # Call the batch_get_assets_history method.
    result = client.batch_get_assets_history request
    
    # The returned object is of type Google::Cloud::Asset::V1::BatchGetAssetsHistoryResponse.
    p result

### #batch_get_effective_iam_policies
    
    
    def batch_get_effective_iam_policies(request, options = nil) -> ::Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesResponse
    def batch_get_effective_iam_policies(scope: nil, names: nil) -> ::Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesResponse

Gets effective IAM policies for a batch of resources.

**Overloads**
    
    
    def batch_get_effective_iam_policies(request, options = nil) -> ::Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesResponse

Pass arguments to `batch_get_effective_iam_policies` via a request object, either of type [BatchGetEffectiveIamPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-BatchGetEffectiveIamPoliciesRequest "Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-BatchGetEffectiveIamPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def batch_get_effective_iam_policies(scope: nil, names: nil) -> ::Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesResponse

Pass arguments to `batch_get_effective_iam_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **scope** (::String) — Required. Only IAM policies on or below the scope will be returned.

This can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345").

To know how to get organization ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

To know how to get folder or project ID, visit [here ](https://cloud.google.com/resource-manager/docs/creating-managing-folders#viewing_or_listing_folders_and_projects). 

  * **names** (::Array<::String>) — Required. The names refer to the [full_resource_names](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types). A maximum of 20 resources' effective policies can be retrieved in a batch. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-BatchGetEffectiveIamPoliciesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-BatchGetEffectiveIamPoliciesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesRequest.new
    
    # Call the batch_get_effective_iam_policies method.
    result = client.batch_get_effective_iam_policies request
    
    # The returned object is of type Google::Cloud::Asset::V1::BatchGetEffectiveIamPoliciesResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the AssetService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client#Google__Cloud__Asset__V1__AssetService__Rest__Client_configure_class_ "Google::Cloud::Asset::V1::AssetService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client-Configuration "Google::Cloud::Asset::V1::AssetService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client-Configuration)) 



### #create_feed
    
    
    def create_feed(request, options = nil) -> ::Google::Cloud::Asset::V1::Feed
    def create_feed(parent: nil, feed_id: nil, feed: nil) -> ::Google::Cloud::Asset::V1::Feed

Creates a feed in a parent project/folder/organization to listen to its asset updates.

**Overloads**
    
    
    def create_feed(request, options = nil) -> ::Google::Cloud::Asset::V1::Feed

Pass arguments to `create_feed` via a request object, either of type [CreateFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-CreateFeedRequest "Google::Cloud::Asset::V1::CreateFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::CreateFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-CreateFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_feed(parent: nil, feed_id: nil, feed: nil) -> ::Google::Cloud::Asset::V1::Feed

Pass arguments to `create_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the project/folder/organization where this feed should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"). 
  * **feed_id** (::String) — Required. This is the client-assigned asset feed identifier and it needs to be unique under a specific parent project/folder/organization. 
  * **feed** ([::Google::Cloud::Asset::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed), ::Hash) — Required. The feed details. The field `name` must be empty and it will be generated in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::CreateFeedRequest.new
    
    # Call the create_feed method.
    result = client.create_feed request
    
    # The returned object is of type Google::Cloud::Asset::V1::Feed.
    p result

### #create_saved_query
    
    
    def create_saved_query(request, options = nil) -> ::Google::Cloud::Asset::V1::SavedQuery
    def create_saved_query(parent: nil, saved_query: nil, saved_query_id: nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Creates a saved query in a parent project/folder/organization.

**Overloads**
    
    
    def create_saved_query(request, options = nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Pass arguments to `create_saved_query` via a request object, either of type [CreateSavedQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-CreateSavedQueryRequest "Google::Cloud::Asset::V1::CreateSavedQueryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::CreateSavedQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-CreateSavedQueryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_saved_query(parent: nil, saved_query: nil, saved_query_id: nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Pass arguments to `create_saved_query` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the project/folder/organization where this saved_query should be created in. It can only be an organization number (such as "organizations/123"), a folder number (such as "folders/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"). 
  * **saved_query** ([::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery), ::Hash) — Required. The saved_query details. The `name` field must be empty as it will be generated based on the parent and saved_query_id. 
  * **saved_query_id** (::String) — Required. The ID to use for the saved query, which must be unique in the specified parent. It will become the final component of the saved query's resource name.

This value should be 4-63 characters, and valid characters are `[a-z][0-9]-`.

Notice that this field is required in the saved query creation, and the `name` field of the `saved_query` will be ignored. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::CreateSavedQueryRequest.new
    
    # Call the create_saved_query method.
    result = client.create_saved_query request
    
    # The returned object is of type Google::Cloud::Asset::V1::SavedQuery.
    p result

### #delete_feed
    
    
    def delete_feed(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_feed(name: nil) -> ::Google::Protobuf::Empty

Deletes an asset feed.

**Overloads**
    
    
    def delete_feed(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_feed` via a request object, either of type [DeleteFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-DeleteFeedRequest "Google::Cloud::Asset::V1::DeleteFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::DeleteFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-DeleteFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_feed(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the feed and it must be in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::DeleteFeedRequest.new
    
    # Call the delete_feed method.
    result = client.delete_feed request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_saved_query
    
    
    def delete_saved_query(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_saved_query(name: nil) -> ::Google::Protobuf::Empty

Deletes a saved query.

**Overloads**
    
    
    def delete_saved_query(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_saved_query` via a request object, either of type [DeleteSavedQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-DeleteSavedQueryRequest "Google::Cloud::Asset::V1::DeleteSavedQueryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::DeleteSavedQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-DeleteSavedQueryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_saved_query(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_saved_query` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The name of the saved query to delete. It must be in the format of:

    * projects/project_number/savedQueries/saved_query_id
    * folders/folder_number/savedQueries/saved_query_id
    * organizations/organization_number/savedQueries/saved_query_id



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::DeleteSavedQueryRequest.new
    
    # Call the delete_saved_query method.
    result = client.delete_saved_query request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #export_assets
    
    
    def export_assets(request, options = nil) -> ::Gapic::Operation
    def export_assets(parent: nil, read_time: nil, asset_types: nil, content_type: nil, output_config: nil, relationship_types: nil) -> ::Gapic::Operation

Exports assets with time and resource types to a given Cloud Storage location/BigQuery table. For Cloud Storage location destinations, the output format is newline-delimited JSON. Each line represents a [google.cloud.asset.v1.Asset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Asset "Google::Cloud::Asset::V1::Asset \(class\)") in the JSON format; for BigQuery table destinations, the output table stores the fields in asset Protobuf as columns. This API implements the [google.longrunning.Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") API, which allows you to keep track of the export. We recommend intervals of at least 2 seconds with exponential retry to poll the export operation result. For regular-size resource parent, the export operation usually finishes within 5 minutes.

**Overloads**
    
    
    def export_assets(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_assets` via a request object, either of type [ExportAssetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ExportAssetsRequest "Google::Cloud::Asset::V1::ExportAssetsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::ExportAssetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ExportAssetsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_assets(parent: nil, read_time: nil, asset_types: nil, content_type: nil, output_config: nil, relationship_types: nil) -> ::Gapic::Operation

Pass arguments to `export_assets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The relative name of the root asset. This can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"), or a folder number (such as "folders/123"). 
  * **read_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Timestamp), ::Hash) — Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results. 
  * **asset_types** (::Array<::String>) — A list of asset types to take a snapshot for. For example: "compute.googleapis.com/Disk".

Regular expressions are also supported. For example:

    * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
    * ".*Instance" snapshots resources whose asset type ends with "Instance".
    * "._Instance._ " snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.

If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types. 

  * **content_type** ([::Google::Cloud::Asset::V1::ContentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ContentType)) — Asset content type. If not specified, no content but the asset name will be returned. 
  * **output_config** ([::Google::Cloud::Asset::V1::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-OutputConfig), ::Hash) — Required. Output configuration indicating where the results will be output to. 
  * **relationship_types** (::Array<::String>) — 

A list of relationship types to export, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP.

    * If specified: it snapshots specified relationships. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_types] or if any of the [asset_types] doesn't belong to the source types of the [relationship_types].
    * Otherwise: it snapshots the supported relationships for all [asset_types] or returns an error if any of the [asset_types] has no relationship support. An unspecified asset types field means all supported asset_types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::ExportAssetsRequest.new
    
    # Call the export_assets method.
    result = client.export_assets request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_feed
    
    
    def get_feed(request, options = nil) -> ::Google::Cloud::Asset::V1::Feed
    def get_feed(name: nil) -> ::Google::Cloud::Asset::V1::Feed

Gets details about an asset feed.

**Overloads**
    
    
    def get_feed(request, options = nil) -> ::Google::Cloud::Asset::V1::Feed

Pass arguments to `get_feed` via a request object, either of type [GetFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-GetFeedRequest "Google::Cloud::Asset::V1::GetFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::GetFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-GetFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_feed(name: nil) -> ::Google::Cloud::Asset::V1::Feed

Pass arguments to `get_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Feed and it must be in the format of: projects/project_number/feeds/feed_id folders/folder_number/feeds/feed_id organizations/organization_number/feeds/feed_id 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::GetFeedRequest.new
    
    # Call the get_feed method.
    result = client.get_feed request
    
    # The returned object is of type Google::Cloud::Asset::V1::Feed.
    p result

### #get_saved_query
    
    
    def get_saved_query(request, options = nil) -> ::Google::Cloud::Asset::V1::SavedQuery
    def get_saved_query(name: nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Gets details about a saved query.

**Overloads**
    
    
    def get_saved_query(request, options = nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Pass arguments to `get_saved_query` via a request object, either of type [GetSavedQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-GetSavedQueryRequest "Google::Cloud::Asset::V1::GetSavedQueryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::GetSavedQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-GetSavedQueryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_saved_query(name: nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Pass arguments to `get_saved_query` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The name of the saved query and it must be in the format of:

    * projects/project_number/savedQueries/saved_query_id
    * folders/folder_number/savedQueries/saved_query_id
    * organizations/organization_number/savedQueries/saved_query_id



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::GetSavedQueryRequest.new
    
    # Call the get_saved_query method.
    result = client.get_saved_query request
    
    # The returned object is of type Google::Cloud::Asset::V1::SavedQuery.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new AssetService REST client object.

**Yields**

  * (config) — Configure the AssetService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Asset::V1::AssetService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_assets
    
    
    def list_assets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::Asset>
    def list_assets(parent: nil, read_time: nil, asset_types: nil, content_type: nil, page_size: nil, page_token: nil, relationship_types: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::Asset>

Lists assets with time and resource types and returns paged results in response.

**Overloads**
    
    
    def list_assets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::Asset>

Pass arguments to `list_assets` via a request object, either of type [ListAssetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ListAssetsRequest "Google::Cloud::Asset::V1::ListAssetsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::ListAssetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ListAssetsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_assets(parent: nil, read_time: nil, asset_types: nil, content_type: nil, page_size: nil, page_token: nil, relationship_types: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::Asset>

Pass arguments to `list_assets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Name of the organization, folder, or project the assets belong to. Format: "organizations/[organization-number]" (such as "organizations/123"), "projects/[project-id]" (such as "projects/my-project-id"), "projects/[project-number]" (such as "projects/12345"), or "folders/[folder-number]" (such as "folders/12345"). 
  * **read_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Timestamp), ::Hash) — Timestamp to take an asset snapshot. This can only be set to a timestamp between the current time and the current time minus 35 days (inclusive). If not specified, the current time will be used. Due to delays in resource data collection and indexing, there is a volatile window during which running the same query may get different results. 
  * **asset_types** (::Array<::String>) — A list of asset types to take a snapshot for. For example: "compute.googleapis.com/Disk".

Regular expression is also supported. For example:

    * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
    * ".*Instance" snapshots resources whose asset type ends with "Instance".
    * "._Instance._ " snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned.

If specified, only matching assets will be returned, otherwise, it will snapshot all asset types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types. 

  * **content_type** ([::Google::Cloud::Asset::V1::ContentType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ContentType)) — Asset content type. If not specified, no content but the asset name will be returned. 
  * **page_size** (::Integer) — The maximum number of assets to be returned in a single response. Default is 100, minimum is 1, and maximum is 1000. 
  * **page_token** (::String) — The `next_page_token` returned from the previous `ListAssetsResponse`, or unspecified for the first `ListAssetsRequest`. It is a continuation of a prior `ListAssets` call, and the API should return the next page of assets. 
  * **relationship_types** (::Array<::String>) — 

A list of relationship types to output, for example: `INSTANCE_TO_INSTANCEGROUP`. This field should only be specified if content_type=RELATIONSHIP.

    * If specified: it snapshots specified relationships. It returns an error if any of the [relationship_types] doesn't belong to the supported relationship types of the [asset_types] or if any of the [asset_types] doesn't belong to the source types of the [relationship_types].
    * Otherwise: it snapshots the supported relationships for all [asset_types] or returns an error if any of the [asset_types] has no relationship support. An unspecified asset types field means all supported asset_types. See [Introduction to Cloud Asset Inventory](https://cloud.google.com/asset-inventory/docs/overview) for all supported asset types and relationship types.



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::Asset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Asset)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::Asset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Asset)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::ListAssetsRequest.new
    
    # Call the list_assets method.
    result = client.list_assets request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Asset::V1::Asset.
      p item
    end

### #list_feeds
    
    
    def list_feeds(request, options = nil) -> ::Google::Cloud::Asset::V1::ListFeedsResponse
    def list_feeds(parent: nil) -> ::Google::Cloud::Asset::V1::ListFeedsResponse

Lists all asset feeds in a parent project/folder/organization.

**Overloads**
    
    
    def list_feeds(request, options = nil) -> ::Google::Cloud::Asset::V1::ListFeedsResponse

Pass arguments to `list_feeds` via a request object, either of type [ListFeedsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ListFeedsRequest "Google::Cloud::Asset::V1::ListFeedsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::ListFeedsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ListFeedsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_feeds(parent: nil) -> ::Google::Cloud::Asset::V1::ListFeedsResponse

Pass arguments to `list_feeds` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **parent** (::String) — Required. The parent project/folder/organization whose feeds are to be listed. It can only be using project/folder/organization number (such as "folders/12345")", or a project ID (such as "projects/my-project-id"). 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::ListFeedsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ListFeedsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::ListFeedsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ListFeedsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::ListFeedsRequest.new
    
    # Call the list_feeds method.
    result = client.list_feeds request
    
    # The returned object is of type Google::Cloud::Asset::V1::ListFeedsResponse.
    p result

### #list_saved_queries
    
    
    def list_saved_queries(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::SavedQuery>
    def list_saved_queries(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::SavedQuery>

Lists all saved queries in a parent project/folder/organization.

**Overloads**
    
    
    def list_saved_queries(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::SavedQuery>

Pass arguments to `list_saved_queries` via a request object, either of type [ListSavedQueriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ListSavedQueriesRequest "Google::Cloud::Asset::V1::ListSavedQueriesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::ListSavedQueriesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ListSavedQueriesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_saved_queries(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::SavedQuery>

Pass arguments to `list_saved_queries` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent project/folder/organization whose savedQueries are to be listed. It can only be using project/folder/organization number (such as "folders/12345")", or a project ID (such as "projects/my-project-id"). 
  * **filter** (::String) — Optional. The expression to filter resources. The expression is a list of zero or more restrictions combined via logical operators `AND` and `OR`. When `AND` and `OR` are both used in the expression, parentheses must be appropriately used to group the combinations. The expression may also contain regular expressions.

See https://google.aip.dev/160 for more information on the grammar. 

  * **page_size** (::Integer) — Optional. The maximum number of saved queries to return per page. The service may return fewer than this value. If unspecified, at most 50 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListSavedQueries` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListSavedQueries` must match the call that provided the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::ListSavedQueriesRequest.new
    
    # Call the list_saved_queries method.
    result = client.list_saved_queries request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Asset::V1::SavedQuery.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Asset::V1::AssetService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Asset::V1::AssetService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-AssetService-Rest-Operations)) 



### #query_assets
    
    
    def query_assets(request, options = nil) -> ::Google::Cloud::Asset::V1::QueryAssetsResponse
    def query_assets(parent: nil, statement: nil, job_reference: nil, page_size: nil, page_token: nil, timeout: nil, read_time_window: nil, read_time: nil, output_config: nil) -> ::Google::Cloud::Asset::V1::QueryAssetsResponse

Issue a job that queries assets using a SQL statement compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql).

If the query execution finishes within timeout and there's no pagination, the full query results will be returned in the `QueryAssetsResponse`.

Otherwise, full query results can be obtained by issuing extra requests with the `job_reference` from the a previous `QueryAssets` call.

Note, the query result has approximately 10 GB limitation enforced by [BigQuery](https://cloud.google.com/bigquery/docs/best-practices-performance-output). Queries return larger results will result in errors.

**Overloads**
    
    
    def query_assets(request, options = nil) -> ::Google::Cloud::Asset::V1::QueryAssetsResponse

Pass arguments to `query_assets` via a request object, either of type [QueryAssetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-QueryAssetsRequest "Google::Cloud::Asset::V1::QueryAssetsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::QueryAssetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-QueryAssetsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def query_assets(parent: nil, statement: nil, job_reference: nil, page_size: nil, page_token: nil, timeout: nil, read_time_window: nil, read_time: nil, output_config: nil) -> ::Google::Cloud::Asset::V1::QueryAssetsResponse

Pass arguments to `query_assets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The relative name of the root asset. This can only be an organization number (such as "organizations/123"), a project ID (such as "projects/my-project-id"), or a project number (such as "projects/12345"), or a folder number (such as "folders/123").

Only assets belonging to the `parent` will be returned. 

  * **statement** (::String) — Optional. A SQL statement that's compatible with [BigQuery SQL](https://cloud.google.com/bigquery/docs/introduction-sql).

Note: The following parameters are mutually exclusive: `statement`, `job_reference`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **job_reference** (::String) — Optional. Reference to the query job, which is from the `QueryAssetsResponse` of previous `QueryAssets` call.

Note: The following parameters are mutually exclusive: `job_reference`, `statement`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **page_size** (::Integer) — Optional. The maximum number of rows to return in the results. Responses are limited to 10 MB and 1000 rows.

By default, the maximum row count is 1000. When the byte or row count limit is reached, the rest of the query results will be paginated.

The field will be ignored when [output_config] is specified. 

  * **page_token** (::String) — Optional. A page token received from previous `QueryAssets`.

The field will be ignored when [output_config] is specified. 

  * **timeout** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Duration), ::Hash) — Optional. Specifies the maximum amount of time that the client is willing to wait for the query to complete. By default, this limit is 5 min for the first query, and 1 minute for the following queries. If the query is complete, the `done` field in the `QueryAssetsResponse` is true, otherwise false.

Like BigQuery [jobs.query API](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query#queryrequest) The call is not guaranteed to wait for the specified timeout; it typically returns after around 200 seconds (200,000 milliseconds), even if the query is not complete.

The field will be ignored when [output_config] is specified. 

  * **read_time_window** ([::Google::Cloud::Asset::V1::TimeWindow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-TimeWindow), ::Hash) — Optional. [start_time] is required. [start_time] must be less than [end_time] Defaults [end_time] to now if [start_time] is set and [end_time] isn't. Maximum permitted time range is 7 days.

Note: The following parameters are mutually exclusive: `read_time_window`, `read_time`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **read_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-Timestamp), ::Hash) — Optional. Queries cloud assets as they appeared at the specified point in time.

Note: The following parameters are mutually exclusive: `read_time`, `read_time_window`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **output_config** ([::Google::Cloud::Asset::V1::QueryAssetsOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-QueryAssetsOutputConfig), ::Hash) — Optional. Destination where the query results will be saved.

When this field is specified, the query results won't be saved in the [QueryAssetsResponse.query_result]. Instead [QueryAssetsResponse.output_config] will be set.

Meanwhile, [QueryAssetsResponse.job_reference] will be set and can be used to check the status of the query job when passed to a following [QueryAssets] API call. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::QueryAssetsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-QueryAssetsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::QueryAssetsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-QueryAssetsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::QueryAssetsRequest.new
    
    # Call the query_assets method.
    result = client.query_assets request
    
    # The returned object is of type Google::Cloud::Asset::V1::QueryAssetsResponse.
    p result

### #search_all_iam_policies
    
    
    def search_all_iam_policies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::IamPolicySearchResult>
    def search_all_iam_policies(scope: nil, query: nil, page_size: nil, page_token: nil, asset_types: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::IamPolicySearchResult>

Searches all IAM policies within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllIamPolicies` permission on the desired scope, otherwise the request will be rejected.

**Overloads**
    
    
    def search_all_iam_policies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::IamPolicySearchResult>

Pass arguments to `search_all_iam_policies` via a request object, either of type [SearchAllIamPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SearchAllIamPoliciesRequest "Google::Cloud::Asset::V1::SearchAllIamPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::SearchAllIamPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SearchAllIamPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def search_all_iam_policies(scope: nil, query: nil, page_size: nil, page_token: nil, asset_types: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::IamPolicySearchResult>

Pass arguments to `search_all_iam_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **scope** (::String) — 

Required. A scope can be a project, a folder, or an organization. The search is limited to the IAM policies within the `scope`. The caller must be granted the [`cloudasset.assets.searchAllIamPolicies`](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope.

The allowed values are:

    * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
    * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
    * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
    * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")
  * **query** (::String) — 

Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-iam-policies#how_to_construct_a_query) for more information. If not specified or empty, it will search all the IAM policies within the specified `scope`. Note that the query string is compared against each IAM policy binding, including its principals, roles, and IAM conditions. The returned IAM policies will only contain the bindings that match your query. To learn more about the IAM policy structure, see the [IAM policy documentation](https://cloud.google.com/iam/help/allow-policies/structure).

Examples:

    * `policy:amy@gmail.com` to find IAM policy bindings that specify user "amy@gmail.com".
    * `policy:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role.
    * `policy:comp*` to find IAM policy bindings that contain "comp" as a prefix of any word in the binding.
    * `policy.role.permissions:storage.buckets.update` to find IAM policy bindings that specify a role containing "storage.buckets.update" permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results.
    * `policy.role.permissions:upd*` to find IAM policy bindings that specify a role containing "upd" as a prefix of any word in the role permission. Note that if callers don't have `iam.roles.get` access to a role's included permissions, policy bindings that specify this role will be dropped from the search results.
    * `resource:organizations/123456` to find IAM policy bindings that are set on "organizations/123456".
    * `resource=//cloudresourcemanager.googleapis.com/projects/myproject` to find IAM policy bindings that are set on the project named "myproject".
    * `Important` to find IAM policy bindings that contain "Important" as a word in any of the searchable fields (except for the included permissions).
    * `resource:(instance1 OR instance2) policy:amy` to find IAM policy bindings that are set on resources "instance1" or "instance2" and also specify user "amy".
    * `roles:roles/compute.admin` to find IAM policy bindings that specify the Compute Admin role.
    * `memberTypes:user` to find IAM policy bindings that contain the principal type "user".
  * **page_size** (::Integer) — Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned. 
  * **page_token** (::String) — Optional. If present, retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters must be identical to those in the previous call. 
  * **asset_types** (::Array<::String>) — Optional. A list of asset types that the IAM policies are attached to. If empty, it will search the IAM policies that are attached to all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types)

Regular expressions are also supported. For example:

    * "compute.googleapis.com.*" snapshots IAM policies attached to asset type starts with "compute.googleapis.com".
    * ".*Instance" snapshots IAM policies attached to asset type ends with "Instance".
    * "._Instance._ " snapshots IAM policies attached to asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned. 

  * **order_by** (::String) — 

Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add " DESC" after the field name to indicate descending order. Redundant space characters are ignored. Example: "assetType DESC, resource". Only singular primitive fields in the response are sortable:

    * resource
    * assetType
    * project All the other fields such as repeated fields (e.g., `folders`) and non-primitive fields (e.g., `policy`) are not supported.



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::IamPolicySearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicySearchResult)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::IamPolicySearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-IamPolicySearchResult)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::SearchAllIamPoliciesRequest.new
    
    # Call the search_all_iam_policies method.
    result = client.search_all_iam_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Asset::V1::IamPolicySearchResult.
      p item
    end

### #search_all_resources
    
    
    def search_all_resources(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::ResourceSearchResult>
    def search_all_resources(scope: nil, query: nil, asset_types: nil, page_size: nil, page_token: nil, order_by: nil, read_mask: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::ResourceSearchResult>

Searches all Google Cloud resources within the specified scope, such as a project, folder, or organization. The caller must be granted the `cloudasset.assets.searchAllResources` permission on the desired scope, otherwise the request will be rejected.

**Overloads**
    
    
    def search_all_resources(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::ResourceSearchResult>

Pass arguments to `search_all_resources` via a request object, either of type [SearchAllResourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SearchAllResourcesRequest "Google::Cloud::Asset::V1::SearchAllResourcesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::SearchAllResourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SearchAllResourcesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def search_all_resources(scope: nil, query: nil, asset_types: nil, page_size: nil, page_token: nil, order_by: nil, read_mask: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Asset::V1::ResourceSearchResult>

Pass arguments to `search_all_resources` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **scope** (::String) — 

Required. A scope can be a project, a folder, or an organization. The search is limited to the resources within the `scope`. The caller must be granted the [`cloudasset.assets.searchAllResources`](https://cloud.google.com/asset-inventory/docs/access-control#required_permissions) permission on the desired scope.

The allowed values are:

    * projects/{PROJECT_ID} (e.g., "projects/foo-bar")
    * projects/{PROJECT_NUMBER} (e.g., "projects/12345678")
    * folders/{FOLDER_NUMBER} (e.g., "folders/1234567")
    * organizations/{ORGANIZATION_NUMBER} (e.g., "organizations/123456")
  * **query** (::String) — 

Optional. The query statement. See [how to construct a query](https://cloud.google.com/asset-inventory/docs/searching-resources#how_to_construct_a_query) for more information. If not specified or empty, it will search all the resources within the specified `scope`.

Examples:

    * `name:Important` to find Google Cloud resources whose name contains `Important` as a word.
    * `name=Important` to find the Google Cloud resource whose name is exactly `Important`.
    * `displayName:Impor*` to find Google Cloud resources whose display name contains `Impor` as a prefix of any word in the field.
    * `location:us-west*` to find Google Cloud resources whose location contains both `us` and `west` as prefixes.
    * `labels:prod` to find Google Cloud resources whose labels contain `prod` as a key or value.
    * `labels.env:prod` to find Google Cloud resources that have a label `env` and its value is `prod`.
    * `labels.env:*` to find Google Cloud resources that have a label `env`.
    * `tagKeys:env` to find Google Cloud resources that have directly attached tags where the [`TagKey.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains `env`.
    * `tagValues:prod*` to find Google Cloud resources that have directly attached tags where the [`TagValue.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by `prod`.
    * `tagValueIds=tagValues/123` to find Google Cloud resources that have directly attached tags where the [`TagValue.name`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly `tagValues/123`.
    * `effectiveTagKeys:env` to find Google Cloud resources that have directly attached or inherited tags where the [`TagKey.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagKeys#resource:-tagkey) contains `env`.
    * `effectiveTagValues:prod*` to find Google Cloud resources that have directly attached or inherited tags where the [`TagValue.namespacedName`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) contains a word prefixed by `prod`.
    * `effectiveTagValueIds=tagValues/123` to find Google Cloud resources that have directly attached or inherited tags where the [`TagValue.name`](https://cloud.google.com/resource-manager/reference/rest/v3/tagValues#resource:-tagvalue) is exactly `tagValues/123`.
    * `kmsKey:key` to find Google Cloud resources encrypted with a customer-managed encryption key whose name contains `key` as a word. This field is deprecated. Use the `kmsKeys` field to retrieve Cloud KMS key information.
    * `kmsKeys:key` to find Google Cloud resources encrypted with customer-managed encryption keys whose name contains the word `key`.
    * `relationships:instance-group-1` to find Google Cloud resources that have relationships with `instance-group-1` in the related resource name.
    * `relationships:INSTANCE_TO_INSTANCEGROUP` to find Compute Engine instances that have relationships of type `INSTANCE_TO_INSTANCEGROUP`.
    * `relationships.INSTANCE_TO_INSTANCEGROUP:instance-group-1` to find Compute Engine instances that have relationships with `instance-group-1` in the Compute Engine instance group resource name, for relationship type `INSTANCE_TO_INSTANCEGROUP`.
    * `sccSecurityMarks.key=value` to find Cloud resources that are attached with security marks whose key is `key` and value is `value`.
    * `sccSecurityMarks.key:*` to find Cloud resources that are attached with security marks whose key is `key`.
    * `state:ACTIVE` to find Google Cloud resources whose state contains `ACTIVE` as a word.
    * `NOT state:ACTIVE` to find Google Cloud resources whose state doesn't contain `ACTIVE` as a word.
    * `createTime<1609459200` to find Google Cloud resources that were created before `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds.
    * `updateTime>1609459200` to find Google Cloud resources that were updated after `2021-01-01 00:00:00 UTC`. `1609459200` is the epoch timestamp of `2021-01-01 00:00:00 UTC` in seconds.
    * `Important` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields.
    * `Impor*` to find Google Cloud resources that contain `Impor` as a prefix of any word in any of the searchable fields.
    * `Important location:(us-west1 OR global)` to find Google Cloud resources that contain `Important` as a word in any of the searchable fields and are also located in the `us-west1` region or the `global` location.
  * **asset_types** (::Array<::String>) — Optional. A list of asset types that this request searches for. If empty, it will search all the asset types [supported by search APIs](https://cloud.google.com/asset-inventory/docs/supported-asset-types).

Regular expressions are also supported. For example:

    * "compute.googleapis.com.*" snapshots resources whose asset type starts with "compute.googleapis.com".
    * ".*Instance" snapshots resources whose asset type ends with "Instance".
    * "._Instance._ " snapshots resources whose asset type contains "Instance".

See [RE2](https://github.com/google/re2/wiki/Syntax) for all supported regular expression syntax. If the regular expression does not match any supported asset type, an INVALID_ARGUMENT error will be returned. 

  * **page_size** (::Integer) — Optional. The page size for search result pagination. Page size is capped at 500 even if a larger value is given. If set to zero or a negative value, server will pick an appropriate default. Returned results may be fewer than requested. When this happens, there could be more results as long as `next_page_token` is returned. 
  * **page_token** (::String) — Optional. If present, then retrieve the next batch of results from the preceding call to this method. `page_token` must be the value of `next_page_token` from the previous response. The values of all other method parameters, must be identical to those in the previous call. 
  * **order_by** (::String) — 

Optional. A comma-separated list of fields specifying the sorting order of the results. The default order is ascending. Add " DESC" after the field name to indicate descending order. Redundant space characters are ignored. Example: "location DESC, name". Only the following fields in the response are sortable:

    * name
    * assetType
    * project
    * displayName
    * description
    * location
    * createTime
    * updateTime
    * state
    * parentFullResourceName
    * parentAssetType
  * **read_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. A comma-separated list of fields that you want returned in the results. The following fields are returned by default if not specified:

    * `name`
    * `assetType`
    * `project`
    * `folders`
    * `organization`
    * `displayName`
    * `description`
    * `location`
    * `labels`
    * `tags`
    * `effectiveTags`
    * `networkTags`
    * `kmsKeys`
    * `createTime`
    * `updateTime`
    * `state`
    * `additionalAttributes`
    * `parentFullResourceName`
    * `parentAssetType`

Some fields of large size, such as `versionedResources`, `attachedResources`, `effectiveTags` etc., are not returned by default, but you can specify them in the `read_mask` parameter if you want to include them. If `"*"` is specified, all [available fields](https://cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/searchAllResources#resourcesearchresult) are returned. Examples: `"name,location"`, `"name,versionedResources"`, `"*"`. Any invalid field path will trigger INVALID_ARGUMENT error. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::ResourceSearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ResourceSearchResult)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Asset::V1::ResourceSearchResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-ResourceSearchResult)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::SearchAllResourcesRequest.new
    
    # Call the search_all_resources method.
    result = client.search_all_resources request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Asset::V1::ResourceSearchResult.
      p item
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_feed
    
    
    def update_feed(request, options = nil) -> ::Google::Cloud::Asset::V1::Feed
    def update_feed(feed: nil, update_mask: nil) -> ::Google::Cloud::Asset::V1::Feed

Updates an asset feed configuration.

**Overloads**
    
    
    def update_feed(request, options = nil) -> ::Google::Cloud::Asset::V1::Feed

Pass arguments to `update_feed` via a request object, either of type [UpdateFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-UpdateFeedRequest "Google::Cloud::Asset::V1::UpdateFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::UpdateFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-UpdateFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_feed(feed: nil, update_mask: nil) -> ::Google::Cloud::Asset::V1::Feed

Pass arguments to `update_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **feed** ([::Google::Cloud::Asset::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed), ::Hash) — Required. The new values of feed details. It must match an existing feed and the field `name` must be in the format of: projects/project_number/feeds/feed_id or folders/folder_number/feeds/feed_id or organizations/organization_number/feeds/feed_id. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Only updates the `feed` fields indicated by this mask. The field mask must not be empty, and it must not contain fields that are immutable or only set by the server. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-Feed)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::UpdateFeedRequest.new
    
    # Call the update_feed method.
    result = client.update_feed request
    
    # The returned object is of type Google::Cloud::Asset::V1::Feed.
    p result

### #update_saved_query
    
    
    def update_saved_query(request, options = nil) -> ::Google::Cloud::Asset::V1::SavedQuery
    def update_saved_query(saved_query: nil, update_mask: nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Updates a saved query.

**Overloads**
    
    
    def update_saved_query(request, options = nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Pass arguments to `update_saved_query` via a request object, either of type [UpdateSavedQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-UpdateSavedQueryRequest "Google::Cloud::Asset::V1::UpdateSavedQueryRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Asset::V1::UpdateSavedQueryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-UpdateSavedQueryRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_saved_query(saved_query: nil, update_mask: nil) -> ::Google::Cloud::Asset::V1::SavedQuery

Pass arguments to `update_saved_query` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **saved_query** ([::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery), ::Hash) — 

Required. The saved query to update.

The saved query's `name` field is used to identify the one to update, which has format as below:

    * projects/project_number/savedQueries/saved_query_id
    * folders/folder_number/savedQueries/saved_query_id
    * organizations/organization_number/savedQueries/saved_query_id
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Asset::V1::SavedQuery](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-asset-v1/latest/Google-Cloud-Asset-V1-SavedQuery)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/asset/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Asset::V1::AssetService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Asset::V1::UpdateSavedQueryRequest.new
    
    # Call the update_saved_query method.
    result = client.update_saved_query request
    
    # The returned object is of type Google::Cloud::Asset::V1::SavedQuery.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
